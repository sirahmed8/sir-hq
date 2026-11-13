# Smoke test for the Cursor agent (free auto model)
Folder: D:/Projects/_SIR. Read only the files named here; edit nothing else.
1. Read ops/AUTOPILOT_QUEUE.json and list the names of tasks whose "done" is false.
2. Read the last 20 lines of ops/autopilot.log.
3. Write ops/agy-runs/reports/smoke-cursor.md with two sections: "Open tasks" (the names) and "Last log lines" (the 20 lines, verbatim).
4. Run: git add ops/agy-runs/reports/smoke-cursor.md && git commit -m "smoke: cursor test report" && git push origin main
5. Finish by writing the done marker: python D:/Projects/_SIR/scripts/agy-done.py smoke-cursor ok "cursor smoke report written and pushed"
