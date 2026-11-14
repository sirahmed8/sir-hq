---
name: karpathy-skills
description: "Use when writing or reviewing AI-assisted code and you need guardrails: think before coding, simplicity first, surgical changes, and goal-driven verification."
---

# Karpathy Skills — AI Software Engineering Guardrails

Based on Andrej Karpathy's foundational observations on common LLM coding pitfalls, these four rules govern all engineering, refactoring, and code changes:

---

## 1. Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing any code:
- State assumptions explicitly. If uncertain about requirements or business logic, ask.
- If multiple interpretations exist, present them clearly—never pick silently.
- If a simpler approach exists, say so immediately. Push back against unnecessary complexity.
- If something is unclear in third-party APIs or legacy code, stop, name what is confusing, and clarify.

---

## 2. Simplicity First (YAGNI)
**Minimum code that solves the problem. Nothing speculative.**

- Write zero features beyond what was explicitly requested.
- Build no speculative abstractions for single-use code.
- Avoid premature "flexibility", "configurability", or generic factory layers that weren't requested.
- Do not write defensive error handling for impossible scenarios.
- If you write 200 lines and it could be cleanly solved in 50 lines, rewrite and simplify.
- Test heuristic: *"Would a Principal Engineer say this is overcomplicated?"* If yes, refactor immediately.

---

## 3. Surgical Precision
**Touch only what you must. Clean up only your own changes.**

When editing existing code:
- **Never rewrite entire files.** Use targeted line/block replacement (`replace_file_content` / `edit_file`).
- Do not randomly "improve" adjacent code, comments, or formatting outside the task scope.
- Do not refactor modules that are already working and tested.
- Match existing repository conventions, casing, and architecture.
- When your changes orphan variables, imports, or functions, remove them cleanly.
- Do not delete pre-existing dead code unless explicitly requested.
- The Golden Rule: *Every single changed line must trace directly to the task goal.*

---

## 4. Goal-Driven Execution
**Define success criteria. Loop until verified.**

Transform every task into concrete, verifiable criteria:
- *"Add validation"* → Write validation test with invalid inputs, make it pass.
- *"Fix the bug"* → Write a reproducing test, observe failure, fix code, verify green.
- *"Refactor X"* → Ensure all test suites pass before and after the change.
- Multi-step tasks state a concrete plan:
  1. `[Step 1]` → verify: `[check]`
  2. `[Step 2]` → verify: `[check]`
  3. `[Step 3]` → verify: `[check]`
- Test execution and browser validation (via Chrome DevTools MCP) must be run to confirm runtime health before marking any task complete.
