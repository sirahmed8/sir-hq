# Review: SIR Study (2026-11-10, independent reviewer)

Repo `D:/Projects/SIR Study`, HEAD `68af90e` (cycle 8). Reviewed by running the project's own tools, calling the live server on 127.0.0.1:3300, rendering pages in a browser at 320, 390, 768, 1280 and 1920 px, and reading code. Nothing was edited, stopped, restarted or committed. (Running `verify_accuracy.py` rewrites `.sir/evidence/accuracy-audit-or-and-sad.md`; git status stayed clean, so the content was identical.)

## Verdict
1. The study guides are real and mostly good: the server answers, 7 guides plus the hub load, no emoji, no em-dash, no TODO text, no AHome text, layout does not overflow at any width I tested, `verify.ps1` and the OR/SAD math checks pass. For the OR exam today the content is usable.
2. The checkpoint over-claims. "All buttons wired" is false (2 dead buttons in the HCI guide, exam on 18/11), the "100 percent graded-work refusal" is a regex that 11 of 18 ordinary phrasings walk past, the daily Telegram briefing is not scheduled and gives a loopback link plus times that contradict the hub, and CI was red once (checkpoint says "0 failing checks in history").
3. The verify chain gives false comfort: it checks that files exist and contain strings, never runs a unit test, the accuracy audit, the button check or the (uninstalled) browser tests. Plan tasks 2 to 7 and the app screens (flashcards, deadlines) are not built.

## Commands run (exact) and results
| Command (cwd `D:/Projects/SIR Study`) | Result |
|---|---|
| `pwsh -NoProfile -File scripts/verify.ps1` | exit 0, "ALL CHECKS PASSED", gitleaks "no leaks found". But the script only tests file presence, regex presence of `viewport-fit`, `manifest.json`, "44px", relative `.html` links, and script file presence. |
| `python scripts/verify_all_buttons_wired.py` | exit 0 while printing "BROKEN ONCLICK HANDLERS (2)" for `hci.html`: `startFittsTrial`, `hitFittsTarget` not defined. Confirmed in the browser: `startFittsTrial()` throws `ReferenceError`. Exit code is 0 even on failure. |
| `python scripts/verify_accuracy.py` | exit 0, PASS 100 percent. Checks 5 hard-coded OR numbers, 7 regex-presence checks for SAD terms, and counts quiz blocks (50 and 50). |
| `python scripts/audit_suite.py` | exit 0, prints a report, asserts nothing. |
| `python scripts/study_ai_explainer.py eval` | exit 0, 10/10 refused, 5/5 answered. Reproduced. See defects H3 for why this number means little. |
| `python .sir/test_sanitized_privacy_gate.py` | passes 6/6 (tests a regex list against 6 planted strings). |
| `python .sir/test_cycle5_e2e.py`, `test_cycle6_e2e.py`, `test_destructive_actions.py`, `test_r13_health.py` | cannot run: `ModuleNotFoundError: playwright`. They are not in CI either. Result: cannot verify. |
| `python scripts/storage_admin.py purge-temp --dry-run` | works, lists 7 pyc files, deletes nothing. |
| `gh run list -L 5` | latest 2 runs green; run `42718092954` (cycle 7 commit) FAILED (gitleaks found 1 secret in a test file), fixed in the next commit. |
| ruff / mypy / eslint / tsc | the project defines none; no `pyproject`, no `package.json`, no `tests/` folder. Not run. |

Service check: `curl http://127.0.0.1:3300/` 200; `/api/health` 200 JSON (pid 39680, uptime 627 s); `/health` 404 (only `/api/health` exists). Foreign `Host: evil.com` on GET gives 403. Path traversal (`/../`, `%2e%2e`) gives 404. `POST /` gives 501.

