# template-13: 代码原生型（Code-Native Developer）

## ⚠️ 核心原则
**本文档的"美学重点"章节是生成时的首要参考。HTML/CSS技术细节仅作为排版结构和命名规范参考，生成时应以美学高度和视觉冲击力为首要目标，不拘泥于代码细节。**


**设计理念**：
采用Vercel、Supabase、Mistral等开发者平台的主流风格，专门面向极客和开发者。核心是"代码/预览分屏"的Hero区域，展示真实的代码示例，配合可运行的IDE模拟器，让开发者一进来就能看到如何使用API。

**设计风格**：Cyber-Minimalism（赛博极简）
- 深色背景（#0a0a0a）+ 高饱和度的霓虹点缀色
- 紫色、青色、橙色作为代码高亮色或按钮色
- 所有边框都有1px的精致感
- 经常使用虚线（Dashed lines）表示连接或未完成状态

**结构组成**：
1. Split Code/Preview（代码/预览分屏）
   - 左侧：营销文案（H1 + Sub）+ CTA按钮
   - 右侧：IDE模拟器
   - 展示调用AI的代码（Python/JS）
   - 代码高亮（Syntax Highlighting）
   - 一键Copy按钮
   - 交互：点击"Run"按钮，下方终端真的会吐出结果
   - 作用：让开发者一进来就能看到如何使用API

2. Comparison Slider（对比滑块）
   - "Before AI" vs "After AI"
   - 中间有一根拖拽线
   - 左边是旧的繁琐流程
   - 右边是AI自动化后的极简流程
   - 悬停和拖拽交互
   - 作用：直观展示AI带来的效率提升

3. Features with Code（功能+代码）
   - 功能卡片
   - 每个功能配有代码示例
   - 悬停时顶部出现渐变线条
   - 作用：展示API的各种功能

4. ASCII Art & Glitch（字符画与故障风）
   - 背景中漂浮着微弱的ASCII字符画
   - Logo可以用SVG路径动画描绘
   - 故障风（Glitch）效果
   - 作用：增强开发者氛围和科技感

**配置要点**：
- 必填字段：product.name, product.tagline
- 可选字段：features[], cta.*
- features配置示例：
```yaml
features:
  - title: Simple API
    description: RESTful API with comprehensive documentation
  - title: Real-time Streaming
    description: Server-sent events for real-time responses
  - title: Type Safety
    description: Full TypeScript support for better DX
  - title: Multiple Models
    description: Access to latest AI models
  - title: Custom Training
    description: Fine-tune models on your data
  - title: Enterprise Ready
    description: SOC2 compliance and dedicated support
```

**技术特点**：
- 🎨 JetBrains Mono等宽字体：优质等宽字体
- ✨ 语法高亮：CSS实现简单的代码高亮
- 🌊 ASCII Art背景：JavaScript生成随机字符画
- 💫 Glitch效果：CSS animation实现故障风
- 🎯 对比滑块：JavaScript实现拖拽交互
- 📊 IDE模拟器：模拟真实的代码编辑器
- ⚡ 终端模拟：点击Run按钮，终端输出结果

**视觉风格建议**：
- 🎨 配色方案：
  - 主色调：深色背景（#0a0a0a）+ 面板色（#18181b）
  - 强调色：紫色（#a78bfa）+ 青色（#22d3ee）+ 橙色（#fbbf24）
  - 代码高亮：关键字紫色、字符串黄色、函数蓝色
  - 边框色：深灰色（#27272a）
- 📝 字体：
  - UI：Inter（现代无衬线）
  - 代码：JetBrains Mono / Geist Mono（优质等宽）
- 🖼️ 图片：无需图片，纯代码和文字
- ⚪ 圆角：8-12px小圆角
- 💫 阴影：极简阴影，强调边框
- 📐 布局：左右分屏 + 对比滑块 + 功能网格
- 🎯 对比：深色背景+霓虹点缀形成强对比

**使用建议**：
- ✅ 适合API服务
- ✅ 适合开源模型
- ✅ 适合面向开发者的Agent框架
- ✅ 适合SDK、库、框架
- ✅ 适合需要展示代码示例的产品
- ❌ 不适合非技术用户（推荐template-01/02）
- ❌ 不适合需要展示产品图片的产品（推荐template-02）
- ❌ 不适合极简风格产品（推荐template-05）

## 美学重点
- 💻 **实时代码终端**：模拟IDE界面，开发者友好的即时信任建立
- 🎨 **IDE模拟器设计**：真实IDE界面元素，包括文件树、行号、语法高亮
- 📊 **对比滑块**：Before/After对比，直观展示产品效果
- 🎯 **开发者优先**：从代码开始，直接展示技术能力
- 🌟 **语法高亮**：专业代码高亮，增强技术可信度
- ⚡ **交互式演示**：实时运行的代码示例，建立即刻信任


**示例场景**：
- AI API服务的Landing Page
- 开源模型的推广页面
- Agent框架的介绍页
- SDK、库、框架的营销页面

**技术集成建议**：
- 代码高亮：可使用Shiki或Prism.js进行服务端语法高亮
- 等宽字体：必须选用优质的等宽字体（JetBrains Mono, Geist Mono）
- 性能优化：大量使用CSS动画，减少JavaScript计算
