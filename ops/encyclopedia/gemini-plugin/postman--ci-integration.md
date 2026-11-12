# ci-integration

- Tool: `gemini-plugin` (plugin: `postman`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\postman\skills\ci-integration\SKILL.md`
- SKILL.md size: 4169 chars

## What it does

Use when adding API tests, structural or governance lint, or AI-readiness gates to CI, or publishing reviewed API artifacts to a Postman workspace after merge. Makes contract checks repeatable and separates validation from shared workspace changes. Use for requests such as "run this collection on every PR".

## When to use (from skill text)

- `postman workspace push -y` changes shared context; a PR-triggered push
- the merge trigger, push strategy, created/updated entities, and conflicts;

## Structure (headings inside SKILL.md)

- CI Integration
- Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 4. Authenticate only jobs that need workspace resources. Use the CI secret

## Key rules (verbatim lines from SKILL.md)

1. 5. Publish only the reviewed branch after its merge checks pass.

## Files inside the skill

- (SKILL.md only)
