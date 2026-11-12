# application-testing

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\application-testing\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An application testing skill that performs end-to-end testing of complete software applications, including UI interactions, API calls, and database state verification. It combines browser automation (Playwright or Cypress) with API testing to verify that the full application stack functions correctly from user input to data persistence. The skill can generate test cases from user stories and run cross-browser validation.

## When to use / when NOT
Use for full-stack quality assurance before releases — the skill verifies that user workflows complete successfully across all supported browsers. Do NOT skip cross-browser testing — the skill automatically tests on Chrome, Firefox, and WebView2; the owner must add Safari/iOS testing if the app targets Apple devices. Do NOT run full application tests on every commit — the skill is designed for nightly or release-cycle runs; running it on every commit will slow down developer feedback.

## Inputs, outputs, tools
- Inputs: user stories or feature descriptions, list of supported browsers, test environment URL, CI/CD integration preference.
- Outputs: test execution results (pass/fail per story), cross-browser coverage report, UI interaction screenshots, database state verification, regression report.
- Tools: Playwright, Cypress, Selenium, Jest, pytest, database assertion tools. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always include at least one happy-path user story** — the skill will verify the entire workflow from UI input to database persistence; without a happy path, the test suite has no baseline.
2. **Run cross-browser tests on at least Chrome and Firefox** — the skill defaults to these two; Safari/iOS testing requires explicit configuration by the owner.
3. **Capture UI screenshots on test failure** — the skill automatically generates PNG screenshots at the point of failure; these are essential for debugging visual regressions.
4. **Verify database state after API-driven tests** — the skill can run SQL assertions to confirm that the correct data was persisted; do not assume the UI correctly persisted data.
5. **Integrate with your CI pipeline for nightly runs** — the skill can be configured to run on every push or on a nightly schedule; the owner should choose the frequency that balances feedback speed with resource usage.

## Risks / owner notes
UI test flakiness is the most common failure mode — elements may be loaded at different times causing intermittent failures. The skill supports waiting strategies, but the owner should also ensure that test IDs are used reliably rather than fragile CSS selectors. Cross-browser differences in UI rendering may cause false failures; the owner should review failed tests to distinguish real regressions from rendering differences.

## Category / tags
testing · e2e, full-stack, cross-browser, playwright, cypress, ui, automation

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.