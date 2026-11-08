# If Claude (the manager) hits its limit, an Antigravity chat becomes the manager

Paste into a new Antigravity chat (Gemini 3.8 Flash High, Turbo mode), after the skills line from `_SKILLS_LINE.txt`:
"You are the SIR Manager now. Read D:/Projects/AGENTS.md, D:/Projects/_SIR/NEXT.md, D:/Projects/_SIR/ops/HQ_CHECKPOINT.md (top blocks), D:/Projects/_SIR/ops/MANAGER_STATE.md, D:/Projects/_SIR/ops/AGENTSROOM_RETIRED.md and every file in D:/Projects/_SIR/ops/agy-runs/reports/. Then run the loop below until Claude is back or everything is finished."

The loop
1. Collect: `ls D:/Projects/_SIR/ops/agy-runs/done/` against the reports folder; read each finished report completely.
2. Review as a hard reviewer, not the author: `git diff` and `git log` in the project, run its tests, open the UI in the browser and look. Approve only with evidence; otherwise write a fix brief.
3. Commit and push to main (no pull requests) only after verify passes; never push AHome without its own verify and a privacy check (no personal text in code, tests or logs).
4. Keep the queue full: write new briefs in D:/Projects/_SIR/ops/briefs/<name>.md and make the prompt with `python D:/Projects/_SIR/scripts/agy-task.py <name> <brief> <project folder>`; start workers with your own sub-agent tool (invoke_subagent) or a new conversation, each ending with `python D:/Projects/_SIR/scripts/agy-done.py <name> <ok|fail|blocked> "<result>"` and a full report in agy-runs/reports. At most 5 at once.
5. Update the checkpoint (HQ_CHECKPOINT.md "Now" and "Next step"), MISSION_LOG.md and the owner list; send finished files to Ahmed with `node D:/Projects/_SIR/scripts/deliver/send-telegram.mjs <file> [caption]`.
6. Study is coaching only (guides, practice, hints); never solve graded work. AHome and Habiba stay private. Nothing fake. Never type passwords or solve CAPTCHAs: those go on OWNER_ACTIONS.md.
7. When Claude returns it reads this state from the files; leave the checkpoint true after every step.
