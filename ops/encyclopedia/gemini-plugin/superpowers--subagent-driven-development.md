# subagent-driven-development

- Tool: `gemini-plugin` (plugin: `superpowers`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\subagent-driven-development\SKILL.md`
- SKILL.md size: 19625 chars

## What it does

Use when executing implementation plans with independent tasks in the current session

## When to use (from skill text)

- The loop triggers when the review reports spec ❌, any Critical or Important
- When it triggers, read [references/fix-loop.md](references/fix-loop.md) and

## Structure (headings inside SKILL.md)

- Subagent-Driven Development
- When to Use
- The Process
- Setup
- Model Selection
- The Task Loop
- 1. Dispatch the implementer
- 2. Handle the report
- 3. Review the task
- 4. The fix loop
- 5. Complete the task
- Final Review
- Common Rationalizations
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Fresh subagent per task (no context pollution) instead of one context doing every task
2. - Review after each task (spec compliance + code quality) instead of only at the end
3. - Both run in this session, share the same plan workspace and ledger, and never pause between tasks
4. - Requires design judgment or broad codebase understanding → most capable model
5. - **Task brief:** before dispatching an implementer, run this skill's

## Files inside the skill

- `implementer-prompt.md` — "Implementer Subagent Prompt Template"
- `re-review-prompt.md` — "Scoped Re-Review Prompt Template"
- `references/batching.md` — "Batching Small Same-Shape Work"
- `references/cannot-verify.md` — ""Cannot Verify From Diff" Items"
- `references/final-review.md` — "Final Review and Finish"
- `references/fix-loop.md` — "The Fix Loop"
- `references/handling-reports.md` — "Handling a Report That Isn't DONE"
- `references/preflight.md` — "The Pre-flight Scan"
- `references/resuming.md` — "Resuming From an Existing Ledger"
- `scripts/review-package`
- `scripts/sdd-repo`
- `scripts/sdd-workspace`
- `scripts/task-brief`
- `task-reviewer-prompt.md` — "Task Reviewer Prompt Template"
