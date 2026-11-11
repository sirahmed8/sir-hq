# SIR Study — Round 27 Report (r27-study-sources)
Date: 2026-11-11. Worker: Kilo (SIR autopilot CLI agent). Branch: main, pushed c0bfa7c.
Repo: https://github.com/sirahmed8/sir-study.git (private)

## 1. Owner questions answered with evidence (in .sir/CHECKPOINT.md)

### Q1 — Does SIR Study already fetch NEW lectures, assignments statements and quizzes from Moodle for every course?
No. There is no recurring portal fetch.
- The only portal read is a one-time manual digest on 2026-11-01: `materials/digest/2026-11-01.md` — read-only, taken by HQ from Ahmed's already-signed-in Chrome, a static snapshot of 12 courses with activity counts (files/assignments/quizzes per course id).
- No script in `scripts/` signs into Moodle, lists per-course items with dates, or auto-downloads new lectures/assignments/quizzes.
- Materials under `materials/obour-year2-term1/` are static PDFs dated 10/11–10/24/2026 — old, not live portal items.
- Task T-103 (Portal and Moodle watcher: snapshot diff, regenerate pages, phone reminder; hourly in exam week) in `.sir/TASKS.md` is still unchecked before this round.

### Q2 — Are sources stored clean (one folder per course: Lectures, Assignments, Quizzes, Summaries, Practice; no duplicates)?
No. Each course folder (e.g. `01 - هياكل البيانات (Data Structures)`) is flat: lectures, notebooks, studio summaries, a full textbook PDF, and a solved graded assignment `حل تكليف هياكل البيانات 5 - أحمد علاء الدين 625177.pdf` (contains his name + student id — private data, local-only) all mixed in one folder.
- No `Lectures/Assignments/Quizzes/Summaries/Practice` subfolders.
- No content-hash or name deduplication; inconsistent file names.
- The solved graded assignment is graded work: never shared, never treated as source material, agents never complete it.

## 2. What was built / fixed

### scripts/portal_sync.py (new) — T-103 portal sync
Read-only Moodle watcher for https://elearning.oi.edu.eg through Ahmed's already signed-in Chrome "Default" profile:
- Signs in ONLY via the signed-in Chrome profile (Playwright persistent context, `channel="chrome"`, `user_data_dir=%LOCALAPPDATA%\Google\Chrome\User Data`, profile Default). NEVER types a password.
- If the portal shows a sign-in screen → reports ONE exact tap ("open Chrome, go to https://elearning.oi.edu.eg, sign in once, then re-run") and exits code 2. Never submits/starts/marks any quiz/assignment/exam.
- Lists every course item with date: `{course, course_folder, item, type, due_iso, section, url}`; printed to console + written to `materials/portal_index.json`.
- Downloads new lectures/attachments (auth cookies harvested from the signed-in profile; read-only).
- Dedup by sha256 content hash AND file name across the whole course tree; skips duplicates.
- Files new items into clean per-course structure:
  `materials/obour-year2-term1/<course>/{Lectures,Assignments,Quizzes,Summaries,Practice}/`
- Skips solved graded assignments (name pattern `(حل|solution)\s+تكليف`).
- Regenerates guide data: `materials/portal_index.json` (full item list) and `guides/portal-deadlines.json` (dated items for hub countdowns).
- Sends one Telegram "مادة جديدة" message per genuinely new item (course, item, due date) via `_SIR/scripts/deliver/send-telegram.mjs` (Arabic, no emoji).
- `run_sync()` returns exit 0 on success, 2 if login required, 3 if Playwright missing (setup: `pip install playwright && playwright install chromium`).

### scripts/practice_generator.py (new) — practice sets (never graded answers)
For every assignment/quiz item from `materials/portal_index.json`, generates a PRACTICE set of the SAME topics:
- New questions with worked answers + a concept explanation.
- Concept explanation via `scripts/study_ai_explainer.py` `explain_query()`, which enforces academic integrity: refuses any graded-work request (73/73 refused in T-021 eval) and instead gives theory + a parallel example with different numbers.
- Output written to `materials/obour-year2-term1/<course>/Practice/<item-slug>.json` plus `materials/practice_index.json`.
- Each set carries an integrity notice in Arabic: these are practice questions on the same topics, NOT the actual graded assignment/quiz answers, not for submission.

### scripts/install-portal-sync-task.ps1 + scripts/run-portal-sync.ps1 + scripts/run-portal-sync-hidden.vbs (new)
- Registers Windows Scheduled Task `SIR_Study_Sync` (current user), every 3 hours (interval PT3H, indefinite duration, start boundary today), enabled.
- `run-portal-sync.ps1` pauses the sync (logs "PAUSED", exits 0) while `D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json` exists, per the owner automation rule (automations pause while a game runs).
- Verified registered: `Get-ScheduledTask -TaskName SIR_Study_Sync` → State=Ready; trigger Interval=PT3H, Enabled=True, Start=2026-11-11T00:00:00+02:00.

