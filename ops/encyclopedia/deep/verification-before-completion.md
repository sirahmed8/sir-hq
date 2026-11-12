# verification-before-completion (gemini-plugin: superpowers)

## Summary
verification-before-completion is the superpowers plugin's anti-bluffing gate: NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE. Before saying anything is done, fixed, passing, or expressing satisfaction, the agent must identify which command proves the claim, run it fresh and complete, read the full output including exit code and failure counts, and only then state the claim with the evidence attached. It includes a claim-vs-requirements table (tests pass needs the test command's 0-failures output; "build succeeds" needs exit 0 — a passing linter proves nothing about compilation), a red-flags list ("should", "probably", "seems to", satisfaction before verification, trusting agent success reports), and the regression-test rule that a bug fix is only proven by a red-green cycle (write test, revert fix, watch it fail, restore, watch it pass).

## When to use / when NOT
Use before ANY completion claim: committing, PRs, task completion, moving to the next task, delegating to agents, or any wording implying success or correctness — including paraphrases and implications, not just exact phrases. Do NOT use it as a substitute for actually running verification; it IS the requirement to run it. It applies even when tired or when "just this once" tempts skipping.

## Inputs, outputs, tools
- Inputs: the claim about to be made and the project's verification commands (test runner, linter, build, typecheck).
- Outputs: a claim backed by pasted command output, or an honest statement of actual status with evidence when verification fails.
- Tools: whatever the repo provides (npm test, pytest, cargo test, tsc, eslint, build scripts) plus VCS diff inspection for delegated work.

## 5 most important rules
1. If you haven't run the verification command in this message, you cannot claim it passes — fresh run every time, no "it passed earlier".
2. Match the proof to the claim: linter clean ≠ build succeeds; agent says success ≠ verified (check the VCS diff yourself).
3. Regression tests require the red-green cycle: revert the fix, watch the test FAIL, restore, watch it pass — a test that never failed proves nothing.
4. Requirements claims need a line-by-line checklist against the plan/spec, not just green tests.
5. Any failure seen — including ones you didn't cause — goes in the report by name; a red test scrolled past is a falsified report.

## Risks / things needing the owner
Costs verification time on every claim; that is the point. In SIR worker context this skill is essentially already law (rule 3 of the worker manual: "green means you saw it"), so it reinforces existing doctrine rather than adding new behavior. Tension: CI is currently quota-dead (flag file), so local verification output is the only acceptable evidence — same conclusion this skill reaches.

## Category / tags
build · verification, testing, honesty, quality-gate, superpowers

## Revisions
Only one revision exists: the gemini-plugin superpowers copy. No divergent copies.
