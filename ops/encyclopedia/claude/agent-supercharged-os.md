# agent-supercharged-os

Source read: `C:\Users\a7med\.config\kilo\skills\agent-supercharged-os\SKILL.md` (2.0 KB; kilo revision; identical copies in codex/cursor/windsurf/opencode; not in claude).

## Summary
A structured 4-phase engineering operating system (Plan → Test → Implement → Review) with cross-session learning via checkpoints. Transforms an agent into a disciplined engineering team. Phase 1: Architecture & Plan — schema, API routes, DB indices, error conditions up front. Phase 2: Test-Driven Validation — unit/integration tests first, boundary conditions exercised. Phase 3: Surgical Implementation — max 300 lines/file, layered architecture (Presentation→Domain→Data→Core), zero placeholders, zero unhandled promises. Phase 4: Multi-Tier Review — Security (OWASP Top 10), Performance (N+1, re-renders, bundle), Accessibility (keyboard, contrast, ARIA). Phase 5: Continuous Learning — update `continuation_checkpoint.md` with tasks, decisions, lessons.

## When to use / when NOT
Use as the default discipline for ALL coding tasks, refactors, features, and reviews. It is not a task-specific skill — it overlays every task. Do NOT skip phases even for "small" changes; the pipeline is the quality floor.

## Inputs, outputs, tools
- Inputs: any coding task, bug, or refactor.
- Outputs: architectural breakdown, failing tests, surgical diffs, review reports, updated checkpoint.
- Tools: test runners (project-specific), Chrome DevTools MCP for browser validation, linters/typecheckers. No MCPs required by the skill itself.

## 5 most important rules
1. **Never write code before an architectural breakdown** (schemas, routes, indices, error conditions).
2. **Write tests first or alongside** — boundary conditions (null, invalid payload, timeout) must be exercised.
3. **Surgical implementation only**: max 300 lines/file, layered architecture, no placeholders, no unhandled promises.
4. **Multi-tier review mandatory**: Security (OWASP), Performance (N+1, bundle), Accessibility (keyboard, contrast, ARIA).
5. **Checkpoint every session**: Update `continuation_checkpoint.md` with active tasks, key decisions, learned lessons.

## Risks / owner notes
The 4-phase pipeline slows initial velocity but prevents rework. Risk: agents skip Phase 1/2 under time pressure. Owner should verify checkpoint exists and review gates ran.

## Category / tags
ops · engineering-discipline, tdd, surgical-code, phased-workflow, checkpoint, review-gates, owasp, a11y, performance

## Revisions
Five byte-identical copies in codex/kilo/cursor/windsurf/opencode (2.0 KB). Not in claude. The kilo/codex family revision is canonical.