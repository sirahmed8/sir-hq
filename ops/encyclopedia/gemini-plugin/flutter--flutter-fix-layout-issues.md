# flutter-fix-layout-issues

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\flutter-fix-layout-issues\SKILL.md`
- SKILL.md size: 5326 chars

## What it does

Fixes Flutter layout errors (overflows, unbounded constraints) using Dart and Flutter MCP tools. Use when addressing "RenderFlex overflowed", "Vertical viewport was given unbounded height", or similar layout issues.

## When to use (from skill text)

- *   **"Vertical viewport was given unbounded height"**: Triggered when a scrollable widget (`ListView`, `GridView`) is placed inside an unconstrained vertical parent (`Column`). The parent provides infinite height, and the child attempts to expand infinitely.
- *   **"An InputDecorator...cannot have an unbounded width"**: Triggered when a `TextField` or `TextFormField` is placed inside an unconstrained horizontal parent (`Row`). The text field attempts to determine its width based on infinite available space.
- *   **"RenderFlex overflowed"**: Triggered when a child of a `Row` or `Column` requests a size larger than the parent's allocated constraints. Visually indicated by yellow and black warning stripes.

## Structure (headings inside SKILL.md)

- Resolving Flutter Layout Errors
- Contents
- Constraint Violation Diagnostics
- Layout Error Resolution Workflow
- Task Progress
- Examples
- Fixing Unbounded Height (ListView in Column)
- Fixing Unbounded Width (TextField in Row)
- Fixing RenderFlex Overflow
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- *   **"RenderFlex overflowed"**: Triggered when a child of a `Row` or `Column` requests a size larger than the parent's allocated constraints. Visually indicated by yellow and black warning stripes.

## Key rules (verbatim lines from SKILL.md)

1. *   **"Incorrect use of ParentData widget"**: Triggered when a `ParentDataWidget` is not a direct descendant of its required ancestor. (e.g., `Expanded` outside a `Flex`, `Positioned` outside a `Stack`).
2. - **If "Incorrect use of ParentData widget"**: Move the `ParentDataWidget` to be a direct child of its required parent. Ensure `Expanded`/`Flexible` are direct children of `Row`/`Column`/`Flex`. Ensure `Positioned` is a direct child of `Stack`.

## Files inside the skill

- (SKILL.md only)
