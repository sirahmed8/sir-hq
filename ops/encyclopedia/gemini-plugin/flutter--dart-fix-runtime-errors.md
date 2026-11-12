# dart-fix-runtime-errors (Flutter plugin)

## Summary
Despite the name and frontmatter (which promise runtime stack traces + hot_reload via get_runtime_errors/LSP), the body is actually a static-analysis resolution guide: run `dart analyze --fatal-infos`, apply `dart fix --dry-run`/`--apply`, then manually resolve remaining errors by category — null-safety (?. ?? late required), type mismatches (explicit generics, strict-casts), invalid overrides (widen param or `covariant`) — with a verify loop. It also carries doctrine on sound typing, never catching `Error` subtypes, and `rethrow`.

## When to use / when NOT
Use when the analyzer reports errors you need to fix systematically. For genuine runtime crashes the description points to get_runtime_errors/hot_reload tooling, but the shipped content covers static errors — treat runtime debugging as only partially supported.

## Inputs, outputs, tools
- Inputs: analyzer diagnostics in the project.
- Outputs: fixed code passing `dart analyze`.
- Tools: `dart analyze`, `dart fix --dry-run/--apply`, `dart format`; analysis_options.yaml strictness flags.

## 5 most important rules
1. Analyzer first with `--fatal-infos`; automated fixes via `dart fix` dry-run then apply.
2. Never catch `Error` subtypes (TypeError, ArgumentError) — they're bugs; enable `avoid_catching_errors`.
3. `rethrow` preserves stack traces; catch `Exception` for recoverable failures.
4. Null-safety fixes: `?.`/`??` when null is possible, `late` only when init is provably deferred, `required` for non-null named params.
5. Override fixes: widen parameter type or mark `covariant` — never silently tighten.

## Risks / things needing the owner
`dart fix --apply` rewrites code — review the dry-run diff first. strict-casts can surface many latent dynamic casts.

## Category / tags
build · dart, flutter, static-analysis, debugging

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-fix-runtime-errors\SKILL.md`. Only gemini-plugin holds it. Note the description/body mismatch above.
