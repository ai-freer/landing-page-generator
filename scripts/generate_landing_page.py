#!/usr/bin/env python3
"""
Landing Page 后处理工具（Post-Processor）

角色定位：AI 智能体生成 HTML 后，本脚本负责最后的校验、图片注入和结构验证。
工作流程：AI 创作 HTML → 本脚本后处理 → 输出最终 landing.html

用法：
  python generate_landing_page.py <config_path> <html_input> <html_output>
  python generate_landing_page.py config.json draft.html landing.html

功能：
  1. 基于 config-guide.md 规范校验 config.json
  2. 将 config 中的图片 URL 注入到 HTML 的 data-slot 标记位
  3. 验证 HTML 基础结构（必要元素检查）
  4. 输出校验报告 + 最终 HTML
"""

import json
import re
import sys
import os


# ============================================================
# 配置校验（基于 config-guide.md 规范）
# ============================================================

VALID_TEMPLATE_IDS = [f"template-{str(i).zfill(2)}" for i in range(1, 16)]

TEMPLATE_NAMES = {
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

# 字段长度限制（来自 config-guide.md 验证规则）
LENGTH_RULES = {
    "product.name": (2, 50),
    "product.tagline": (10, 100),
    "product.description": (50, 500),
    "features[].title": (2, 30),
    "features[].description": (10, 200),
}

# 各模板的推荐可选字段
TEMPLATE_OPTIONAL_FIELDS = {
    "template-02": ["product.price", "product.image"],
    "template-03": ["story"],
    "template-04": ["content_sections", "video_embed"],
    "template-05": ["product.info"],
    "template-06": ["zigzag_sections", "faq"],
    "template-07": ["hero.image_url"],
    "template-08": ["hero.image_url", "immersive_section"],
    "template-09": ["connected_sections"],
    "template-10": ["structured_sections"],
    "template-11": ["input_placeholder"],
    "template-13": ["code_snippets"],
    "template-15": ["gallery_images"],
}

# 图片 URL 字段映射：config 字段 → data-slot 名称
IMAGE_SLOT_MAP = {
    "product.image": "hero",
    "hero.image_url": "hero",
    "immersive_section.image_url": "immersive",
}


def load_config(config_path: str) -> dict:
    """加载并解析 config.json"""
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"配置文件不存在: {config_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON 格式错误: {e}")


def validate_config(config: dict) -> list:
    """
    基于 config-guide.md 规范校验配置。
    返回 (errors, warnings) 元组，errors 是致命问题，warnings 是建议。
    """
    errors = []
    warnings = []

    # --- 必填字段 ---
    template_id = config.get("template_id")
    if not template_id:
        errors.append("缺少必填字段: template_id")
    elif template_id not in VALID_TEMPLATE_IDS:
        errors.append(f"无效的 template_id: {template_id}（有效范围: template-01 到 template-15）")

    product = config.get("product", {})
    if not product.get("name"):
        errors.append("缺少必填字段: product.name")
    if not product.get("tagline"):
        errors.append("缺少必填字段: product.tagline")

    # --- 长度校验 ---
    length_checks = [
        ("product.name", product.get("name", "")),
        ("product.tagline", product.get("tagline", "")),
        ("product.description", product.get("description", "")),
    ]
    for field_name, value in length_checks:
        if value and field_name in LENGTH_RULES:
            min_len, max_len = LENGTH_RULES[field_name]
            if len(value) < min_len:
                warnings.append(f"{field_name} 过短（{len(value)}字符，建议≥{min_len}）")
            elif len(value) > max_len:
                warnings.append(f"{field_name} 过长（{len(value)}字符，建议≤{max_len}）")

    # --- features 校验 ---
    features = config.get("features", [])
    if features:
        for i, feat in enumerate(features):
            title = feat.get("title", "")
            desc = feat.get("description", "")
            if not title:
                errors.append(f"features[{i}] 缺少 title")
            elif len(title) < 2 or len(title) > 30:
                warnings.append(f"features[{i}].title 长度({len(title)})超出建议范围(2-30)")
            if desc and (len(desc) < 10 or len(desc) > 200):
                warnings.append(f"features[{i}].description 长度({len(desc)})超出建议范围(10-200)")
    else:
        warnings.append("未提供 features 数组（大多数模板推荐提供3-6个功能）")

    # --- 颜色格式校验 ---
    theme = config.get("theme", {})
    hex_pattern = re.compile(r"^#[0-9a-fA-F]{6}$")
    for color_field in ["primary_color", "secondary_color", "background_color", "text_color"]:
        color_val = theme.get(color_field)
        if color_val and not hex_pattern.match(color_val):
            warnings.append(f"theme.{color_field} 格式不标准: {color_val}（建议 #RRGGBB）")

    # --- URL 格式校验 ---
    image_url = product.get("image")
    if image_url and not (image_url.startswith("http://") or image_url.startswith("https://")):
        warnings.append(f"product.image 不是有效 URL: {image_url}")

    # --- 模板特定字段建议 ---
    if template_id and template_id in TEMPLATE_OPTIONAL_FIELDS:
        for field in TEMPLATE_OPTIONAL_FIELDS[template_id]:
            # 检查嵌套字段
            parts = field.split(".")
            obj = config
            found = True
            for part in parts:
                if isinstance(obj, dict) and part in obj:
                    obj = obj[part]
                else:
                    found = False
                    break
            if not found:
                style_name = TEMPLATE_NAMES.get(template_id, template_id)
                warnings.append(f"「{style_name}」风格建议提供 {field} 字段")

    return errors, warnings


