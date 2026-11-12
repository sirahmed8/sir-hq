# api-testing

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-testing\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An API testing skill that automates the execution of API test suites, validates responses against expected schemas, and performs regression testing. It integrates with CI/CD pipelines to run tests on every PR and can perform data-driven testing with multiple payloads. The skill generates detailed test reports, identifies failing endpoints, and can automatically create new test cases from recorded traffic patterns.

## When to use / when NOT
Use in every CI/CD pipeline to catch API regressions early. Do NOT skip the schema validation step — the skill will fail tests if responses don't match the OpenAPI-defined schemas, which is the primary way it catches regressions. Do NOT run API tests against a mock server in production — the skill is designed for real API testing, and mock-based tests may not catch all integration issues.

## Inputs, outputs, tools
- Inputs: OpenAPI/Swagger specification, test execution environment (base URL), authentication credentials, data-driven payload set (optional).
- Outputs: test results (pass/fail per endpoint), response validation report, data-driven test matrix, new test case suggestions from traffic patterns.
- Tools: Newman (Postman CLI), Jest, pytest, OpenAPI schema validators, CI/CD integrations (GitHub Actions, GitLab CI). MCP: gemini-plugin connector.

## 5 most important rules
1. **Always run API tests as part of every PR** — the skill integrates with GitHub Actions/GitLab CI to block merges if tests fail.
2. **Validate response schemas on every test run** — the skill compares actual responses against the OpenAPI-defined schemas; this is the primary regression detection mechanism.
3. **Use data-driven testing with multiple payloads** — the skill can execute the same test with different input values to uncover edge-case failures.
4. **Generate test reports with trend analysis** — the skill accumulates results over time; the owner should review the trend report weekly to identify recurring failures.
5. **Fail the CI build on any 5xx response** — the skill can be configured to treat server errors as build-breakers, ensuring that backend issues are caught early.

## Risks / owner notes
Test suite bloat is a common issue — running too many tests can slow down CI feedback loops. The owner should prioritize the most critical endpoints and use test filtering to focus on high-risk changes. Schema drift (OpenAPI changes without corresponding code changes) will cause test failures; the owner must ensure the OpenAPI source stays in sync with the implementation.

## Category / tags
api · testing, ci-cd, regression, schema-validation, automation, report

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.