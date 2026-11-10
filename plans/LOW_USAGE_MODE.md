# Low-usage mode (owner, 2026-11-10; stays on until the owner or HQ ends it in `ops/HQ_CHECKPOINT.md`)
Argon and Claude 5.5 are exhausted; the Pro Gemini accounts are out until their weekly resets (4 to 6 days). Quota is the scarce thing now, so work slows down on purpose and nothing is wasted.

1. Pace: at most TWO chats work at the same time (Laptop and Control first, then Jobs, Study, AHome, Planner in turns). The others stay idle, with their state saved in `.sir/CHECKPOINT.md`.
2. Task size: light tasks only (one file or one screen, one commit), each with a written plan, acceptance check and a stop line. No sweeping rounds, no full audits, no rewrites until the weekly resets.
3. No loops that burn quota: the perpetual loop runs one cycle per day per project, not continuously; each cycle reads only the files it needs.
4. Save rule: commit, push and checkpoint after every step, so a quota cut or an account switch loses nothing.
5. Free models for small work: OpenCode (`opencode/glm-5.3-flash-free`, deepseek, big-pickle, Muse Spark 1.3 via openrouter), Kilo auto-free, Devin CLI (swe-2-flash-medium) and ZCode (GLM-5.3), started in the project folder (commands: `CLI_AGENT_INSTRUCTIONS.md`; the autopilot `scripts/hq_autopilot.py` starts them when a project is idle for 25 minutes).
6. Account order: `ops/ACCOUNT_ROTATION.md`, section CURRENT ORDER (free Antigravity accounts in both Chrome profiles, then the free CLI agents, ZCode, Pro accounts after their resets, the paid reserve, Codex, HQ). The older order written here (Argon first) is superseded because Argon and Claude 5.5 are exhausted. The ledger ops/ACCOUNT_LEDGER.md records every account and its reset time; HQ returns to an account when its window resets.
7. When every option is exhausted: stop cleanly, report on Telegram once, resume at the first reset.
