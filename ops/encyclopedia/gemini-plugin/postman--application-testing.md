# application-testing

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\application-testing\SKILL.md`
- SKILL.md size: 11516 chars

## What it does

Sets up, runs, debugs, and interprets results from `postman application test` — the Postman layer that runs your Playwright tests, captures their network traffic, matches it against a collection contract, runs pm.test assertions, and publishes results to Application Inventory. Covers the Postman side of the integration only — not Playwright test authoring or Playwright failures unrelated to capture. Use when the user asks to "set up application testing," "test my application with Postman," "connect my Playwright tests to Postman," "capture network traffic from Playwright," "Playwright tests are running but nothing shows up in Postman," "why isn't application testing capturing anything," "exclude certain requests from capture," "generate a collection from my app's traffic," "set up application testing in CI," "what API coverage do my e2e tests have," "which APIs are my Playwright tests not hitting.

## When to use (from skill text)

- **Capture-only mode** — when the goal is to stage and review traffic before committing a collection manually, there is a mode that skips collection matching and writes captured traffic as a collection to disk. Use this only as a review step, not the normal run path.
- 3. **Transformers run before matching, not before capture.** The raw URL is stored; the transformer rewrites it for the matching step only. Use this to normalise staging/prod URL differences without losing the original for debugging.

## Structure (headings inside SKILL.md)

- Application Test
- Overview
- Prerequisites
- Playwright project
- Authentication
- Workspace link
- Capture plugin
- Server reachability
- Running
- Config File (`postman.config.cjs`)
- Debugging
- Requests show "not matched" in the summary table
- Critical Rules
- Anti-patterns
- Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. **Transformers run before matching, not before capture.** The raw URL is stored; the transformer rewrites it for the matching step only. Use this to normalise staging/prod URL differences without losing the original for debugging.

## Key rules (verbatim lines from SKILL.md)

1. - If the key is not available, surface the gap to the user — do not initiate `postman login` in an agentic context, as it requires a human to complete a browser flow.
2. - If publishing is needed and the workspace is missing, load the `workspaces` skill to set it up. In a non-interactive context this must be done locally first, then `.postman/resources.yaml` committed.
3. - *Test command*: check `package.json` scripts for a project-specific test command (e.g. `npm run test:e2e`). Present what you find and ask the user to confirm — the CLI defaults to `npx playwright test` when a Playwright config is found, but do not assume that is what they want.
4. - **Rewrite URLs before matching** — add `transformers` (config entries that normalize staging/proxy prefixes before the CLI matches captured URLs against the collection)
5. - URLs have a staging prefix or proxy path — add a `transformers` entry in `postman.config.cjs` to rewrite them before matching.

## Files inside the skill

- (SKILL.md only)
