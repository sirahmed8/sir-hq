# dart-fix-runtime-errors

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-fix-runtime-errors\SKILL.md`
- SKILL.md size: 6257 chars

## What it does

Uses get_runtime_errors and lsp to fetch an active stack trace, locate the failing line, apply a fix, and verify resolution via hot_reload.

## When to use (from skill text)

- Use this sequential workflow to identify, fix, and verify static analysis errors in a Dart project. Copy the checklist to track your progress.

## Structure (headings inside SKILL.md)

- Resolving Dart Static Analysis Errors
- Contents
- Core Concepts & Guidelines
- Type System & Soundness
- Null Safety
- Error Handling
- Workflows
- Workflow: Static Analysis Resolution
- Preview changes
- Apply changes
- Examples
- Example: Fixing Dynamic List Assignments
- Example: Fixing Method Overrides (Contravariance)
- Example: Fixing Null Safety with `late`
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- *   **Wildcards:** Use the `_` wildcard variable (Dart 3.7+) for non-binding local variables or parameters to avoid unused variable warnings.

## Key rules (verbatim lines from SKILL.md)

1. *   **Method Overrides:** Maintain sound return types (covariant) and parameter types (contravariant). Never tighten a parameter type in a subclass unless explicitly marked with the `covariant` keyword.
2. *   **Generics & Collections:** Add explicit type annotations to generic classes (e.g., `List<T>`, `Map<K, V>`). Never assign a `List<dynamic>` to a typed list (e.g., `List<Cat>`).
3. *   **Downcasting:** Avoid implicit downcasts from `dynamic`. Use explicit casts (e.g., `as List<Cat>`) when necessary, but ensure the underlying runtime type matches to prevent `TypeError` exceptions.
4. *   **Modifiers:** Apply `?` for nullable types, `!` for null assertions, and `required` for named parameters that cannot be null.
5. *   **Late Initialization:** Use the `late` keyword for non-nullable variables guaranteed to be initialized before use. Apply this specifically to top-level or instance variables where Dart's control flow analysis cannot definitively prove initialization.

## Files inside the skill

- (SKILL.md only)
