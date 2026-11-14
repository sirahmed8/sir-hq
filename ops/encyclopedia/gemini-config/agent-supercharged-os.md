# agent-supercharged-os

Source read: `C:\Users\a7med\.claude\skills\agent-supercharged-os\SKILL.md`.

## Summary
Agent Supercharged OS is a compact engineering discipline that pushes coding agents through an architecture plan, test-first validation, surgical implementation, multi-tier review, and session checkpointing. It is meant to make every coding task behave like a small engineering team rather than a one-shot answer.

## When to use / when NOT
Use as the default working discipline for features, bug fixes, refactors, reviews, and multi-step implementation work where quality and continuity matter. Do not use it as a task-specific feature skill, and do not skip phases for supposedly small changes; the value is that the same gates apply every time.

## Inputs, outputs, tools
Input is the coding task, bug report, or review target. Outputs are an architectural breakdown, tests or test contracts, bounded implementation diffs, security/performance/accessibility review notes, and an updated `continuation_checkpoint.md`. Tools are the project's normal test runner, linter, type checker, and browser or runtime verification when relevant; the skill itself requires no MCP.

## 5 most important rules
1. Never write code before producing an architectural breakdown with schemas, routes, indices, dependencies, and error conditions.
2. Write unit and integration tests before or alongside implementation, including nulls, invalid payloads, and timeouts.
3. Keep implementation surgical: maximum 300 lines per file, layered Presentation to Domain to Data to Core structure, no placeholders, no unhandled promises.
4. Run multi-tier review for OWASP-style security, N+1 queries, re-renders, bundle bloat, keyboard navigation, contrast, and ARIA.
5. Persist progress by updating `continuation_checkpoint.md` with active tasks, design decisions, and learned lessons.

## Risks / owner notes
The pipeline trades early speed for fewer rework cycles, and agents may be tempted to skip planning or tests under pressure. The owner should verify that the checkpoint file exists, tests actually ran, and review gates were not just narrated. It also assumes the project has or can adopt a layered structure.

## Category / tags
ops · engineering-discipline, tdd, planning, code-review, checkpoint, security, performance, accessibility

## Revisions
The claude copy is selected by the source rule and has the fullest frontmatter description. Codex, kilo, cursor, windsurf, and opencode copies are near-identical older revisions, and the gemini-plugin advanced-engineering copy has the same body with a truncated description.