# ============================================================
# 图片注入
# ============================================================

def get_image_urls_from_config(config: dict) -> dict:
    """
    从 config 中提取所有图片 URL，返回 {slot_name: [url, ...]} 映射。
    """
    urls = {}

    # product.image → hero slot
    product_image = config.get("product", {}).get("image")
    if product_image:
        urls.setdefault("hero", []).append(product_image)

    # hero.image_url → hero slot
    hero_image = config.get("hero", {}).get("image_url")
    if hero_image:
        urls.setdefault("hero", []).append(hero_image)

    # immersive_section.image_url → immersive slot
    immersive_image = config.get("immersive_section", {}).get("image_url")
    if immersive_image:
        urls.setdefault("immersive", []).append(immersive_image)

    # connected_sections[].image_url → step slot
    for section in config.get("connected_sections", []):
        img = section.get("image_url")
        if img:
            urls.setdefault("step", []).append(img)

    # structured_sections[].image_url → section slot
    for section in config.get("structured_sections", []):
        img = section.get("image_url")
        if img:
            urls.setdefault("section", []).append(img)

    # zigzag_sections[].image_url → section slot
    for section in config.get("zigzag_sections", []):
        img = section.get("image_url")
        if img:
            urls.setdefault("section", []).append(img)

    # content_sections[].image_url → content slot
    for section in config.get("content_sections", []):
        img = section.get("image_url")
        if img:
            urls.setdefault("content", []).append(img)

    # gallery_images[].url → gallery slot
    for img_obj in config.get("gallery_images", []):
        img = img_obj.get("url")
        if img:
            urls.setdefault("gallery", []).append(img)

    return urls


def inject_images(html: str, image_urls: dict) -> tuple:
    """
    将图片 URL 注入到 HTML 中带有 data-slot 属性的 <img> 标签。
    返回 (修改后的 HTML, 注入统计)。
    """
    stats = {"injected": 0, "empty_slots": 0}

    # 为每个 slot 维护一个索引计数器
    slot_counters = {}

    def replace_img(match):
        full_tag = match.group(0)

        # 提取 data-slot
        slot_match = re.search(r'data-slot="([^"]*)"', full_tag)
        if not slot_match:
            return full_tag

        slot_name = slot_match.group(1)
        available = image_urls.get(slot_name, [])

        # 获取该 slot 的当前索引
        idx = slot_counters.get(slot_name, 0)
        slot_counters[slot_name] = idx + 1

        if idx < len(available):
            url = available[idx]
            # 替换 src="" 为实际 URL
            new_tag = re.sub(r'src="[^"]*"', f'src="{url}"', full_tag, count=1)
            stats["injected"] += 1
            return new_tag
        else:
            stats["empty_slots"] += 1
            return full_tag

    # 匹配所有带 data-slot 的 img 标签
    result = re.sub(r"<img\b[^>]*data-slot=[^>]*>", replace_img, html)

    return result, stats


# ============================================================
# HTML 结构验证
# ============================================================

def validate_html_structure(html: str) -> list:
    """
    检查 HTML 基础结构，返回 warnings 列表。
    不做严格的 HTML 语法校验，只检查 Landing Page 的关键要素。
    """
    warnings = []

    # 基础结构
    if "<!DOCTYPE html>" not in html and "<!doctype html>" not in html:
        warnings.append("缺少 <!DOCTYPE html> 声明")

    if "<html" not in html:
        warnings.append("缺少 <html> 标签")

    if "<head" not in html:
        warnings.append("缺少 <head> 标签")

    if "<meta" not in html and 'charset' not in html.lower():
        warnings.append("建议添加 <meta charset> 声明")

    if "<title" not in html:
        warnings.append("缺少 <title> 标签")

    # 视口适配
    if "viewport" not in html:
        warnings.append("缺少 viewport meta 标签（影响移动端适配）")

    # Landing Page 关键区域
    if "<nav" not in html and "navbar" not in html:
        warnings.append("未检测到导航栏（nav/navbar）")

    # Hero 区域（几乎所有 LP 必备）
    if "hero" not in html.lower():
        warnings.append("未检测到 Hero 区域")

    # CTA（Landing Page 核心）
    cta_patterns = ["cta", "call-to-action", "btn-primary", "button-primary", "get-started"]
    if not any(p in html.lower() for p in cta_patterns):
        warnings.append("未检测到 CTA 按钮/区域")

    # Footer
    if "<footer" not in html:
        warnings.append("缺少 <footer> 标签")

    # 无障碍
    img_tags = re.findall(r"<img\b[^>]*>", html)
    imgs_without_alt = [tag for tag in img_tags if 'alt=' not in tag]
    if imgs_without_alt:
        warnings.append(f"{len(imgs_without_alt)} 个 <img> 标签缺少 alt 属性")

    return warnings


