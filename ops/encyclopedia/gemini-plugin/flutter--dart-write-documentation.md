# dart-write-documentation

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-write-documentation\SKILL.md`
- SKILL.md size: 6727 chars

## What it does

Rules and formatting guidelines for writing Dart /// API documentation and doc comments. Use when documenting Dart code, writing doc comments for any Dart declaration (libraries, classes, methods, variables, etc.), or when instructed to follow the Effective Dart documentation guidelines.

## When to use (from skill text)

- 1. Run `dart analyze` to ensure all bracketed references resolve properly without triggering `comment_references` warnings.
- /// To use this, you must pass a [Client].
- /// To use this, you must pass a [Client].

## Structure (headings inside SKILL.md)

- Writing Dart API Documentation
- Contents
- 1. Scope and Structure
- 2. Tone and Openers
- 3. Strict Anti-Patterns (Banned)
- 4. Technical Placement & Resolution
- 5. Linking and Markdown
- 6. Verification
- Examples
- 1. Banned Tags vs. Prose
- 2. The Annotation Placement Trap
- 3. Openers and Tone
- 4. Constructor Linking
- 5. Out-of-Scope Links (@docImport)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- *   [3. Strict Anti-Patterns (Banned)](#3-strict-anti-patterns-banned)
- *   **Getter/Setter Pairs:** If a property has both a getter and a setter, place the documentation only on the getter. Tooling will emit a warning if both are documented.
- 1. Run `dart analyze` to ensure all bracketed references resolve properly without triggering `comment_references` warnings.

## Key rules (verbatim lines from SKILL.md)

1. *   **Target Public APIs:** Focus your documentation efforts on public declarations. Do not document private members (those starting with an underscore `_`) unless explicitly instructed, as they do not appear in generated API reference sites.
2. *   **Always use `///`:** Use `///` consecutive line comments for all API documentation. Never use `/** ... */` block comments.
3. *   **The First Paragraph:** The first paragraph of a doc comment must be a single, concise sentence that summarizes the element. End it with a period. Dartdoc extracts this verbatim for list views.
4. *   **Separation:** Always separate the first sentence summary from the rest of the documentation with a blank line containing `///`. Never output a completely empty newline (e.g., a `\n` without `///`), as this terminates the doc comment block.
5. *   **Avoid redundancy:** Do not restate the signature or the element name. Do not say "This class is a..." or "The foo method does...".

## Files inside the skill

- (SKILL.md only)