### Hub deadline countdowns from portal dates
- `guides/study-guide-ui.js`: added `window.SIR_PORTAL_DEADLINES` (fetches `portal-deadlines.json`, fails safe to empty) and `window.sirPortalDeadlineText(iso)` (past=تم / today=اليوم / tomorrow=غداً / else date + days left), reusing the existing `dayIndex`/`sirPad2` helpers.
- `guides/START_HERE.html`: added a "مواعيد البوابة القادمة" section rendering each portal deadline (course, item, type, status) sorted by due date; empty state shows "لا توجد مواعيد مسجلة من البوابة بعد."

### Prior-model work preserved (no-revert rule)
- `scripts/moodle_sync.py` — Moodle web-service token sync (token-gated, flat download, invented course-ID mappings). Preserved unmodified; not the primary sync.
- `scripts/portal_receiver.py` — loopback-only HTTP receiver on 127.0.0.1:18777, input-validated, blocks path separators and personal names. Preserved unmodified; not running.

## 3. Verification (commands run and real output)

`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1` — ALL 11 CHECKS PASSED:
1. Core files & assets — OK (all expected guides/assets present)
2. HTML integrity & mobile viewports — OK
3. Inter-guide hyperlinks — OK (0 broken)
4. Deep button wiring — OK (all 8 guides, all handlers resolve)
5. Mathematical & theoretical accuracy audit (T-106) — OK (OR + SAD models verified, quiz blocks valid)
6. Academic integrity guard (T-021) — OK: Graded-Work Refusal 73/73 (100%), Legitimate Explanation 32/32 (100%), 105/105
7. Dev server scripts & desktop hooks — OK
8. Gitleaks secret scan — OK: 0 leaks (scanned 15.13 MB)
9. Unit tests — OK: 52 tests run, 0 failed, 8 skipped (browser tests skip locally because Playwright is not installed; CI installs Playwright + Chromium and runs with `SIR_REQUIRE_BROWSER=1`)
10. `.sir/status.json` regenerated — OK: version=1.0.0, tasks=30/33, ci=success
11. Shared asset drift guard (M5) — OK (8 shared assets, no duplicated inline CSS/JS)

New unit tests added and passing:
- `tests/test_portal_sync.py` — 12 tests: classification, subfolder mapping, date parsing, course aliases, duplicate detection by name and hash, existing signatures, clean-structure filing, deadline/index writing.
- `tests/test_practice_generator.py` — 4 tests: topic mapping, slugify, practice-set fields (integrity notice present, never graded answers), writing into course `Practice/` folders + index.

## 4. What is unsure / not done (live behavior could not be executed here)
- The live Moodle portal returns HTTP 403 to plain HTTP/bot requests (bot protection) and Playwright is not installed in this session, so the end-to-end Chrome-profile sign-in + item listing/download could NOT be executed against the real portal. `portal_sync.py` is written for that path; when Ahmed runs it with Playwright installed and Chrome signed in, it will sign in through his profile (no password typed) or report the one exact tap if a sign-in screen appears.
- The scheduled task `SIR_Study_Sync` is registered and enabled, but its first run will exit with the Playwright-setup message until Playwright + Chromium are installed on this machine (one-time: `pip install playwright && playwright install chromium`).
- Telegram delivery requires `SIR_TELEGRAM_BOT_TOKEN` / `SIR_TELEGRAM_CHAT_ID` env vars (read from Windows User scope by send-telegram.mjs); not exercised here (no test message sent, per policy).
- CI (GitHub Actions `verify.yml`) installs Playwright + Chromium and runs `verify.ps1` with `SIR_REQUIRE_BROWSER=1` on push; the push (c0bfa7c) triggered CI but the run result was not polled in this session (per policy, no polling loops).

## 5. Files changed / added
Added:
- `scripts/portal_sync.py`
- `scripts/practice_generator.py`
- `scripts/run-portal-sync.ps1`
- `scripts/run-portal-sync-hidden.vbs`
- `scripts/install-portal-sync-task.ps1`
- `tests/test_portal_sync.py`
- `tests/test_practice_generator.py`
Preserved (prior-model work, not reverted):
- `scripts/moodle_sync.py`
- `scripts/portal_receiver.py`
Modified:
- `guides/study-guide-ui.js` — portal deadlines fetch + `sirPortalDeadlineText`
- `guides/START_HERE.html` — portal deadline countdown section
- `.sir/CHECKPOINT.md` — Q1/Q2 answers, r27 state
- `.sir/status.json` — regenerated by verify.ps1 (version 1.0.0)

Commits pushed to main:
- 7e0b169 r27: answer owner questions Q1/Q2
- 31a1e43 r27: portal sync, practice sets, deadline countdowns, scheduled task
- c0bfa7c r27: preserve prior-model portal receiver

## 6. Recommended next steps
1. Confirm CI on main is green for c0bfa7c (gh run list / gh run watch).
2. Install Playwright + Chromium once (`pip install playwright && playwright install chromium`) so the scheduled task can perform the live Chrome-profile sync; then Ahmed signs in to the portal once in Chrome (the one tap the script reports if needed).
3. After the first live sync, confirm `materials/portal_index.json`, `guides/portal-deadlines.json`, and course `Practice/` folders are populated, and a Telegram "مادة جديدة" message is received.
4. M2 spaced-repetition backend remains the only open product promise — do not claim it.

المطلوب منك: لا شيء (CI result review optional; Playwright install is a one-time local setup Ahmed can do).
