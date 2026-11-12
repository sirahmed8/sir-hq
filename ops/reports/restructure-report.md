# Restructure report: SIR Platform cancelled, SIR Obour Hub renamed SIR Education Hub

Date: 2026-11-12. Source: owner direction `plans/PRODUCT_DIRECTION_2026-11-12.md`. Done by the restructure agent (Claude Haiku 5.5).

## Status at a glance

| Item | Result |
|---|---|
| SIR Platform project folder `D:\Projects\SIR Platform` | NOT moved. Locked by a running worker (see "Locked") |
| SIR Platform Desktop folder | Moved to `D:\Projects\old projects\desktop-folders-removed\SIR Platform` |
| SIR Platform plan files | Moved to `D:\Projects\old projects\SIR Platform-plans-from-SIR\` (4 files) |
| SIR Obour Hub folder | Renamed to `D:\Projects\SIR Education Hub` (git intact, remote updated) |
| SIR Obour Hub Desktop folder | Renamed to `C:\Users\a7med\Desktop\SIR Projects\SIR Education Hub` |
| GitHub repo | `sirahmed8/sir-obour-hub` renamed to `sirahmed8/sir-education-hub` (verified with ls-remote) |
| TickTick SIR HQ | Updated (see below) |
| Commits pushed | `_SIR`: 1ff921a, 07a9cec, 9898eba, 7968e5d. `SIR Education Hub`: 633a157 |

## 1. SIR Platform

- Process check before any move: no process had `SIR Platform` as its working folder by command line. Only a worker (opencode 37228, shell 36792, timeout 39816, started 17:42) carries the text in its prompt. The r51 aider run stopped on a payment error at 17:30. Queue entries r51 and r52-plan-sir-platform are done.
- Desktop folder moved: `C:\Users\a7med\Desktop\SIR Projects\SIR Platform` to `D:\Projects\old projects\desktop-folders-removed\SIR Platform`. Its .lnk files still point at the old path (archived, not fixed on purpose).
- Plan files moved out of `_SIR` into `D:\Projects\old projects\SIR Platform-plans-from-SIR\`: `sir-platform.md`, `sir-platform-DEEP.md`, `sir-platform-competitors.md` (was `plans/competitors/sir-platform.md`), `sir-platform-bus.md` (was `ops/bus/sir-platform.md`). Note: the first move overwrote two files with the same name. Both were restored from git HEAD (d176c93) before anything else ran, so no content was lost.
- Product removed from: `AGENTS.md` (portfolio map now names the standards kit), `ops/PORTFOLIO.md`, `plans/MAIN_PLAN.md`, `plans/WAVE_STUDY.md`, `plans/PROJECT_MERGE_RECORD.md` (ideas 6, 7, 8 now read "standard for every product"), `plans/SHARED_PLATFORM_KIT.md` (retitled "SHARED STANDARDS KIT (not a product)"), generator data (see section 4), and the live workspace docs `START_HERE.md`, `START_ANY_AI.md`, `core/07-reporting.md`, `phases/03`, `04`, `05`, `08`.
- `plans/SHARED_PLATFORM_KIT.md` file name kept; `Projects-Hub.html` has no mention of either name, so it was not changed.
- Round labels: `scripts/round_labels.py` was run after the queue edit. Its SHORT map had no `SIR Platform` or `SIR Obour Hub` entry, so nothing needed removing there. The done r51 round still shows as "SIR Platform R1" because the label comes from the folder name. That is history.

## 2. SIR Obour Hub to SIR Education Hub

- Folder: `D:\Projects\SIR Education Hub` (git status clean except the pre-existing uncommitted `assets/brand/icon.png`, `scripts/dev-start.ps1`, `scripts/dev-stop.ps1`, which were not mine and were not committed).
- Commit 633a157 in the project repo: `AGENTS.md` and `.sir/CHECKPOINT.md` first lines renamed.
- Desktop folder: three .lnk files renamed and retargeted (target, arguments, working folder, icon path). `desktop.ini` icon path updated (UTF-16, attributes restored). `Versions.txt` product name and repository line updated.
- GitHub: `gh repo rename` succeeded. `origin` now `https://github.com/sirahmed8/sir-education-hub.git`.
- Plans: `plans/sir-obour-hub.md` renamed to `plans/sir-education-hub.md`. Vision from direction section 2 placed on top. The old plan sits below "## Previous plan (merge into the new one in the next round)". `plans/sir-obour-hub-DEEP.md` renamed to `plans/sir-education-hub-DEEP.md` with a note at the top. Competitor files and bus file renamed to `*-education-hub.md`.
- "Obour Institute" and "Obour Academic Hub" kept where they name the institute or the legacy folder.
- Generator data renamed: `products_a.py`, `repos.json`, `brand.json`, `icon-prompts.json`, `waves.json`, `order.json`, `wave_order.py`, `wave_study.py`, `make_folders.py`, `scripts/merge-legacy.ps1`, `scripts/deliver/format-briefing.mjs`, `mods/sir-guards/hooks/register.test.ts`.

