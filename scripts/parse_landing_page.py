#!/usr/bin/env python3
"""
Landing Page 解析器（HTML → Config）

角色定位：从已有 HTML 文件中提取结构化信息，生成符合 config-guide.md 规范的 config.json。
用于 Skill 的"模式B：从已有 HTML 优化"工作流。

用法：
  python parse_landing_page.py <input.html> <output_config.json>

功能：
  1. 识别模板风格（全 15 种）
  2. 提取产品信息、功能、评价、主题色等
  3. 识别图片槽位和现有图片 URL
  4. 输出符合 config-guide.md 规范的 config.json
"""

import json
import re
import sys
from bs4 import BeautifulSoup


# ============================================================
# 模板风格识别（全 15 种）
# ============================================================

# 每个模板的特征签名：(CSS class 或结构特征, 权重)
TEMPLATE_SIGNATURES = {
    "template-01": [
        ("features-grid", 3), ("feature-card", 2), ("hero", 1),
        ("testimonials", 2),
    ],
    "template-02": [
        ("product-showcase", 4), ("product-hero", 3), ("price", 2),
        ("hero-image-wrapper", 1),
    ],
    "template-03": [
        ("story-hero", 4), ("story-section", 3), ("mission", 3),
        ("story-image", 2), ("brand-story", 2),
    ],
    "template-04": [
        ("split-section", 4), ("video-section", 3), ("content-media", 2),
        ("video-thumbnail", 2), ("content-sections", 2),
    ],
    "template-05": [
        ("minimal-container", 4), ("cyberpunk", 3), ("neon", 2),
        ("glitch", 2), ("terminal", 1),
    ],
    "template-06": [
        ("zigzag-section", 4), ("zigzag-image", 3), ("illustration", 2),
        ("faq-section", 1), ("zigzag-content", 2),
    ],
    "template-07": [
        ("hero-split", 3), ("colorful", 2), ("layer", 2),
        ("float-badge", 3), ("multi-color", 2),
    ],
    "template-08": [
        ("immersive", 4), ("dark-hero", 2), ("nebula", 2),
        ("immersive-section", 3), ("glass-card", 2),
    ],
    "template-09": [
        ("connected", 3), ("step-card", 3), ("path-line", 2),
        ("fun-connect", 2), ("framed-illustration", 3),
    ],
    "template-10": [
        ("structured-section", 4), ("dynamic-business", 2), ("velocity", 1),
        ("skew", 2), ("structured-image", 3),
    ],
    "template-11": [
        ("bento", 4), ("cell-", 3), ("input-spotlight", 3),
        ("agent", 2), ("grid-showcase", 2),
    ],
    "template-12": [
        ("cinematic", 4), ("hardware", 3), ("macro", 2),
        ("spec-table", 3), ("film-grain", 2),
    ],
    "template-13": [
        ("code-block", 4), ("terminal", 3), ("syntax", 2),
        ("ide-", 2), ("code-snippet", 3), ("monospace", 1),
    ],
    "template-14": [
        ("glass-sphere", 4), ("iridescent", 3), ("liquid-glass", 3),
        ("aurora", 2), ("frosted", 2), ("backdrop-filter", 1),
    ],
    "template-15": [
        ("editorial", 4), ("gallery-strip", 3), ("tactile", 3),
        ("craft-label", 2), ("gallery-item", 2), ("chiaroscuro", 2),
    ],
}


def identify_template(soup, html_text: str) -> tuple:
    """
    识别模板类型。返回 (template_id, confidence_score, style_name)。
    通过 CSS class 名称和 HTML 结构特征进行加权匹配。
    """
    # 获取所有 class 名称
    all_classes = set()
    for tag in soup.find_all(True, class_=True):
        for cls in tag.get("class", []):
            all_classes.add(cls.lower())

    # 也检查 HTML 文本中的关键词（覆盖 CSS 变量名、注释等）
    html_lower = html_text.lower()

    scores = {}
    for tid, signatures in TEMPLATE_SIGNATURES.items():
        score = 0
        for keyword, weight in signatures:
            keyword_lower = keyword.lower()
            # 检查 class 名称（部分匹配）
            for cls in all_classes:
                if keyword_lower in cls:
                    score += weight
                    break
            else:
                # 检查 HTML 文本
                if keyword_lower in html_lower:
                    score += weight * 0.5  # 文本匹配权重减半
        scores[tid] = score

    # 选择得分最高的
    best = max(scores, key=scores.get)
    best_score = scores[best]

    # 置信度：最高分与第二高分的差距
    sorted_scores = sorted(scores.values(), reverse=True)
    confidence = best_score - sorted_scores[1] if len(sorted_scores) > 1 else best_score

    style_names = {
        "template-01": "经典Hero+Features",
        "template-02": "产品展示+CTA",
        "template-03": "故事讲述型",
        "template-04": "双列布局+视频",
        "template-05": "深色赛博风",
        "template-06": "极简插画风",
        "template-07": "多彩层级版",
        "template-08": "深色沉浸式",
        "template-09": "趣味连接型",
        "template-10": "动态商务风",
        "template-11": "便当盒式",
        "template-12": "电影感/硬件流",
        "template-13": "代码原生型",
        "template-14": "浅色虹彩液态玻璃",
        "template-15": "数字工坊/静谧艺廊",
    }

    return best, best_score, style_names.get(best, "未知")


