# Landing Page Generator

**[中文](#中文) | [English](#english)**

---

<a id="中文"></a>

## 中文

AI 驱动的 Landing Page 生成器 —— 一个面向 AI 智能体的 Skill，内置 15 种经过精心打磨的专业模板，覆盖 2025 年三大核心设计趋势。通过对话式交互，从产品描述到可部署的完整网站，一步到位。

### 设计哲学

在 2025 年，一张优秀的 Landing Page 不再只是一张网页，更像是一个独立运行的应用程序或一部预告片。

| 设计趋势 | 关键词 | 代表模板 |
|----------|--------|---------|
| **物理质感回归** | 液态玻璃、体积光、磨砂透视、真实材质 | 深色沉浸式、电影感/硬件流、浅色虹彩液态玻璃、数字工坊 |
| **网格化与模块化** | Bento Grid、卡片式布局、非线性浏览 | 便当盒式、多彩层级版、动态商务风 |
| **展示即交互** | 实时代码终端、可交互演示、流式动画 | 代码原生型、趣味连接型、双列布局+视频 |

### 15 种模板风格

#### 物理质感回归派

| 风格 | 核心视觉 | 适用场景 |
|------|---------|---------|
| 浅色虹彩液态玻璃 | 玻璃材质 + 虹彩球体 + 流体渐变 | 现代 SaaS、消费级科技 |
| 电影感/硬件流 | 微距特写 + 体积光 + 暗黑参数表 | AI 硬件、高端消费级应用 |
| 深色沉浸式 | 深蓝渐变 + 玻璃态 + 极光渐变 | 企业级 SaaS、高科技产品 |
| 数字工坊/静谧艺廊 | 光影质感 + 明暗对照法 + 零 UI | 高端消费品、奢侈品 |

#### 网格化与模块化派

| 风格 | 核心视觉 | 适用场景 |
|------|---------|---------|
| 便当盒式 | Bento Grid + 输入优先 + 聚光灯 | AI Agent 平台、多模态工具 |
| 多彩层级版 | 色块分区 + 分屏 Hero + 视觉引导 | 现代 SaaS、功能密集型产品 |
| 动态商务风 | 几何切割 + 斜切角 + 线条感 | 企业 B2B、专业工具 |

#### 展示即交互派

| 风格 | 核心视觉 | 适用场景 |
|------|---------|---------|
| 代码原生型 | 实时代码终端 + IDE 模拟器 | API 服务、开发者工具 |
| 趣味连接型 | 虚线路径串联 + 步骤引导 | 流程化工具、教程类 |
| 双列布局+视频 | 视频演示 + 交替分屏 | 在线课程、教育平台 |

#### 经典商业风格

| 风格 | 核心视觉 | 适用场景 |
|------|---------|---------|
| 经典 Hero+Features | 渐变 Hero + 功能网格 + 用户评价 | SaaS 平台、工具类软件 |
| 产品展示+CTA | 分屏展示 + 价格 CTA | 电商产品、实物商品 |
| 故事讲述型 | 品牌故事 + 情感化设计 | 品牌展示、服务介绍 |
| 深色赛博风 | 深色背景 + 霓虹配色 + 动态动画 | 科技产品、创意工具 |
| 极简插画风 | 极简主义 + 手绘插画 + Z 型布局 | 生活方式产品、创意工具 |

### 工作模式

**模式 A：从零开始** — 提供产品描述 → AI 推荐风格 → 规划图片 → 生成完整网站包

**模式 B：从已有 HTML 优化** — 上传 HTML → 自动解析配置 → 对话式持续修改

### 项目结构

```
landing-page-generator/
├── SKILL.md                 # Skill 主入口（AI 读取）
├── scripts/
│   ├── generate_landing_page.py   # 后处理：校验 + 图片注入 + 结构验证
│   └── parse_landing_page.py      # 解析器：从 HTML 提取配置
├── references/
│   ├── index.md                   # 模板分类索引与选择指南
│   ├── config-guide.md            # 配置文件格式说明
│   ├── image-generation-guide.md  # 图片动态规划框架
│   ├── aesthetic-enhancement-guide.md  # 美学增强实现指南
│   ├── workflows.md               # 对话流程示例
│   ├── template-usage.md          # 模板与配置字段映射
│   └── templates/                 # 15 个模板的详细设计文档
├── template/                # 15 个 HTML 模板（最佳实践标杆）
│   ├── landing-page-01.html
│   ├── ...
│   └── landing-page-15.html
└── assets/                  # 图片资源目录（生成时动态填充）
```

### 安装

#### 作为 Cursor Skill

```bash
git clone https://github.com/ai-freer/landing-page-generator.git ~/.cursor/skills/landing-page-generator
```

#### 作为 Codex Skill

```bash
git clone https://github.com/ai-freer/landing-page-generator.git ~/.codex/skills/landing-page-generator
```

#### 依赖

```bash
pip install beautifulsoup4>=4.12.0
```

### 交付物

生成的网站包结构：

```
output/
├── index.html      ← Landing Page（图片使用相对路径）
└── assets/
    ├── hero.png
    ├── feature-1.png
    └── ...
```

用户下载后可直接在浏览器打开预览，也可部署到 GitHub Pages、Vercel、Netlify 等静态托管平台。

### 许可证

MIT

---

<a id="english"></a>

## English

An AI-powered Landing Page Generator — an Agent Skill with 15 professionally crafted templates covering the three core design trends of 2025. Through conversational interaction, go from product description to a deploy-ready website in one step.

### Design Philosophy

In 2025, a great landing page is no longer just a webpage — it's more like a standalone app or a movie trailer.

| Design Trend | Keywords | Representative Templates |
|-------------|----------|------------------------|
| **Return of Physics** | Liquid Glass, Volumetric Lighting, Frosted Glass, Real Materials | Dark Immersive, Cinematic/Hardware, Light Iridescent Liquid Glass, Digital Atelier |
| **Bento & Modular** | Bento Grid, Card Layout, Non-linear Browsing | Bento Box, Colorful Tiered, Dynamic Business |
| **Show, Don't Tell** | Live Terminal, Interactive Demo, Streaming Animation | Code Native, Playful Connector, Split Layout+Video |

### 15 Template Styles

#### Return of Physics

| Style | Core Visuals | Best For |
|-------|-------------|----------|
| Light Iridescent Liquid Glass | Glass material + iridescent spheres + fluid gradients | Modern SaaS, consumer tech |
| Cinematic / Hardware Flow | Macro close-ups + volumetric lighting + dark spec sheets | AI hardware, premium apps |
| Dark Immersive | Deep blue gradients + glassmorphism + aurora | Enterprise SaaS, high-tech products |
| Digital Atelier / Quiet Gallery | Chiaroscuro + light-shadow textures + zero UI | Luxury goods, premium consumer products |

#### Bento & Modular

| Style | Core Visuals | Best For |
|-------|-------------|----------|
| Bento Box | Bento Grid + input-first + spotlight effects | AI Agent platforms, multimodal tools |
| Colorful Tiered | Color-block zones + split Hero + visual guidance | Modern SaaS, feature-rich products |
| Dynamic Business | Geometric cuts + angled edges + line aesthetics | Enterprise B2B, professional tools |

#### Show, Don't Tell

| Style | Core Visuals | Best For |
|-------|-------------|----------|
| Code Native | Live code terminal + IDE simulator | API services, developer tools |
| Playful Connector | Dashed path connections + step guidance | Workflow tools, tutorials |
| Split Layout + Video | Video demos + alternating split sections | Online courses, education platforms |

#### Classic Commercial

| Style | Core Visuals | Best For |
|-------|-------------|----------|
| Classic Hero + Features | Gradient Hero + feature grid + testimonials | SaaS platforms, software tools |
| Product Showcase + CTA | Split display + pricing CTA | E-commerce, physical products |
| Storytelling | Brand narrative + emotional design | Brand showcase, service introduction |
| Dark Cyberpunk | Dark background + neon palette + dynamic animation | Tech products, creative tools |
| Minimal Illustration | Minimalism + hand-drawn illustrations + Z-layout | Lifestyle products, creative tools |

### Workflow Modes

**Mode A: From Scratch** — Provide product description → AI recommends style → Plan images → Generate complete website package

**Mode B: Optimize Existing HTML** — Upload HTML → Auto-parse config → Conversational iteration

### Project Structure

```
landing-page-generator/
├── SKILL.md                 # Skill entry point (read by AI)
├── scripts/
│   ├── generate_landing_page.py   # Post-processing: validation + image injection
│   └── parse_landing_page.py      # Parser: extract config from HTML
├── references/
│   ├── index.md                   # Template index & selection guide
│   ├── config-guide.md            # Config file format spec
│   ├── image-generation-guide.md  # Image planning framework
│   ├── aesthetic-enhancement-guide.md  # Aesthetic enhancement guide
│   ├── workflows.md               # Conversation flow examples
│   ├── template-usage.md          # Template-to-config field mapping
│   └── templates/                 # Design docs for all 15 templates
├── template/                # 15 HTML templates (best-practice benchmarks)
│   ├── landing-page-01.html
│   ├── ...
│   └── landing-page-15.html
└── assets/                  # Image assets directory (populated at generation time)
```

### Installation

#### As a Cursor Skill

```bash
git clone https://github.com/ai-freer/landing-page-generator.git ~/.cursor/skills/landing-page-generator
```

#### As a Codex Skill

```bash
git clone https://github.com/ai-freer/landing-page-generator.git ~/.codex/skills/landing-page-generator
```

#### Dependencies

```bash
pip install beautifulsoup4>=4.12.0
```

### Output

The generated website package:

```
output/
├── index.html      ← Landing Page (images use relative paths)
└── assets/
    ├── hero.png
    ├── feature-1.png
    └── ...
```

Users can open it directly in a browser for preview, or deploy to static hosting platforms like GitHub Pages, Vercel, or Netlify.

### License

MIT
