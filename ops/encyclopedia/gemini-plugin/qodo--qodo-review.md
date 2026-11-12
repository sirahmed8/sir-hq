# qodo-review

Tools: gemini-plugin (qodo plugin). Source: C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-review\SKILL.md (497 lines) + references/{review-turn-context,context-delivery,connected-progress,local-triage,finding-results,skill-updates}.md

## Summary
Runs Qodo's AI review on LOCAL uncommitted/unpushed changes via `qodo review` (diff + new files + session context to Qodo's servers; base must be on remote, nothing is pushed). Governs when to review (light `--fast --async` checkpoints during coding, auto for final pre-PR review, `--deep` only for justified high blast radius), how to collect async results, how to attach decision/note/recent-work context, and how to own dispositions on returned findings.

## When to use / not use
Use for local diff review during substantive coding and before PR/handoff; for findings already posted on a remote PR use `qodo-review-resolver` instead. Not for non-code chores.

## Inputs, outputs, dependencies
Input: local git worktree + optional `.qodo/session-context.json` + `--ticket`/`--context-file`. Output: structured findings (`{findings, meta}`) with categories, action levels, coverage flags; agent then fixes/dismisses/investigates. Needs: authenticated `qodo` CLI >=2.0.0, remote base ref (merge-base SHA passed as `--base`), minutes-long runtime or async polling.

## Key rules
1. Depth policy: `--fast` for checkpoints, auto (no flag) for final review, `--deep` only with a concrete blast-radius reason — never by diff size or timeout pressure; mutually exclusive flags.
2. Commit task changes locally before each review (uncommitted edits included but HEAD SHA is the review anchor); max one active async checkpoint per task.
3. Context is the reviewer's only window into intent: `decisions` (who chose what + why), `notes` (evidence/constraints/verification), `recent_work` (what changed since last review) — never strip context to beat the clock, never include secrets.
4. Result discipline: zero findings ≠ clean if `coverage.complete`/`finding_state.complete` is false; assess `.introduced` AND `.still_open`; a superseded result can't certify newer work; results expire after 1h.
5. Authority: report-only requests get assessment and stop; fix authority covers code edits only — stored dismissals need separate explicit authorization (`pr-review-dismiss` with reason).

## Risks / owner items
- Closed preview: `closed_preview` error means org not enrolled — surface message+hint and STOP, never retry.
- `--async` has no streaming progress and no human-in-the-loop; killed clients can cause server cancellation — use async or keep connected process alive.
- Finding writes are forge-adjacent state in Qodo's DB; misapplied dismissals pollute future reviews.

## Category and tags
ai, build, security — qodo, code-review, pre-pr, llm-review, quality-gate.

## Revision note
Single plugin revision (v1.10.15); the heaviest skill in the slice — essentially a full review-lifecycle runbook.
