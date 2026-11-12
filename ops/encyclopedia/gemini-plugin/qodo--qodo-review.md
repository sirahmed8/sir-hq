# qodo-review

- Tool: `gemini-plugin` (plugin: `qodo`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-review\SKILL.md`
- SKILL.md size: 39080 chars

## What it does

Review local changes with Qodo during substantive coding milestones and before a PR or completed-work handoff. Use light background checkpoints while coding, collect and assess findings with session context, and run a final review before handing off. Also use for "review my local diff", "pre-PR review", or "run qodo review". Use qodo-review-resolver for findings already posted on a PR.

## When to use (from skill text)

- Use this skill for local changes, including unpushed work on an existing PR. Use `qodo-review-resolver` to work on findings from the PR's remote review; do not duplicate that review for an unchanged pushed snapshot.

## Structure (headings inside SKILL.md)

- Local Review
- Description
- Prerequisites
- Choose when and how deeply to review
- Checkpoints and final handoff
- Prepare a PR handoff
- Instructions
- Choose the execution path
- Handle a skill update notice
- Execution
- Runtime compatibility gate
- Quick start
- Choose execution for the selected review
- Submit and collect with `--async`
- This collection attempt returns failures to the host for classification under Recover a review.
- On nonzero exit, preserve the operation ID and emitted error; apply bounded recovery there.
- Preflight
- What gets reviewed
- Attach coding-session context
- Present the review result
- Act on the findings
- Recover a review
- If the run is gated: closed preview
- Configuration
- Error Handling
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP tool, MCP review, MCP Tasks

## Risks / cautions found in text

- - The **tracked diff** vs the base, plus **new/untracked files** (secrets, binaries, oversized,
- - **Never strip context to beat the clock.** Dropping `--context-file` doesn't make a run faster —

## Key rules (verbatim lines from SKILL.md)

1. - Review a completed, testable slice when its feedback can guide the remaining work. Do not review
2. - Before final review, collect the outstanding checkpoint and reconcile its findings. Review the
3. - Windows CLI: read [shell guidance](references/windows-shells.md) before the first call; [launcher recovery](references/windows-launcher.md) only if invocation fails. Reuse the resolved invocation.
4. - Capture the process exit status, reap the child and disarm its PID before parsing. On interruption,
5. - **The result is kept for 1 hour** after the review finishes, then it is discarded. Collect it

## Files inside the skill

- `agents/openai.yaml`
- `references/connected-progress.md` — "Connected review progress example"
- `references/context-delivery.md` — "Context receipt field reference"
- `references/finding-results.md` — "Finding results and local run metadata"
- `references/local-triage.md` — "Record local triage"
- `references/review-turn-context.md` — "Session context examples"
- `references/skill-updates.md` — "Manual enterprise skill updates"
- `references/windows-launcher.md` — "Windows launcher recovery"
- `references/windows-shells.md` — "Windows shells"
