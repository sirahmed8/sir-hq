# dart-migrate-to-checks-package

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-migrate-to-checks-package\SKILL.md`
- SKILL.md size: 19324 chars

## What it does

|- Replace the usage of `expect` and similar functions from `package:matcher` to `package:checks` equivalents.

## When to use (from skill text)

- Use this skill when you need to migrate a Dart test suite from the legacy
- - [When to Use This Skill](#when-to-use-this-skill)
- - [How to Use This Skill (The Workflow)](#how-to-use-this-skill-the-workflow)

## Structure (headings inside SKILL.md)

- Migrating Dart Tests to Package Checks
- Contents
- When to Use This Skill
- How to Use This Skill (The Workflow)
- 1. Dependency Setup
- 2. Identify and Plan Target Files
- 3. Migrating a File (Incremental or Full)
- 4. Verification and Feedback Loops
- Key Syntax Differences and Pitfalls
- 1. Collection Equality Pitfall (`equals` vs `deepEquals`)
- 2. The `reason` Parameter is now `because`
- 3. Regular Expression Matching (`matches` vs `matchesPattern`)
- 4. Property Extraction (`TypeMatcher.having` vs `.has`)
- 5. Synchronous vs. Asynchronous `throws`
- 6. RegExp / Pattern Equality
- 7. Strict Nullable Boolean Safety (`bool?` fields)
- 8. Map Key Containment (`containsKey` vs `contains`)
- 9. Explicit Generic Parameters for Extension Types
- 10. Dynamic Map / JSON Lookup Casting
- Matcher-to-Checks Mapping Table
- Matchers with No Direct Replacements
- 1. Specific Error Matchers
- 2. The `anything` Matcher
- 3. Specific Numeric Toggles
- 4. Numeric Ranges
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Remediation**: You **must** replace collection equality assertions with
2. - **Remediation**: To match using a regular expression, you must explicitly
3. - **Crucial Pitfall**: Trying to chain expectations directly after an awaited
4. - **Remediation**: For fields declared as `bool?`, you must either refine the

## Files inside the skill

- (SKILL.md only)
