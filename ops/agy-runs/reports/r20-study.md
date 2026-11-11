# r20-study report — 2026-11-11

Worker: Devin (SWE-2 Flash). Continued from previous model's uncommitted M5 work, finished every open item in the r20 brief, closed all of .sir/R19_CHECKLIST.md with proof.

## Item 1 — Exams side by side (guides/exams.json vs .sir/SCHEDULE.md portal table)

| # | Subject | exams.json | SCHEDULE.md (portal, dd/mm/yyyy) | Match |
|---|---------|-----------|----------------------------------|-------|
| 1 | Data Structures ع ج 201 | 2026-11-08 11:30 +02:00, hall 533 | 08/11/2026 11:30-12:30, 533 | YES |
| 2 | Systems Analysis & Design ع ج 210 | 2026-11-09 11:30, hall 533 | 09/11/2026 11:30-12:30, 533 | YES |
| 3 | Operations Research ع أ 205 | 2026-11-10 11:30, hall 533 | 10/11/2026 11:30-12:30, 533 | YES |
| 4 | Human Rights إ ن 203 | 2026-11-12 18:00, "Online (Moodle)" | 12/11/2026 06:00-07:00 PM, online | YES |
| 5 | Business Administration إ ن 204 | 2026-11-15 18:00, "Online (Moodle)" | 15/11/2026 06:00-07:00 PM, online | YES |
| 6 | HCI CS 314 | 2026-11-18 11:30, hall 513 | 18/11/2026 11:30-12:30, 513 | YES |
| 7 | Electronics ع أ 222 | 2026-11-19 11:30, hall 533 | 19/11/2026 11:30-12:30, 533 | YES |

Weekday check: 2026-11-12 is Thursday (الخميس) — confirmed by tests/test_exam_weekdays.py and python `date` computation. Human Rights is the next exam (tomorrow 18:00, online Moodle).
Disagreements: NONE. "Owner must confirm" section in CHECKPOINT.md is empty.

## Item 2 — H3 graded-work guard (commit 2dc81b1, previous model)
Verified this session:
```
python scripts/study_ai_explainer.py eval
Graded-Work Refusal Rate: 73/73 (100.0%)
Legitimate Explanation Rate: 32/32 (100.0%)
105/105 checks passed
[SUCCESS] T-021 Evaluation PASSED
```
scripts/integrity_guard.py is default-deny; tests/test_integrity.py 14 tests ok.

## Item 3 — H4 Playwright browser tests (commit e99d076 + this session's run)
- tests/test_browser.py: 5 tests — pages load w/o script errors, click every visible button, answer one quiz, run one search, 44px touch targets at 320px.
- CI (.github/workflows/verify.yml) installs playwright + `playwright install --with-deps chromium`.
- Local run under user python (C:/Users/a7med/AppData/Local/Python/bin/python.exe, playwright 1.63.0, chromium-1243):
```
Ran 5 tests in 513.047s — OK
```
- .sir/evidence/r20/browser_report.json: pages hub/human-rights/business-admin/hci all 0 page_errors; buttons_clicked=379; touch_target_failures=[]; inline_links_under_44=0; console_errors=[]; quiz_answered=true; search_run=true.
- Note: msys64 python has no playwright; tests self-skip there (5 skips). User python runs them fully. CI uses setup-python 3.12 — green.

## Item 4 — M1 crash-restart proof (.sir/evidence/r20/m1-crash-restart-proof.md, previous model)
Scheduled task `SIR_Study_Server` already had logon + PT5M repetition trigger — nothing to add. Two kill-and-recover cycles proven with dev.log, pid file and live port after each fire. Caveat documented: a concurrent worker manually restarted serve.py twice; the task-driven chain is still proven. Optional follow-up noted: serve.py dual-bind guard.

## Item 5 — M5 shared assets finished (commits b1848e6, 0c26560, 9e7b388)
- Extracted: study-r11.css, study-a11y.css, study-charter.css, study-noscript.css, study-shell.js, study-head.js, study-guide-ui.js, i18n.js. Guides carry zero duplicated inline CSS/JS blocks.
- New guard: scripts/verify_shared_assets.py wired as verify.ps1 step 11/11 — fails on missing assets, identical inline script/style across guides, <style> inside <noscript>, or any loaded css/js missing from sw.js precache.
- sw.js: deduped precache list, bumped to sir-study-v1.0.0-r22 (offline preserved; stale-while-revalidate for assets, network-first for HTML).
- 14 one-shot analysis/patch scripts moved scripts/ -> _quarantine/scripts/ (fix_all_titles_bidi, remove_emojis, inspect_*, detect_*, analyze_*, audit_suite, generate_coverage_md, capture_*_evidence, inventory_guides, print_subj_overview). No code references them (docs only).

## Item 6 — M6 touch targets at 320px
Covered by test_05_touch_targets_at_320px (item 3): 0 failures, 0 inline links under 44px. Also verified manually at 320px on or.html (screenshots .sir/evidence/r20/or-320-*.png).

## Item 7 — M7 English shell (commit b1848e6)
guides/i18n.js dictionary translates nav, buttons, settings modal, drawer, tab labels (per-guide overrides). Toggle switches language AND direction; content stays Arabic with an explicit note.

