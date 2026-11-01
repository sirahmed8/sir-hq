# WORKFORCE: every AI Ahmed has, and how any chat uses them

Rule from Ahmed (2026-11-01): when something is hard, never say "I cannot". Say "let's try a different way", then search how, look at the tools and connectors you have, and try again.

## The tools on this PC (verified 2026-11-01)
| Worker | How to call it | Best for | Notes |
|---|---|---|---|
| Claude subagents (haiku, sonnet, opus) | the Agent tool with `model` and `effort` set | everything; table in `plans/MODEL_ROUTING.md` | the main workforce of every project chat |
| Antigravity CLI `agy` (Gemini, named by Ahmed "Gemini 3.8 high") | Bash: `agy --print "<prompt>" --print-timeout 300s` in the project folder | bulk text, drafts, research digests, code drafts to be reviewed | headless runs save no image files; for images use the Gemini desktop app (recipe in `ops/TOOLS.md`) |
| OpenCode (Ahmed's "Muse Spark 1.3") | Bash: `opencode run "<prompt>"` | second opinion, drafts, free-model work | only the free models listed in `ops/TOOLS.md` may get workspace text |
| Kilo | Bash: `kilo run "<prompt>"` | public-text tasks only | data terms in `ops/TOOLS.md` |
| Local models (Ollama: qwen3:8b, qwen2.5, bge-m3) | `scripts/ai/ask.ps1 -Provider local` | anything private; embeddings | nothing leaves the PC |
| Computer use, Claude in Chrome, built-in browser | `plans/COMPUTER_USE.md` | any screen task: apps, sites, dashboards, installers | |
| All connectors (Cloudflare, Firebase, Google Workspace, PostHog, Figma, TickTick, Gmail, Calendar) | MCP tools | their own jobs | |

One wrapper routes the external ones with fallback and a usage ledger: `D:/Projects/_SIR/scripts/ai/ask.ps1 -Provider auto -Task <prompt file> -Out <answer file>`.

## Rules
- Use these as extra hands, not as the reviewer: whatever an external model writes is reviewed by a Claude agent before it is merged; the author never grades its own work.
- Privacy: AHome, Habiba and anything private go to local models only (`-Sensitive`). Never send secrets to an outside model.
- Usage limits are real. When a provider says limit, use the next worker in the chain or wait for the reset. Do not rotate or cycle through several accounts to get around a provider's limit (its terms forbid it, and it can get all accounts banned). Ahmed's Google AI Pro plan is used through the account signed in to Antigravity.
- Quality: any non-Claude worker is given `plans/WEAK_MODEL_PLAYBOOK.md` with the task, so its output meets the same bar.
