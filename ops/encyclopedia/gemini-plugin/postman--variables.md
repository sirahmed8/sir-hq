# variables

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\variables\SKILL.md`
- SKILL.md size: 3362 chars

## What it does

Use when parameterizing requests across environments, choosing variable scopes, chaining values in scripts, or referencing credentials without committing or exposing them. Keeps one reusable collection while separating target configuration from secret values. Use for requests such as "where should I put this API key".

## Structure (headings inside SKILL.md)

- Variables
- Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 4. Store durable credentials in the shared vault and commit references.

## Key rules (verbatim lines from SKILL.md)

1. 1. Put API defaults in collection variables and target-specific values, such
2. 2. Resolve surprises through precedence: local script values override
3. 3. Use runtime values for chaining responses into later requests. Choose

## Files inside the skill

- (SKILL.md only)
