# R45 report: SIR Jobs scout findings — search input i18n + per-character bidi

**Task:** r45-jobs-scout-fixes
**Project:** D:/Projects/SIR Jobs
**Branch:** main, commit 7bdfda7 (pushed), CI run 43169917756 green
**Date:** 2026-11-12

## What was fixed (root level)

Finding 1 — two search inputs (#pipeline-search index.html:156, #jobs-search index.html:225) showed hardcoded English placeholders/aria-labels in Arabic mode while the palette input localized correctly:

- `src/public/index.html:156` — #pipeline-search now has `data-i18n-placeholder="pipeline.filterPlaceholder" data-i18n-aria-label="pipeline.searchAriaLabel" dir="auto"` (hardcoded English kept as fallback).
- `src/public/index.html:225` — #jobs-search now has `data-i18n-placeholder="openings.searchPlaceholder" data-i18n-aria-label="openings.searchAriaLabel" dir="auto"`.
- `src/public/js/i18n.js:49-58` — `applyI18n()` now also applies `[data-i18n-aria-label]` translations (previously only `data-i18n` text and `data-i18n-placeholder`).
- `src/public/i18n/en.json` and `ar.json` — added keys `pipeline.searchAriaLabel`, `openings.searchPlaceholder`, `openings.searchAriaLabel` (161 keys each, parity preserved; `pipeline.filterPlaceholder` reused for the pipeline placeholder).

Finding 2 — no text input did per-character bidi detection; every input/textarea inherited `direction: rtl` from `html[dir="rtl"]` with its own `dir` null (violates L8 / OWNER_DEFAULTS.md item 15):

- `dir="auto"` added to #pipeline-search, #jobs-search, #palette-input (index.html) and #prop-personal-note textarea (src/public/js/views/proposals.js:137). `dir="auto"` is the browser-native per-first-strong-character detection: Arabic types from the right, Latin from the left, live as the user types.
- `src/public/js/views/proposals.js:137` — textarea `aria-label` now toggles EN/AR with `currentLang` (`data-i18n-aria-label="prop.notesAriaLabel"` keeps it right on every re-render; keys added to both dictionaries).

## Verification run

Commands run, all in D:/Projects/SIR Jobs:

- `node --check src/public/js/i18n.js` / `proposals.js` — OK
- `npm run lint` (eslint --max-warnings 0) — exit 0, 0 problems
- `npm run typecheck` (tsc --noEmit) — exit 0, 0 errors
- `npm test` (40+ suites incl. test-r34-bidi Chrome CDP audit at 1280 EN+AR, DOM-wide mixed-direction audit clean on all views) — exit 0, all suites pass
- `npm run verify` — snapshot drill DRILL PASSED, gitleaks "no leaks found" across 133 commits, privacy/anti-leak audit 0 leaks across 1230 tracked files, dashboard smoke test 200 OK → "verify: all green", exit 0
- On-screen CDP probe (`C:\Users\a7med\AppData\Local\Temp\kilo\verify-r45.mjs`, not committed): loaded http://127.0.0.1:3456/ at 320/390/768/1280 px, EN and AR; checked placeholder, aria-label, dir on #pipeline-search, #jobs-search, #palette-input, #prop-personal-note — all 32 checks PASS:
  - EN: "Filter applications (company, role)..." / "Filter by skill (React, Python, AI)..." / dir=auto
  - AR: "تصفية الطلبات (الشركة، المسمى)..." / "تصفية حسب المهارة (React, Python, AI)..." / aria-label "تصفية الطلبات حسب الشركة أو المسمى" / "البحث في الإعلانات بالمهارة أو المسمى" / dir=auto
  - palette placeholder correctly "اكتب أمراً أو ابحث..." in AR, now also dir=auto
- Screenshot captured: C:\Users\a7med\AppData\Local\Temp\kilo\r45-shots\ar-390-search.png

CI (GitHub Actions, run 43169917756): windows job ✓ (lint, typecheck, npm test, 3m48s), secrets job ✓ (gitleaks clean, 12s). Overall run success.

## Checkpoint

Updated D:/Projects/SIR Jobs/.sir/CHECKPOINT.md with r45 done section.

## Still open / recommendations

None required by the brief. The palette aria-label remains hardcoded English ("Command palette input") — not part of either scout finding; can be added under the same `data-i18n-aria-label` pattern if desired. The previous model's uncommitted tree changes (.sir/jobs/TRACKER.md, docs/Ahmed_Oraby_Verified_CV.pdf, tsconfig.tsbuildinfo) were preserved and committed along with this work, per the never-revert rule.
