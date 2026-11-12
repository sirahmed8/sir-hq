# skill

## Summary
The `skill` entry under the agent-reach plugin is the user-facing surface of Agent Reach, a CLI that reads content from many social and web platforms in one command (`agent-reach`). It is read-only by design: search posts, read articles, pull comments, fetch video subtitles, look up stock quotes and job listings, and never write, like, comment or DM on any platform. The CLI returns one-line JSON (`ok: true` → `items[]` with `title/url/author/published_at/text/raw`; `ok: false` → `error.code` + `error.hint`). Public content is tried first with the agent's own search/read tools; the Reach CLI is the fallback when those are missing, incomplete, or when the user explicitly asks for a channel action.

## When to use / when NOT
Use when the user links or mentions Xiaohongshu, Bilibili, Twitter/X, Reddit, YouTube, GitHub, V2EX, Xueqiu (stock quotes), LinkedIn/Boss直聘 (jobs), Instagram, Facebook, or Xiaoyuzhou podcasts, or asks to install/manage Agent Reach. Do NOT use for posting, commenting, liking, DMing or any write action. Do NOT use to log in on the user's behalf or to ask for passwords/Cookies. Do NOT retry a failed platform by switching accounts or backends.

## Inputs, outputs, tools
- Inputs: a platform name or URL, plus optional actions (`search`, `read`) and flags (`--limit`, `--backend public-web|<后端>`).
- Outputs: JSON items or an error envelope with a code table (`NEED_SETUP`, `NEED_LOGIN`, `UPSTREAM_BROKEN`, `TIMEOUT`, `RATE_LIMITED`, `PLATFORM_BLOCKED`, `BUSY`, `NOT_FOUND`, `BAD_INPUT`).
- Tools: the `agent-reach` CLI (`channels`, `add`, `remove`, `login`, `logout`, `doctor`, `check`, `update`, `uninstall`, `skill link`). Needs a dedicated browser (CloakBrowser, falling back to Chrome) for login-gated channels; parallel caps are 2 per platform, 4 total.

## 5 most important rules
1. Always try the agent's own search/read tools first; only fall back to Reach when they are missing or incomplete.
2. On `NEED_LOGIN`, stop and let the user log in themselves — never type credentials.
3. On `PLATFORM_BLOCKED`, `RATE_LIMITED`, `NEED_LOGIN` or `BUSY`, stop the attempt; do not switch accounts, backends or browsers to work around it.
4. Never claim to have understood images or video from Xiaohongshu `read` — it returns text description only.
5. Never guess a salary number when `salary_encoded=true` on Boss直聘; read the job detail for readable pay.

## Risks / things needing the owner
Login, API keys (`NEED_SETUP`), and platform verification blocks (`PLATFORM_BLOCKED`) need the owner. Adding a channel with `agent-reach add` may install dependencies; upgrades need explicit user consent.

## Category / tags
media · read-only, multi-platform, CLI, social, research

## Revisions
Only one revision, in the agent-reach plugin (`C:\Users\a7med\.gemini\config\plugins\agent-reach\agent_reach\skill\SKILL.md`). No divergent copies on other tools.