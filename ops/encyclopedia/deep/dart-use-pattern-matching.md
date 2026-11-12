# dart-use-pattern-matching (Flutter plugin)

## Summary
Idiomatic Dart 3 pattern-matching guide: a selection strategy mapping situations to pattern types (JSON/schema validation → object/list/map patterns; path segments & split tokens → list patterns with rest elements; polymorphic payloads → switch expressions over sealed hierarchies; multi-return → record patterns; ranges/conditions → relational+logical patterns), plus syntax rules for all pattern kinds, switch statement-vs-expression choice, and pragmatic anti-patterns (prefer `is` promotion over if-case for single variables).

## When to use / when NOT
Use when refactoring if-else chains, parsing JSON/API responses, destructuring lists/records/maps, or enforcing exhaustiveness on sealed classes. Do NOT use for simple boolean conditions or single-variable `is` promotion.

## Inputs, outputs, tools
- Inputs: Dart code with complex conditionals/destructuring needs.
- Outputs: idiomatic pattern-based code.
- Tools: none — language feature guide; examples/ dir.

## 5 most important rules
1. Switch expressions produce values (single expression per arm, exhaustive, no fallthrough); switch statements execute side effects.
2. List patterns need rest elements (`...`, `...final rest`) for variable-length input — kills manual length/index arithmetic.
3. Logical-or branches must bind identical variable sets; logical-and must not overlap.
4. `?` null-check binds non-nullable; `!` null-assert throws; `_` wildcard discards.
5. Don't pattern-match what `is` promotion already handles cleanly — patterns are for structure, not simple type checks.

## Risks / things needing the owner
Exhaustiveness on sealed classes is compile-enforced — adding a subtype breaks switches until handled (that's the point, but expect churn). Patterns can obfuscate simple logic if over-applied.

## Category / tags
build · dart, patterns, refactoring, language-features

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-use-pattern-matching\SKILL.md` (with examples/). Only gemini-plugin holds it.
