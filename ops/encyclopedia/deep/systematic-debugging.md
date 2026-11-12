# systematic-debugging (gemini-plugin: superpowers)

## Summary
systematic-debugging is the superpowers plugin's disciplined bug-fixing protocol built on one iron law: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST. It runs four mandatory phases — (1) root cause investigation (read errors fully, reproduce consistently, check recent changes, add boundary instrumentation in multi-component systems, trace data flow backward), (2) pattern analysis (find working examples, read reference implementations completely, list every difference), (3) hypothesis and testing (one hypothesis at a time, smallest possible change, verify before continuing), (4) implementation (write a failing test first, apply ONE fix, verify, and after 3 failed fixes STOP and question the architecture rather than attempt fix #4). It ships support files: root-cause-tracing.md, defense-in-depth.md, condition-based-waiting.md plus find-polluter.sh and a TS example.

## When to use / when NOT
Use for ANY technical issue: test failures, production bugs, unexpected behavior, performance problems, build failures, integration issues — especially under time pressure or when a "quick fix" tempts guessing, and after any previous fix failed. Do NOT use for feature design (no bug), for issues already root-caused (go implement the fix), or as a license to skip it because the bug "seems simple".

## Inputs, outputs, tools
- Inputs: the symptom (error message, failing test, misbehavior) and access to reproduce it.
- Outputs: a confirmed root cause, a failing-then-passing test proving the fix, and a single targeted change — plus documentation if the cause turns out environmental.
- Tools: the project's test runner, logging/instrumentation, git diff/log for recent changes, and the bundled references (backward call-stack tracing, defense-in-depth validation layers, condition-based waiting to replace arbitrary timeouts).

## 5 most important rules
1. Phase order is mandatory: no fix proposal before Phase 1 investigation is complete.
2. Reproduce consistently first; if not reproducible, gather data — never guess.
3. In multi-component systems, instrument each boundary (what enters/exits each layer) and run once to find WHERE it breaks before investigating that component.
4. One hypothesis, one variable, smallest change; if it fails, form a NEW hypothesis — do not stack fixes.
5. After 3 failed fixes, stop: repeated fixes revealing new coupling elsewhere means an architectural problem, which needs discussion, not fix #4.

## Risks / things needing the owner
The process is deliberately slower up front; under a real emergency the skill still insists systematic is faster than thrashing. The "discuss architecture with your human partner" step is the only place it pauses. Pairs with test-driven-development (failing test in Phase 4) and verification-before-completion. Nothing needs the owner beyond that discussion gate.

## Category / tags
build · debugging, root-cause, testing, methodology, superpowers

## Revisions
Only one revision exists: the gemini-plugin superpowers copy, which is unusually complete (SKILL.md plus four support files). No divergent copies.
