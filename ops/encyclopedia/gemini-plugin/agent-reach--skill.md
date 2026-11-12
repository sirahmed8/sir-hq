# skill

- Tool: `gemini-plugin` (plugin: `agent-reach`)
- Category: media
- Source: `C:\Users\a7med\.gemini\config\plugins\agent-reach\agent_reach\skill\SKILL.md`
- SKILL.md size: 3885 chars

## What it does

> 只读读取各平台内容：搜索、读帖、看评论、取字幕、查行情和职位。 Use when 用户提到或贴出链接：小红书/xiaohongshu、B站/bilibili、Twitter/X、Reddit、 YouTube（字幕、转录）、GitHub、V2EX、雪球/股票行情、LinkedIn/Boss直聘 职位、 Instagram、Facebook、小宇宙播客；或说"帮我搜/看看/读一下这个链接"而自带网页搜索/读取不可用、失败或拿不到正文； 或要安装、加上/去掉某个平台、登录/退出、看状态、更新、卸载 Agent Reach。 不做：发帖、评论、点赞、私信等任何写操作；不替用户登录、不索要密码。 公开内容优先用 Agent 自带工具，Reach 补缺口。

## Structure (headings inside SKILL.md)

- Agent Reach
- 选路
- 结果与错误
- 登录与专用浏览器
- 平台注意
- 渠道
- 安装完成时
- 用户要管理 Agent Reach 时
- 有新版本时
- 红线
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - 公开内容先用你自带的搜索/读取工具（可加 `site:域名`）。正文、评论、字幕分别核对是否已拿到；够了就直接回答，不装渠道、不登录。
2. - 自带工具不可用、结果缺了用户要的部分、或用户要的是渠道声明的站内动作时，再用 Reach。不确定有哪些动作和参数先跑 `agent-reach channels`。
3. - 渠道已经加上（默认渠道或 `add` 过）时，搜索/阅读直接走该站工具；还没加的渠道，搜索/阅读先试免登录公开网页，结果里 `backend: public-web` 标明来源。`--backend public-web` 只查公开网页；`--backend <后端>` 指定站内工具。

## Files inside the skill

- `references/capabilities.md` — "能力边界 / Capability scope"
- `references/maintenance.md` — "维护"
- `references/sessions.md` — "会话与专用浏览器"
- `SKILL_en.md` — "Agent Reach"
