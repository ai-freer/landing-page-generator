# 模板与Config映射

## ⚠️ 重要提示
**本指南说明模板与 Config 字段的映射关系。AI 以 `template/landing-page-{N}.html` 为最佳实践标杆创作 HTML，后处理脚本基于此映射校验 config 的完整性。**

## 映射关系

| 模板ID | HTML 代码标杆 | 必需字段 | 可选字段 |
|--------|-------------|---------|---------|
| template-01 | landing-page-01.html | product.name, product.tagline | features[], mock_data.testimonials[], cta.*, theme.* |
| template-02 | landing-page-02.html | product.name, product.tagline | product.price, product.image, cta.*, theme.* |
| template-03 | landing-page-03.html | product.name, product.tagline | story.*, features[], theme.* |
| template-04 | landing-page-04.html | product.name, product.tagline | content_sections[], video_embed, features[], cta.*, theme.* |
| template-05 | landing-page-05.html | product.name, product.tagline | product.info[], cta.*, theme.* |
| template-06 | landing-page-06.html | product.name, product.tagline | zigzag_sections[], faq[], cta.*, theme.* |
| template-07 | landing-page-07.html | product.name, product.tagline | features[], hero.image_url, cta.*, theme.* |
| template-08 | landing-page-08.html | product.name, product.tagline | features[], immersive_section.*, cta.*, theme.* |
| template-09 | landing-page-09.html | product.name, product.tagline | connected_sections[], faq[], cta.*, theme.* |
| template-10 | landing-page-10.html | product.name, product.tagline | structured_sections[], cta.*, theme.* |
| template-11 | landing-page-11.html | product.name, product.tagline | features[], input_placeholder.*, cta.*, theme.* |
| template-12 | landing-page-12.html | product.name, product.tagline | features[], hero.stats[], cta.*, theme.* |
| template-13 | landing-page-13.html | product.name, product.tagline | features[], code_snippets[], cta.*, theme.* |
| template-14 | landing-page-14.html | product.name, product.tagline | features[], cta.*, theme.* |
| template-15 | landing-page-15.html | product.name, product.tagline | features[], gallery_images[], cta.*, theme.* |

## 使用方式

AI 生成 HTML 的工作流：

1. **读取标杆**：阅读 `template/landing-page-{N}.html`，理解该风格的 CSS 技巧、动效、布局结构和交互模式
2. **参考映射**：根据上表确认该模板支持的 config 字段，确保用户提供的内容能被充分利用
3. **创作 HTML**：以模板为质量基线，结合用户的具体产品内容，创作完整 HTML
4. **后处理校验**：`generate_landing_page.py` 基于上表中的必需/可选字段校验 config，并注入图片 URL
