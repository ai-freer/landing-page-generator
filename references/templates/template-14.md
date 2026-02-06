# template-14: 浅色虹彩液态玻璃

## ⚠️ 核心原则
**本文档的"美学重点"章节是生成时的首要参考。HTML/CSS技术细节仅作为排版结构和命名规范参考，生成时应以美学高度和视觉冲击力为首要目标，不拘泥于代码细节。**


**设计理念**：
Fluid Glassmorphism / Iridescent 3D - 2024-2025年前沿设计风格。将磨砂玻璃的通透感与流体渐变的动态感完美结合，并引入3D渲染的虹彩/色散效果，创造出既干净专业又极具未来科技感的视觉体验。

**核心隐喻**：
- 液态物质比喻"数据流"（Data Flow）- 流动的渐变层模拟数据在系统中的流动
- 透明玻璃容器比喻"清晰的洞察"（Clear Insights）- 玻璃的通透感代表AI带来的清晰认知

## 结构层级详细拆解

### Section 1: Navigation Bar（悬浮导航栏）
- **结构定义**：顶部的 Flex 布局容器
- **组成**：左侧品牌 Logo + 右侧导航链接（About, Technology, Contact）
- **式样**：极其简约，没有背景色或分割线，文字直接浮在浅色背景上，保持通透感

### Section 2: The Hero Section（核心首屏）
- **结构定义**：Split Layout with Integrated 3D（融合 3D 的分屏布局）
- **Left Column（Text & CTA）**：
  - Headline (H1)：超大字号，深蓝色。强调核心价值 "Data Intelligence, Liquefied."
  - Sub-headline：简短的描述性文字
  - CTA Button：精致的玻璃按钮。带有轻微的蓝色渐变填充、高亮的边缘描边和内部光泽感
- **Right Column（Main Visual）**：
  - Visual Anchor：一个巨大的3D虹彩玻璃球体。球体内部包裹着一个发光的神经网络结构
- **Background Elements**：巨大的、流动的液态玻璃条带在背景中穿插，环绕着文本和球体，增加动态感

### Section 3: Feature Cards（功能卡片区）
- **结构定义**：3-Column Grid（三列网格）
- **Container Style（重点）**：这里采用了扁平、清晰的圆角矩形玻璃面板（Flat, Clear Glass Panels）。面板本身没有扭曲，保持了信息的规整性。
- **Card Content**：
  - Top Icon：每个卡片顶部都有一个精美的 3D 玻璃图标（流体波浪、大脑、棱镜）
  - Title (H3)：深色标题
  - Description：浅灰色描述文本

### Section 4: The Visualization Demo（可视化演示区）
- **结构定义**：Large Full-Width Glass Panel（大型全宽玻璃面板）
- **Container Style**：一个巨大的、扁平的透明玻璃屏幕，边缘清晰锐利
- **Content Visual**：
  - 左侧（Input）：一个 3D 玻璃烧杯正在倒出液态数据
  - 右侧（Output）：数据流入一个抽象的玻璃仪表盘界面，转化为折线图、柱状图和数据指标
- **Metaphor**：极其直观地展示了"原材料数据 → AI 处理 → 清晰图表"的转化过程

### Section 5: Glass Footer（玻璃页脚）
- **结构定义**：底部的一个悬浮玻璃条
- **组成**：左侧是 Logo，右侧是辅助链接
- **式样**：与顶部导航呼应，但增加了一个 subtle 的玻璃背景条，给页面一个清晰的收尾

## 式样与视觉细节定义

### A. 玻璃材质规范

**透明度**：
- 高透，背景模糊度（Blur）较低，更接近水晶而非毛玻璃
- `rgba(255, 255, 255, 0.45-0.6)`

**边缘**：
- 厚重且圆润的高光边缘（Thick, Rounded Rim Light）。这是关键细节，玻璃板和按钮的边缘都有一圈明亮的光晕，强调厚度感
- `border: 1px solid rgba(255, 255, 255, 0.5-0.6)`
- `box-shadow: inset 0 2px 2px rgba(255, 255, 255, 0.6)`

**表面**：
- 光滑如镜，带有锐利的镜面反射（Specular Highlights）
- 多层阴影体系模拟厚度和光泽

**backdrop-filter**：
- `blur(40-50px) saturate(180%)`

### B. 虹彩与色散

**色彩来源**：
- 颜色不是涂在物体上的，而是像光线穿过棱镜一样"折射"出来的

**核心色板**：
- Cyan（青）：#06b6d4
- Magenta（品红）：#a855f7
- Purple（紫）：#ec4899
- Gold（金）：#fbbf24

**应用位置**：
- 主要体现在背景流体、3D图标和玻璃球体的受光面上

### C. 字体与排版

**字体家族**：
- 现代、干净的无衬线体（如 Inter, SF Pro Display, Gilroy）

**色彩层级**：
- **Primary Text（H1, H3）**：深蓝灰色（#1d1d1f），确保在浅色背景上的可读性
- **Secondary Text**：中灰色（#64748b）

### D. 背景系统

**浅色底色**：
- 从#f5f5f7到#e8e8ed的渐变

**流体blob**：
- 4层动态渐变层，不同颜色、位置、动画时长
- 使用`radial-gradient`和`animation`实现流动效果

**网格叠加**：
- 60px间距，透明度0.02，增强科技感

## Config字段要求

### 必需字段
- product.name
- product.tagline

### 推荐字段
- features[]（建议3-6个）
- cta.*

### 配置示例
```json
{
  "template_id": "template-14",
  "product": {
    "name": "DataFlow AI",
    "tagline": "Data Intelligence, Liquefied."
  },
  "features": [
    {
      "title": "Fluid Intelligence",
      "description": "Liquid data processing with crystal-clear insights"
    },
    {
      "title": "Iridescent Design",
      "description": "Stunning 3D glass effects with dynamic color flow"
    },
    {
      "title": "Real-time Analytics",
      "description": "Watch raw data transform into beautiful visualizations"
    }
  ],
  "cta": {
    "button_text": "Get Started"
  }
}
```

## 适用场景
- ✅ 现代SaaS平台
- ✅ 消费级科技产品
- ✅ AI/数据可视化类产品
- ✅ 强调视觉冲击力的产品

## 不适合场景
- ❌ 企业B2B软件（推荐template-01/10）
- ❌ 奢侈品（推荐template-15）
- ❌ 深色主题产品（推荐template-08/12）

## 美学重点
- 🌟 **真实材质渲染**：玻璃的高透、边缘光晕、镜面反射，模拟真实的物理质感
- 💡 **虹彩色散效果**：光线穿过棱镜的自然折射，创造动态色彩变化
- 🎨 **液态流动感**：背景流体的动态渐变，赋予页面呼吸感和生命力
- 🎭 **3D玻璃球体**：神经网络结构的内部包裹，增强视觉焦点
- 📐 **扁平玻璃面板**：保持信息规整性的同时维持通透感
- 🔮 **厚度与层次**：多层阴影体系、backdrop-filter模糊，营造空间深度
