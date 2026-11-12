# dart-migrate-to-checks-package (Flutter plugin)

## Summary
Migration workflow from `package:matcher` expectations to the type-safe `package:checks` library: add dev dep, swap `package:test/test.dart` for `test/scaffolding.dart` + `checks/checks.dart` (keep `test/expect.dart` import for incremental migration), translate assertions via the matcher→checks mapping table, and exploit the compiler — remove the legacy import and un-migrated `expect` calls surface as errors.

## When to use / when NOT
Use when asked to migrate tests to package:checks for static type safety, autocomplete, and literate failure output. Do NOT use for new tests written directly in checks style (just write them) or non-test code.

## Inputs, outputs, tools
- Inputs: test files with `expect`/`expectLater`.
- Outputs: migrated test files using `check()` syntax.
- Tools: `dart pub add dev:checks`, `dart analyze`, `dart test`; grep discovery patterns in the skill.

## 5 most important rules
1. THE critical pitfall: legacy `expect(actual, equals(coll))` did DEEP equality on collections; checks `.equals()` is identity — collections MUST use `.deepEquals()`.
2. Incremental path: keep `import 'package:test/expect.dart'` until fully migrated; removing it turns leftovers into compile errors (free checklist).
3. Replace the test import trio: scaffolding + checks (+expect.dart only while migrating).
4. Watch async: await check futures; `unawaited_futures` warnings flag missed awaits.
5. Verify with `dart analyze` then `dart test` — checks failure output is verbose and precise, use it to tell real failures from mistranslations.

## Risks / things needing the owner
Silent behavior changes if deep-equality cases are mistranslated — the mapping table exists because line-for-line ports can false-pass. Run the full suite after migrating.

## Category / tags
build · dart, testing, migration, checks

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-migrate-to-checks-package\SKILL.md`. Only gemini-plugin holds it.
