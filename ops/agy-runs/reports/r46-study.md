# r46-study report (2026-11-12)

Round r46: competitor matrix + feature-gap round for SIR Study. All brief items complete. Everything pushed straight to `main`.

## What was done

### 1. Competitor research and plans
- Researched 7 competitors/best-in-class apps via web search (official pages + pricing pages; third-party prices marked unverified): Quizlet, Anki, Brainscape, RemNote, StudyFetch, Duolingo, Knowt (plus open-source cousins noted in the matrix).
- Wrote `.sir/plans/COMPETITOR_MATRIX.md` in the same format as `D:/Projects/SIR AI/.sir/plans/COMPETITOR_MATRIX.md`: per competitor, strongest 3 features, weakest 3 flaws, what SIR Study copies, what SIR Study does better, pricing.
- Wrote `.sir/plans/FEATURE_GAPS.md`: 22 ranked gaps (G1-G22), each with a concrete acceptance test. G1-G3 marked DONE; G4-G22 remain as the ranked backlog.
- Commit `2da4b3d` pushed to main.

### 2. Implemented the 3 highest-value, lowest-risk gaps

**G1 - Per-guide section read progress** (commit `230d03f`)
- `guides/study-guide-ui.js`: discovers content headings (`h2/h3.card-title`, `h2/h3.section-title` conventions) in all 7 subject guides, injects a 44px mark-as-read toggle per section, persists state per guide file in `localStorage` key `sir_study_read_<file>`, and renders a progress chip in `.nav-actions` showing `done/total` with a jump-to-first-unread action.
- `guides/study-r11.css`: toggle + chip styles, RTL-aware.
- `guides/i18n.js`: new keys in BOTH English and Arabic dicts (root cause found during verification: `sirText()` checks the AR snapshot `SIR_I18N.dict`, so EN-only keys silently fell back to Arabic).
- Hub page untouched (no `h2.card-title` headings there), verified zero controls injected.

**G2 - Hub study-streak widget** (commit `1c586f0`)
- `guides/study-guide-ui.js`: new `sirMarkStudyDay()` activity log (`sir_study_active_days` localStorage) written by read-progress toggles, `.btn-mastery` ratings (delegated listener), and pomodoro completion in `guides/study-shell.js`. Quiz days derived from existing `sir_study_review_log`.
- `guides/START_HERE.html`: streak card on the hub showing current streak (today-or-yesterday grace), best streak, and 7 day dots. Honest empty state when no activity.
- Real bug found and fixed during verification: `bestStreak` counted backward from run start and returned 1 for a full run; corrected.
- i18n keys added EN+AR.

**G3 - ICS add-to-calendar export** (commit `ec7abab`)
- `guides/START_HERE.html`: client-side ICS generation (Blob download, works offline after page load). Exam cards get a 44px calendar button; `DTSTART` in UTC from `start_iso`, `DURATION` PT1H/PT2H parsed from duration text, bilingual `SUMMARY`, escaped `DESCRIPTION`, 1-hour `VALARM`.
- Portal deadlines: `.portal-ics` button rendered only when a due date exists. Date-only dues become all-day events via `DTSTART;VALUE=DATE` literal (no timezone shift); timestamp dues become 30-minute timed events in UTC.
- Real bug found by test_18 and fixed: `new Date("YYYY-MM-DD")` parsed as local midnight shifted the all-day date back one day in this timezone; fixed by treating date-only values as calendar dates and building `DTEND` via `Date.UTC`.
- i18n keys added EN+AR; buttons fully labeled `aria-label`/`title`.

### 3. Tests added (`tests/test_browser.py`)
- `test_16` read progress, `test_17` streak widget, `test_18` calendar export (routes a sample `portal-deadlines.json` fixture for the currently-empty deadlines file; verifies exam DTSTART `20261115T160000Z`, PT1H duration, VALARM, date-only `VALUE=DATE` all-day event, and timestamp deadline `20261121T215900Z` + PT30M).
- Earlier focused runs: test_17 ok (3.65s), test_18 ok (3.49s).

