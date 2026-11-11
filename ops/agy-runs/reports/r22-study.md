# r22-study report (2026-11-11)

Round 22 of SIR Study. Brief: `/d/Projects/_SIR/ops/briefs/r22-study.prompt.txt`.
This session continued work left uncommitted by the previous worker; all 11
brief items are now closed with proof.

## What was already done before this session (commits on main)

- `2950d5b`, `932812e` — item 1: removed the stray repeated "n" glyph row
  under the header on all 8 pages (broken ligature artifact).
- `852e728` — items 2-10: unified single-row sticky header on all 8 pages;
  tab labels <=2 words, active tab scrolls into view, flick-swipe between
  tabs; every countdown/badge driven by `guides/exams.json` + real date
  (past = تم, today = اليوم, tomorrow = غداً, else days left); hub dev
  details (port/pid) moved into a hidden developer panel; settings sheet
  rebuilt as segmented controls + real switches; flashcard flipped state
  made visually distinct with colored mastery buttons and speaker/theme
  icons; toasts pinned top, one line, auto-dismiss; new bottom audio bar
  with persisted volume slider; integrity notice shown once on the hub and
  as a one-line link inside guides; calmer drawer active state, larger
  date badges, labelled version footer.
- `tests/test_browser.py` — added test_06/07/08 covering horizontal scroll,
  header clearance, tab label fit/active visibility, and exams.json status
  correctness.

## What this session did

The previous worker was cut mid item 11 (self-audit loop). Uncommitted work
found: `guides/study-r11.css` overflow-x fix, `.sir/DEFECTS_R22.md` cycle
2-3 logs, `.sir/evidence/r22/audit_r22.py` + 128 audit screenshots,
`.sir/CHECKPOINT.md` progress notes. Nothing was reverted; all of it was
verified and committed.

1. Re-ran the full audit fresh to prove the "3 clean cycles" claim:
   `python .sir/evidence/r22/audit_r22.py` (user python with playwright,
   server already on 127.0.0.1:3300). Result:

   ```
   OK     START_HERE.html 320px dark navH=75 seg=4 sw=2
   ... (64 lines, all OK) ...
   OK     electronics.html 1280px light navH=75 seg=4 sw=2
   ==== SUMMARY: CLEAN
   ```

   8 pages x 4 widths (320/390/768/1280) x 2 themes (dark/light) = 64
   combinations, every tab clicked, drawer + settings opened on each:
   0 defects, 0 page errors. This is the third consecutive clean cycle;
   cycles A/B findings and fixes are logged in `.sir/DEFECTS_R22.md`.

2. Ran the unit + browser suite under the user python (msys python lacks
   playwright; skips are expected there):

   ```
   "/c/Users/a7med/AppData/Local/Python/bin/python.exe" -m unittest discover -s tests -v
   -> test_01..test_08 all ok (incl. the 3 new r22 tests)
   -> integrity eval 73/73 refused, 32/32 answered, 105/105 checks passed
   -> Ran 36 tests ... OK
   ```

3. Committed the pending work: `984048a` "r22 item11: self-audit cycles 2-3
   clean - overflow-x clip fix, audit detector hardened, 64-combo sweep
   evidence" (includes audit script, 128 drawer/settings screenshots,
   DEFECTS_R22.md, CHECKPOINT.md, hq report note, regenerated
   browser_report.json).

4. Updated `.sir/CHECKPOINT.md` header to "Round 22 complete".

## Item-by-item status vs the brief

| # | Item | Status |
|---|------|--------|
| 1 | Stray "n" glyph row | Fixed (2950d5b, 932812e) |
| 2 | Unified sticky header | Fixed (852e728) |
| 3 | Tab bar labels/scroll/swipe | Fixed (852e728) + test_07 |
| 4 | Countdown/date chips from exams.json | Fixed (852e728) + test_08 |
| 5 | Hub dev details hidden | Fixed (852e728) |
| 6 | Flashcard states/buttons | Fixed (852e728) |
| 7 | Audio bar + top toasts | Fixed (852e728) |
| 8 | Settings segmented controls/switches | Fixed (852e728) |
| 9 | Drawer calm/footer | Fixed (852e728) |
| 10 | Integrity notice once + link | Fixed (852e728) |
| 11 | Self-audit loop, 3 clean cycles | Done: cycles A/B/C logged in DEFECTS_R22.md; cycle C re-verified CLEAN this session |

## Commands run (real output)

- `git status` / `git diff --stat` / `git log` — found 3 modified files +
  untracked audit evidence; finished and committed them.
- `curl http://127.0.0.1:3300/START_HERE.html` -> `200` (serve.py running).
- `python .sir/evidence/r22/audit_r22.py` (msys python) ->
  `ModuleNotFoundError: No module named 'playwright'` -> re-ran under
  `C:\Users\a7med\AppData\Local\Python\bin\python.exe` -> CLEAN.
- `python -m unittest discover -s tests -v` (msys) -> `Ran 36 tests, OK
  (skipped=8)` (playwright skips expected).
- `python.exe -m unittest discover -s tests -v` (user python) -> all 8
  browser tests ok, integrity 105/105, exit 0.
- `git commit` -> `984048a`; `git push` -> see below.

## Still open (unchanged, honestly marked)

- M2 spaced-repetition scheduling for flashcards: still OPEN, not claimed.
- Optional serve.py dual-bind guard on port 3300: noted, not built.
- Human Rights exam 2026-11-12 18:00 online: tomorrow; briefing task
  handles the daily reminder (checkpoint "Next step").

## CI

- Last green run on main before this push: `gh run list --limit 5` showed
  `completed success` for 852e728 (run 42947679513).
- This push triggers a new Verify run; result checked after push (see
  checkpoint/report tail).