## Claims table
| # | Claim (source) | Result | Evidence |
|---|---|---|---|
| 1 | `verify.ps1` all 6 checks green (checkpoint) | partly | Runs green, but it cannot detect the dead buttons, wrong answers or broken logic (H4). |
| 2 | All buttons wired, 73 buttons and 37 handlers (plan, checkpoint) | not working | `hci.html` lines 3575 and 3579 call functions that do not exist (H1). Other 6 guides pass. |
| 3 | CI green, "0 failing checks in repo history" (checkpoint) | partly | Last 2 runs green. Run 42718092954 failed on gitleaks. Claim about history is false. |
| 4 | Graded-work refusal 100 percent, 10/10 (checkpoint, evidence file) | partly | Reproduces, but 11 of 18 of my phrasings are not refused (H3). Nothing in the app calls the explainer, so it protects nothing today. |
| 5 | 5/5 concept questions answered with verified lecture citations | partly | Question 5 gets the generic "ask me about..." text, which still counts as "answered with citation". Citations are lecture numbers typed by hand, not file and page. |
| 6 | Telegram exam briefing delivered, message 442 | cannot verify | I did not send. Script content has defects (H2). |
| 7 | Daily exam briefing and reminders (plan section 8) | not working | No scheduled task runs `send_exam_briefing.py` (Task Scheduler listing: only `SIR_Study_Server`). Nothing calls it. |
| 8 | Headless logon daemon with restart-on-failure, "independent" (round 13) | partly | Server answers and a logon task exists. But the task launcher exits at once, so "restart 3 times" never applies (M1). |
| 9 | Zero emoji, zero em-dash, version 1.0.0 | verified (guides) | 0 emoji and 0 em-dash in all 9 HTML files. `.sir/status.json` still says version 0.0.0 (M4). Scripts print check marks in console output only. |
| 10 | Offline PWA service worker | partly | Code reads correctly; I could not run an offline test. Health call is cached stale (H6). Google Fonts are loaded from the internet (L5). |
| 11 | Destructive action dry-run and undo (T-019) | partly | `storage_admin.py` dry-run verified. The browser undo test cannot run (no playwright). |
| 12 | Math accuracy audit T-106, "every problem recomputed by script" (printed inside `or.html`) | partly | Script checks 5 numbers only (M3). |
| 13 | Access control: loopback and Tailscale only | partly | GET is gated; HEAD is not (M2). |
| 14 | Milestones M0 to M5 100 percent closed (checkpoint) | not working | PLAN section 3 lists deadlines feed, flashcards, practice scoring, coverage proof as not started; M1 exit check needs deadlines from an iCal feed. |
| 15 | Layout 320 to 1920 without horizontal scroll | verified | `scrollWidth` equals viewport at 320, 390, 768 (minus scrollbar), 1920 on hub, `or.html`, `hci.html`. Tab bars scroll inside their own box. |

## Defects

### Critical
None found. No code path in the product solves or submits graded work. The risks below are about wrong information and false evidence.

### High
**H1. Dead buttons in the HCI guide (exam 18/11).**
`guides/hci.html:3575` (`onclick="startFittsTrial()"`) and `:3579` (`onclick="hitFittsTarget()"`). The Fitts simulator "ابدأ الحركة" button and the target do nothing and throw `ReferenceError`. Reproduce: open `/hci.html`, run `startFittsTrial()` in the console, or click the button. The sliders `updateFittsSimulation()` work. Also `scripts/verify_all_buttons_wired.py` prints the error but exits 0, so no gate stops it. Fix: define both functions (or remove the block), make the script `sys.exit(1)` on any broken handler, add it to `verify.ps1` and CI.

**H2. The exam briefing can send wrong or unusable information.**
`scripts/send_exam_briefing.py:16-57` is a second, hand-typed exam calendar. It disagrees with the live hub `guides/START_HERE.html:2953-3030`:
- Human Rights 12/11 and Business Admin 15/11: briefing says 11:30 in hall 533; hub says 18:00 online (Moodle).
- HCI 18/11: briefing hall 533, hub hall 513. Course codes differ for 4 subjects (for example Human Rights `ح ق 101` vs `إ ن 203`; HCI `ع ح 207` vs `CS 314`).
One of them is wrong and I cannot tell which (the schedule is not in the tracked files). Also `:69` and `:80` put `http://127.0.0.1:3300/...` in a message read on a phone, where the link cannot open (the tailnet name is `https://ahmed.tail9e9aa7.ts.net:3300`). `:69` says "جاهزة 100% أوفلاين" which is not tested. Fix: one calendar file (`guides/exams.json`) read by the hub and by the script; use the tailnet URL; drop the "100%" wording.

