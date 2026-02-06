# 图片动态规划指南（Image Planning Guide）

## 概述

本文档定义了 Landing Page 生成过程中**图片的动态规划策略**。图片内容不是预定义在模板中的，而是根据用户的产品描述、提供的素材和选定的模板，在运行时动态规划生成的。

**核心原则**：
- 模板定义"哪里放图、多大、如何与 CSS 协同"，本指南定义"怎么根据产品内容决定放什么图"
- `template/` 下的 HTML 模板是图片集成的**最佳实践标杆**——不仅要看它放了什么图，更要学习图片如何与布局、动效、CSS 滤镜协同工作

---

## 从模板标杆学习图片集成

每个模板不仅展示了"放什么图"，更展示了**图片如何融入整体设计**。AI 在规划图片时，应先阅读对应模板的 HTML/CSS，理解以下集成模式：

### 物理质感回归派 — 图片是"材质"的载体

| 模板 | 图片集成模式 | AI 生成图片时应注意 |
|------|------------|------------------|
| 深色沉浸式 (08) | 图片叠加体积光渐变、玻璃态遮罩，营造深度感 | 图片应偏暗调，留出上层 CSS 叠加空间，避免高亮区域过多 |
| 电影感/硬件流 (12) | 纯 CSS 光影效果为主，图片是可选的锦上添花 | 若提供图片，应为**微距特写**，配合 CSS `filter` 和 `mix-blend-mode` |
| 浅色虹彩液态玻璃 (14) | 图片置于玻璃球体容器内，`backdrop-filter` 增强质感 | 图片需有透明感或浅色背景，不能太"实"，要配合玻璃容器的半透明效果 |
| 数字工坊/静谧艺廊 (15) | Gallery 横向滚动条、editorial 大图，图片是视觉主角 | 图片质量要求最高：需要**摄影级构图**，明暗对照法（chiaroscuro），全套图片色调统一 |

### 网格化与模块化派 — 图片服务于"容器"

| 模板 | 图片集成模式 | AI 生成图片时应注意 |
|------|------------|------------------|
| 便当盒式 (11) | 图片在 Bento Grid 的某个 cell 中，被裁切为特定比例 | 主体居中，边缘留白可被裁切，避免关键信息在边缘 |
| 多彩层级版 (07) | Hero 分屏布局，图片占据一侧；Zigzag 交替图文 | Hero 图偏方形，Zigzag 图偏横向。每张图色调应与对应色块区域协调 |
| 动态商务风 (10) | 图片在斜切角容器中，可能有几何线条装饰叠加 | 图片应简洁、专业，避免复杂背景与斜切角产生视觉冲突 |

### 展示即交互派 — 图片即"演示"

| 模板 | 图片集成模式 | AI 生成图片时应注意 |
|------|------------|------------------|
| 趣味连接型 (09) | 步骤图在圆角框架中，虚线路径串联 | 每张步骤图应有明确的**单一动作焦点**，风格统一（同一插画/截图风格） |
| 双列布局+视频 (04) | 图文交替左右分屏，视频缩略图带播放按钮 | 配图应与文字内容直接对应（不是装饰，而是"证据"），视频缩略图需有清晰画面 |

### 经典商业风格 — 图片是"第一印象"

| 模板 | 图片集成模式 | AI 生成图片时应注意 |
|------|------------|------------------|
| 经典 Hero+Features (01) | Hero 大图 + 渐变叠加文字 | 图片右下区域需留空给渐变过渡，主体偏左上 |
| 产品展示+CTA (02) | 产品图是视觉焦点，白底/简洁底 | 产品图需**边缘干净**、可融入页面背景，非矩形裁切 |
| 故事讲述型 (03) | 多张图讲述时间线/叙事 | 全套图片应有**叙事连贯性**（同一视觉语言、同一色温） |
| 极简插画风 (06) | 手绘风插画配 Zigzag 布局 | 插画风格必须统一（线条粗细、色彩饱和度、人物/物体风格一致） |
| 深色赛博风 (05) | 深色背景 + 霓虹光效叠加 | 图片应偏暗调，主体带霓虹色边缘光，配合页面的 glow 效果 |

