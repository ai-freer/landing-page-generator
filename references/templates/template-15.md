# template-15: 数字工坊/静谧艺廊

## ⚠️ 核心原则
**本文档的"美学重点"章节是生成时的首要参考。HTML/CSS技术细节仅作为排版结构和命名规范参考，生成时应以美学高度和视觉冲击力为首要目标，不拘泥于代码细节。**


**设计理念**：
与SaaS/AI完全相反的奢侈品逻辑 - 追求渴望感(Desire)、排他性(Exclusivity)、沉浸感(Immersion)和仪式感(Ritual)。我们不卖"功能"，我们卖"梦境"和"身份"。

**适用场景**：
- 豪华电动车（Lucid, Polestar）
- 高级珠宝（Cartier, Tiffany）
- 高端腕表
- 设计师家具

## 结构层级详细拆解

### Section 1: The Cinematic Reveal（电影级揭幕）
- **结构定义**：Zero UI / Immersive Video（零 UI / 沉浸视频）
- **内容**：
  - 没有巨大的标题，没有喧闹的按钮
  - 全屏播放一段极高画质、慢节奏的视频。光线缓慢扫过产品的轮廓（车身流线或钻石切面）
  - 交互：唯一的 UI 是底部的极简品牌 Logo 和一个微弱的"向下探索"指示器
- **心理学**：这种"留白"和"慢"传达了自信。只有顶级品牌才敢在首屏不说话

### Section 2: The Editorial Narrative（杂志式叙事）
- **结构定义**：Asymmetrical Typography（非对称排版）
- **布局**：类似高端时尚杂志（如 Vogue 或 Kinfolk）
- **左侧**：大面积留白
- **右侧**：一段精雕细琢的衬线体 (Serif) 文字，字号较小，行间距极大。讲述设计哲学而非参数
- **视觉**：配一张非居中的、艺术感极强的局部特写图（如车灯内部的纹理，或戒指的镶嵌工艺）

### Section 3: The "Tactile" Detail（触感交互区）
- **结构定义**：Interactive Macro Zoom（交互式微距缩放）
- **核心**：展示"工艺（Craftsmanship）"
- **交互**：这是一个巨大的图片区域。当用户移动鼠标时，像放大镜一样查看产品的极致细节（皮革的缝线、金属的拉丝）
- **配文**：极简的标注，如"Nappa Leather, Hand-stitched"

### Section 4: The Gallery Strip（横向艺廊）
- **结构定义**：Horizontal Scroll（横向滚动）
- **页面滚动逻辑**在此处暂时变为横向
- 像在画廊看画一样，一张张极高水准的生活方式摄影作品（Lifestyle Photography）缓缓滑过
- **氛围**：展示产品在真实高端场景中的样子（停在现代建筑前的车，晚宴上的珠宝）

### Section 5: The "Concierge" CTA（礼宾式转化）
- **结构定义**：Minimalist Invitation（极简邀约）
- **拒绝**：不要用 "Buy Now"（立即购买）这种廉价的词
- **采用**：Inquire（咨询）、Reserve（预定）、Configure（配置）、Locate a Boutique（查找精品店）
- **式样**：按钮通常是细线描边（Outline）或纯文字链接，带有优雅的下划线动画

## 式样与视觉分析

### A. 字体策略

**主标题（Headlines）**：
- Elegant Serif（优雅衬线体）
- 如 Didot, Bodoni, GT Super, Playfair Display
- 这种字体有粗细对比，自带历史感和贵族气

**正文/参数（Body）**：
- Premium Sans-Serif（高级无衬线体）
- 如 Helvetica Now, Graphik, Inter
- 保持现代感和易读性

### B. 色彩与光影

**底色 - "Old Money" Colors（老钱风色调）**：
- 深炭灰（Charcoal）：#1a1a1a
- 暖铂金（Warm Platinum）：#e8e4dc
- 午夜蓝（Midnight Blue）：#1e293b
- 象牙白（Ivory）：#f5f5f0

**避免**：
- 纯黑（#000）或纯白（#FFF）
- 使用 #1a1a1a 或 #f5f5f0 这种更有质感的颜色

**光影逻辑 - Chiaroscuro（明暗对照法）**：
- 像伦勃朗的画一样，背景压暗，只用一束光打亮产品的轮廓
- 营造神秘感和戏剧性

### C. 节奏与动效

**慢（Slow）**：
- 所有的动效时长（Duration）都要拉长
- 比如图片淡入需要 1.2秒，而不是普通的 0.3秒

**Parallax（视差）**：
- 图片和文字滚动的速度不同步，产生一种深邃的空间感

**缓动函数**：
- `cubic-bezier(0.25, 0.1, 0.25, 1)` - 奢华优雅

## Config字段要求

### 必需字段
- product.name
- product.tagline

### 推荐字段
- features[]（建议3-6个，强调工艺和 exclusivity）
- cta.*（建议使用"Inquire"、"Reserve"等词汇）
- gallery_images[]（建议5-10张高质量生活方式摄影）

### 配置示例
```json
{
  "template_id": "template-15",
  "product": {
    "name": "Luxury Time",
    "tagline": "传承百年的工艺"
  },
  "features": [
    {
      "title": "Craftsmanship",
      "description": "Hand-stitched Nappa leather with 48 hours of meticulous work"
    },
    {
      "title": "Heritage",
      "description": "Over 100 years of traditional craftsmanship meets modern innovation"
    },
    {
      "title": "Exclusivity",
      "description": "Limited to 50 pieces worldwide, each numbered and certified"
    }
  ],
  "gallery_images": [
    {
      "url": "https://example.com/gallery1.jpg",
      "caption": "Product showcased in modern architecture"
    },
    {
      "url": "https://example.com/gallery2.jpg",
      "caption": "Elegant lifestyle photography"
    }
  ],
  "cta": {
    "button_text": "Inquire"
  }
}
```

## 特殊注意事项

### CTA用词
- ✅ 推荐：Inquire（咨询）、Reserve（预定）、Configure（配置）、Locate a Boutique（查找精品店）
- ❌ 避免：Buy Now（立即购买）、Purchase（购买）、Add to Cart（加入购物车）

### 图片要求
- 画廊图片需要高质量、专业的生活方式摄影
- 建议WebP/AVIF格式
- 展示产品在高端场景中的样子

## 适用场景
- ✅ 高端消费品
- ✅ 奢侈品品牌
- ✅ 豪华汽车
- ✅ 高级珠宝/腕表
- ✅ 设计师家具

## 不适合场景
- ❌ SaaS/AI产品（推荐template-01/14）
- ❌ 消费级科技（推荐template-02/14）
- ❌ 需要转化率的产品（推荐template-01）

## 美学重点
- 🖼️ **零UI设计**：极致克制，去除所有装饰性UI元素，纯粹的内容展示
- 💡 **明暗对照法**：强光影对比，营造电影级视觉冲击
- 🎭 **奢华动效**：丝滑缓动、微妙悬停，奢华感源于克制
- 📸 **生活方式摄影**：高端场景中的产品展示，营造奢华氛围
- 🏛️ **艺术画廊美学**：极简布局、大量留白，如静谧艺廊
- 🎯 **高端定位**：通过克制和精致，传递品牌的价值感

