---
name: landing-page-generator
description: 根据产品描述和参考图智能推荐设计风格并生成Landing Page，根据产品自动解析配置，专为Coze平台设计，支持对话式持续修改、上下文配置管理、文件自动生成，交付可直接部署的完整网站包（HTML + 图片资源）。提供15种专业模板：经典Hero+Features、产品展示+CTA、故事讲述型、双列布局+视频、深色赛博风、极简插画风、多彩层级版、深色沉浸式、趣味连接型、动态商务风、便当盒式、电影感/硬件流、代码原生型、浅色虹彩液态玻璃、数字工坊/静谧艺廊
dependency:
  python:
    - beautifulsoup4>=4.12.0
---

# Landing Page 生成器

## 设计哲学（2025核心趋势）

在2025年，一张优秀的Landing Page不再只是一张网页，更像是一个独立运行的应用程序或一部预告片。

### 物理质感回归（Return of Physics）
摒弃了死板的扁平化（Flat Design），在数字世界中重建"重量感"和"价值感"。
- **关键词**：液态玻璃（Liquid Glass）、体积光（Volumetric Lighting）、磨砂透视（Frosted Glass）、真实材质渲染
- **代表风格**：深色沉浸式、电影感/硬件流、浅色虹彩液态玻璃、数字工坊/静谧艺廊

### 网格化与模块化（Bento & Modular）
受AI Agent和系统化思维影响，信息不再线性堆叠，而是被封装在独立的"容器"中。
- **关键词**：Bento Grid（便当盒网格）、卡片式布局、非线性浏览
- **代表风格**：多彩层级版、动态商务风、便当盒式

### 展示即交互（Show, Don't Tell）
用户不再相信静态截图，他们要看"活"的东西，建立即刻信任（Instant Trust）。
- **关键词**：实时代码终端（Live Terminal）、可交互演示（Interactive Demo）、流式生成动画（Streaming Text）
- **代表风格**：双列布局+视频、趣味连接型、代码原生型

### 生成原则
1. **美学优先**：整体美学高度和视觉冲击力是首要目标，代码只是实现载体
2. **最佳实践**：`template/` 下的 15 个 HTML 模板是每种风格的**代码标杆**——CSS 技巧、动效实现、响应式布局、交互模式均经过验证。AI 生成时应以此为质量基线，对齐或超越，而非仅参考风格
3. **视觉冲击**：优先考虑动效、光影、质感等视觉元素，提升页面"活"的感觉
4. **灵活创作**：模板是标杆而非模具——AI 应理解其设计精髓后，根据具体产品灵活调整布局、数量、配色，不拘泥于模板的具体实现细节

## 任务目标
根据产品描述/参考图智能推荐模板并生成Landing Page，或从已有HTML解析配置进行优化，支持对话式持续修改。

## Coze平台规范

### 文件路径
- `./config.json` - 临时配置文件（脚本调用）
- `./output/` - **交付包目录**（用户下载的完整网站）
  - `./output/index.html` - Landing Page 主文件
  - `./output/assets/` - 图片资源目录（AI 生成 / 用户提供的图片）
- `./template/` - 模板库（Skill自带，15种风格的最佳实践标杆）
- `./` - 对话工作目录

### 上下文管理
- 智能体在对话上下文中维护config变量
- 每次生成前将config写入`./config.json`
- 修改时更新上下文config，重新生成

### 交付包结构
最终交付给用户的是 `output/` 目录，结构如下：
```
output/
├── index.html          ← Landing Page（图片引用相对路径 assets/xxx.png）
└── assets/
    ├── hero.png         ← Hero 主图
    ├── feature-1.png    ← 功能配图
    ├── feature-2.png
    └── ...              ← 其他图片资源
```
- HTML 中图片使用**相对路径** `assets/xxx.png`，用户下载整个 `output/` 目录后可直接在浏览器打开 `index.html` 预览
- 图片文件命名规则：`{槽位类型}-{序号}.{ext}`（如 `hero.png`、`feature-1.png`、`gallery-3.jpg`）
- 用户也可将整个 `output/` 目录直接部署到静态托管（GitHub Pages、Vercel、Netlify 等）

## 操作步骤

