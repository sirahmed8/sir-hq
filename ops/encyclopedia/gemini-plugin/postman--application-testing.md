# application-testing

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\application-testing\SKILL.md` (11.6 KB; gemini-plugin/postman).

## Summary
Skill for running the Postman layer over application traffic: it spawns the app's Playwright test command, captures network traffic, matches requests against collections, runs saved `pm.test` assertions and publishes results to Postman Application Inventory.

## When to use / when NOT
Use when setting up application testing, connecting Playwright tests to Postman, capturing traffic, or interpreting capture and match results. Do NOT use for authoring Playwright tests or diagnosing Playwright failures unrelated to capture.

## Inputs, outputs, tools
- Inputs: Playwright project, test command, collection or generated collection, target.
- Outputs: captured, matched and asserted counts, summary table, published results.
- Tools: `postman app test`, `postman app setup-capture`, postman config file at repo root, Playwright withPostman capture plugin.

## 5 most important rules
1. `postman application test` captures traffic; it does not drive requests. The test runner drives the app; Postman observes and asserts.
2. "Not matched" is a coverage gap, not a test failure; unmatched requests run no assertions and do not affect the exit code.
3. Transformers run before matching, not before capture; the raw URL is stored and rewritten for matching only.
4. Results are published per run; pass `--report-events false` for dry runs or local debugging that should not be recorded.
5. The CLI exit code is the test runner's exit code, not the Postman assertion pass or fail count.

## Risks / things needing the owner
Publishing results requires a Postman API key or workspace; the app servers must be running for a real run.

## Category / tags
Category: automation. Tags: api, postman, playwright, application, capture, assertions.

## Revisions
Single gemini-plugin/postman copy. No competing revisions.
