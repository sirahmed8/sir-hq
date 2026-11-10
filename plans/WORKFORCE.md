# WORKFORCE: every AI Ahmed has, and how any chat uses them (rewritten 2026-11-10)

Rule from Ahmed (2026-11-01): when something is hard, never say "I cannot". Say "let's try a different way", then search how, look at the tools and connectors you have, and try again.

## The workers
| Worker | How to call it | Best for | Notes |
|---|---|---|---|
| Antigravity (Gemini, builder) | Desktop app, one chat per project; start with `python D:/Projects/_SIR/scripts/agy-task.py <name> <brief-file> <cwd>`; guide: `plans/ANTIGRAVITY_OPERATOR.md` | Building, fixing, deploying | Main builder. Quota and account order: `ops/ACCOUNT_ROTATION.md` |
| Antigravity CLI `agy` | `agy --print "<prompt>" --print-timeout 300s` in the project folder | Bulk text, drafts, research digests, code drafts to be reviewed | Headless runs save no image files. The separate Gemini CLI free tier is discontinued |
| Kilo | `kilo run --auto -m kilo/kilo-auto/free "<task>"` | Free building when Antigravity is out | Public text only unless data terms say otherwise (`ops/TOOLS.md`) |
| OpenCode | `opencode run -m opencode/big-pickle "<task>"` (thorough), `opencode/glm-5.3-flash-free` (fast); Muse Spark 1.3 through OpenCode only | Free building, second opinion | Daily free limit |
| Devin CLI | `devin -p --model swe-2-flash-medium --permission-mode smart --respect-workspace-trust false -- "<task>"` | Free building | Only that model is free; others cost credits, do not use them |
| ZCode (desktop app, GLM-5.3 free Start plan) | Driven by a Haiku computer-use operator | Free building | Details in `plans/CLI_AGENT_INSTRUCTIONS.md` |
| Local models (Ollama: qwen3:8b, qwen2.5, bge-m3) | `scripts/ai/ask.ps1 -Provider local` | Anything private; embeddings | Nothing leaves the PC |
| Claude (HQ manager, Claude desktop app) | Agent tool with `model` and `effort` | Review, audits, plans, briefs, screen operation by haiku | Subscription ends around 2026-11-23; level table in `plans/MODEL_ROUTING.md` |
| Computer use, Claude in Chrome, built-in browser, SIR Autonomy | `plans/COMPUTER_USE.md` | Any screen task: apps, sites, dashboards, installers | |
| Connectors (Cloudflare, Firebase, Google Workspace, PostHog, Figma, TickTick, Gmail, Calendar) | MCP tools | Their own jobs | |

One wrapper routes the text providers with fallback and a usage ledger: `D:/Projects/_SIR/scripts/ai/ask.ps1 -Provider auto -Task <prompt file> -Out <answer file>`.

## Rules
- Use these as extra hands, not as the reviewer: whatever an external model writes is reviewed by a fresh chat (not its author) before it is final.
- Privacy: AHome, Habiba and anything private go to local models only (`-Sensitive`). Never send secrets to an outside model.
- Usage limits are real. When a provider says limit, use the next worker in the order of `ops/ACCOUNT_ROTATION.md`. Switching between Ahmed's own accounts by that procedure is his rule of 2026-11-09 and is allowed. Never use accounts that are not his or not given with consent, never create accounts, never buy credits. (This replaces the 2026-11-01 line that forbade all account switching.)
- Quality: any non-top worker is given `plans/WEAK_MODEL_PLAYBOOK.md` and `GEMINI.md` with the task, so its output meets the same bar.