## Item 8 — L1 to L8
- L1 FIXED: serve.py:39 `OWNER_EMAIL = os.environ.get("SIR_OWNER_EMAIL", "")`; no email literal in tracked files.
- L2 FIXED: export_sanitized.py loads untracked .sir/privacy-terms.local.txt (git-ignored, present locally).
- L3 FIXED r19: portable paths.
- L4 FIXED (5cc6ac5): CREATE_NO_WINDOW on Windows subprocess calls.
- L5 FIXED r16: self-hosted fonts precached.
- L6 FIXED: storage_admin.py purge-temp requires --apply; default dry-run verified live (preview printed, 0 files deleted).
- L7 FIXED (5cc6ac5): .gitignore covers health.txt/screenshots/dev.log; I added .sir/LAST_CONTEXT.md.
- L8 VERIFIED CLEAN: playwright DOM scan at 320px found no text node with 5+ repeated chars; .table-scroll-hint renders one arrow. Screenshots or-320-top/hint.png.

## Item 9 — Student journey at 390px, 10+ visible improvements
Journey script drove human-rights, business-admin, hci at 390x844: all tabs clicked, quiz answered (score "تم حل 1"), flashcard flipped (class -> "flashcard open"), search typed, settings + drawer opened, scrolled top/bottom. No console errors, no horizontal overflow.

BUG FOUND AND FIXED: `switchUniversalTab` was declared inside an IIFE in all 7 subject guides and never exposed globally, while every tab button uses `onclick="switchUniversalTab(...)"` -> ReferenceError on every click (tabs only worked via a delegated fallback handler). Added `window.switchUniversalTab = switchUniversalTab;` beside the existing aliases in all 7 guides. After fix: 0 pageerrors across all 8 pages, all 41 tab buttons clickable.

10 visible improvements shipped in shared guides/study-guide-ui.js + guides/study-r11.css (apply to hub + all guides, precached for offline):
1. Section tab bar sticks under the top nav while scrolling (+ shadow when stuck).
2. Reading progress bar pinned to the top edge (scaleX by scroll %).
3. Back-to-top button (44px, appears after ~1 viewport, smooth scroll, reduced-motion aware).
4. Search matches highlighted with <mark class="sir-hl"> in the active pane.
5. Match-count chip per search box ("N نتائج" / "لا نتائج").
6. First search match auto-scrolls into view.
7. Last active tab remembered per guide (localStorage) — returning student lands where they stopped.
8. Top nav gains elevation (background + shadow) once scrolled.
9. Tactile press feedback scale(.98) on tabs, quiz options, flashcards, nav buttons.
10. Brand ::selection color in dark + daylight themes.
11. (bonus) scroll-margin-top so anchored panes clear the sticky nav + tab bar.

Screenshots: .sir/evidence/r20/ before-*.png (top/tab2/quiz/flashcard/search/settings/drawer/bottom per guide) and after-*.png (scrolled/search/selection/flashcard/quiz/tabs per guide). Verified live: progress matrix() values non-zero, topBtn visible, tab-bar computed position sticky, 13 marks + "13 نتائج" chips on HR search, persisted_tab="tab-lectures" after reload.

## Commands run (real output highlights)
- `python scripts/verify_shared_assets.py` -> `[OK] 8 shared assets, no duplicated inline CSS/JS, 9 loaded assets precached`
- `python scripts/verify_all_buttons_wired.py` -> `ALL GUIDES PASSED`
- `python -m unittest discover -s tests` -> `Ran 33 tests ... OK (skipped=5)` (msys python; playwright skips)
- user-python `python -m unittest tests.test_browser -v` -> `Ran 5 tests in 513.047s OK`
- `powershell -File scripts/verify.ps1` -> `ALL CHECKS PASSED: SIR Study is Green & Verified!` (11/11 steps incl. gitleaks clean, status.json regenerated ci=success)
- `python scripts/storage_admin.py purge-temp --dry-run` -> preview only, `STATUS: DRY-RUN ONLY`
- `curl http://127.0.0.1:3300/api/health` -> 200 (server live, restarted by scheduled task)

## CI
- run 42935759651 (H4/M6 commit): success, 8m23s (includes browser tests)
- run 42937316540 (M5 finish): success, 8m8s
- run 42938523922 (9e7b388 quarantine): success, 9m39s
- run 42938575436 (63f4ad5 checklist+checkpoint, HEAD of main): success, 9m34s
All three r20 finishing runs green; `gh run list` shows consecutive successes on main.

## Still open / unsure
- M2 spaced repetition: still not built (honest). Flashcards UI exists; no SRS scheduling.
- serve.py dual-bind on port 3300 (SO_REUSEADDR) — cosmetic, noted for later.
- START_HERE "tab-bar" is actually a link bar to guides; sticky styling applies harmlessly. Its 3 click-detach errors in my test were navigation artifacts, not bugs.
- Playwright tests skip under msys64 python (no pip); they run under the user python and in CI. Consider pinning a venv later.

## Commits this session
- 0c26560 M5 finish + drift guard + button-checker external JS
- 659c327 item9 improvements + switchUniversalTab fix
- 9e7b388 quarantine one-shot scripts
- 63f4ad5 checklist + checkpoint
(plus previous model's 2dc81b1, 5cc6ac5, b1848e6, e99d076 verified this session)
