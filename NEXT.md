# NEXT (read this first; updated 2026-11-10)
Program: every product is rebuilt as a new SIR project. Rules and order: `plans/MASTER_REBUILD_PLAN.md` (rules), `plans/WAVE_STUDY.md` (order). How every AI works: `plans/AGENT_PROTOCOL.md`. Each product's plan: `plans/<slug>.md` (same file in `<folder>/.sir/PLAN.md`). Agents run everything.

## Where we are (2026-11-10)
- The Claude subscription ends around 2026-11-23. After that, Gemini in Antigravity and the free CLI agents (Kilo, OpenCode, Devin CLI, ZCode) run everything from `D:\Projects\AGENTS.md`, `GEMINI.md` and these files.
- Low-usage mode is on (`plans/LOW_USAGE_MODE.md`): at most 2 chats work at once, light tasks only, one commit per step.
- The autopilot (`scripts/hq_autopilot.py`) works the queue `ops/AUTOPILOT_QUEUE.json` without Claude: r14-ahome, r15-laptop, r15-jobs, r15-control. State: `ops/HQ_CHECKPOINT.md`.
- Model and account order: `ops/ACCOUNT_ROTATION.md`. Free CLI agents: `plans/CLI_AGENT_INSTRUCTIONS.md`.

## How chats work (Ahmed, 2026-11-01, updated 2026-11-10)
- **HQ chat (folder D:\Projects):** manages all projects, reviews reports in `ops/bus/sir-hq.md`, writes briefs in `ops/briefs`, keeps the dashboard true. Protocol: `plans/HQ_PROTOCOL.md`. HQ does not build product code; since 2026-11-10 it may use its own subagents for review, audits and improvement work.
- **Project chat (one per project folder):** reads its plan, builds (Gemini in Antigravity, or a free CLI agent when quota is out), proves it on screen, reports to HQ. Start prompt: `plans/START_PROMPT.md`.
- **Build order:** `plans/WAVE_STUDY.md`. SIR Negm Furniture is plans only (friend's project). SIR Odysseus is removed.
- No pull requests: commit and push straight to `main` once `verify` passes. Version stays 1.0.0. Dashboard: the pinned "SIR Control Room" page (link in `ops/DASHBOARD_URL.txt`).

## Rules every chat follows
- Use the computer, Chrome and apps for any task and work out how (`plans/COMPUTER_USE.md`). Talk to other projects in `ops/bus/<slug>.md`. Dashboard mods live in `_SIR/mods` and any chat may improve them.
- Desktop: `Desktop\SIR Projects\<project>\` holds open, start dev and stop dev shortcuts, each with its own icon; regenerate with `scripts/make-icons-and-desktop.ps1`.

## Next for HQ
1. Keep the autopilot queue moving; review each finished report (diff, tests, one on-screen check of the riskiest change) and push or write a fix brief.
2. Before 2026-11-23: finish the successor files (`GEMINI.md`, `plans/INSTRUCTIONS_FOR_MANAGER.md`, `plans/MANAGER_MEMORY.md`) and test them by starting one fresh Antigravity chat that must continue from the checkpoint alone.
3. Open gaps (owner-side, never blocking): key rotation for the Obour Institutes keys when SIR Obour Hub ships; `ADMIN_SECRET_KEY` at the GTA deploy; legal truthful-claims sweep; publisher identity, domains, store accounts and payment keys (the owner buys them; see `ops/OWNER_ACTIONS.md`).
4. Per product the project chat owns: port from `legacy\` (inventories in `ops/inventory/`), build, deploy, push to `main`; at M6 move `legacy\*` to `old projects\`. Never delete `legacy\` before M6.
