# 配置文件格式指南

## ⚠️ 重要提示
**本指南仅说明Config字段的定义和格式约束，用于数据验证和解析。生成HTML时应以美学高度和视觉冲击力为首要目标，不拘泥于代码细节。**

## ⚠️ 用户交互提示
**与用户对话时，使用风格名称（如"经典Hero+Features"、"便当盒式"等）推荐和描述风格。template_id仅作为内部标识符传递给脚本，不应向用户暴露模板编号。**

## 目录
- [图片路径规范](#图片路径规范)
- [配置文件结构](#配置文件结构)
- [字段详细说明](#字段详细说明)
- [配置示例](#配置示例)
- [验证规则](#验证规则)

## 图片路径规范

Config 中所有图片相关字段（`product.image`、`hero.image_url`、`*_images[].url`、`image_url` 等）支持两种路径格式：

### 本地相对路径（推荐）

```
assets/hero.png
assets/section-1.png
assets/gallery-3.jpg
```

- **适用场景**：AI 生成的图片、用户上传后落盘的图片
- **命名规则**：`assets/{data-slot类型}-{序号}.{ext}`（如 `assets/hero.png`、`assets/step-2.png`）
- **优势**：交付包自包含，用户下载 `output/` 目录即可离线使用，无外部依赖
- **要求**：图片文件必须存在于 `output/assets/` 目录中

### 外部 URL（可选）

```
https://example.com/product-image.jpg
https://cdn.example.com/hero.png
```

- **适用场景**：用户直接提供的在线图片链接
- **注意**：外部 URL 依赖网络，**建议在最终交付前将外部图片下载到 `output/assets/` 并转为本地路径**，确保交付包完整性

### 最终交付标准

| 阶段 | 允许的路径格式 | 说明 |
|------|--------------|------|
| 对话过程中 | 本地路径 + 外部 URL 均可 | 用户可随时提供 URL，AI 随时生成本地图片 |
| 最终交付时 | **仅本地相对路径** | `output/` 目录应完全自包含，所有图片在 `output/assets/` 中 |

## 配置文件结构

配置文件采用JSON格式，以下是完整的结构定义：

```json
{
  "template_id": "string",
  "product": {
    "name": "string",
    "tagline": "string",
    "description": "string",
    "image": "string (图片路径)",
    "price": "string",
    "info": ["string", ...]
  },
  "features": [
    {
      "title": "string",
      "description": "string"
    }
  ],
  "content_sections": [
    {
      "title": "string",
      "description": "string",
      "media_placeholder": "string"
    }
  ],
  "story": {
    "origin": "string",
    "journey": "string",
    "mission": "string",
    "why_us": "string"
  },
  "story_images": ["string (图片路径)", "..."],
  "video_embed": "string",
  "video_thumbnail": "string (图片路径)",
  "editorial_images": [
    {
      "url": "string (图片路径)",
      "caption": "string"
    }
  ],
  "mock_data": {
    "testimonials": [
      {
        "quote": "string",
        "author": "string"
      }
    ],
    "stats": [
      {
        "value": "string",
        "label": "string"
      }
    ]
  },
  "theme": {
    "primary_color": "string (hex)",
    "secondary_color": "string (hex)",
    "background_color": "string (hex)",
    "text_color": "string (hex)"
  }
}
```

## 字段详细说明

### 根级字段

**template_id（必需）**
- 类型：string
- 可选值："template-01" 到 "template-15"
- 示例："template-01"

**完整模板列表**：
- template-01: 经典Hero+Features
- template-02: 产品展示+CTA
- template-03: 故事讲述型
- template-04: 双列布局+视频
- template-05: 深色赛博风
- template-06: 极简插画风
- template-07: 多彩层级版
- template-08: 深色沉浸式
- template-09: 趣味连接型
- template-10: 动态商务风
- template-11: 便当盒式
- template-12: 电影感/硬件流
- template-13: 代码原生型
- template-14: 浅色虹彩液态玻璃
- template-15: 数字工坊/静谧艺廊

### product对象（必需）

**product.name（必需）**
- 类型：string
- 长度限制：2-50字符
- 示例："TaskFlow Pro"

**product.tagline（必需）**
- 类型：string
- 长度限制：10-100字符
- 示例："让团队协作更高效"

**product.description（必需）**
- 类型：string
- 长度限制：50-500字符
- 示例："TaskFlow Pro是一款强大的项目管理工具，帮助团队高效协作，提升生产力。"

**product.image（可选）**
- 类型：string（图片路径，详见[图片路径规范](#图片路径规范)）
- 来源：AI 动态生成并落盘到 `output/assets/`，或用户提供的图片 URL
- 适用模板：所有含产品图展示位的模板（如 template-02, template-03 等）
- 示例：`"assets/hero.png"`（本地路径，推荐）或 `"https://example.com/product-image.jpg"`（外部 URL）

**product.price（可选）**
- 类型：string
- 适用模板：template-02
- 示例："¥199", "$29/month"

**product.info（可选）**
- 类型：array of strings
- 适用模板：template-05
- 示例：["功能1", "功能2", "功能3"]

### features数组（可选但推荐）

**features[].title（必需）**
- 类型：string
- 长度限制：2-30字符
- 示例："实时协作"

**features[].description（必需）**
- 类型：string
- 长度限制：10-200字符
- 示例："团队成员可以同时编辑同一份文档"

**建议**：提供3-6个核心功能

### content_sections数组（可选）

**content_sections[].title（必需）**
- 适用模板：template-04
- 示例："核心功能介绍"

**content_sections[].description（必需）**
- 适用模板：template-04

**content_sections[].media_placeholder（必需）**
- 适用模板：template-04
- 示例："图片占位符"

**建议**：提供2-4个内容段落

### story对象（可选）

**story.origin（必需）**
- 适用模板：template-03
- 示例："我们的故事从2018年开始..."

**story.journey（必需）**
- 适用模板：template-03

**story.mission（必需）**
- 适用模板：template-03

**story.why_us（必需）**
- 适用模板：template-03

### story_images数组（可选，template-03专用）

- 类型：array of strings（图片路径，详见[图片路径规范](#图片路径规范)）
- 对应 HTML 中 `data-slot="story"` 的图片槽位
- 来源：AI 动态生成并落盘，或用户提供的品牌/故事图片
- 建议：提供2张，分别对应"起源"和"使命"叙事场景
- 示例：`["assets/story-1.png", "assets/story-2.png"]`

### video_embed（可选）

- 适用模板：template-04
- 示例："https://www.youtube.com/embed/VIDEO_ID"

### video_thumbnail（可选，template-04专用）

- 类型：string（图片路径，详见[图片路径规范](#图片路径规范)）
- 对应 HTML 中 `data-slot="video-thumbnail"` 的图片槽位
- 来源：视频封面截图或 AI 生成并落盘
- 示例：`"assets/video-thumbnail.png"`

### mock_data对象（可选但推荐）

**mock_data.testimonials数组（推荐）**
- 字段：quote（引用）、author（作者）
- 建议：提供3-6个用户评价

**mock_data.stats数组（可选）**
- 字段：value（数值）、label（标签）

### zigzag_sections数组（可选，template-06专用）

- 字段：title、description、image_url（图片路径，详见[图片路径规范](#图片路径规范)）、image_position（left/right）
- 建议：提供3个zigzag_sections，依次使用right/left/right
- image_url 示例：`"assets/section-1.png"`（本地路径，推荐）或 `"https://example.com/image.jpg"`

### faq数组（可选，template-06专用）

- 字段：question、answer
- 建议：提供3-6个常见问题

### cta对象（可选，多个模板通用）

- cta.title：CTA区域标题（template-06, 11, 14, 15）
- cta.subtitle：CTA区域副标题（template-06, 11, 14, 15）
- cta.button_text：CTA按钮文字（所有模板）

### footer对象（可选，多个模板通用）

- footer.tagline：品牌标语（template-05, 14, 15）
- footer.social_links：社交媒体链接数组（template-06, 07）

### input_placeholder对象（可选，template-11专用）

- input_placeholder.default：输入框占位符文本

### code_snippets数组（可选，template-13专用）

- 字段：language、code
- 建议：提供2-4个代码示例

### gallery_images数组（可选，template-15专用）

- 字段：url（图片路径，详见[图片路径规范](#图片路径规范)）、caption
- 对应 HTML 中 `data-slot="gallery"` 的图片槽位
- 来源：AI 根据产品调性动态生成并落盘，或用户提供的作品集图片
- 建议：提供5-10张高质量图片，风格与模板"数字工坊/静谧艺廊"的艺术调性一致
- url 示例：`"assets/gallery-1.png"`

### editorial_images数组（可选，template-15专用）

- 字段：url（图片路径，详见[图片路径规范](#图片路径规范)）、caption
- 对应 HTML 中 `data-slot="editorial"` 的图片槽位
- 来源：AI 动态生成并落盘，或用户提供的编辑级大图
- 建议：提供2张高质量大幅图片（1200×800 / 1200×600），配合模板的明暗对照法（chiaroscuro）艺术风格
- url 示例：`"assets/editorial-1.png"`

### hero对象（可选，template-07/08专用）

- hero.image_url：首屏右侧插图路径（图片路径，详见[图片路径规范](#图片路径规范)）
- 示例：`"assets/hero.png"`（本地路径，推荐）或 `"https://example.com/hero.jpg"`

### immersive_section对象（可选，template-08专用）

- 字段：title、description、image_url（图片路径，详见[图片路径规范](#图片路径规范)）
- image_url 示例：`"assets/immersive.png"`

### connected_sections数组（可选，template-09专用）

- 字段：title、description、image_url（图片路径，详见[图片路径规范](#图片路径规范)）
- image_url 来源：AI 动态生成并落盘，或用户提供
- image_url 示例：`"assets/step-1.png"`
- 建议：提供3个步骤

### structured_sections数组（可选，template-10专用）

- 字段：title、description、image_url（图片路径，详见[图片路径规范](#图片路径规范)）
- image_url 来源：AI 动态生成并落盘，或用户提供
- image_url 示例：`"assets/section-1.png"`
- 建议：提供3个区块

### theme对象（可选）

- theme.primary_color：主色调（#RRGGBB）
- theme.secondary_color：次要色调（#RRGGBB）
- theme.background_color：背景色（#RRGGBB）
- theme.text_color：文字颜色（#RRGGBB）

## 配置示例

### 示例1：SaaS产品（template-01）

```json
{
  "template_id": "template-01",
  "product": {
    "name": "TaskFlow Pro",
    "tagline": "让团队协作更高效",
    "description": "TaskFlow Pro是一款强大的项目管理工具，帮助团队高效协作，提升生产力。支持实时协作、任务分配、进度跟踪等功能。"
  },
  "features": [
    {
      "title": "实时协作",
      "description": "团队成员可以同时编辑同一份文档，所有更改实时同步"
    },
    {
      "title": "任务管理",
      "description": "轻松创建、分配和跟踪任务，确保项目按时完成"
    },
    {
      "title": "数据洞察",
      "description": "丰富的报表和仪表板，帮助团队了解项目进展"
    }
  ],
  "mock_data": {
    "testimonials": [
      {
        "quote": "TaskFlow Pro帮助我们团队效率提升了50%！",
        "author": "李四，科技公司项目经理"
      },
      {
        "quote": "界面简洁，功能强大，非常好用！",
        "author": "王五，初创公司CEO"
      }
    ]
  }
}
```

### 示例2：电商产品（template-02）

```json
{
  "template_id": "template-02",
  "product": {
    "name": "智能手表 Pro",
    "tagline": "健康生活，从手腕开始",
    "description": "智能手表Pro集成了健康监测、运动追踪、智能提醒等功能，24小时陪伴您的健康生活。",
    "image": "assets/hero.png",
    "price": "¥1,299"
  },
  "features": [
    {
      "title": "健康监测",
      "description": "24小时心率监测、血氧检测、睡眠分析"
    },
    {
      "title": "运动追踪",
      "description": "支持100+种运动模式，精准记录运动数据"
    }
  ]
}
```

### 示例3：品牌故事（template-03）

```json
{
  "template_id": "template-03",
  "product": {
    "name": "GreenLife",
    "tagline": "让生活更美好",
    "description": "GreenLife致力于提供环保、可持续的生活用品，帮助人们过上更健康、更环保的生活。",
    "image": "assets/hero.png"
  },
  "story": {
    "origin": "GreenLife的故事始于2020年，当时我们的创始人发现日常生活中的很多产品都含有有害化学物质。",
    "journey": "从最初的手工皂，到现在的完整产品线，我们始终坚持使用天然、环保的原料。",
    "mission": "我们的使命是让每个人都能轻松地过上更健康、更环保的生活。",
    "why_us": "选择GreenLife的理由：100%天然原料、零塑料包装、支持可持续发展。"
  },
  "story_images": ["assets/story-1.png", "assets/story-2.png"]
}
```

### 示例4：视频教程（template-04）

```json
{
  "template_id": "template-04",
  "product": {
    "name": "编程入门课程",
    "tagline": "从零开始学编程",
    "description": "通过视频教程和实践项目，帮助初学者快速掌握编程基础。"
  },
  "content_sections": [
    {
      "title": "课程介绍",
      "description": "本课程涵盖Python基础语法、数据结构、算法等核心内容，适合零基础学员。",
      "media_placeholder": "课程介绍视频"
    },
    {
      "title": "学习路径",
      "description": "从Hello World到实战项目，循序渐进地学习编程知识。",
      "media_placeholder": "学习路径图"
    }
  ],
  "video_embed": "https://www.youtube.com/embed/VIDEO_ID",
  "features": [
    {
      "title": "视频教学",
      "description": "高清视频讲解，随时随地学习"
    },
    {
      "title": "实战项目",
      "description": "真实项目练习，快速提升能力"
    }
  ]
}
```

### 示例5：深色赛博风（template-05）

```json
{
  "template_id": "template-05",
  "product": {
    "name": "QuickNote",
    "tagline": "快速记录，永不丢失",
    "description": "QuickNote是一个简单的在线笔记工具，支持实时同步、多设备访问，让您的灵感不再丢失。",
    "info": [
      "实时同步到云端",
      "支持Markdown格式",
      "免费使用，无广告"
    ]
  },
  "features": [
    {
      "title": "快速记录",
      "description": "3秒内创建笔记，快速记录灵感"
    },
    {
      "title": "云端同步",
      "description": "多设备访问，随时随地查看笔记"
    }
  ]
}
```

## 验证规则

### 必填字段
- template_id
- product.name
- product.tagline

### 字段类型
- template_id：有效的模板ID（template-01到template-15）
- features：数组，每个元素包含title和description
- 图片路径字段（product.image、hero.image_url、各 image_url / url 字段）：`assets/xxx.png`（本地路径）或 `https://...`（外部 URL），详见[图片路径规范](#图片路径规范)
- theme.*：hex颜色格式（#RRGGBB）

### 长度限制
- product.name：2-50字符
- product.tagline：10-100字符
- product.description：50-500字符（可选）
- features[].title：2-30字符
- features[].description：10-200字符

### 常见错误

**错误1：缺少必填字段**
```
错误信息: "Missing required field: product.name"
解决: 确保config.json中包含product.name字段
```

**错误2：无效的template_id**
```
错误信息: "Invalid template_id: template-99"
解决: 使用有效的模板ID（template-01到template-15）
```

**错误3：JSON格式错误**
```
错误信息: "JSON decode error: Expecting property name enclosed in double quotes"
解决: 检查JSON格式，确保使用双引号，逗号正确
```
