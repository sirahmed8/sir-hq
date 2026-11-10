SIR Study, round 20 (2026-11-10). Read AGENTS.md, .sir/CHECKPOINT.md and .sir/R19_CHECKLIST.md first. Round 19 made CI green (confirmed by HQ) but left findings open because commands could not run for most of that round. This round closes every line marked OPEN in .sir/R19_CHECKLIST.md.

Rules: no pull requests, commit and push to main after every item. Version stays 1.0.0. No emoji. Help the owner learn; never produce graded work for him. Never revert the edits of another tool. CI must stay green: check `gh run list --limit 3` after each push.

1. Exams first (Human Rights is on 2026-11-12, a Thursday). Print guides/exams.json and the source timetable under materials/ side by side in the report and state for each exam: date, weekday, time, place, and which source it came from. If the two disagree anywhere, do not guess: keep the timetable value, and write the disagreement at the top of .sir/CHECKPOINT.md under "Owner must confirm".
2. H3: the graded-work guard. Make it default-deny for requests that ask for a finished answer to an assignment, quiz or exam, run `python scripts/study_ai_explainer.py eval`, and paste the counts. All cases must pass.
3. H4: install Playwright (chromium only) and add browser tests that open the hub and the Human Rights, Business Admin and HCI guides, click every button, answer one quiz and run one search. Run them in CI.
4. M1: prove restart after a crash. Kill the server process, wait for the scheduled task, show the port answers again. Add a repeat trigger if only a logon trigger exists. Paste commands and output.
5. M5: finish moving shared CSS and JS out of the guides; no guide may keep a copy. Offline use must still work (service worker precache).
6. M6: measure every button and link at 320 px in the browser tests; fail when one is under 44 px; fix them.
7. M7: either translate the shell (navigation, buttons, labels) to English or remove the toggle. No half state.
8. L1 to L8: fix each one still open (owner email in serve.py, private names in tracked deny-lists moved to an untracked file, CREATE_NO_WINDOW on subprocess calls, and the rest).
9. Use the three nearest guides like a student at 390 px and ship at least 10 visible improvements with before and after screenshots under .sir/evidence/r20/.

Finish: update .sir/R19_CHECKLIST.md (every line fixed with proof), .sir/CHECKPOINT.md (Now, exact Next step, Open promises), append one line to D:/Projects/_SIR/ops/bus/sir-hq.md, commit and push.
