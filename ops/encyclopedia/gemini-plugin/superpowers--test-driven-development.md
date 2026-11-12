# test-driven-development

- Tool: `gemini-plugin` (plugin: `superpowers`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\test-driven-development\SKILL.md`
- SKILL.md size: 9556 chars

## What it does

Use when implementing any feature or bugfix, before writing implementation code

## Structure (headings inside SKILL.md)

- Test-Driven Development (TDD)
- Overview
- When to Use
- The Iron Law
- Red-Green-Refactor
- RED - Write Failing Test
- Verify RED - Watch It Fail
- GREEN - Minimal Code
- Verify GREEN - Watch It Pass
- REFACTOR - Clean Up
- Repeat
- Good Tests
- Common Rationalizations
- Red Flags - STOP and Start Over
- Example: Bug Fix
- Verification Checklist
- When Stuck
- Debugging Integration
- Final Rule
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Delete means delete
- - Output pristine (no errors, warnings)
- - Name the production change that would make the test fail — before writing it
- - Keep test-only code in test utilities, out of production classes

## Key rules (verbatim lines from SKILL.md)

1. - Don't keep it as "reference"
2. - Don't "adapt" it while writing tests
3. - Name the production change that would make the test fail — before writing it
4. - Assert on real behavior, never on mock behavior
5. - Understand a dependency's side effects before mocking it

## Files inside the skill

- `writing-good-tests.md` — "Writing Good Tests"