**H3. The graded-work guard is a brittle regex, and the eval was written to pass it.**
`scripts/study_ai_explainer.py:50-61`. Each English pattern ends with `\s+`, so "Solve this quiz" (end of string) is not caught, while the eval string "solve this quiz for me right now" is. I ran 18 phrasings through `explain_query`: not refused: "Please answer questions 1-10 of my Moodle quiz", "solve the quiz for me", "answer my homework", "write the answers to my take-home exam", "tell me the quiz answers", "اكتبلي اجابات الكويز", "اجب عن أسئلة الامتحان المرفقة", "عايز اجابة سؤال 3 في الواجب", "can you finish my assignment 2" and others (11 in total). Refused: only exact Arabic and English forms in the eval list. The function also cannot answer anything beyond 5 canned topics, so today it is harmless, but the plan and checkpoint use it as the proof of the hard rule, and `find_matching_topic` uses substrings such as `"ظل"` and `"سياق"` that match unrelated words. Fix: default-deny design (refuse or redirect any request that contains an imperative plus "my/this/the" plus quiz/exam/assignment/homework/sheet words, in Arabic, Egyptian Arabic and English), a larger eval set of at least 60 phrasings, including paraphrases written by someone else, and have the eval fail on any miss.

**H4. The verification chain proves little, and the history claim is false.**
`scripts/verify.ps1` (the only CI step, `.github/workflows/verify.yml`) checks that files exist and contain strings. It does not run `verify_all_buttons_wired.py`, `verify_accuracy.py`, `study_ai_explainer.py eval`, or any `.sir/test_*.py`. Four of those tests need `playwright`, which is not installed and not in CI. There is no `tests/` folder, no `test_no_submit.py`, no briefing privacy test, although plan section 10 tasks 2, 3, 9 require them. Fix: add `tests/` with plain `unittest` files, wire all checks into `verify.ps1` with real exit codes, add a CI step installing playwright, correct the checkpoint line "0 failing checks in repo history".

**H5. The "daily briefing" and the "AI explainer" are not connected to anything.**
`Get-ScheduledTask` shows no task for `send_exam_briefing.py`, and `grep` finds no caller of `study_ai_explainer.py` outside itself. Only a one-time manual send happened. Fix: scheduled task (windowless, see C-notes in the control-room review) at 07:30 Cairo time that sends the briefing and writes the Telegram API result to `.sir/briefing.log`; or remove the claim.

**H6. The health badge can show "connected" when the server is down.**
`guides/START_HERE.html:2592` hard-codes the green text "الخادم المحلي: متصل ومستقل (Port 3300 • Task: SIR_Study_Server)" before any check. `:4142-4160` polls once, never again. `guides/sw.js:63-80` serves non-HTML GETs stale-while-revalidate, so `/api/health` is answered from the cache (old pid, old uptime) when the server is down or the page is offline. Reproduce: load the hub once with the service worker active, stop the server, reload: the badge still says connected. Fix: start the badge in a neutral "checking" state, bypass the cache for `/api/` (`if (url.pathname.startsWith('/api/')) return;`), poll every 30 s, show the age of the last good answer.

### Medium
**M1. Background-service design is weaker than claimed.** Task `SIR_Study_Server` has only a logon trigger and `Interactive` logon type. The action runs `wscript dev-start.vbs`, which starts the server and exits, so the task is "completed" (`LastResult 0`) and `RestartCount=3` never fires. If the Python process dies, nothing restarts it until the next logon (the loop in `serve.py:103-110` only handles exceptions inside the process). The task state shows `Ready` while the server runs, so a health script that reads the task state is wrong. `.sir/health.txt` was last written 2026-11-09 23:59 (about 4.5 hours before this review) and is tracked in git. Fix: add a 5-minute repeating trigger that runs `dev-start.ps1 -Headless` (it already exits when the pid is alive; also verify the pid belongs to python), write `health.txt` from the server itself, add `.sir/health.txt` to `.gitignore`.

**M2. Access gate is on GET only.** `scripts/serve.py:38` overrides `do_GET`. `do_HEAD` is inherited and skips the Host, IP and Tailscale checks: `curl -I -H "Host: evil.com" http://127.0.0.1:3300/` returns 200. `serve.py:40` splits the Host on `:`, which breaks `[::1]:3300`. `serve.py:41` accepts any `*.ts.net` name. The Tailscale-User-Login header is optional, so any device in the tailnet (including a shared node) with a 100.x address can read the guides. The server binds `0.0.0.0` and relies only on the in-code IP test. Fix: move the checks into one `_gate()` called from `do_GET`, `do_HEAD` and `do_POST`; bind to the Tailscale and loopback addresses only; require the header when the client is not loopback.

