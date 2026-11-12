# dart-use-pattern-matching

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-use-pattern-matching\SKILL.md`
- SKILL.md size: 13710 chars

## What it does

>- Applies Dart 3 pattern matching, switch expressions, and destructuring idiomatically to validate data schemas, handle algebraic data types, and decompose control flow. Use when refactoring complex if-else chains, parsing polymorphic JSON or API responses, destructuring Lists, URI/path segments, String.split() tokens, Records, or Maps, or enforcing exhaustiveness on sealed classes. Don't use for simple boolean conditions, single-variable type promotion (use `is`), or basic collection filtering.

## When to use (from skill text)

- Do not use `if-case` in loops or deserialization to filter elements if malformed data should trigger an error or diagnostic warning.

## Structure (headings inside SKILL.md)

- Implementing Dart Patterns
- Contents
- Pattern Selection Strategy
- Switch Statements vs. Expressions
- Core Pattern Implementations
- Pragmatic Balance & Anti-Patterns
- 1. Prefer `is` Type Promotion over `if-case` for Single Promotable Variables
- 2. Consolidate Nullable Types in Switch Arms
- 3. Preserve Fast-Fail Validation (Do Not Silently Drop Data)
- 4. Avoid Single-Case or Boolean Switches
- 5. Use Object Destructuring for Multi-Field Unpacking, Not Single Properties or Passthroughs
- 6. Avoid `if-case` for Standalone Scalar Comparisons
- Workflows
- Task Progress: Implementing Pattern Matching
- Feedback Loop 1: Exhaustiveness Checking (Static Verification)
- Feedback Loop 2: Runtime Map & JSON Pattern Verification
- Examples
- Polymorphic JSON Deserialization (Discriminated Unions)
- Nested JSON Validation and Optional Fields
- List and Path Segment Destructuring
- Algebraic Data Types (Sealed Classes)
- Variable Swapping and Destructuring
- Guard Clauses and Logical-or
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- *   **If inspecting URL/path segments (`uri.pathSegments`, `p.split(path)`) or `String.split()` tokens:** Use List patterns with rest elements (`['api', 'comments', ...]`, `['assets', ...final rest]`, `[..., final parent, _]`) instead of manual `.length` checks, `.first`, `.skip(1)`, or `length - N`
- *   **If producing a value:** Use a **switch expression**.
- 2. **Review errors:** Look for "The type 'X' is not exhaustively matched by the switch cases" or unreachable pattern arm warnings.

## Key rules (verbatim lines from SKILL.md)

1. *   **If inspecting URL/path segments (`uri.pathSegments`, `p.split(path)`) or `String.split()` tokens:** Use List patterns with rest elements (`['api', 'comments', ...]`, `['assets', ...final rest]`, `[..., final parent, _]`) instead of manual `.length` checks, `.first`, `.skip(1)`, or `length - N`
2. *   Rule: Each case must be a single expression. No implicit fallthrough. Must be exhaustive.
3. *   Rule: Empty cases fall through to the next case. Non-empty cases implicitly break (no `break` keyword required).
4. *   **Logical-or (`||`):** `pattern1 || pattern2`. Both branches must define the exact same set of variables.
5. *   **Logical-and (`&&`):** `pattern1 && pattern2`. Branches must *not* define overlapping variables.

## Files inside the skill

- `examples/json_patterns.dart`
