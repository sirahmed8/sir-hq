# ai-readiness

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\ai-readiness\SKILL.md`.

## Summary
This Postman plugin skill scores how well an API contract can be discovered, called, and recovered from by AI agents. It runs Postman's readiness check against a real Postman collection or OpenAPI spec, reports a readiness score, bucket, confidence, and documentation coverage, then turns measured gaps into contract improvements that can be re-tested.

## When to use / when NOT
Use when prioritizing API consumability for agents, checking whether contract improvements worked, or enforcing a team-agreed readiness threshold in CI. Skip it for typo fixes, one-off endpoint checks, or changes that do not affect the contract or agent usability; use api-testing when the question is whether the live API behaves correctly.

## Inputs, outputs, tools
Inputs are a Postman collection path or ID, or an OpenAPI spec path or ID, plus optional `--min-score` for a CI gate. Outputs are the readiness score, bucket from Limited to Excellent, confidence, documentation coverage signal, remaining gaps, and the threshold exit code when used. Tools are the Postman CLI commands `postman collection ai-readiness` and `postman spec ai-readiness`, the API artifact itself, and related skills for documentation, collection schema, testing, and CI integration.

## 5 most important rules
1. Score the artifact consumers actually use; do not generate a collection only to score a spec.
2. Keep `confidence` separate from the score because low confidence means important signals could not be measured.
3. Prioritize gaps that change caller behavior, such as unclear required inputs, missing auth instructions, or errors without recovery guidance.
4. Establish actual behavior before adding descriptions or examples; invented certainty can raise the score while misleading agents.
5. Re-run after edits to prove gaps closed, and use `--min-score` only as a separate CI readiness gate rather than a substitute for tests or lint.

## Risks / owner notes
A readiness score measures contract consumability, not live correctness, so a high score can still hide broken behavior. Low confidence or documentation coverage means the result is incomplete. The owner should choose the CI threshold from a real baseline and keep contract quality, tests, and lint as separate signals.

## Category / tags
ai · postman, openapi, api-contract, ai-readiness, agent-consumability, documentation, ci-gate

## Revisions
Single installed gemini-plugin Postman revision, modified 2026-11-12. No codex, claude, kilo, cursor, opencode, or windsurf copy was present.
