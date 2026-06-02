# ✍️ 公众号 AI 全自动写作 Skill

> 即装即用 · 输入选题 → AI 搜素材 → AI 写正文 → AI 生成标题 → AI 排版 → 一键推送微信草稿箱

<p align="center">
  <img src="assets/logo.png" width="200" alt="公众号 AI 全自动写作">
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white" alt="Python"></a>
  <a href="https://openai.com"><img src="https://img.shields.io/badge/OpenAI-GPT--4o-412991?logo=openai&logoColor=white" alt="OpenAI"></a>
  <a href="https://mp.weixin.qq.com"><img src="https://img.shields.io/badge/WeChat-公众号-07C160?logo=wechat&logoColor=white" alt="WeChat"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
</p>

## 一句话流程

```
输入选题 → AI 搜素材 → AI 写标题 → AI 写正文 → AI 排版 → 自动进草稿箱 → 人点群发
```

## 功能特性

- **8 步标准化工作流**：选题 → 素材搜集 → 结构拆解 → 大纲 → 正文 → 标题 → 封面 → 排版 → 推送
- **去 AI 味写作风格**：口语化、短句、有节奏感，每段不超过 3 行
- **爆款标题生成**：数字法、悬念法、痛点法、反常识法、对话法，5 种公式批量产出
- **一键自动化脚本**：即装即用，配置好 API Key 后输入选题即可全自动完成
- **微信草稿箱直推**：文章自动进入公众号后台草稿箱，无需手动复制粘贴

## 快速开始

### 方式一：手动执行（分步 AI 对话）

按 `SKILL.md` 中的 8 个步骤，逐段调用 AI 完成写作。

### 方式二：全自动脚本（推荐）

1. **安装依赖**
   ```bash
   pip install requests
   ```

2. **配置参数**
   编辑 `scripts/wechat_writer.py` 顶部的 4 个配置项：
   ```python
   OPENAI_API_KEY = "sk-xxx"          # OpenAI API Key
   SERPER_API_KEY = "xxx"             # serper.dev API Key（可选，用于搜素材）
   WECHAT_APPID = "wx-xxx"            # 微信公众号 AppID
   WECHAT_SECRET = "xxx"              # 微信公众号 AppSecret
   AUTHOR = "你的笔名"
   ```

3. **准备封面图**
   放一张 `cover.jpg` 在脚本同目录下。

4. **运行**
   ```bash
   python scripts/wechat_writer.py
   ```
   输入选题，3 分钟后文章自动进入公众号草稿箱。

## 获取微信 API 凭证

1. 登录 [mp.weixin.qq.com](https://mp.weixin.qq.com)
2. 左侧菜单：设置与开发 → 基本配置
3. 获取 **AppID** 和 **AppSecret**
4. 添加 IP 白名单（你运行脚本的服务器/电脑公网 IP）

> 个人订阅号即可使用，无需认证。

## 8 步工作流详解

| 步骤 | 动作 | 说明 |
|------|------|------|
| Step 0 | 接收选题 | 用户给话题，或 AI 生成 5 个候选选题 |
| Step 1 | 素材搜集 | 核心观点、案例、金句、反常识角度、读者痛点 |
| Step 2 | 结构拆解 | 分析 3 种爆款结构，推荐最适合的一种 |
| Step 3 | 生成大纲 | 标注字数、钩子位置、情绪节奏 |
| Step 4 | 写作正文 | 口语化、短句、去 AI 味，Markdown 输出 |
| Step 5 | 生成标题 | 5 种公式各 3 个，选 Top 3 推荐 |
| Step 6 | 封面提示词 | 输出 Midjourney / GPT-4o 可用的英文提示词 |
| Step 7 | 排版转 HTML | Markdown → 微信公众号 HTML 格式 |
| Step 8 | 推草稿箱 | 调用微信 API，一键进入后台 |

## 进阶优化方向

| 优化点 | 说明 |
|--------|------|
| 标题 A/B 测试 | 生成 2 个标题，先发朋友圈测点击率 |
| 封面自动生成 | 接入 Midjourney / GPT-4o Image API |
| 文中插图自动插入 | 关键词触发时自动搜索/生成配图 |
| 定时发布 | 调用微信 API 的发布接口，设定时间 |
| 数据回流 | 发布后 24h 自动读数据，写复盘报告 |

## 文件结构

```
chen-wechat-ai-writer/
├── SKILL.md              # Anthropic 官方格式 Skill 文件
├── scripts/
│   └── wechat_writer.py  # 一键自动化脚本
└── README.md             # 本文件
```

## 使用示例

```
用户：帮我写一篇公众号，选题是"普通人怎么用 AI 做副业"

→ AI 执行全流程
→ 3 分钟后输出：草稿已创建，ID: xxx
→ 用户进公众号后台 → 草稿箱 → 点群发
```

## 适用场景

- 自媒体日更：每天固定时间自动产出文章
- 热点追踪：快速将热点事件写成公众号文章
- 内容矩阵：批量生成系列文章
- 个人 IP：保持更新频率，沉淀内容资产

## 注意事项

- 脚本中的 API Key 等敏感信息请勿上传到公开仓库
- 微信 API 有调用频率限制，大量发文需注意配额
- 建议先手动跑通全流程，再启用自动化脚本

---

如果这个项目对你有帮助，欢迎 Star ⭐
