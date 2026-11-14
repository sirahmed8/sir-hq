# api-mocking

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-mocking\SKILL.md` (7.3 KB; gemini-plugin/postman).

## Summary
Skill for standing up a stand-in API: use the owning team's published mock first, otherwise build one from the spec or collection that behaves like the real API, run it, and publish it for other teams.

## When to use / when NOT
Use when something needs an API that is not built or reachable yet, or when other teams should build against your API before it ships. Use api-simulation to run your own code against the services it calls.

## Inputs, outputs, tools
- Inputs: API under mock, contract (spec or collection), owner workspace.
- Outputs: mock folder, deploy state, run evidence.
- Tools: postman mock commands, `postman dependency add mock`, `postman mock run`, `postman request`.

## 5 most important rules
1. Prefer the owner's published mock; never edit `postman/.dependencies/`, copy a mock to `postman/mocks/` to customize it.
2. Build from the contract; a generated mock is a replay, so `x-mock-response-code` must carry the documented error statuses.
3. Set `interceptRequests: true` in the mock config or request body and query stay undefined and async handler errors kill the mock.
4. Make mocks stateful when callers write then read; use scenarios and session keys appropriately.

## Risks / things needing the owner
Mock server deployment needs a paid plan; `--public` needs an explicit ask before use.

## Category / tags
Category: build. Tags: api, mock, postman, testing, state, scenarios.

## Revisions
Single gemini-plugin/postman copy. No competing revisions.