---

## 图片规划流程

```
① 产品分析 → ② 模板标杆研读 → ③ 素材盘点 → ④ 规划决策 → ⑤ 图片获取 → ⑥ AI 生成 HTML + 后处理注入
```

### 步骤详解

#### ① 产品分析
从用户输入中提取关键信息：
- **产品类型**：SaaS、硬件、消费品、课程、开源工具...
- **行业领域**：科技、教育、电商、金融、生活方式...
- **视觉调性**：用户是否有明确偏好（科技感、温暖、极简、奢华...）
- **品牌色彩**：如果用户提供了品牌色，图片应与之协调

#### ② 模板标杆研读
**关键步骤**：阅读选定模板的 `template/landing-page-{N}.html`，不仅识别图片槽位，更要理解：
- 图片容器的 CSS 样式（`border-radius`、`overflow`、`clip-path`）→ 决定图片的裁切方式
- 图片上层的叠加效果（`mix-blend-mode`、`overlay`、渐变遮罩）→ 决定图片的明暗要求
- 图片与周围元素的间距和比例关系 → 决定构图方式
- 图片的 `loading="lazy"` 和响应式策略 → 技术约束

图片槽位速查（`data-slot` 值 → 对应 config 字段）：

| data-slot | 典型尺寸 | 使用模板 | 对应 config 字段 | 说明 |
|-----------|---------|---------|----------------|------|
| `hero` | 1200×600 / 800×800 | 01-11, 14 | `product.image` / `hero.image_url` | 首屏核心视觉 |
| `section` | 400×300 / 600×400 | 06, 07, 10, 14 | `zigzag_sections[].image_url` / `structured_sections[].image_url` | 功能/内容分区配图 |
| `content` | 600×400 | 04 | `content_sections[].image_url` | 双列内容区配图 |
| `step` | 400×300 | 09 | `connected_sections[].image_url` | 步骤配图 |
| `story` | 600×400 | 03 | `story_images[]` | 叙事配图 |
| `immersive` | 1200×600 | 08 | `immersive_section.image_url` | 沉浸式大图 |
| `editorial` | 1200×800 / 1200×600 | 15 | `editorial_images[].url` | 编辑大图 |
| `gallery` | 400×500 | 15 | `gallery_images[].url` | 画廊/作品集 |
| `video-thumbnail` | 600×340 (16:9) | 04 | `video_thumbnail` | 视频封面 |
| — | 80×80 圆形 | 有评价区的模板 | — | 用户评价头像（CSS 处理） |

> **注意**：部分模板（便当盒式、电影感/硬件流、代码原生型）以 CSS 视觉效果为主，图片需求较少或可选。

#### ③ 素材盘点
评估用户提供了什么：

| 用户提供的素材 | 处理方式 |
|--------------|---------|
| 产品截图/照片 | 优先用于 Hero 主图或产品展示位 |
| 品牌 Logo | 用于导航栏品牌区域 |
| 团队照片 | 用于故事讲述型的叙事区域 |
| 参考风格图 | 分析风格调性，指导图片生成 |
| 无任何图片 | 全部由 AI 根据产品描述动态生成 |

#### ④ 规划决策
将槽位与素材匹配，生成**图片规划清单**：

```
图片规划清单：
├── Hero 主图：使用用户提供的产品截图（已有）
├── Feature 配图 ×3：AI 生成（需规划 Prompt）
├── Avatar ×2：AI 生成或使用 SVG 占位符
└── 背景装饰：CSS 渐变处理（无需图片）
```

#### ⑤ 图片获取与落盘
按规划清单逐一获取图片（详见下方"Prompt 生成规则"）。获取后将图片保存到 `output/assets/` 目录，按 `{data-slot类型}-{序号}.{ext}` 命名规则存储（如 `hero.png`、`section-1.png`、`step-2.png`、`gallery-3.jpg`）。

