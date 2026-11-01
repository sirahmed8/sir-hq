# NEXT (read this first; updated 2026-10-30)
Program: rebuild every product as a new SIR project. Rules and order: `plans/MASTER_REBUILD_PLAN.md`. How every AI works: `plans/AGENT_PROTOCOL.md`. Targets: `plans/TIMELINE.md`. Each product's big plan: `plans/<slug>.md` (same file in `<folder>/.sir/PLAN.md`). Agents run everything.

## HOW CHATS WORK (Ahmed, 2026-11-01)
- **HQ chat (folder D:\Projects, this chat):** manages all projects and the waves. It opens a project chat, reviews its reports in `ops/bus/sir-hq.md`, replies, and when a project is truly finished (plan and tasks done, in production, all platform builds) it tells Ahmed what the next project needs and waits for his OK before opening it. Protocol: `plans/HQ_PROTOCOL.md`; start prompt: `plans/START_PROMPT.md`. HQ never builds product code.
- **Project chat (one per project folder):** analyses the whole project, makes its plan 100x better, builds with subagents chosen by task level, proves it, reports to HQ.
- **Build order:** `plans/WAVE_STUDY.md` (AHome; SIR Study, SIR Jobs, SIR Laptop Manager; SIR Negm Furniture as a friend's handoff pack; SIR AI, SIR Content Creation Studio; SIR Business, SIR Hagoozat, SIR Obour Hub; SIR ModPack, SIR Mods for GTA V, SIR Life; SIR Platform and SIR Portfolio last; SIR Controller optional last). SIR Odysseus is removed.
- No pull requests: commit and push straight to `main` once `verify` passes. Dashboard: the pinned "SIR Control Room" page (link in `ops/DASHBOARD_URL.txt`, `/sir`).

## Rules every chat follows (from Ahmed)
- Use the computer, Chrome and apps for any task and work out how (`plans/COMPUTER_USE.md`). Read `plans/MAIN_PLAN.md`. Talk to other projects in `ops/bus/<slug>.md` and with ListAgents/SendMessage. Dashboard mods live in `_SIR/mods` and any chat may improve them or add a pane.
- Desktop: `Desktop\SIR Projects\<project>\` holds open, start dev (play badge) and stop dev (stop badge) shortcuts, each with its own icon; regenerate with `scripts/make-icons-and-desktop.ps1`.

## Next for HQ (preparation only; HQ never builds)
1. Close the readiness gaps below, one per session, and keep `plans/KIT.md` current: re-run `python plans/generate_plans.py` then `python plans/generate_kit.py` after any data change.
2. Gaps still open: key rotation for the Obour Institutes keys when SIR Obour Hub ships; the Telegram bot token (BotFather, Ahmed's Telegram); `ADMIN_SECRET_KEY` at the GTA deploy; parity test of the shared setup in Antigravity, OpenCode and Kilo and the agent-config sync test (both are tasks in SIR Laptop Manager); legal truthful-claims sweep; x360ce app (no folder); publisher identity "SIR", domains, store accounts and payment keys (owner decisions, never blocking). Done 2026-10-30: logos for all 17 projects (Gemini app), studied wave order, deep-scan-first task in every project, SIR Control Room and SIR Guards mods installed.
3. Per product the project chat owns: port from `legacy\` (inventories in `ops/inventory/`), build, deploy, push to `main`; at M6 move `legacy\*` to `old projects\`.
