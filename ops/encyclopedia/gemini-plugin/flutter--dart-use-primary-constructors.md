# dart-use-primary-constructors

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-use-primary-constructors\SKILL.md`
- SKILL.md size: 11362 chars

## What it does

> Help users write syntactically and semantically correct primary constructors in Dart, and migrate/use the new constructor syntax, empty-body semicolon syntax, in-body initializer list syntax, and abbreviated concise constructor syntax.

## When to use (from skill text)

- Use this skill when helping users write, refactor, or debug code using Dart's **Primary Constructors** feature.
- - The representation variable cannot use the `var` modifier (using `var` triggers the `representation_field_modifier` error).

## Structure (headings inside SKILL.md)

- Dart Primary Constructors & New Constructor Syntax Skill
- Dart Version Requirements
- 1. Overview
- Key Benefits
- 2. Syntax Reference
- 2.1 Basic Class Header Syntax
- 2.2 Declaring, Initializing, and Plain Parameters
- 2.3 Constant Primary Constructors
- 2.4 Extension Types
- 2.5 Empty Body Semicolon Shorthand (`;`)
- 2.6 The In-Body Part of a Primary Constructor (`this ...`)
- 2.7 Abbreviated Concise Constructor Syntax
- 3. Semantics & Scoping Rules
- 3.1 Primary Initializer Scope
- 3.2 Late Instance Variables Restriction
- 3.3 Shadowing
- 3.4 Generative Constructor Restrictions
- 3.5 Parameter Mutation Errors
- 3.6 Double Initialization Errors
- 4. Diagnostics & Troubleshooting
- 5. Step-by-Step Refactoring Workflows
- Workflow 5.1: Migrating a Class to a Primary Constructor
- Workflow 5.2: Applying Abbreviated (Concise) In-Body Constructors
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. *   **Dart 3.12**: The feature is available but experimental. Users must explicitly enable the experiment flag `primary-constructors` via `--enable-experiment=primary-constructors` or in `analysis_options.yaml`:
2. 3. **Regular Parameters**: Declared without modifiers (e.g., `int y`). They do not become fields and are only available during initialization (e.g., in field initializers or the `this :` initializer list in the class body).
3. - Since `late` variables can be evaluated after construction has completed, their initializers cannot safely access constructor parameters.
4. - All other generative constructors declared in the body **must** redirect (directly or indirectly) to the primary constructor.

## Files inside the skill

- (SKILL.md only)
