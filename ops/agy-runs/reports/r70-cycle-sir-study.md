# r70-cycle-sir-study — DONE

Lens: **data integrity and backups**. Date: 2026-11-13. Worker: devin.

## Result

Full audit/build cycle complete. 12 commits pushed to `main` (7c55f80..53f22ff), all local verification green. CI on main cannot run — `ops/ci-quota-exhausted.flag` present, GitHub Actions fails in ~2s with 0 job steps (billing). Local verification is the documented substitute; no CI-green claim made.

## What was found ("Found without being told")

- Portal sync scheduled task was dead since 2026-11-12: PS5 `2>&1`+`Stop` killed it on first stderr line; scheduled python also lacked Playwright.
- Sync opened a visible Chrome window every 3h; crashed with tracebacks whenever the owner's Chrome held the profile lock.
- `test_portal_sync.py` polluted the production `.sir/portal_sync.log` with temp paths.
- Flashcard mastery: resets wrote `sir_study_<id>_fc_mastered` (dead key) while readers use `sir_study_<id>_mastered`; `or.html` generic reset only wrote the dead key.
- Empty-state overlays counted the wrong card set.
- `getStudyProgressKeys` missed read markers, streak, review log — "reset progress" was incomplete.
- Unguarded `JSON.parse(localStorage...)` at init in all guides — corrupt storage kills the page script.
- `search-index.json` drifted with no freshness guard.
- No progress export/import existed.
- Hub showed portal deadlines with no data-age indicator.

## Improvements shipped (one commit each)

1. `7c55f80` cycle plan + findings
2. `bbdf5c0` portal sync runner: PS5 stderr fix + playwright-python probe
3. `9011d81` `--dry-run` + headless-first fetch
4. `cdb7092` clean exit-4 skip on locked Chrome profile
5. `75baf69` test log isolation
6. `a8a1005` flashcard mastery reset + empty states unified (all 7 guides)
7. `e344ee5` `sirStorageGet` guarded init reads
8. `c951bc7` full progress reset w/ preference allowlist
9. `c7dde01` progress export/import backup in Settings > Data (EN+AR)
10. `86918a8` search-index `--check` + regenerated index
11. `b4bd3df` `verify_data_integrity.py` in verify.ps1 step 17 + or.html dead-key fix
12. `11e4f7c` portal staleness warning on hub

## Verification evidence

- `scripts/verify.ps1`: **ALL CHECKS PASSED** — 17/17 steps (files, py compile, htmlhint, ESLint, Prettier, Ruff, MyPy, HTML/viewport, hyperlinks, button wiring all 8 guides, T-106 accuracy, T-021 integrity 105/105, dev scripts, gitleaks [2 known gitignored .env false positives, non-blocking], unit tests, shared assets, index freshness + data-integrity guards).
- `python -m unittest discover -s tests`: **51 tests OK** (2 browser skips under msys python).
- `tests.test_browser` with `PLAYWRIGHT_NODEJS_PATH="/c/Program Files/nodejs/node"` + user-site Python (chromium-1243 installed this round): **19/19 OK in 711s**.
- Portal sync live probe: locked profile -> clean exit 4, one log line, no traceback.

## Files

- Cycle report: `.sir/reports/2026-11-13-cycle.md`
- Plan: `.sir/cycles/2026-11-13-1.md`
- Checkpoint: `.sir/CHECKPOINT.md` (r70 section appended)

## Open promises (honest)

- M2 spaced-repetition backend: OPEN, not claimed.
- T-103: sync healthy but a real portal read still needs Chrome closed (auto-retries every 3h).
- T-107 Drive mirror, T-023 Obour retirement, T-113 post-exam rotation: unchanged.
