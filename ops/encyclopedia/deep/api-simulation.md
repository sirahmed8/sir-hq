# api-simulation

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-simulation\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An API simulation skill that creates realistic test environments for REST APIs by replaying recorded request/response traffic. It can capture live API traffic, generate simulated responses that match the original patterns, and replay scenarios for load testing or regression testing. The skill supports parameter substitution, so simulations can vary responses based on input parameters, and can inject faults or delays to test error handling.

## When to use / when NOT
Use when you need to test client applications against a simulated API before the real backend is available, or when replaying historical traffic to reproduce bugs. Do NOT use simulation as a replacement for integration tests with the real API — the skill is intended for early-stage development and testing. Do NOT inject realistic delays without configuring them based on actual measurements; the skill defaults to 200ms which may not reflect your real API's latency.

## Inputs, outputs, tools
- Inputs: recorded traffic file (HAR, JSON), simulation duration, parameter substitution rules, fault injection options (delay, error codes).
- Outputs: running simulation server URL, varied response generation, fault injection confirmation, traffic analysis report.
- Tools: Postman, HAR parser, mountebank, traffic capture scripts. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always capture traffic from a real environment when possible** — the simulation is only as good as the recorded traffic; capturing from staging or dev environments produces the most accurate results.
2. **Use parameter substitution to test edge cases** — the skill can vary responses based on input values; define substitution rules to test boundary conditions.
3. **Inject faults deliberately to test error handling** — the skill can return 500 errors, timeouts, or slow responses; this ensures your client code handles failures gracefully.
4. **Limit simulation duration for load testing** — the skill can run for a specified time or number of requests; do not run indefinite simulations in production environments.
5. **Validate simulation output against the original OpenAPI** — the skill will flag any responses that deviate from the specification; review these before relying on the simulation.

## Risks / owner notes
Simulations that are not based on real traffic may produce unrealistic response patterns, giving a false sense of security. The owner should always validate the simulation against the original OpenAPI specification. Fault injection that is too aggressive (e.g., 100% error rate) can mask genuine integration issues; use moderate fault rates (10-20%) for testing error handling.

## Category / tags
api · simulation, testing, development, mountebank, replay, regression-testing

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.