# ============================================================
# 主流程
# ============================================================

def post_process(config_path: str, html_input_path: str, html_output_path: str) -> dict:
    """
    后处理主流程：
    1. 加载并校验 config
    2. 加载 AI 生成的 HTML
    3. 注入图片 URL
    4. 验证 HTML 结构
    5. 输出最终 HTML 和报告
    """
    report = {
        "config_errors": [],
        "config_warnings": [],
        "html_warnings": [],
        "image_stats": {},
        "success": False,
    }

    # 1. 加载并校验 config
    config = load_config(config_path)
    errors, warnings = validate_config(config)
    report["config_errors"] = errors
    report["config_warnings"] = warnings

    if errors:
        report["success"] = False
        return report

    # 2. 加载 HTML
    try:
        with open(html_input_path, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        report["config_errors"].append(f"HTML 文件不存在: {html_input_path}")
        return report

    # 3. 注入图片
    image_urls = get_image_urls_from_config(config)
    html, image_stats = inject_images(html, image_urls)
    report["image_stats"] = image_stats

    # 4. 验证 HTML 结构
    html_warnings = validate_html_structure(html)
    report["html_warnings"] = html_warnings

    # 5. 输出最终 HTML
    output_dir = os.path.dirname(html_output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(html_output_path, "w", encoding="utf-8") as f:
        f.write(html)

    report["success"] = True
    report["template_id"] = config.get("template_id", "unknown")
    report["template_name"] = TEMPLATE_NAMES.get(config.get("template_id", ""), "未知")
    report["html_size"] = len(html)

    return report


def print_report(report: dict):
    """打印格式化的报告"""
    print("=" * 60)
    print("  Landing Page 后处理报告")
    print("=" * 60)

    if report.get("template_id"):
        name = report.get("template_name", "")
        print(f"\n  模板: {report['template_id']}（{name}）")

    # Config 校验
    errors = report.get("config_errors", [])
    warnings = report.get("config_warnings", [])

    if errors:
        print(f"\n  ✗ Config 校验失败（{len(errors)} 个错误）:")
        for e in errors:
            print(f"    ✗ {e}")
        print("\n  请修正以上错误后重试。")
        return

    print(f"\n  ✓ Config 校验通过")
    if warnings:
        print(f"    ⚠ {len(warnings)} 条建议:")
        for w in warnings:
            print(f"      - {w}")

    # 图片注入
    stats = report.get("image_stats", {})
    injected = stats.get("injected", 0)
    empty = stats.get("empty_slots", 0)
    print(f"\n  ✓ 图片注入: {injected} 张已注入, {empty} 个槽位待填充")

    # HTML 结构
    html_warnings = report.get("html_warnings", [])
    if html_warnings:
        print(f"\n  ⚠ HTML 结构建议（{len(html_warnings)} 条）:")
        for w in html_warnings:
            print(f"      - {w}")
    else:
        print(f"\n  ✓ HTML 结构检查通过")

    # 总结
    if report.get("success"):
        size_kb = report.get("html_size", 0) / 1024
        print(f"\n  ✓ 生成成功（{size_kb:.1f} KB）")
    print("=" * 60)


def main():
    """命令行入口"""
    if len(sys.argv) < 4:
        print("Landing Page 后处理工具")
        print()
        print("用法:")
        print("  python generate_landing_page.py <config.json> <input.html> <output.html>")
        print()
        print("示例:")
        print("  python generate_landing_page.py config.json draft.html landing.html")
        print()
        print("功能:")
        print("  1. 校验 config.json（基于 config-guide.md 规范）")
        print("  2. 将 config 中的图片 URL 注入到 HTML")
        print("  3. 验证 HTML 基础结构")
        print("  4. 输出最终 landing.html + 校验报告")
        print()
        print("也可仅校验 config（不处理 HTML）:")
        print("  python generate_landing_page.py config.json --validate-only")
        sys.exit(1)

    config_path = sys.argv[1]

    # 仅校验模式
    if len(sys.argv) == 3 and sys.argv[2] == "--validate-only":
        try:
            config = load_config(config_path)
            errors, warnings = validate_config(config)
            print("=" * 60)
            print("  Config 校验报告")
            print("=" * 60)
            if errors:
                print(f"\n  ✗ {len(errors)} 个错误:")
                for e in errors:
                    print(f"    ✗ {e}")
            else:
                print(f"\n  ✓ 校验通过")
            if warnings:
                print(f"\n  ⚠ {len(warnings)} 条建议:")
                for w in warnings:
                    print(f"    - {w}")
            print("=" * 60)
            sys.exit(1 if errors else 0)
        except Exception as e:
            print(f"✗ 校验失败: {e}", file=sys.stderr)
            sys.exit(1)

    html_input = sys.argv[2]
    html_output = sys.argv[3]

    try:
        report = post_process(config_path, html_input, html_output)
        print_report(report)
        sys.exit(0 if report["success"] else 1)
    except Exception as e:
        print(f"✗ 处理失败: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