# ============================================================
# 内容提取
# ============================================================

def extract_product(soup) -> dict:
    """提取产品基本信息"""
    product = {}

    # 产品名称：优先取 h1，其次取 brand/logo 文字
    h1 = soup.find("h1")
    if h1:
        product["name"] = h1.get_text(strip=True)
    else:
        brand = soup.find(class_=re.compile(r"brand|logo|site-name", re.I))
        if brand:
            product["name"] = brand.get_text(strip=True)

    # 标语：hero 区域的副标题或第一个 p
    hero = soup.find(class_=re.compile(r"hero"))
    if hero:
        # 优先找 subtitle/tagline class
        subtitle = hero.find(class_=re.compile(r"subtitle|tagline|hero-desc", re.I))
        if subtitle:
            product["tagline"] = subtitle.get_text(strip=True)
        else:
            p = hero.find("p")
            if p:
                text = p.get_text(strip=True)
                if 10 <= len(text) <= 100:
                    product["tagline"] = text

    # 描述：hero 或第一个 section 中较长的段落
    for section in [hero, soup.find("section")]:
        if not section:
            continue
        for p in section.find_all("p"):
            text = p.get_text(strip=True)
            if 50 <= len(text) <= 500 and text != product.get("tagline"):
                product["description"] = text
                break
        if "description" in product:
            break

    # 图片 URL
    images = extract_images(soup)
    hero_images = [img for img in images if img.get("slot") == "hero"]
    if hero_images and hero_images[0].get("url"):
        product["image"] = hero_images[0]["url"]

    # 价格
    price_el = soup.find(class_=re.compile(r"price", re.I))
    if price_el:
        price_text = price_el.get_text(strip=True)
        if re.search(r"[¥$€£\d]", price_text):
            product["price"] = price_text

    # 默认值
    product.setdefault("name", "产品名称")
    product.setdefault("tagline", "产品标语")

    return product


def extract_features(soup) -> list:
    """提取功能列表"""
    features = []

    # 策略1：从 feature-card / feature-item 类中提取
    cards = soup.find_all(class_=re.compile(r"feature[-_]?(card|item|box)", re.I))
    for card in cards:
        title_el = card.find(["h3", "h4", "h2"])
        desc_el = card.find("p")
        if title_el:
            feat = {"title": title_el.get_text(strip=True)}
            if desc_el:
                feat["description"] = desc_el.get_text(strip=True)
            else:
                feat["description"] = ""
            features.append(feat)

    # 策略2：从 grid 容器中的子元素提取
    if not features:
        grid = soup.find(class_=re.compile(r"features?[-_]?(grid|list|container)", re.I))
        if grid:
            for child in grid.find_all(["div", "article", "li"], recursive=False):
                title_el = child.find(["h3", "h4", "h2"])
                desc_el = child.find("p")
                if title_el:
                    feat = {"title": title_el.get_text(strip=True)}
                    if desc_el:
                        feat["description"] = desc_el.get_text(strip=True)
                    else:
                        feat["description"] = ""
                    features.append(feat)

    # 策略3：bento grid 中的 cell
    if not features:
        cells = soup.find_all(class_=re.compile(r"cell|bento[-_]?item", re.I))
        for cell in cells:
            title_el = cell.find(["h3", "h4"])
            desc_el = cell.find("p")
            if title_el:
                feat = {"title": title_el.get_text(strip=True)}
                if desc_el:
                    feat["description"] = desc_el.get_text(strip=True)
                else:
                    feat["description"] = ""
                features.append(feat)

    return features


def extract_testimonials(soup) -> list:
    """提取用户评价"""
    testimonials = []

    cards = soup.find_all(class_=re.compile(r"testimonial[-_]?(card|item|quote)", re.I))
    for card in cards:
        quote_el = card.find(class_=re.compile(r"quote|text|content", re.I))
        author_el = card.find(class_=re.compile(r"author|name|attribution", re.I))

        if not quote_el:
            quote_el = card.find("p")
        if not author_el:
            # 尝试找 cite 或最后一个小文本
            author_el = card.find("cite")

        testimonial = {}
        if quote_el:
            testimonial["quote"] = quote_el.get_text(strip=True)
        if author_el:
            testimonial["author"] = author_el.get_text(strip=True)

        if testimonial.get("quote"):
            testimonials.append(testimonial)

    return testimonials


