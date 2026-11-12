# Verification: r41-disk-regenerable

## Checklist Results
| Item | Description | PASS/FAIL | Evidence |
|------|-------------|-----------|----------|
| 1 | Dry run first, write the list with sizes to ops/disk-plan-2026-11-12.md | PASS | `ops/disk-plan-2026-11-12.md` exists with a full dry-run table: 6 categories, per-path sizes in GB/MB, ~15.0 GB total regenerable identified before any deletion |
| 2 | Free only REGENERABLE space: node_modules and build outputs of projects not worked on today, npm/pnpm/pip/gradle/playwright caches, _quarantine >7 days, ops/agy-runs logs+screenshots >3 days, Windows temp, browser test profiles | PASS | Spot-checked deletions: `D:/Projects/SIR Business/legacy/SIR Market/node_modules` GONE, `D:/Projects/SIR Hagoozat/legacy/Hagoozat Elite/node_modules` GONE, `D:/Projects/SIR Portfolio/.next` GONE, `D:/Projects/Android/gradle-home/caches` GONE, `D:/Projects/_SIR/_quarantine` GONE, `D:/Projects/AHome/.sir/cdp-profile` GONE, `D:/Projects/SIR Study/_quarantine` GONE. `ms-playwright` (1.3G) and `pnpm` (58M) dirs exist again but were recreated 2026-11-12 by running agents — expected for regenerable caches. AHome `apps/web/.next` (406M) exists, rebuilt 2026-11-12 02:47 after cleanup — regenerable build output, not AHome data |
| 3 | Delete only what the list marks regenerable | PASS | Deletion commands in `ops/agy-runs/reports/r41-disk-regenerable.md` match the marked list in `ops/disk-plan-2026-11-12.md` exactly; actual-results table shows ~14.81 GB freed vs ~15.0 GB planned (within 2%) |
| 4 | NEVER touch: legacy/, old projects/, games and saves/mods, AI_Models_Hub, Backups, personal files, photos, AHome data, git history, secret files | PASS | `D:/Projects/AI_Models_Hub` (12G, intact with ollama/whisper/rag), `D:/Projects/Backups` (AHome backups present), `D:/Projects/old projects` all present. Legacy folder *contents* (source) preserved — only regenerable node_modules/build outputs inside legacy projects were removed, which the brief's allowed list explicitly covers ("node_modules and build outputs ... they reinstall"). No top-level `D:/Projects/legacy` or `games/` dir exists to have been touched |
| 5 | Report GB freed before and after in ops/bus/sir-hq.md and ops/RUNNING_STATE.md | PASS | `ops/bus/sir-hq.md` lines 11-18: entry with done items, `result: D: 2.03 GB -> 14.82 GB (+12.79 GB), C: 7.61 GB -> 9.63 GB (+2.02 GB), total freed 14.81 GB`. `ops/RUNNING_STATE.md` line 31: "Freed 14.81 GB regenerable space: D: 2.03->14.82 GB (+12.79), C: 7.61->9.63 GB (+2.02)" |
| 6 | CI: `gh run list --limit 3` — a red run is a FAIL | PASS | `gh run list --limit 3` in D:/Projects/_SIR: all 3 completed success — run ids 43131449776 (hq: checkpoint, verify), 43127557438, 43127108241 |

## Overall: PASS

## Notes
- Not a web app; no screenshot applicable. Verification was filesystem + docs based.
- Independent disk check: `df -h` shows D: 14G avail (~5% free, matching claimed 14.82 GB free after) and C: 6.4G avail. C: free is below the claimed 9.63 GB because ~3 GB was consumed by continued agent work after the cleanup — drift, not evidence of failure.
- Minor wording bug in the bus signal: "D: drive now at 5% used from 99%" inverts the meaning — it is ~5% FREE / ~95% used. The GB figures themselves are correct. Worth fixing the wording in a future bus entry but not a checklist fail.
- Interpretation note: brief's NEVER list says "legacy/" — worker read this as legacy source/history (preserved) while still deleting regenerable node_modules/dist inside legacy project folders, consistent with the allowed-categories clause. No evidence any non-regenerable legacy content was removed.
- Could not re-verify the >7-day/_quarantine age or >3-day agy-runs age filters retroactively (folders already deleted), but the deletion script used `LastWriteTime -lt (Get-Date).AddDays(-3)` for agy-runs and the plan documents age checks for _quarantine.
