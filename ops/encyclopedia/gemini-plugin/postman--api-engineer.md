# api-engineer

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-engineer\SKILL.md` (5.9 KB; gemini-plugin/postman).

## Summary
Postman skill that makes API knowledge reusable across implementation, tests, mocks and teammates: establishes the intended contract before implementation, records the contract in a runnable collection, matches verification to the behavior at risk, and routes to the related API skills.

## When to use / when NOT
Use when designing, implementing, mocking, testing, monitoring, documenting or deploying an API, or for requests such as "implement this endpoint". Do NOT use for tasks with no API component or for general code review.

## Inputs, outputs, tools
- Inputs: API task, behavior change, contract or implementation state.
- Outputs: contract updates, code, tests, mocks, docs, verification evidence.
- Tools: postman CLI, collections, workspaces, variables, mock and simulation tooling; related skills: api-documentation, api-testing, api-discovery, api-simulation, api-mocking, webhook-testing.

## 5 most important rules
1. Establish the intended contract before implementing, and update it where behavior changes; flag design trade-offs that make callers work harder.
2. Record the contract in a runnable collection so the same source can generate a spec, mock, SDK or performance suite.
3. Match verification to the behavior at risk; report what the results actually establish.
4. Keep specs, collections, environments and mocks in local files so changes can be diffed and reviewed in Git and CI.
5. When a CLI command suggests an action or blocks on a plan, subscription, credit or usage restriction, follow the workspaces CLI suggested actions.

## Risks / things needing the owner
CLI subscription and credit limits can block implementation or verification work; publishing and credentials need owner decisions.

## Category / tags
Category: build. Tags: api, postman, engineering, contracts, implementation, verification.

## Revisions
Single gemini-plugin/postman copy. No competing revisions.
