# test-driven-development (gemini-plugin: superpowers)

## Summary
test-driven-development is the superpowers plugin's strict TDD discipline: NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST. The cycle is RED (write one minimal test for one behavior, with a clear name and real code not mocks) → verify it fails for the right reason → GREEN (write the simplest code that passes, nothing more) → verify pass with a pristine suite → REFACTOR (clean up only while staying green). Code written before its test must be DELETED, not kept as reference — "delete means delete." It includes a good-tests/bad-tests contrast, a rationalization table demolishing excuses ("too simple to test", "I'll test after", "already manually tested", "TDD is dogmatic"), a when-stuck table (hard-to-test = unclear design; mock-everything = too coupled), and integration with systematic-debugging (every bug fix starts with a failing reproduction test).

## When to use / when NOT
Always for new features, bug fixes, refactoring and behavior changes. Exceptions require asking the human partner: throwaway prototypes, generated code, configuration files. Do NOT use it as permission to test-after; tests written after implementation "answer what does this do" instead of "what should this do" and are biased by the code already written.

## Inputs, outputs, tools
- Inputs: the behavior to implement or the bug to fix.
- Outputs: a failing test first, minimal production code, a green suite, then refactoring.
- Tools: the project's test framework (examples in TypeScript/Jest but language-agnostic), plus writing-good-tests.md reference for test-honesty rules (name the production change that would fail the test, assert real behavior, keep test-only code in utilities, understand dependency side effects before mocking).

## 5 most important rules
1. Watch every test fail before implementing; if it passes immediately you are testing existing behavior — fix the test.
2. Verify RED properly: the failure must be the expected one (feature missing), not a typo or error.
3. GREEN means minimal code to pass — no speculative features, no bundled refactoring, no "while I'm here" improvements.
4. "Other tests" means the whole project suite, not just your file; run the project's test command before calling the change done, and report every failure by name including ones you didn't cause.
5. Code before test = delete it and start over; no exceptions without explicit human permission.

## Risks / things needing the owner
Strict TDD slows greenfield exploration; the skill acknowledges exploration is fine but says throw it away and restart with TDD. For SIRE worker tasks that are docs/config-only, the exceptions apply (ask first). Legacy codebases without tests need tests added for existing code rather than skipped. Nothing else needs the owner.

## Category / tags
build · tdd, testing, methodology, superpowers, quality

## Revisions
Only one revision exists: the gemini-plugin superpowers copy (SKILL.md plus writing-good-tests.md). No divergent copies.
