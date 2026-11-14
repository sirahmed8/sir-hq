# Report: normal-7-ahome-audit-models-fix1

Task: normal-7-ahome-audit-models-fix1 (fix round for the failed item of normal-7-ahome-audit-models).
Project: D:/Projects/AHome. Failed item: 6 (report file is written AND committed).

## Result

Item 6 fixed, ticked and committed: the audit report now exists at the required path and the
report/verification files are committed in the _SIR repo.

## What was broken (cause)

- The audit worker wrote the report to `ops/agy-runs/reports/7-ahome-audit-models.md` while the
  worker prompt required `ops/agy-runs/reports/normal-7-ahome-audit-models.md`.
- The report was never committed, so `git -C D:/Projects/_SIR status` showed
  `?? ops/agy-runs/reports/7-ahome-audit-models.md` (untracked, never committed).

## What was done (fix)

- Wrote the missing worker report at the required path:
  `ops/agy-runs/reports/normal-7-ahome-audit-models.md` (content identical to the verified audit
  report at `ops/agy-runs/reports/7-ahome-audit-models.md`).
- Committed `ops/agy-runs/reports/7-ahome-audit-models.md`,
  `ops/agy-runs/reports/normal-7-ahome-audit-models.md`,
  `ops/verifications/normal-7-ahome-audit-models.md` and this fix report in the _SIR repo
  (commit message: `report+verify: normal-7-ahome-audit-models-fix1 PASS`).

## Checklist item 6

- Before: FAIL - report untracked at short path, missing at required path.
- After: PASS - report written AND committed at the required path; verification file item 6 ticked.

## Verification (real output)

- Before fix: `git -C /d/Projects/_SIR status --porcelain=v1` listed
  `?? ops/agy-runs/reports/7-ahome-audit-models.md`.
- After fix: the same command no longer lists that file (files committed).
- Audit content itself was re-checked and found real (chain, installed models, 1090 local-core tests pass).

## Notes / unsure

- No application code changed; no new tests needed (report-file defect only).
- CI: `ops/ci-quota-exhausted.flag` present (2026-11-12) - per rule 18 local verification substitutes
  CI green; the audit round already ran the local gates (1090 local-core tests passed).

## Next

- Manager/verifier closes task normal-7-ahome-audit-models via taskboard sync (fix1 verification now PASS).
- Optional separate tasks from the audit recommendations: docs sync to ctx 16384, move classify to
  nemotron-3-nano:4b, Arabic TTS via piper.