def extract_stats(soup) -> list:
    """提取数据统计"""
    stats = []

    stat_items = soup.find_all(class_=re.compile(r"stat[-_]?(item|card|value|number)", re.I))
    for item in stat_items:
        value_el = item.find(class_=re.compile(r"value|number|count", re.I))
        label_el = item.find(class_=re.compile(r"label|desc|text", re.I))

        if not value_el:
            # 尝试找大字体数字
            for el in item.find_all(["h2", "h3", "span", "div"]):
                text = el.get_text(strip=True)
                if re.match(r"[\d,\.]+[+%KMkm]*", text):
                    value_el = el
                    break

        stat = {}
        if value_el:
            stat["value"] = value_el.get_text(strip=True)
        if label_el:
            stat["label"] = label_el.get_text(strip=True)

        if stat.get("value"):
            stats.append(stat)

    return stats


def extract_images(soup) -> list:
    """提取所有图片信息（URL + 槽位 + 尺寸）"""
    images = []

    for img in soup.find_all("img"):
        info = {
            "url": img.get("src", ""),
            "alt": img.get("alt", ""),
            "slot": img.get("data-slot", ""),
            "size": img.get("data-size", ""),
            "class": " ".join(img.get("class", [])),
        }

        # 如果没有 data-slot，尝试从 class 或父元素推断
        if not info["slot"]:
            classes = info["class"].lower()
            parent_classes = " ".join(img.parent.get("class", [])).lower() if img.parent else ""
            all_ctx = classes + " " + parent_classes

            if "hero" in all_ctx:
                info["slot"] = "hero"
            elif "gallery" in all_ctx:
                info["slot"] = "gallery"
            elif "feature" in all_ctx:
                info["slot"] = "feature"
            elif "story" in all_ctx or "editorial" in all_ctx:
                info["slot"] = "editorial"
            elif "step" in all_ctx or "connected" in all_ctx:
                info["slot"] = "step"
            elif "immersive" in all_ctx:
                info["slot"] = "immersive"

        # 过滤掉 data URI 和小图标
        if info["url"].startswith("data:image/svg"):
            continue

        images.append(info)

    return images


def extract_theme(soup, html_text: str) -> dict:
    """提取主题配色"""
    theme = {}

    # 从 CSS 变量中提取
    css_var_pattern = re.compile(r"--(?:primary|accent|main)[-_]?color\s*:\s*(#[0-9a-fA-F]{3,8})")
    matches = css_var_pattern.findall(html_text)
    if matches:
        theme["primary_color"] = matches[0]

    css_var_pattern2 = re.compile(r"--(?:secondary|accent2)[-_]?color\s*:\s*(#[0-9a-fA-F]{3,8})")
    matches2 = css_var_pattern2.findall(html_text)
    if matches2:
        theme["secondary_color"] = matches2[0]

    # 从 style 标签中提取颜色
    if not theme:
        style_tags = soup.find_all("style")
        all_colors = []
        for style in style_tags:
            colors = re.findall(r"#[0-9a-fA-F]{6}", style.string or "")
            all_colors.extend(colors)

        # 过滤常见的黑白灰
        skip_colors = {"#ffffff", "#000000", "#333333", "#666666", "#999999",
                       "#f5f5f5", "#fafafa", "#eeeeee", "#e5e5e5", "#cccccc"}
        unique_colors = []
        for c in all_colors:
            c_lower = c.lower()
            if c_lower not in skip_colors and c_lower not in unique_colors:
                unique_colors.append(c_lower)

        if len(unique_colors) >= 1:
            theme["primary_color"] = unique_colors[0]
        if len(unique_colors) >= 2:
            theme["secondary_color"] = unique_colors[1]

    # 检测背景色（深色/浅色）
    body = soup.find("body")
    if body:
        style = body.get("style", "")
        bg_match = re.search(r"background[-_]?color\s*:\s*(#[0-9a-fA-F]{3,8})", style)
        if bg_match:
            theme["background_color"] = bg_match.group(1)

    return theme


