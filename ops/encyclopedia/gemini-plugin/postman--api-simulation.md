# api-simulation

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-simulation\SKILL.md` (12.9 KB; gemini-plugin/postman) plus `reference/sim_yaml_schema.md` and `reference/context_file.md`.

## Summary
Skill for running services, frontends, tests or demos against stand-ins for their HTTP dependencies, served locally or at a deployed URL; records simulation context and assumptions beside each simulation.

## When to use / when NOT
Use when adding or changing code that calls other services and you need to run it against mocks, prove a fix, or reproduce an upstream failure without the real services. Do NOT use for simple lookups or for building mocks; use api-discovery and api-mocking.

## Inputs, outputs, tools
- Inputs: simulation file, mocks, context document, code under test.
- Outputs: simulation run log, context claims, pass or fail judgment.
- Tools: `postman simulation run`, `postman simulation create`, `postman mock run`, `postman request`; CLI 1.70.0 or later required.

## 5 most important rules
1. The code under test must run for real; a member standing in for the dependency means the test only proves the mock.
2. Pull the owner's mock even when one is deployed; only members take conditions and appear in the log.
3. `simulation deploy` is public by default, unlike mock deploy; ask before deploying without `--private`.
4. What the run proves depends on `origin:`; a member with no origin is never matched under `--proxy`.
5. Claim a simulation passes only after the code ran and the expected response or state change was observed; write findings into the context document.

## Risks / things needing the owner
Simulation deploy or public exposure needs an explicit owner ask; context documents accumulate claims that need refreshing.

## Category / tags
Category: automation. Tags: api, postman, simulation, mocks, testing, context.

## Revisions
Single gemini-plugin/postman copy. No competing revisions.
