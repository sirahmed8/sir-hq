# dart-collect-coverage (Flutter plugin)

## Summary
Guide for collecting Dart/Flutter test coverage: add `coverage` as a dev_dependency, run `dart run coverage:test_with_coverage` to produce `coverage/lcov.info` (+ raw coverage.json), use `// coverage:ignore-line|start|end|file` directives for intentional exclusions, and — for granular control — a manual workflow driving the VM service (`--pause-isolates-on-exit --enable-vm-service`) with `coverage:collect_coverage` and optional `--function-coverage`/`--branch-coverage`.

## When to use / when NOT
Use when measuring or reporting test coverage, wiring coverage into CI, or chasing missing coverage on specific files. Do NOT use as a substitute for writing the tests themselves (dart-add-unit-test) or for non-Dart projects.

## Inputs, outputs, tools
- Inputs: existing test suite; optional ignore directives in source.
- Outputs: `coverage/coverage.json` and `coverage/lcov.info` LCOV report.
- Tools: `coverage` package (`dart pub add dev:coverage` / `flutter pub add dev:coverage`), `dart run coverage:test_with_coverage`, manual `dart run --pause-isolates-on-exit ... test` + `coverage:collect_coverage`; in workspaces pass explicit test dirs.

## 5 most important rules
1. `coverage` goes in dev_dependencies only — never runtime deps.
2. Prefer the bundled `test_with_coverage` script; use the manual VM-service flow only when you need function/branch coverage or custom control.
3. Validate output: `coverage/` dir, `coverage.json`, `lcov.info` must exist.
4. Missing coverage on a file means it isn't imported/executed by tests — or add `// coverage:ignore-file` if intentionally excluded.
5. Enforce ignore directives with `--check-ignore` during formatting.

## Risks / things needing the owner
Coverage % can be gamed by ignore directives — review them in PRs. Branch/function coverage needs Dart VM 2.17+.

## Category / tags
build · dart, flutter, testing, coverage

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-collect-coverage\SKILL.md`. Only gemini-plugin holds it.
