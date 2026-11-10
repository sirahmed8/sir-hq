# OWNER ACTIONS (pending manual commands)

## 2026-11-10 - sir-jobs r15 (Inbox Assistant phase 1)

The agent's shell permission layer rejected every mutating/executing command
(node test runs, git add/commit/push, rm, powershell verify) while read-only
commands passed. The following commands must be run by the owner (or approved
in the agent session) to finish r15-jobs:

```bat
cd /d "D:\Projects\SIR Jobs"
del test\temp-inbox-smoke.mjs
node test\test-r15-inbox.mjs
npm test
npm run doctor
powershell -ExecutionPolicy Bypass -File scripts\verify.ps1
git add -A
git commit -m "feat(r15): inbox assistant phase 1 - read-only collector, classifier, local-model digest, telegram buttons, dashboard tab"
git push
```

Also add this entry to `D:\Projects\_SIR\ops\telegram-actions.json` (agent was
denied write access outside the project folder):

```json
"jobs_inbox_scan": {
  "cmd": ["node", "D:/Projects/SIR Jobs/scripts/inbox/run.mjs", "--process-only"]
}
```

Then run the done signal:

```bat
python D:/Projects/_SIR/scripts/agy-done.py r15-jobs ok "phase-1 inbox assistant built; awaiting verification commands above"
```
