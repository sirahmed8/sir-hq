# NEXT (read this first; updated 2026-10-30)
Program: rebuild every product as a new SIR project. Rules and order: `plans/MASTER_REBUILD_PLAN.md`. How every AI works: `plans/AGENT_PROTOCOL.md`. Targets: `plans/TIMELINE.md`. Each product's big plan: `plans/<slug>.md` (same file in `<folder>/.sir/PLAN.md`). Agents run everything; only the last section needs Ahmed.

## NEW-CHAT STARTER (paste or just say "continue")
"Continue the SIR rebuild. Read D:\Projects\_SIR\NEXT.md, then plans/MASTER_REBUILD_PLAN.md, then do the first item under 'Next' that is not blocked. Update the checkpoint and MISSION_LOG, never ask me, keep replies short."

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
- GitHub: new private repos created for most products; old repos get renamed sir-legacy-* and archived by scripts/github-organize.ps1 AFTER the 5 PRs are merged; then re-run github-create-new-repos.ps1 for Content Creation Studio, Controller, ModPack, GTA mods.

## Next, in this order
1. Protect live users: rotate keys (Google AI Studio, OpenRouter) in Ahmed's Chrome; fix failing Actions (SIR-Controller build, sir-content-creation-studio CI, odysseus CI + Container scan, agent-suite CI); then `github-organize.ps1`.
2. Push the latest plan/merge updates of every new repo (commit + push in each new folder).
3. SIR Platform M0-M2 (`plans/sir-platform.md`), SIR Portfolio M0-M1, then SIR Obour Hub M0-M6 (first full product: new Firebase, login brand check, Cloudflare), then SIR Hagoozat, SIR Business (Restaurant first), the rest per `plans/TIMELINE.md`.
4. Each merge product: port everything from `legacy\` (inventories in `ops/inventory/`), deploy, push, production mode; at M6 move `legacy\*` to `old projects\`.
5. Not done yet, never forget: benchmark vs best apps per product (at each M0), parity test of the SIR setup in Antigravity/OpenCode/Kilo, test of the agent-config sync script, Wave 0 leftovers (webhook timestamp-in-payload, native Stripe/Paymob, SIR AI bearer on portal chat, firebase-admin for the Optimizer), x360ce app (no folder), legal truthful-claims sweep, publisher identity "SIR" (owner decision), developer accounts.

## Only Ahmed can do (the agents already prepared the command)
1. Make the AI logos: pwsh -NoProfile -File D:/Projects/_SIR/scripts/generate-icons-agy.ps1 (the safety check blocks agents from launching agy; icons are temporary letters until you run it).
2. Merge the 5 security fixes: pwsh -NoProfile -File D:/Projects/_SIR/scripts/merge-approved-prs.ps1 (the safety check blocks agents from merging). Agents then run github-organize.
3. Accounts and decisions only you can do: move passwords out of the TickTick notes into a password manager; change the Moodle password; be logged in to Google AI Studio and OpenRouter in Chrome when asked; decide the company/publisher entity SIR for the stores.
Everything else (finding locks, stopping old programs, moving folders, fixing scripts) is done by the agents themselves.
