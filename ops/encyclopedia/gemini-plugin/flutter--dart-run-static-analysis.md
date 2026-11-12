# dart-run-static-analysis (Flutter plugin)

## Summary
Guide for Dart static analysis and automated fixes: configure `analysis_options.yaml` (include lints package, strict-casts/inference/raw-types, don't mix list/map rule syntax, formatter page_width/trailing_commas, analyzer plugins as dev_deps), suppress diagnostics at the right level (exclude globs for generated files, `ignore_for_file`, `ignore:` line, `# ignore:` in pubspec, plugin-prefixed codes), run `dart analyze` (optionally `--fatal-infos`), then `dart fix --dry-run` → `--apply` → `dart format .` → re-analyze.

## When to use / when NOT
Use during development and before committing to catch type errors, lints, runtime risks. Do NOT use as the only quality gate (pair with tests) or for runtime debugging.

## Inputs, outputs, tools
- Inputs: Dart/Flutter project with analysis_options.yaml.
- Outputs: clean analyzer output, auto-fixed code.
- Tools: `dart analyze`, `dart fix --dry-run/--apply`, `dart format`; optional analyze_files/dart_fix/dart_format MCP tools; examples/ dir.

## 5 most important rules
1. Always include a base lint set (`lints/recommended` or `flutter_lints`); enable strict-casts/inference/raw-types.
2. Never mix list and map syntax in the same `linter.rules` block.
3. Suppress at the narrowest correct level — exclude `**/*.g.dart` via analyzer.exclude rather than ignoring everywhere.
4. `dart fix` flow is dry-run → review → apply → format → re-analyze; enable the relevant lint rules or fixes won't be proposed.
5. `--fatal-infos` when info-level issues must fail CI.

## Risks / things needing the owner
`dart fix --apply` mass-edits code — review dry-run first. Over-broad `ignore_for_file` hides real issues; keep suppressions justified.

## Category / tags
build · dart, flutter, lint, static-analysis, code-quality

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-run-static-analysis\SKILL.md`. Only gemini-plugin holds it.
