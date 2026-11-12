# executing-plans

## Summary
The "inline executor" half of the superpowers plan-execution pair: instead of dispatching a fresh implementer subagent per task, the same session executes every task of a written plan itself, task by task, with TDD as the per-task gate and one fresh-context whole-branch review at the end. Its core idea is that the plan already did the thinking, so execution is transcription plus testing — the ledger file (not chat memory) is what survives compaction.

## When to use / when NOT
Use when you hold a plan produced by superpowers:writing-plans and either the human chose inline execution or the harness has no subagent tool. Prefer subagent-driven-development when the human wants a review gate per task or the plan is long enough that later tasks would run on compacted context. Requires mostly independent tasks.

## Inputs, outputs, tools
- Inputs: a plan file (with per-task briefs, Interfaces blocks, Expected lines, commit steps) and optionally a Spec it argues from; a git worktree (never implement on main without explicit consent).
- Outputs: committed code per the plan's commit steps, a ledger at `.superpowers/sdd/<plan>/progress.md` with `Task <N>: complete` lines and `Ruling:` entries, a final review and branch finish via superpowers:finishing-a-development-branch.
- Tools: bash scripts `scripts/task-start` and `scripts/task-done` (which delegate to the sibling subagent-driven-development scripts: sdd-workspace, task-brief, sdd-repo), git, the test command named per task, and a reviewer (subagent or self-review fallback).

## 5 most important rules
1. Track progress in the ledger file, not todos or memory — compaction does not wait; resume from `Task <N>: complete` lines and `git log`.
2. Every step with an `Expected:` line must be run and its real output compared; mismatches are either code bugs (systematic-debugging) or plan defects (rule and ledger).
3. Deviations are decisions: record `Ruling: <what> — <why> — <cost if wrong>`; unledgered deviation is a decision made in secret. Only four things stop you (irreversible ops, security-sensitive, external side effects like push/publish, plan so broken every path is a guess).
4. TDD is mandatory: watch each test fail then pass; `task-done` runs the task's test command and only then appends the completion line — a failing run records nothing.
5. Finish with one whole-branch review by a fresh reviewer on the most capable model (or an honestly-labeled self-review), one fix pass for Critical/Important findings verified by RED→GREEN tests, minors deferred to the ledger, then delete the plan workspace.

## Risks / owner needs
Medium process risk: it commits per plan steps and ends by finishing a branch — pushes/merges to shared branches are among the four stop conditions, so the human still gates those. Long plans degrade because later tasks get the least context; the ledger mitigates but does not eliminate that.

## Category and tags
Category: build. Tags: superpowers, plan-execution, tdd, ledger, code-review, workflow.

## Revisions
Only the gemini-plugin superpowers copy exists here; the scripts are bash and assume a bash-capable shell.