## Commands run and real output

- `python -m unittest discover -s tests -p "test_*.py"` (background, ~11.5 min):
  `Ran 62 tests in 693.314s` / `OK` (59 prior + 3 new r46 tests; BrowserAcceptance ran with Playwright).
- Integrity eval (inside suite and standalone): `105/105 checks passed` (73/73 graded-work refusals, 32/32 legitimate answers with citations).
- `scripts/verify.ps1`: steps 1-7, 9-11 all OK (core files, mobile/PWA/44px audit, hyperlinks, button wiring, math accuracy, integrity guard, dev-server scripts, unit tests, status.json refresh, shared-asset drift guard). Step [8/11] gitleaks `detect --no-git` reports 2 hits, both in gitignored untracked `.env` (pre-existing local-only false positive; verified via `gitleaks ... --report-path` showing `File: D:/Projects/SIR Study/.env | generic-api-key` x2). Script exits 1 on this step -> overall "VERIFICATION FAILED" is the known `.env` artifact, same as recorded in earlier checkpoints.
- JS syntax check earlier this round: `ALL-JS-OK`.
- Manual Playwright verification across 320/390/768/1280 px, EN/AR, light/dark: no horizontal overflow (`scrollWidth == innerWidth` at every combo), zero page errors, all new controls >=44px, ICS download verified end-to-end (Blob -> file content inspected).
- `git push origin main`: all commits pushed (`2da4b3d`, `230d03f`, `1c586f0`, `ec7abab`, `a70cc30`).

## CI status (honest)

`ops/ci-quota-exhausted.flag` exists. Latest main CI run `43240019924` (Full Verification Suite & PWA Audit) failed in **2 seconds with 0 job steps** - the documented quota/billing signature, not a code failure (`gh api .../jobs` shows `steps_count: 0`, `started_at`/`completed_at` 2s apart). Per WORKER_PREAMBLE, local verification substitutes while the flag exists. `.sir/status.json` was regenerated by verify.ps1 and now records `ci: "failure (run 43240019924)"`; committed as-is for accuracy.

## Files changed

- `.sir/plans/COMPETITOR_MATRIX.md` (new)
- `.sir/plans/FEATURE_GAPS.md` (new)
- `guides/study-guide-ui.js` (read progress + activity log)
- `guides/study-shell.js` (pomodoro activity hook)
- `guides/study-r11.css` (toggle/chip/ics styles)
- `guides/i18n.js` (EN+AR strings for all three features)
- `guides/START_HERE.html` (streak card, ICS exam + portal buttons, ICS helpers)
- `tests/test_browser.py` (test_16/17/18)
- `.sir/CHECKPOINT.md`, `.sir/status.json`, `.sir/evidence/r20/browser_report.json` (evidence regenerated by audit tooling)

## Uncertainties / notes

- Gitleaks local `--no-git` step will keep failing verify.ps1 until `.env` is excluded from the scan or moved; recommend adding `.env` to a `.gitleaksignore`/config or scoping the scan. Not changed this round (out of brief scope, pre-existing).
- Portal deadlines file is currently empty, so portal ICS buttons only appear when dated items exist; test_18 covers the rendering path via a routed fixture.
- `sir_study_active_days` starts empty for existing users; streak shows honest zero state until first activity. Quiz days are derived retroactively from `sir_study_review_log`, so past quiz activity counts.
- Competitor prices from third-party pages are marked unverified in the matrix.

## Recommended next steps

- G4-G22 in FEATURE_GAPS.md are the ranked backlog; highest remaining value items include spaced-repetition scheduling for flashcards and per-subject progress dashboards.
- Fix the gitleaks `.env` false positive so verify.ps1 exits green locally.
- Re-run CI once `ci-quota-exhausted.flag` clears.