#### ⑥ AI 生成 HTML + 后处理注入
AI 以模板为标杆创作 HTML，图片使用**相对路径** `assets/xxx.png` 引用。将图片路径写入 config 对应字段，然后由 `generate_landing_page.py` 后处理脚本校验 config、注入图片路径到 `data-slot` 标记位、验证 HTML 结构，输出到 `output/index.html`。最终 `output/` 目录即为用户可下载的完整网站包。

---

## 用户素材处理策略

### 场景一：用户提供了完整图片

用户给了足够覆盖所有槽位的图片。

**处理**：
1. 将图片按内容匹配到对应槽位
2. 检查尺寸是否合适，必要时建议裁剪
3. **检查风格与模板集成模式是否兼容**（参考"从模板标杆学习图片集成"）——例如深色沉浸式模板需要偏暗调的图片

### 场景二：用户提供了部分图片

用户给了 1-2 张图，但模板需要更多。

**处理**：
1. 优先将用户图片分配到最重要的槽位（通常是 Hero）
2. 分析用户图片的风格调性（色调、明暗、质感）
3. 剩余槽位生成的图片应**与用户图片风格保持一致**，且**适配模板的 CSS 集成模式**
4. 向用户展示规划方案："您提供的产品截图将用于首屏，其余 3 张配图我来为您生成"

### 场景三：用户未提供任何图片

**处理**：
1. 根据产品描述 + 模板调性 + 模板集成模式，规划所有图片的内容和风格
2. 向用户展示图片规划方案，确认后生成
3. 生成时保持全套图片的**风格一致性**和**叙事连贯性**

### 场景四：用户图片与模板风格不匹配

例如：用户选了"深色沉浸式"模板，但给了一张白底产品图。

**处理**：
1. 提醒用户风格差异，解释模板的图片集成方式（如"深色沉浸式模板会在图片上叠加体积光渐变，白底图效果会不理想"）
2. 建议方案 A：更换为更匹配的模板
3. 建议方案 B：保留模板，对图片进行适当的视觉处理（如调整背景融合度）
4. 用户决定后执行

---

## Prompt 生成规则

当需要 AI 生成图片时，Prompt 由四个维度交叉组合：

```
Prompt = 产品内容描述 + 模板调性关键词 + 图片集成约束 + 槽位技术要求
```

### 维度一：产品内容描述

从 config 中提取，让图片与产品相关：

| 产品类型 | 内容关键词示例 |
|----------|-------------|
| SaaS 工具 | dashboard, analytics, team collaboration, workflow |
| 智能硬件 | device close-up, product photography, premium materials |
| 在线课程 | learning interface, video tutorial, students |
| 电商消费品 | product showcase, lifestyle photography, clean background |
| 开发者工具 | code editor, terminal, API documentation |
| 品牌/故事 | team photo, workshop, behind the scenes |

### 维度二：模板调性关键词

每种模板风格有对应的视觉调性词，生成时必须携带：

| 模板风格 | 调性关键词 |
|----------|-----------|
| 经典 Hero+Features | clean, professional, gradient background, modern UI |
| 产品展示+CTA | product photography, white background, studio lighting |
| 故事讲述型 | warm tones, storytelling, emotional, human-centric |
| 双列布局+视频 | educational, clear, friendly, instructional |
| 深色赛博风 | dark background, neon glow, cyberpunk, futuristic |
| 极简插画风 | illustration, minimal, hand-drawn, pastel colors |
| 多彩层级版 | colorful, geometric shapes, vibrant, layered |
| 深色沉浸式 | dark luxury, volumetric lighting, cinematic, premium |
| 趣味连接型 | playful, connected, cartoon style, orange-yellow |
| 动态商务风 | corporate, dynamic, blue tones, professional |
| 便当盒式 | modular, grid-based, clean UI components |
| 电影感/硬件流 | macro photography, volumetric light, dark, IMAX quality |
| 代码原生型 | code syntax, terminal green, dark theme, developer |
| 浅色虹彩液态玻璃 | iridescent, liquid glass, translucent, soft gradient |
| 数字工坊/静谧艺廊 | editorial, chiaroscuro, gallery, minimal, artistic |

### 维度三：图片集成约束（新增）

根据模板的 CSS 集成方式，对图片本身提出约束：

