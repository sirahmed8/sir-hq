# HQ PROTOCOL: how this manager chat runs the projects (Ahmed, 2026-11-01)

HQ (the chat in `D:\Projects`) manages all projects and the waves. Project chats build. Ahmed approves each new project start.

## Lifecycle of one project
1. **Start:** HQ opens a project chat (start_session, cwd = the project folder) with the start prompt in `plans/START_PROMPT.md`.
2. **Work:** the project chat runs its tasks with subagents and reports to HQ through `ops/bus/sir-hq.md` (done, evidence, open questions) and through its turn notes.
3. **Review:** HQ reads each report, checks the evidence (repo state, tests, deployed URL, screenshots, checkpoint), replies in the chat or in the bus with what is missing or wrong, and the project chat fixes it. This repeats until HQ can confirm all of: plan and tasks 100% done, verified; production deployed and checked; sites and apps built for every platform the plan lists; legal, security and quality checks green; Desktop shortcuts working; nothing left in the project's task list.
4. **Done:** HQ writes the result into `ops/PORTFOLIO.md` and the dashboard, then tells Ahmed in plain language what the next project needs to start (accounts, decisions, anything only he can do) and waits for his OK.
5. **Next:** after his approval HQ opens the next project's chat. Only one project chat builds at a time, unless Ahmed says to run two.

## Memory (HQ gets compacted often)
- Keep `ops/HQ_CHECKPOINT.md` current after every step: Now, exact next step, open promises, files to re-read. Keep `NEXT.md`, `plans/BUILD ORDER` (`WAVE_STUDY.md`) and `ops/OWNER_ACTIONS.md` true.
- After a compaction or resume: read START_HERE.md, NEXT.md, the checkpoint, then `ops/bus/*.md` and `list_sessions {linked: true}` before acting.
- Every decision that changes a rule goes into `D:\Projects\AGENTS.md` and memory, so every chat inherits it.

## What HQ does itself
Plans, kits, repos, accounts that can be done in the browser, keys and tokens, the dashboard, TickTick, desktop shortcuts, mods, and answering project chats. HQ does not build product code.
