# sir-session-end

## Summary
SIR session-end is the end-of-session ritual for every SIR worker. It is not a builder; it is a closing checklist. When a session ends (quota cut, task done, blocked round), the worker updates the project checkpoint (`<project>/.sir/CHECKPOINT.md`), appends one line to `_SIR/ops/MISSION_LOG.md`, commits and pushes to `main`, and writes a report in the A5 shape: outcome, changes, verification, upgrades applied, risks and unverified items, owner actions, next best step. It also keeps `_SIR/REQUIREMENTS.md` rows current (status and evidence only, never delete a row) and routes anything only Ahmed can do to `_SIR/ops/OWNER_ACTIONS.md` with exact steps. The skill is a single SKILL.md with no scripts and no references.

## When to use / when NOT
Use at the end of every SIR work session, after the last check passes or after a clean stop. Do NOT use it to start work, to build features, or mid-task. Do NOT use it as a substitute for the checkpoint during the session; the checkpoint is updated incrementally, and this skill only formalises the final write.

## Inputs, outputs, tools
- Inputs: the session's own state (what changed, what was verified, what is open).
- Outputs: updated `.sir/CHECKPOINT.md`, appended `_SIR/ops/MISSION_LOG.md`, a report file in `_SIR/ops/agy-runs/reports/`, optionally `_SIR/ops/OWNER_ACTIONS.md` and `_SIR/REQUIREMENTS.md` rows.
- Tools: git (commit/push), the filesystem. No MCPs, no external services. Run `gitleaks dir` before committing if any new file could hold a secret.

## 5 most important rules
1. Never delete a row in `_SIR/REQUIREMENTS.md`; only update status and evidence.
2. Push only when `D:/Projects/_SIR` changed, and never commit secrets.
3. Owner-only steps go to `OWNER_ACTIONS.md` with exact commands; they never block other work.
4. The report states decisions and never asks questions.
5. If a request was completed or changed, its requirements row is updated in the same pass.

## Risks / things needing the owner
None internal; the only owner-facing item is a step that truly requires Ahmed (sign-in, 2FA, payment, CAPTCHA). Everything else is decided and logged by the worker.

## Category / tags
ops · session ritual, checkpoint, git, report

## Revisions
Only one revision exists, in `D:/Projects/.agents/skills/sir-session-end/SKILL.md` (workspace copy). No divergent copies to compare.