| 集成模式 | Prompt 约束词 | 适用模板 |
|---------|-------------|---------|
| 渐变叠加 | leave space for gradient overlay, darker edges | 01, 05, 08 |
| 玻璃容器 | soft translucent feel, light background compatible | 14 |
| 斜切/裁切容器 | centered subject, safe margins, clean background | 07, 10 |
| Zigzag 交替 | consistent style across set, alternating compositions | 03, 06, 07 |
| 全幅沉浸 | edge-to-edge composition, no important content at borders | 08, 15 |
| Gallery 序列 | editorial quality, cohesive color palette, varied but unified | 15 |
| 步骤序列 | single action focus per image, uniform style across steps | 09 |
| 微距特写 | extreme close-up, shallow depth of field, dramatic lighting | 12 |

### 维度四：槽位技术要求

根据图片在页面中的位置添加约束：

| 槽位 | 技术要求补充 |
|------|------------|
| Hero 主图 | wide composition, high resolution, 1200x600, 4K quality |
| 产品图（正方形） | centered subject, 800x800, clean edges |
| Feature 配图 | focused, simple composition, 400x300 |
| Gallery 图 | artistic, editorial quality, varied compositions |
| Avatar | portrait, headshot, professional, 80x80 |

### Prompt 组装示例

**场景**：用户做一个"AI 写作助手"的 Landing Page，选了"浅色虹彩液态玻璃"模板，需要 Hero 图。

```
组装过程：
  产品内容   → "AI writing assistant interface, text generation, content creation"
  模板调性   → "iridescent, liquid glass, translucent, soft gradient"
  集成约束   → "soft translucent feel, light background compatible"（玻璃容器模式）
  槽位要求   → "wide composition, high resolution, 1200x600, 4K quality"

最终 Prompt：
  "AI writing assistant interface showing text generation,
   iridescent liquid glass aesthetic, translucent elements with soft gradient background,
   soft translucent feel suitable for glass container overlay,
   wide composition, high resolution, 1200x600, 4K quality, modern and elegant"
```

**场景**：用户做一个"手工腕表"品牌 Landing Page，选了"数字工坊/静谧艺廊"模板，需要 Gallery 序列（5 张）。

```
组装过程：
  产品内容   → "luxury handmade watch, Swiss craftsmanship, leather strap, rose gold"
  模板调性   → "editorial, chiaroscuro, gallery, minimal, artistic"
  集成约束   → "editorial quality, cohesive color palette, varied but unified"（Gallery 序列模式）
  槽位要求   → "artistic, editorial quality, varied compositions"

5 张 Prompt 序列（保持统一调性，变化构图）：
  1. "Luxury watch on wrist in morning light, architectural background, editorial chiaroscuro, warm golden tones, 400x500"
  2. "Watch detail in minimalist interior space, editorial composition, chiaroscuro lighting, 400x500"
  3. "Evening scene with watch at formal dinner, dramatic lighting, editorial quality, warm tones, 400x500"
  4. "Close-up of leather strap and rose gold clasp, macro detail, chiaroscuro, editorial, 400x500"
  5. "Watch in afternoon sunlight, soft shadows, contemplative mood, editorial, unified color palette, 400x500"
```

> **序列图片的关键**：每张的色温、明暗对比、拍摄风格保持统一，构图角度和场景变化。

---

## 无图片模板的处理

以下模板以 CSS 视觉效果为主，**可以完全不依赖外部图片**：

| 模板 | CSS 视觉方案 | 图片策略 |
|------|-------------|---------|
| 便当盒式 (11) | CSS Grid + 色块 + 渐变 | 可选：Hero 区域可添加产品截图提升说服力 |
| 电影感/硬件流 (12) | CSS 光影 + 体积光效果 | 可选：产品微距特写可极大提升效果（需配合 `mix-blend-mode`） |
| 代码原生型 (13) | 代码高亮 + 终端模拟 | 通常不需要图片 |
| 浅色虹彩液态玻璃 (14) | CSS 渐变 + backdrop-filter | 可选：3D 渲染图可增强玻璃质感（需透明/半透明底） |
| 数字工坊/静谧艺廊 (15) | CSS 明暗对照 + 艺术效果 | **强烈推荐**：Gallery 图是此模板的视觉核心，没有图片效果大打折扣 |

