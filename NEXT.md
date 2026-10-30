# NEXT (read this first; updated 2026-10-30)
Program: rebuild every product as a new SIR project. Rules and order: `plans/MASTER_REBUILD_PLAN.md`. How every AI works: `plans/AGENT_PROTOCOL.md`. Targets: `plans/TIMELINE.md`. Each product's big plan: `plans/<slug>.md` (same file in `<folder>/.sir/PLAN.md`). Agents run everything.

## HOW CHATS WORK (Ahmed, 2026-10-30)
- **HQ chat (folder D:\Projects):** manager only. It prepares and maintains plans, kits, repos, agent and tool setup. It never builds or codes a product.
- **Project chat (one per project folder):** opens in `D:\Projects\<SIR project>`, says `/continue` (or "continue"), reads `.sir/CHECKPOINT.md` and `.sir/TASKS.md`, and builds with its own sub-agents. Kit overview: `plans/KIT.md`.
- Start order for Ahmed's project chats (studied, see `plans/WAVE_STUDY.md`): Wave 1 AHome; Wave 2 SIR Platform (only the slice the next project needs) with SIR Jobs, SIR Negm Furniture, SIR Portfolio; Wave 3 SIR Business, SIR Content Creation Studio, SIR Hagoozat, SIR Obour Hub; Wave 4 SIR Controller, SIR ModPack, SIR Mods for GTA V, SIR AI, SIR Life; Wave 5 SIR Laptop Manager, SIR Study, SIR Odysseus.
- Every project chat starts with its first task: a deep scan of `legacy/` (the source code to port from, never deleted before M6) and of the plan, then improves the plan from what it finds.
- No pull requests anywhere: commit and push straight to `main` once `verify` passes.

## Progress
See `plans/PROGRESS.md` (generated: boxes done per product, now 26 of 233 = foundations only). Re-run `python plans/generate_plans.py` after ticking boxes.

## State of the folders (2026-10-30, after the merge)
- D:/Projects now holds ONLY: the SIR product folders, AHome (private, own name), AI_Models_Hub (model store), Android and Backups (you moved them in), old projects, _SIR, and the three auto-read rule files AGENTS.md / CLAUDE.md / GEMINI.md (Claude, Codex and Gemini read these automatically in every chat started in D:/Projects, so they stay).
- Every old project lives INSIDE its new product as legacy/: SIR Hagoozat (Hagoozat Elite, 11Players, EGFootball5) · SIR Business (Restaurant, Market, Pharmacy, Library) · SIR Controller (v1, Optimizer) · SIR Laptop Manager (Laptop manager, agent suite) · SIR Obour Hub (Obour Academic Hub) · SIR AI (SIR AI v1, SIR Tele Gateway) · SIR Portfolio (sirahmed8 profile repo) · SIR Jobs (Jobs data) · SIR Content Creation Studio, SIR ModPack, SIR Mods for GTA V, SIR Negm Furniture, SIR Odysseus (their v1). SIR Study holds the old Obour Institute study folder in materials/ and the Moodle scripts in _quarantine/.
- AHome is NOT a SIR product: private project of Ahmed and Habiba, keeps its name, services run from D:/Projects/AHome (port 8090 verified), plan in AHome/.sir/PLAN.md.
- One empty leftover: D:/Projects/Laptop manager (an empty shell; Ahmed's open Laptop manager chat sits in it; it disappears when that chat is closed or any agent can delete it then).
- Old SIR AI app and SIR PowerSync were stopped at Ahmed's request. A duplicate whisper cache is in AI_Models_Hub/_whisper_duplicate_from_restore.
- INCIDENT (fixed, nothing lost): a bug in merge-legacy.ps1 moved parts of D:/Projects into a legacy folder; restored with scripts/restore-misplaced.ps1 + restore-finish.ps1; the bug is fixed (a missing alias no longer resolves to the Projects folder).
- Handy: scripts/who-holds.ps1 lists the programs that keep a folder from moving (agents run it themselves; Ahmed never has to look).
- GitHub (done 2026-10-30): the 5 security PRs were merged; 18 old repos renamed `sir-legacy-*` and archived; every product has a new private repo with `origin` set and the kit pushed to `main` (ModPack's private source repo is `sir-modpack-source`; `sir-modpack` is the public release repo). AHome keeps `ahmed-and-habiba-sanctuary` and is never pushed from HQ. Odysseus (`sirahmed8/odysseus`) is left alone: its source is copied into SIR Odysseus\legacy, its PRs are not merged.
- Public release repos still public on purpose (they hold download links): SIR-*-Public and SIR-ModPack, plus the profile repo `sirahmed8`.

## Rules every chat follows (from Ahmed)
- Use the computer, Chrome and apps for any task and work out how (`plans/COMPUTER_USE.md`). Read `plans/MAIN_PLAN.md`. Talk to other projects in `ops/bus/<slug>.md` and with ListAgents/SendMessage. Dashboard mods live in `_SIR/mods` and any chat may improve them or add a pane.
- Desktop: `Desktop\SIR Projects\<project>\` holds open, start dev (play badge) and stop dev (stop badge) shortcuts, each with its own icon; regenerate with `scripts/make-icons-and-desktop.ps1`.

## Next for HQ (preparation only; HQ never builds)
1. Close the readiness gaps below, one per session, and keep `plans/KIT.md` current: re-run `python plans/generate_plans.py` then `python plans/generate_kit.py` after any data change.
2. Gaps still open: key rotation for the Obour Institutes keys when SIR Obour Hub ships; the Telegram bot token (BotFather, Ahmed's Telegram); `ADMIN_SECRET_KEY` at the GTA deploy; parity test of the shared setup in Antigravity, OpenCode and Kilo and the agent-config sync test (both are tasks in SIR Laptop Manager); legal truthful-claims sweep; x360ce app (no folder); publisher identity "SIR", domains, store accounts and payment keys (owner decisions, never blocking). Done 2026-10-30: logos for all 17 projects (Gemini app), studied wave order, deep-scan-first task in every project, SIR Control Room and SIR Guards mods installed.
3. Per product the project chat owns: port from `legacy\` (inventories in `ops/inventory/`), build, deploy, push to `main`; at M6 move `legacy\*` to `old projects\`.
