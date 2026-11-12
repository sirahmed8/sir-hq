# api-mocking

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-mocking\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An API mocking skill that generates realistic mock servers from OpenAPI/Swagger specifications. It can simulate endpoint responses including status codes, response bodies, headers, and delay times. The skill supports stateful mocking (different responses based on request patterns), error simulation (HTTP errors, timeouts), and can be used for frontend-backend integration development when the actual API is not yet available.

## When to use / when NOT
Use when the API is still in design phase and frontend teams need to proceed without the backend, or when testing edge cases that are difficult to reproduce with a real API. Do NOT use mock data in production — the skill is strictly for development and testing environments. Do NOT skip the response template customization; the skill generates sensible defaults but your domain logic may require specific mock responses.

## Inputs, outputs, tools
- Inputs: OpenAPI/Swagger YAML/JSON file, mock server port, response delay (ms), stateful behavior rules (optional).
- Outputs: running mock server URL, generated client mock configurations, example curl commands for edge cases.
- Tools: Prism (SmartBear), MockServer, openapi-mock CLI, node.js for config generation. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always specify realistic response delays** — the skill defaults to 500ms; set this to match your real API's typical response time for realistic frontend testing.
2. **Configure error status codes for edge cases** — the skill can mock 4xx and 5xx responses; define these so frontend error handling is tested.
3. **Use stateful mocking for complex workflows** — if the API has multi-step processes, define state transitions so the mock responds correctly across requests.
4. **Pin the mock server version** — the skill will start a specific Prism version; upgrading the mock server may change response behaviors.
5. **Stop the mock server after testing** — running mock servers in the background can consume ports and cause conflicts; the skill provides a stop command.

## Risks / owner notes
Mock servers that too closely mimic the real API can hide genuine bugs that would be caught by the actual API's behavior. The owner should ensure that mock responses are intentionally simplified and do not replicate all real API quirks. Mock server port conflicts are common; always specify a unique port or use the skill's port auto-assignment.

## Category / tags
api · mocking, testing, development, mock-server, prism, integration-testing

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.