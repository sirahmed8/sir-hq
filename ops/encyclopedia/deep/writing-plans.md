# writing-plans (gemini-plugin: superpowers)

## Summary
writing-plans produces implementation plans for an engineer (human or subagent) who has never seen the codebase or spec. It assumes the implementer writes idiomatic code once given exact interfaces and tests, and decides everything the implementer cannot: which files, which names/signatures, which spec values, which tests prove each task. Plans are saved to `docs/superpowers/plans/YYYY-MM-DD-<feature>.md`, must open with a mandatory header (goal, architecture, tech stack, spec path, Global Constraints, Review Focus), and decompose work into right-sized tasks — each the smallest unit carrying its own test cycle and worth a reviewer's gate. Every task lists exact files, Interfaces (Consumes/Produces with signatures), and TDD steps as checkboxes: write failing test, run to verify fail, implement, run to verify pass, commit. A self-review checklist (spec coverage, step scan, type consistency, review focus, proportion) runs before handoff, which then offers subagent-driven vs native execution.

## When to use / when NOT
Use when you have a spec or requirements for a multi-step task, BEFORE touching code. Do NOT use for single-step changes, when there is no spec yet (brainstorm first), or for plans covering multiple independent subsystems — those should be split into one plan per subsystem during brainstorming.

## Inputs, outputs, tools
- Inputs: the spec/design doc (which the plan argues from and links), codebase conventions, and global constraints.
- Outputs: a dated plan markdown file with header, global constraints, review focus, and checkbox tasks.
- Tools: none executable; pure authoring. Its output feeds subagent-driven-development or executing-plans.

## 5 most important rules
1. Document decisions, not code: exact values, names, signatures and test assertions go in; implementation bodies appear only when signature+tests don't determine them. A plan longer than the code it describes is a transcript, not a plan.
2. Every step must be unambiguous — one action with a checkable result ("write the failing test", "run it to verify it fails", "commit").
3. Global Constraints section carries the spec's project-wide requirements verbatim; every task implicitly includes them.
4. Review Focus lists the 5 input classes/failure modes the spec implies but no task tests — each gets a test added to the owning task.
5. Self-review before handoff: spec coverage, step scan, type consistency across tasks, review focus coverage, and proportion vs spec length.

## Risks / things needing the owner
The handoff explicitly asks the human to review the plan and choose execution method (subagent-driven recommended for thoroughness vs native for speed/cost) — in SIR's autonomous context that choice is typically pre-decided by the worker manual (subagent limits, quota). Ambiguity left open becomes implementer guesses; the plan's job is to eliminate them. Type/name drift between tasks is the most common self-review catch.

## Category / tags
build · planning, tdd, specifications, superpowers, documentation

## Revisions
Only one revision exists: the gemini-plugin superpowers copy. No divergent copies.
