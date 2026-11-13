# AHome folder icon and desktop shortcut icons (run inside the AHome chat)
Project folder: D:/Projects/AHome. Scope: icon only. Do not open private content (vault, messages, notes, photos).
Owner request (Telegram, 2026-11-13): the project folder and its Desktop shortcut folder still show no icon; the shortcut icon should be the pink house shape.
Steps:
1. Read AHome/.sir/CHECKPOINT.md and AHome/.sir/TOOLKIT.md. Check `git status` first: folder.ico is already modified (370070 bytes) and not committed.
2. Use the icon pipeline in D:/Projects/_SIR/scripts/make-icons-and-desktop.ps1. Icon: a pink house shape, the same style as the other SIR folder icons (see D:/Projects/_SIR/plans/icon-prompts.json, entry for AHome if present, else create one with the same rules).
3. Set folder.ico and desktop.ini on AHome and on the Desktop folder C:/Users/a7med/Desktop/AHome. Keep the Desktop shortcut pointing at the AHome folder.
4. Verify: take a screenshot of both folders in Explorer at 100 percent scale and paste the path in the report.
5. Commit only folder.ico and the icon scripts; push to main. Write D:/Projects/_SIR/ops/agy-runs/reports/ahome-folder-icon.md with the exact paths and PASS or FAIL.
Done = both icons visible in Explorer, report written, pushed.
