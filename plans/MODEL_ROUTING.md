# MODEL AND EFFORT BY TASK LEVEL (Ahmed 2026-10-30, rewritten 2026-11-10 for who builds)

Who builds (Ahmed, 2026-11-09 and 2026-11-10): Gemini in Antigravity builds, fixes and deploys. When its quota is out, the free CLI agents build: Kilo, OpenCode, Devin CLI, ZCode (`CLI_AGENT_INSTRUCTIONS.md`). Claude manages, reviews and writes briefs; it does not build product code. Since 2026-11-10 Claude HQ may use its own haiku and sonnet subagents for review, audits, plans and improvement work. The Claude subscription ends around 2026-11-23; after that the Claude rows below simply do not exist and Gemini or a CLI agent does the review with a fresh chat.

## Claude subagents (HQ only: review, audits, plans, screen operation)
Set `model` and `effort` explicitly. At most 3 agents at once (`USAGE_POLICY.md`).

| Level | Task | Model | Effort |
|---|---|---|---|
| 0 | Search, inventory, read logs or large files, link and licence checks, formatting, repeated checks, screen operation (Antigravity chats, account rotation) | haiku | low (medium if results come back shallow) |
| 2 | Design review, architecture, plans, ADRs, review of every significant diff, hard debugging, plan upgrades | sonnet | high |
| 3 | Review of auth, security rules, payments and webhooks, data migrations, legal pages, anything touching secrets or user data | sonnet, then a second sonnet reviewer | high (xhigh for threat models) |
| 4 | Stuck after two tries, architecture that is expensive to undo, security or payment design review | opus | high or xhigh, logged with the reason |

## Builders (Gemini in Antigravity, then the free CLI agents)
| Level | Task | Who | Setting |
|---|---|---|---|
| 1 | Implement from a written spec, unit tests, UI from a design, translations, docs, config files | Gemini (model id carries the level) or a CLI agent | High for design and logic, medium for routine edits, only where the model offers it free |
| 2-3 | Design, architecture, auth, payments, migrations, legal pages | Gemini on the strongest available account; the result is reviewed by a fresh chat that did not write it | High |

## Rules
- Write the delegation brief first (objective, files to read, files it may edit, done-when commands, return format, budget). A good brief is what lets a weaker model do level 1 well. Template: `CHAT_PROMPT_TEMPLATES.md`.
- The author never grades its own work: a fresh reviewer (a Claude subagent while Claude exists, otherwise a new Gemini chat) approves each significant change.
- Bulk non-sensitive text (translation drafts, content drafts, research digests) may go to the local model or Gemini through `_SIR/scripts/ai/ask.ps1`. Private text (AHome, Habiba, study material, credentials) stays local.
- Do not spawn for jobs under about eight tool calls or for tightly coupled edits in the same files.
- Parallel builders get their own git worktree and disjoint files; push to `main` yourself after verify, no pull requests.
- Never use Claude 4.x or paid-credit models. Order of models and accounts: `ops/ACCOUNT_ROTATION.md`.
