# template-12: 电影感/硬件流（Cinematic Hardware）

## ⚠️ 核心原则
**本文档的"美学重点"章节是生成时的首要参考。HTML/CSS技术细节仅作为排版结构和命名规范参考，生成时应以美学高度和视觉冲击力为首要目标，不拘泥于代码细节。**


**设计理念**：
采用Rabbit R1和Humane Pin带火的"电影感硬件流"风格，把软件当做"精密仪器"来卖，极度强调光影质感和物理世界的连接。核心是"微距特写"的Hero区域，展示产品的精密细节，配合滚动叙事和超大号字体，营造电影般的视觉冲击。

**设计风格**：Monochromatic Black（单色黑）+ Volumetric Lighting（体积光）
- 极致的黑底（#000000），配合银色、冷灰色的文字
- Volumetric Lighting：模拟真实摄影棚的打光，产品边缘有高光反射
- Grotesk / Monospace字体：结合无衬线字体（现代感）和等宽字体（代码/机器感）

## 结构组成

### 1. Macro Close-up（微距特写）- 滚动叙事（Scrollytelling）
- **结构定义**：全屏极其清晰的3D渲染图或实拍图
- **聚焦细节**：聚焦在产品的某个局部（如AI的"眼睛"/摄像头/光圈）
- **滚动交互**：随着用户向下滚动，产品模型在3D空间中旋转、拆解、组合
- **内容**：
  - 产品名称和标语
  - 滚动指示器
- **作用**：展示产品的精密细节，营造电影感

### 2. Typography as Image（文字即图像）
- **结构定义**：巨大的、甚至溢出屏幕的超大号字体（Display Typography）
- **视觉冲击**：短促有力的单词，如"UNSEEN", "PRECISION", "INTELLIGENCE"
- **悬停交互**：文字悬停时有渐变效果和缩放动画
- **内容**：配合简短的功能描述
- **作用**：用文字本身作为视觉元素，强化品牌理念

### 3. Dark Mode Specs（暗黑参数表）
- **结构定义**：类似相机参数表的精密排版
- **视觉特征**：使用极细的线条分割
- **内容**：罗列模型参数、算力、响应速度
- **悬停交互**：悬停时高亮显示
- **作用**：展示技术参数，强调精密和专业性

### 4. Features Grid（可选）
- **结构定义**：编号的功能卡片
- **字体特征**：等宽字体展示描述
- **悬停交互**：悬停时顶部出现渐变线条
- **作用**：展示产品核心功能

### 5. CTA Section（可选）
- **结构定义**：简洁的CTA提示
- **悬停交互**：悬停时出现光晕效果
- **作用**：引导转化

## 配置要点

### 必需字段
- product.name
- product.tagline

### 推荐字段
- hero.stats[]（精密参数表）
- features[]（核心功能）
- cta.*

### 技术参数示例
```yaml
hero:
  stats:
    - label: Processor
      value: Neural Engine X1
    - label: Compute Power
      value: 40 TOPS
    - label: Latency
      value: < 50ms
    - label: Power Consumption
      value: 5W (typical)
    - label: Sensors
      value: 108MP Camera + LiDAR
    - label: Connectivity
      value: Wi-Fi 7 + 5G
    - label: Battery Life
      value: Up to 24 hours
    - label: Storage
      value: 256GB + Cloud
    - label: Dimensions
      value: Φ 45mm × 12mm
    - label: Weight
      value: 42g
```

### features配置示例
```yaml
features:
  - title: Neural Processing
    description: Advanced AI chip delivers 40 TOPS of compute power
  - title: Ultra-Low Latency
    description: Sub-50ms response time for instant interactions
  - title: Precision Sensors
    description: 108MP camera with LiDAR for depth perception
  - title: All-Day Battery
    description: 24-hour battery life with intelligent power management
  - title: Cloud Integration
    description: Seamless sync with cloud storage and services
  - title: Always On
    description: Voice-activated and always ready to assist
```

## 技术特点
- 🎨 CSS Grid布局：参数表使用grid布局
- ✨ 体积光效果：CSS radial-gradient模拟真实摄影棚打光
- 🌊 滚动触发动画：JavaScript监听scroll事件，触发模型旋转
- 💫 视差效果：超大字体随滚动产生视差移动
- 🎯 精密排版：极细线条分割，类似相机参数表
- 📊 等宽字体：Courier New等宽字体展示技术参数
- 🎭 悬停效果：渐变线条、光晕、缩放动画

## 视觉风格建议
- 🎨 配色方案：
  - 主色调：纯黑（#000000）+ 银色（#c0c0c0）
  - 强调色：冷灰色（#a0a0a0）+ 凉蓝色（#b0c4de）
  - 文字色：白色（#ffffff）+ 灰色（#808080）
  - 边框色：极细线条（rgba(255, 255, 255, 0.1)）
- 📝 字体：
  - 标题：Inter / Grotesk（现代无衬线）
  - 技术：Courier New / SF Mono（等宽字体）
  - 字重：800（Display Typography）+ 400（Body）
- 🖼️ 图片：高质量的产品3D渲染图或实拍图
- ⚪ 圆角：少量使用，保持硬朗线条
- 💫 阴影：极简阴影，强调光影质感
- 📐 布局：全屏Hero + 居中大字 + 表格参数
- 🎯 对比：极致黑底+银色文字形成强对比

## 使用建议
- ✅ 适合AI硬件产品（如Rabbit R1、Humane Pin）
- ✅ 适合高端消费级应用
- ✅ 适合具身智能产品
- ✅ 适合需要展示精密技术参数的产品
- ✅ 适合强调物理质感和光影效果的产品
- ❌ 不适合SaaS软件产品（推荐template-01/07）
- ❌ 不适合极简风格产品（推荐template-05）
- ❌ 不适合情感化叙事为主的产品（推荐template-06）

## 示例场景
- AI硬件设备的Landing Page（如AI Pin、AI眼镜）
- 高端消费级智能硬件的推广页面
- 具身智能机器人的产品页
- 精密仪器的营销页面

## 技术集成建议
- 3D引擎：可集成Three.js或React Three Fiber加载GLTF模型
- 滚动触发：可使用GSAP ScrollTrigger控制滚动时的模型动画
- 性能优化：大量使用CSS动画，减少JavaScript计算

## 美学重点
- 🎬 **电影级视觉冲击**：微距特写、超大字体、精密排版，每一帧都像电影画面
- 💡 **体积光效果**：模拟真实摄影棚打光，边缘高光反射，营造真实空间感
- 🌊 **滚动叙事**：3D模型随滚动旋转拆解，增强叙事沉浸感
- 📊 **暗黑参数表**：精密技术参数，强化专业感和精密仪器气质
- 🎭 **Display Typography**：文字即图像，超大字号冲击力，文字本身成为视觉焦点
- ⚫ **极致黑底**：纯黑背景+银色文字，奢华感强烈，营造高端定位
- 🎯 **光影质感**：每一像素都精心雕琢，光影、材质服务于"奢华"和"精密"的视觉感受
