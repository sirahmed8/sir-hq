# karpathy-skills

Source read: `C:\Users\a7med\.claude\skills\karpathy-skills\SKILL.md` (2.9 KB; claude revision; codex/cursor/kilo/opencode/windsurf listed).

## Summary
Four engineering guardrails distilled from Andrej Karpathy's observations on LLM coding pitfalls: (1) Think Before Coding — state assumptions, surface interpretations and tradeoffs, push back on complexity, stop and clarify confusion in third-party APIs or legacy code; (2) Simplicity First/YAGNI — no speculative features, abstractions, configurability, or defensive handling for impossible cases; rewrite 200 lines that could be 50; the Principal-Engineer test; (3) Surgical Precision — never rewrite whole files, touch only what the task requires, match repo conventions, remove only your own orphaned code, never delete pre-existing dead code, every changed line must trace to the goal; (4) Goal-Driven Execution — convert tasks into verifiable steps ("fix the bug" → write failing repro test, fix, verify green), state a plan with per-step verification for multi-step work, and run tests plus browser validation before marking complete.

## When to use / when NOT
Use as standing guardrails for any AI-assisted coding, refactoring, or review. It is a discipline overlay, not a task-specific procedure — pair with project verify commands for the concrete checks.

## Inputs, outputs, tools
- Inputs: any coding task or diff under review.
- Outputs: smaller diffs, explicit assumptions, test-first verification, honest "not done" until runtime checks pass.
- Tools: none required; references test runners and Chrome DevTools MCP for browser validation.

## 5 most important rules
1. State assumptions and interpretations explicitly; ask rather than guess silently.
2. Minimum code that solves the problem — no speculative abstraction or impossible-case handling.
3. Surgical diffs only: every changed line traces to the task; leave working code and dead code alone.
4. Goal-driven verification: turn each task into a checkable step; failing test first for bugs.
5. Nothing is "done" until tests and runtime/browser validation actually ran green.

## Risks / owner notes
None operational; it is pure methodology. Its "ask when unclear" can conflict with the workspace's never-stop autonomy rule — prefer logging the assumption in the checkpoint and continuing when the decision is reversible.

## Category and tags
Category: build. Tags: engineering-discipline, yagni, surgical-diffs, tdd, code-review, karpathy.
