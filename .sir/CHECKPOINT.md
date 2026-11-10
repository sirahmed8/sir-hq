# SIR Control Room checkpoint (r15-control)

## Now
- r15-control implementation is COMPLETE in the working tree (uncommitted): Telegram `/menu` buttons, sanitized autopilot + account-ledger dashboard sections (EN/AR), `ask-approval.mjs` + `approve_ok`/`approve_no` handling into `ops/bus/approvals.json`, artifact regeneration verified by the refresh worker (hash `3a9daf04` at 10:48).
- Full report written: `ops/agy-runs/reports/r15-control.md`.
- BLOCKED on commit/push/CI: every mutating shell command (`git add`, `git commit`, `git push`, `rm`) and every interpreter (`python`, `node`, `gh`, `curl`, `powershell`) was rejected by tool permissions this session. Only read-only commands and file tools worked.
- Checklist `.sir/r15-control_CHECKLIST.md`: items 1-3 ticked; item 4 (CI green) unticked because GitHub Actions could not be observed.

## Next step (exact)
1. In a session with shell write permissions: `git add -A` the r15 files (exclude `ops/locks/`), commit, push to `main`, and confirm the `verify` workflow.
2. Optionally run one live approval round-trip test, then remove test rows from `ops/bus/approvals.json`.
3. Delete the stale lock `ops/locks/_SIR` (owner=devin-cli-r15-control) once a new worker takes over.

## Open promises
- Keep version `1.0.0`; no emoji; simple Arabic; AHome private data never leaves local systems.
- `ops/artifact/PUBLISHED.txt` stays at last published hash until HQ republishes.

## Re-read list
`AGENTS.md`, `NEXT.md`, `ops/HQ_CHECKPOINT.md`, `.sir/MASTER_PLAN.md`, `.sir/plans/r15-control.md`, `.sir/r15-control_CHECKLIST.md`, `ops/briefs/r15-control.prompt.txt`, `ops/agy-runs/reports/r15-control.md`

## HQ note (2026-11-10 14:10)
- Now: queue done by free CLIs today (claims, unverified): r15-control 10:54, r16-study 12:54, r16-control 13:45. Running: r16-jobs (since 09:29, last commit 3 hours ago: check it is not stuck) and r17-ahome-verify (since 13:50). Antigravity is signed in again (owner) and works AHome; Claude and SIR Autonomy Chrome extensions are installed; ZCode quota is full, plan ends 2026-11-14.
- Next step: `tail -20 ops/agy-runs/cli-r16-jobs.log`; `git status -sb` here (the r15-control worker reported uncommitted files); verify r15-control, r16-study, r16-control against `ops/reviews/2026-11-10/`; then queue the next round with `python scripts/queue-add.py`.
- Open promises: verification of every overnight and today's claim; Control Room C1 (server serves all of ops/) confirmed fixed by test.
- Re-read after a reset: `ops/HQ_CHECKPOINT.md`, `ops/AUTOPILOT_QUEUE.json`, `ops/autopilot.log`.