### 模式A：从零开始
1. 需求收集（产品描述、参考图、风格偏好）
2. 智能分析并推荐模板（参考[index.md](references/index.md)和[templates/](references/templates/)目录）
3. 生成设计草案，用户选择
4. 补充关键信息（标语、功能列表、评价等）
5. 智能体在上下文中创建config
6. **图片动态规划**：根据产品内容+模板槽位+用户素材，规划图片方案（参考[image-generation-guide.md](references/image-generation-guide.md)）
7. 向用户展示图片规划方案，确认后获取图片（AI生成/用户提供）
8. **图片落盘**：将获取到的图片保存到 `./output/assets/` 目录，按命名规则存储
9. **AI 生成 HTML**：以对应的 `template/landing-page-{N}.html` 为最佳实践标杆，结合用户内容创作完整 HTML。图片使用相对路径 `assets/xxx.png` 引用
10. **后处理**：`python scripts/generate_landing_page.py ./config.json ./draft.html ./output/index.html`（校验config + 注入图片路径 + 验证结构）
11. 展示预览（用户可直接打开 `output/index.html` 在浏览器预览完整效果）
12. 循环：用户提出修改 → 更新config → AI 修改 HTML → 后处理 → 预览
13. **交付**：用户下载整个 `output/` 目录（HTML + assets 图片），可直接部署

### 模式B：从已有HTML优化
1. 用户上传HTML文件
2. 解析HTML：`python scripts/parse_landing_page.py ./uploaded.html ./config.json`
3. 智能体加载config到上下文
4. 展示解析结果，用户确认
5. 用户提出修改 → 基于config精确修改 → 重新生成
6. 循环直到满意
7. **交付**：打包 `output/` 目录（`index.html` + `assets/` 图片），用户下载完整网站包

### 修改定位规则
| 用户指令 | config字段 |
|---------|-----------|
| "把标语改成xxx" | `product.tagline` |
| "增加功能xxx" | `features`数组append |
| "第三个功能改成xxx" | `features[2]` |
| "删除第二个评价" | `testimonials`数组splice |
| "背景色改成xxx" | `theme.background_color` |

### 用户交互规范

**推荐风格时**：
- ✅ 使用风格名称："经典Hero+Features"、"便当盒式"、"深色沉浸式"、"电影感/硬件流"等
- ✅ 描述风格特点："紫色渐变Hero"、"Bento Grid布局"、"微距特写"、"实时代码终端"
- ❌ 避免暴露：template_id（template-01、template-11等）、模板文件名

**用户请求切换风格**：
- 用户说："换个简单的" → 推荐："极简插画风"风格
- 用户说："要科技感强的" → 推荐："深色赛博风"或"电影感/硬件流"风格
- 用户说："要展示代码的" → 推荐："代码原生型"风格

**内部实现**：
- 智能体内部维护风格名称→template_id的映射
- 对话中使用风格名称，config中使用template_id
- 切换风格时更新config.template_id，但不向用户暴露

## 资源索引

### 脚本
- [generate_landing_page.py](scripts/generate_landing_page.py) - 后处理工具：校验config（基于config-guide.md）+ 注入图片URL + 验证HTML结构
- [parse_landing_page.py](scripts/parse_landing_page.py) - 解析器：从已有HTML提取config（支持全15种模板识别）

### 参考文档
- [index.md](references/index.md) - 模板分类索引与选择指南（风格分派、关键词映射、设计哲学）
- [templates/](references/templates/) - 各模板详细文档（template-01到template-15）
- [template-usage.md](references/template-usage.md) - 模板与Config字段映射关系
- [config-guide.md](references/config-guide.md) - 配置文件格式与字段说明
- [image-generation-guide.md](references/image-generation-guide.md) - 图片动态规划框架（运行时根据产品内容规划图片）
- [aesthetic-enhancement-guide.md](references/aesthetic-enhancement-guide.md) - 美学增强实现指南（CSS/JS代码模板）
- [workflows.md](references/workflows.md) - 对话流程示例（从零开始、从已有HTML优化、含图片等场景）

### 模板库
[template/](template/) - 15种HTML模板代码参考（landing-page-01到landing-page-15）

**注意**：HTML 模板是每种风格的最佳实践标杆——CSS 技巧、动效、响应式、交互模式均经过验证。AI 生成时应以此为质量基线对齐或超越，同时根据具体产品灵活调整，不拘泥于模板的具体数据和布局细节。图片在生成阶段根据用户产品内容动态规划，模板本身不打包任何图片资源。
