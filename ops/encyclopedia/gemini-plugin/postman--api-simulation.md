# api-simulation

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-simulation\SKILL.md`
- SKILL.md size: 12875 chars

## What it does

Runs services, frontends, tests or demos against stand-ins for their HTTP dependencies, served as one environment locally or at a deployed URL. Use when you add or change code that calls other services and need to run it, test it, prove a fix or reproduce an upstream failure (timeouts, 5xx, 409, 429) end to end, locally or in CI, without the real services because they're unreachable, need credentials, cost money, have side effects or don't exist yet. Also answers what happens to a request, or to the data it writes, when a service it calls goes down, is slow or returns errors ("what happens to a booking if the email service is down?"), by exercising relevant failures and observing caller outcomes. Applies even when nobody says mock or simulation, and a `postman/simulations/` directory in the repository is itself a reason to load this before changing code it covers. To give a frontend or another team a stand-in for an API, use api-mocking. Covers `postman simulation`.

## Structure (headings inside SKILL.md)

- API Simulation
- Building it
- Running it
- Running it on one port instead
- Reading the log
- When a dependency goes down
- Its context document
- Keeping it
- Rules
- Before you say it works
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Bring in each mock you don't own as a dependency first, then build the
2. 1. **What you're testing is never a member.** It must run for real, or the

## Files inside the skill

- `reference/context_file.md` — "`<name>.context.yaml`"
- `reference/sim_yaml_schema.md` — "`.sim.yaml` reference"
