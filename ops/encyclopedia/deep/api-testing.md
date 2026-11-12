# api-testing

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-testing\SKILL.md` (3.4 KB; gemini-plugin/postman).

## Summary
Skill for testing an endpoint or running collection assertions: saved requests preserve auth, payloads and assertions; pick the smallest execution mode and derive assertions from the contract and the behavior at risk.

## When to use / when NOT
Use when testing an endpoint, running collection assertions, or checking real application traffic against an API contract. Do NOT use for building mocks or simulating failures; use api-mocking and api-simulation.

## Inputs, outputs, tools
- Inputs: endpoint, saved request, collection, contract, target (real or mocked).
- Outputs: pass or fail evidence, assertion counts, exported reports.
- Tools: `postman request`, `postman collection run`, `postman application test`, variables and datasets for input handling.

## 5 most important rules
1. The useful result is evidence about an intended guarantee; a successful HTTP exchange alone does not establish correctness.
2. Reuse a matching saved request under `postman/collections/` before reconstructing its HTTP fields.
3. Derive assertions from the contract and the behavior at risk; a test that repeats the current implementation can bless its bug.
4. Choose a real or mocked target per claim; passing against a mock does not verify the real service.
5. Report the target, tested behavior, assertion counts and exit code; the exit code reflects failed assertions, not HTTP status alone.

## Risks / things needing the owner
Workspace-bound resources need a signed-in CLI; datasets and variables may need owner-provided inputs.

## Category / tags
Category: automation. Tags: api, postman, testing, assertions, collections.

## Revisions
Single gemini-plugin/postman copy. No competing revisions.
