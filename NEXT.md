# NEXT (read this first; updated 2026-10-30)
Program: rebuild every product as a new SIR project. Rules and order: `plans/MASTER_REBUILD_PLAN.md`. How every AI works: `plans/AGENT_PROTOCOL.md`. Targets: `plans/TIMELINE.md`. Each product's big plan: `plans/<slug>.md` (same file in `<folder>/.sir/PLAN.md`). Agents run everything; only the last section needs Ahmed.

## NEW-CHAT STARTER (paste or just say "continue")
"Continue the SIR rebuild. Read D:\Projects\_SIR\NEXT.md, then plans/MASTER_REBUILD_PLAN.md, then do the first item under 'Next' that is not blocked. Update the checkpoint and MISSION_LOG, never ask me, keep replies short."

## Progress
See `plans/PROGRESS.md` (generated: boxes done per product, now 26 of 233 = foundations only). Re-run `python plans/generate_plans.py` after ticking boxes.

## State of the folders (2026-10-30)
- 17 new SIR project folders exist with plan, agent files, icon (placeholder), Desktop folder (open / start dev / stop dev) and git. Merged products hold their old projects in `legacy\` (SIR Hagoozat, Business, Controller (v1 only so far), Laptop Manager (agent suite), Negm Furniture, Odysseus, Content Creation Studio, ModPack, Mods for GTA V) and the study folder is `SIR Study\materials\obour-year2-term1` (Moodle scripts in `SIR Study\_quarantine`).
- Still at the top level until `finish-merges.ps1` runs (they are locked or running; the safety check does not let agents stop programs): AHome (daemons), Laptop manager, Jobs, sirahmed8, SIR AI (app running), SIR Optimizer (PowerSync running), Obour Academic Hub (locked by an open window). `AI_Models_Hub` stays (model store, not a project).
- GitHub: 10 new private repos created (sir-platform, sir-obour-hub, sir-hagoozat, sir-business, ... ); old repos get renamed `sir-legacy-*` and archived by `scripts/github-organize.ps1` AFTER the 5 PRs are merged.

## Next, in this order
1. Protect live users: rotate keys (Google AI Studio, OpenRouter) in Ahmed's Chrome; fix failing Actions (SIR-Controller build, sir-content-creation-studio CI, odysseus CI + Container scan, agent-suite CI); then `github-organize.ps1`.
2. Push the latest plan/merge updates of every new repo (commit + push in each new folder).
3. SIR Platform M0-M2 (`plans/sir-platform.md`), SIR Portfolio M0-M1, then SIR Obour Hub M0-M6 (first full product: new Firebase, login brand check, Cloudflare), then SIR Hagoozat, SIR Business (Restaurant first), the rest per `plans/TIMELINE.md`.
4. Each merge product: port everything from `legacy\` (inventories in `ops/inventory/`), deploy, push, production mode; at M6 move `legacy\*` to `old projects\`.
5. Not done yet, never forget: benchmark vs best apps per product (at each M0), parity test of the SIR setup in Antigravity/OpenCode/Kilo, test of the agent-config sync script, Wave 0 leftovers (webhook timestamp-in-payload, native Stripe/Paymob, SIR AI bearer on portal chat, firebase-admin for the Optimizer), x360ce app (no folder), legal truthful-claims sweep, publisher identity "SIR" (owner decision), developer accounts.

## Only Ahmed can do (the agents already prepared the command)
1. `pwsh -NoProfile -File D:\Projects\_SIR\scripts\generate-icons-agy.ps1` : makes the AI logo for every product with agy (the safety check blocks agents from launching agy). It rebuilds the folder icons and Desktop shortcuts at the end.
2. `pwsh -NoProfile -File D:\Projects\_SIR\scripts\merge-approved-prs.ps1` : merges the 5 security PRs (classifier blocks agents from merging). Then agents run github-organize.
3. **`pwsh -NoProfile -File D:\Projects\_SIR\scriptsinish-merges.ps1`** (after closing Antigravity/VS Code/Explorer windows that have D:\Projects folders open: they lock folders). It stops the old SIR AI and PowerSync apps, moves SIR AI, SIR Optimizer, Obour Academic Hub, Laptop manager, Jobs and sirahmed8 into their new products, moves AHome into SIR Home\legacy with its daemons repointed (verifies port 8090), and rebuilds icons and Desktop folders. Agents may not stop running programs, so this is the one thing left for the top-level cleanup.
4. Delete the empty leftover folder `D:\Quarantine` (the safety check does not let agents remove it).
5. Move passwords out of the TickTick notes; change the Moodle password; be logged in to Google AI Studio and OpenRouter in Chrome when asked; decide the company/publisher entity "SIR" for the stores.
