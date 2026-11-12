# api-mocking

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-mocking\SKILL.md`
- SKILL.md size: 7314 chars

## What it does

Finds, builds, runs and publishes a stand-in for one API — the owning team's published mock when there is one, otherwise one built from its spec or collection that behaves like the real API, stateful when callers write then read. Use when something needs an API that isn't built or reachable yet (a frontend, client or demo), when other teams should build against your API before it ships, or when asked to mock an API or fake a backend. To run and test your own code against the services it calls, use api-simulation. Covers `postman mock` and `postman dependency add mock`.

## Structure (headings inside SKILL.md)

- API Mocking
- Use the owner's mock first
- Or build one that behaves like the real API
- Check it against the contract
- Publish it for other teams
- Before you say it's done
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Ask before `--public`.** It serves the mock and its data to anyone with

## Files inside the skill

- (SKILL.md only)
