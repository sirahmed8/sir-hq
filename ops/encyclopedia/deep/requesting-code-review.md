# requesting-code-review

Tools: gemini-plugin (superpowers). Source: C:\Users\a7med\.gemini\config\plugins\superpowers\skills\requesting-code-review\SKILL.md (95 lines) + code-reviewer.md template

## Summary
Dispatches a dedicated code-reviewer subagent with precisely crafted context (description, requirements, BASE_SHA, HEAD_SHA) instead of reviewing inline — protecting the coordinator's context window. Mandatory after each task in subagent-driven development, after major features, and before merging to main.

## When to use / not use
Use after completing tasks/features and before merge; also valuable when stuck, before refactoring (baseline), or after complex bug fixes. Not for trivial one-line changes or when no VCS/diff exists.

## Inputs, outputs, dependencies
Input: git SHAs (BASE via `git rev-parse HEAD~1` or `git merge-base origin/main HEAD`; HEAD via `git rev-parse HEAD`) + description + plan/requirements. Output: structured review (strengths, Critical/Important/Minor issues, assessment). Needs: a subagent mechanism (general-purpose agent), the code-reviewer.md template, git history.

## Key rules
1. Review early and often — mandatory checkpoints: after each task, after major feature, before merge. Never skip because "it's simple".
2. The reviewer gets crafted context, NEVER your session history — hand it the work product, not your thought process.
3. Act on feedback by severity: Critical = fix immediately, Important = fix before proceeding, Minor = note for later.
4. You may push back on a wrong reviewer — with technical reasoning and code/test evidence, not argument.
5. Don't burn coordinator context reviewing diffs inline; the diff and evaluation belong in the subagent's context, only findings return.

## Risks / owner items
- Reviewer quality depends entirely on the crafted context — vague DESCRIPTION/PLAN produces vague review.
- Subagent availability varies by harness; template assumes a dispatchable general-purpose agent.
- "Review often" can become review theater if findings aren't acted on — severity discipline is the safeguard.

## Category and tags
build, ops, ai — code-review, subagents, quality-gate, workflow.

## Revision note
Single superpowers revision; sender-side pair to receiving-code-review.