## 3. SIR Business and SIR Hagoozat

- `plans/sir-business.md` and `plans/sir-hagoozat.md`: vision blocks at the top (direction sections 3 and 4). Old content kept below "## Previous plan (merge in the next round)". Sector list and booking-idea decisions are marked as next-round research, not invented.

## 4. Generators and registries

- Product entries for `sir-platform` removed from `plans/products_a.py`, `plans/kit_products_a.py`, `plans/kit_overrides.py` (builder call), `plans/wave_study.py`, `plans/wave_order.py`, `plans/generate_main_plan.py` (provides list), and the JSON registries `repos.json`, `brand.json`, `icon-prompts.json`, `waves.json`, `order.json`. All JSON files re-parsed after editing. Python files parsed.
- `plans/sync_docs.py` portfolio template updated to match `AGENTS.md`, so a sync run does not restore the old product line.

## 5. TickTick (list SIR HQ)

- "SIR Obour Hub" renamed "SIR Education Hub", status line updated to the new vision. Child "Wave 5: SIR Obour Hub" renamed too.
- "SIR Platform" parent: note "cancelled by the owner 2026-11-12: shared standards, not a product" set, M0 to M6 items completed with the same note, parent completed. Its two child tasks ("Wave 7: SIR Platform" and "Wave 2: SIR Platform kit slice") also completed with the same note, because they are SIR Platform work and would otherwise stay open.
- "SIR Business" and "SIR Hagoozat" status lines updated. The Wave 5 Business task text now says "shared standards kit", not SIR Platform.
- Not touched: the "Accounts" note, the column "habobty", and no list was created.

## 6. Verification

- `grep "SIR Platform"` in `_SIR` (excluding agy-runs, archive, encyclopedia, reports, verifications, legacy, snapshots, evidence, `.claude/worktrees`): remaining hits are history or intended notes. Examples: `plans/PRODUCT_DIRECTION_2026-11-12.md`, the cancellation notes in `MAIN_PLAN.md`, `WAVE_STUDY.md`, `PROJECT_MERGE_RECORD.md`, `SHARED_PLATFORM_KIT.md`, `sir-hagoozat.md`, `sync_docs.py`, `ops/PORTFOLIO.md`; briefs and MISSION_LOG (history); `ops/bus/planner.md` (log); `ops/AUTOPILOT_QUEUE.json` (queue names are not changed); `_local/ticktick_refresh.json` (local cache); `scripts/deliver/test-format-briefing.mjs` (test fixture string); `plans/MANAGER_MEMORY.md` and `plans/PROGRESS.md` (paths to the archive).
- Generated, not regenerated by me: `ops/dashboard.html`, `ops/public/dashboard.html`, `ops/artifact/control-room.html`, `ops/health.json`, `ops/HEALTH_REPORT.md`. They still show the old names until the next dashboard run.
- `grep "Obour Hub"` in `_SIR`: same kind of history; plus `plans/sir-education-hub*.md` that name the rename on purpose.
- Desktop and `AGENTS.md`: `AGENTS.md` mentions the two names only in the intended lines (2 hits, both the rename note and the cancellation note).

## Locked

- `D:\Projects\SIR Platform` (repo folder) is still locked. `Move-Item` and `mv` both return "being used by another process" / "Device or resource busy". Retries over about 2 minutes did not clear it. Likely holder: a worker process started 17:42 (opencode 37228, sh 36792, timeout 39816), whose prompt names SIR Platform. Its working folder cannot be read from here. Nothing was killed, because it is another agent's job. Next step: run the move once that worker finishes, as `mv "D:/Projects/SIR Platform" "D:/Projects/old projects/SIR Platform"`.
- The folder has uncommitted changes (`.gitignore`, `assets/brand/icon.png`, `scripts/dev-start.ps1`, `scripts/dev-stop.ps1`). They move with the folder. Not committed by me.

## Things to know

- Three files I had edited (`ops/PORTFOLIO.md`, `plans/MAIN_PLAN.md`, `plans/WAVE_STUDY.md`) were reset to their committed versions during the run. The cause was not identified. I re-applied the edits and committed them (07a9cec). A worker or a regeneration step may be resetting files; the control-room agent regenerates `ops/PORTFOLIO.md` from its own data, which can overwrite the rename again.
- Not touched: GitHub repo `sirahmed8/sir-platform` (the cancelled project's repo still exists; decide later whether to archive it), the old SIR Platform .lnk files in the archive, the legacy folders.
- Other agents' uncommitted files were left alone, including `ops/READ_LOG.md`, `ops/artifact/*`, `plans/sir-study.md`, `ops/competitors/sir-laptop-manager.md`. `plans/sir-mods-for-gta-v.md` was skipped by the text pass because another agent was editing it.