---

## 图片质量标准

基于模板最佳实践总结的质量基线：

### 风格一致性
- 同一页面内所有图片的**色温、饱和度、对比度**应统一
- 多图序列（zigzag、gallery、steps）需要**视觉叙事连贯性**
- 用户提供的图片和 AI 生成的图片之间不能有明显的风格断裂

### 与 CSS 效果的协同
- 图片不是孤立元素——它会被 CSS 滤镜、混合模式、遮罩、裁切容器处理
- 暗色模板的图片应留出**暗边过渡区域**，避免被渐变叠加后主体不可见
- 玻璃/透明效果模板的图片应偏**浅色/半透明**，不能太"实"

### 构图安全区
- Hero 图在移动端会被裁切——**主体不要贴边**
- 被圆角/斜切容器裁切的图片——**关键信息保持在中心 80% 区域内**
- Gallery 图在横向滚动中只展示部分——**每张图独立可看**

---

## CSS 降级方案

所有模板必须配置 CSS 渐变背景作为图片加载失败时的降级：

```css
/* 通用降级 */
.hero-image img,
.content-image img {
    background: linear-gradient(135deg, 
        rgba(var(--primary-rgb), 0.08), 
        rgba(var(--secondary-rgb), 0.08));
    min-height: 300px;
    object-fit: cover;
}
```

### 风格配色对照

| 风格调性 | 降级渐变色 A | 降级渐变色 B |
|---------|------------|------------|
| 紫色渐变 | `rgba(102,126,234, 0.08)` | `rgba(118,75,162, 0.08)` |
| 蓝色科技 | `rgba(66,153,225, 0.08)` | `rgba(49,130,206, 0.08)` |
| 赛博霓虹 | `rgba(0,242,255, 0.05)` | `rgba(124,58,237, 0.05)` |
| 暖色柔和 | `rgba(255,176,136, 0.06)` | `rgba(196,181,253, 0.06)` |
| 深蓝/金色 | `rgba(44,82,130, 0.08)` | `rgba(236,201,75, 0.06)` |

---

## 图片技术规格

### 文件格式
- **PNG**：支持透明背景，适合 Logo、UI 截图
- **JPEG/WebP**：适合照片类，文件更小
- **SVG**：适合图标、头像占位符

### 分辨率建议
- **Hero 图片**：1200-1920px 宽度
- **产品图**：800-1000px 宽度
- **配图/Feature 图**：400-600px 宽度
- **图标/头像**：80-200px

### 文件大小控制
- **Hero 图片**：< 300KB
- **产品图**：< 200KB
- **配图**：< 100KB
- **图标/头像**：< 50KB

### HTML 最佳实践
```html
<!-- 懒加载（非首屏图片） -->
<img src="feature.jpg" loading="lazy" alt="产品功能展示">

<!-- 响应式图片 -->
<img src="hero-1200.jpg" 
     srcset="hero-600.jpg 600w, hero-900.jpg 900w, hero-1200.jpg 1200w"
     sizes="(max-width: 768px) 100vw, 1200px"
     alt="产品展示">
```

---

## 向用户展示图片规划

在生成前，应向用户清晰展示图片规划方案，说明每张图片的**用途、来源和生成策略**：

```
图片规划方案：

1. Hero 主图 (1200×600)
   → 使用您提供的产品截图
   → 集成方式：顶部渐变叠加，图片暗边过渡到背景色
   
2. 功能配图 ×3 (400×300)
   → AI 生成（风格与您的截图保持一致）：
     - "实时协作"：团队协作界面截图风格
     - "数据分析"：数据仪表盘截图风格
     - "安全加密"：安全盾牌图标风格

3. 用户头像 ×2 (80×80)
   → 使用 SVG 占位符（圆形渐变）

确认后开始生成，您也可以调整任意一项。
```

这样用户对最终效果有预期，也有机会在生成前调整方向。
