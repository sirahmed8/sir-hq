# flows

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\flows\SKILL.md`
- SKILL.md size: 3977 chars

## What it does

Use when running, deploying, or debugging an existing Postman Flow. Distinguishes local graph execution from a deployed webhook, reuses named input scenarios, and follows a run to the failing block rather than treating an HTTP response as whole-flow success. Use for requests such as "why did this flow fail".

## When to use (from skill text)

- local JSON file; `postman flows trigger <flow-id>` calls the deployed
- webhook, including trigger auth and configuration. Local View and Cloud
- For deployed flows with side effects, `trigger --dry-run` lets you inspect

## Structure (headings inside SKILL.md)

- Postman Flows
- Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1. Choose the artifact the user means. `postman flows run <path>` executes a
2. 2. Resolve hosted IDs through `flows list --workspace <id>`; there is no
3. 3. Reuse a Start-block scenario when the same payload should travel with the

## Files inside the skill

- `reference/flow_cli_flags.md` — "Flows CLI Flags"