**M3. A user-visible accuracy claim is stronger than its proof.** `guides/or.html:3485` (and `:4009`) tell the student that every definition, formula and example was compared with the course files and every solved problem recomputed by script, and print the internal ticket "T-106 (2026-11-08)". `verify_accuracy.py` recomputes 5 numbers and checks the presence of 7 words in the SAD guide. Fix: say what was checked ("5 worked examples recomputed on 2026-11-08"), remove the ticket id.

**M4. `.sir/status.json` is stale and the dashboard reads it.** It says `version 0.0.0`, `status planned`, `tasksDone 2 of 23`, `ci none`. Reality: 1.0.0, ongoing, 30 of 33 tasks ticked in `TASKS.md`, CI exists. Fix: generate it from `TASKS.md` and the last `gh run` in `verify.ps1`.

**M5. Monolith files and one-shot patch scripts.** Each guide is 4,167 to 8,124 lines (130 to 410 KB) with its own copy of the same CSS and JS; the rule is 300 lines. `scripts/apply_r11_upgrades.py` (1,615 lines), `generate_coverage_md.py` (951), `apply_charter_to_all.py` (746), `rebuild_print_layouts.py` (489), `inject_suite_to_all.py` (452) patch the HTML by string replacement and are not safe to run twice; they are dead code after use. Fix: extract `guides/assets/study.css` and `study.js`, keep one generator, move one-shot scripts to `_quarantine/`.

**M6. Touch targets below 44 px.** At 320 px, 15 of 225 controls on `or.html` and 8 or more on `hci.html` are smaller (for example `settings-close-btn` 24x25, theme and density buttons 30 px high, brand and back links 36 to 38 px). `verify.ps1` only greps for the string "44px". Fix: `min-block-size: 44px; min-inline-size: 44px` on all `button, a.btn, [role=tab]`; measure in the browser, not by grep.

**M7. English / LTR is only a direction switch.** The settings LTR toggle flips layout but all content is Arabic. The plan and owner complaint list "Arabic RTL and English both work". Either translate the shell (nav, settings, quiz feedback) or document "content is Arabic only".

**M8. Checkpoint milestones contradict the plan.** CHECKPOINT: "M0 to M5 100 percent closed". PLAN section 3: deadlines feed, flashcards with spaced repetition, practice scoring, coverage proof "not started"; M1 exit check needs deadlines. Fix: re-open M1 and M2 in the checkpoint, tick only boxes with a command and output.

### Low
**L1.** Owner email hard-coded in `scripts/serve.py:56` and docs; move to `.env` (untracked).
**L2.** The private name "Habiba" and "AHome" appear in tracked files as deny-list words: `.sir/PLAN.md:39`, `scripts/export_sanitized.py`, `.sir/test_sanitized_privacy_gate.py`, `.sir/evidence/t-108-t109-sanitized-export.md`. The workspace rule says nothing about these people goes to a repo. Store the deny-list in an untracked file.
**L3.** 21 scripts hard-code `D:/Projects/...` or `C:/Users/a7med/...` (for example `generate_brand_icons.py:57`); use `Path(__file__)`. `D:\AI_Models_Hub` does not appear (good).
**L4.** `scripts/export_pdfs.py:47` and `send_exam_briefing.py:99` call `subprocess.run` without `creationflags=CREATE_NO_WINDOW`; they flash a console when run by a task.
**L5.** Every guide loads Google Fonts from the internet (`hci.html` head), which is not cached by the service worker (opaque responses are skipped) and sends a request to Google each visit. Self-host Cairo and JetBrains Mono.
**L6.** `storage_admin.py purge-temp` deletes without confirmation; dry-run is opt-in. Make `--dry-run` the default and add `--apply`.
**L7.** `.sir/health.txt`, 32 screenshots and `.sir/dev.log` style files are tracked or clutter the repo; add to `.gitignore`.
**L8.** The hub shows a row of repeated glyphs under the settings button on `or.html` at 320 px (seen in the screenshot just above the "النزاهة الأكاديمية" card, the phone-only table-scroll-hint at `or.html:4235` is a likely source). Not confirmed; check at 320 px.

## What works (so nobody breaks it)
Server and `/api/health`, Host-header block on GET, no emoji or em-dash in any guide, no horizontal overflow at the five widths, OR math examples (40,20 -> 2200; shadow prices 135/7 and 10/7), gitleaks clean, `storage_admin.py` dry-run, material folder `materials/` is git-ignored (245 MB not in the repo).