def extract_faq(soup) -> list:
    """提取 FAQ"""
    faq = []

    faq_items = soup.find_all(class_=re.compile(r"faq[-_]?(item|question|entry)", re.I))
    for item in faq_items:
        q_el = item.find(class_=re.compile(r"question|title|header", re.I))
        a_el = item.find(class_=re.compile(r"answer|content|body|text", re.I))

        if not q_el:
            q_el = item.find(["h3", "h4", "button"])
        if not a_el:
            a_el = item.find("p")

        entry = {}
        if q_el:
            entry["question"] = q_el.get_text(strip=True)
        if a_el:
            entry["answer"] = a_el.get_text(strip=True)

        if entry.get("question"):
            faq.append(entry)

    return faq


def extract_cta(soup) -> dict:
    """提取 CTA 信息"""
    cta = {}

    cta_section = soup.find(class_=re.compile(r"cta[-_]?(section|area|block)", re.I))
    if cta_section:
        title_el = cta_section.find(["h2", "h3"])
        if title_el:
            cta["title"] = title_el.get_text(strip=True)

        subtitle_el = cta_section.find("p")
        if subtitle_el:
            cta["subtitle"] = subtitle_el.get_text(strip=True)

    # CTA 按钮文字
    btn = soup.find(class_=re.compile(r"cta[-_]?(btn|button)", re.I))
    if not btn:
        btn = soup.find("a", class_=re.compile(r"btn[-_]?primary|button[-_]?primary|get[-_]?started", re.I))
    if btn:
        cta["button_text"] = btn.get_text(strip=True)

    return cta


# ============================================================
# 主流程
# ============================================================

def parse_html_to_config(html_path: str, output_path: str) -> dict:
    """
    解析 HTML → config.json

    返回解析结果 dict，包含 config 和解析元数据。
    """
    with open(html_path, "r", encoding="utf-8") as f:
        html_text = f.read()

    soup = BeautifulSoup(html_text, "html.parser")

    # 1. 识别模板
    template_id, score, style_name = identify_template(soup, html_text)

    # 2. 提取所有内容
    config = {
        "template_id": template_id,
        "product": extract_product(soup),
        "features": extract_features(soup),
    }

    # 3. 提取可选内容
    testimonials = extract_testimonials(soup)
    stats = extract_stats(soup)
    if testimonials or stats:
        config["mock_data"] = {}
        if testimonials:
            config["mock_data"]["testimonials"] = testimonials
        if stats:
            config["mock_data"]["stats"] = stats

    theme = extract_theme(soup, html_text)
    if theme:
        config["theme"] = theme

    faq = extract_faq(soup)
    if faq:
        config["faq"] = faq

    cta = extract_cta(soup)
    if cta:
        config["cta"] = cta

    # 4. 提取图片信息（供 AI 参考）
    images = extract_images(soup)
    if images:
        config["_parsed_images"] = images  # 带下划线前缀，表示元数据

    # 5. 输出
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    # 返回结果（含元数据）
    return {
        "config": config,
        "meta": {
            "template_id": template_id,
            "style_name": style_name,
            "confidence_score": score,
            "features_count": len(config.get("features", [])),
            "testimonials_count": len(testimonials),
            "images_count": len(images),
            "has_faq": bool(faq),
            "has_cta": bool(cta),
        },
    }


def main():
    """命令行入口"""
    if len(sys.argv) < 3:
        print("Landing Page 解析器（HTML → Config）")
        print()
        print("用法:")
        print("  python parse_landing_page.py <input.html> <output_config.json>")
        print()
        print("示例:")
        print("  python parse_landing_page.py landing.html config.json")
        print()
        print("功能:")
        print("  1. 识别模板风格（全 15 种）")
        print("  2. 提取产品信息、功能、评价等")
        print("  3. 输出符合 config-guide.md 规范的 config.json")
        sys.exit(1)

    html_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        result = parse_html_to_config(html_path, output_path)
        meta = result["meta"]

        print("=" * 60)
        print("  Landing Page 解析报告")
        print("=" * 60)
        print(f"\n  ✓ 识别风格: {meta['style_name']}（{meta['template_id']}）")
        print(f"    置信度: {meta['confidence_score']:.1f}")
        print(f"\n  提取内容:")
        print(f"    产品名称: {result['config']['product'].get('name', '未知')}")
        print(f"    产品标语: {result['config']['product'].get('tagline', '未知')}")
        print(f"    功能数量: {meta['features_count']}")
        print(f"    用户评价: {meta['testimonials_count']}")
        print(f"    图片数量: {meta['images_count']}")
        print(f"    FAQ: {'有' if meta['has_faq'] else '无'}")
        print(f"    CTA: {'有' if meta['has_cta'] else '无'}")
        print(f"\n  ✓ 配置已输出: {output_path}")
        print("=" * 60)

        return 0
    except Exception as e:
        print(f"✗ 解析失败: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
