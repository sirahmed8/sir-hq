# dart-add-unit-test (Flutter plugin)

## Summary
Guide for writing Dart/Flutter unit tests with `package:test` (or `flutter_test`): mirror the `lib/` structure under `test/` with `_test.dart` suffixes, use `group()`/`test()`/`expect()` with matchers, `setUp()`/`tearDown()`, async tests via plain async/await, `package:mockito` for DI-based code, and run `dart test` or `flutter test` (integration tests need the explicit `integration_test` path).

## When to use / when NOT
Use when creating new logic or fixing bugs that need regression coverage. Do NOT use for widget/golden testing specifics (broader flutter_test territory) or e2e device tests beyond pointing at the integration_test folder.

## Inputs, outputs, tools
- Inputs: the code under test, existing test conventions.
- Outputs: test files under `test/`, passing `dart test`/`flutter test` runs.
- Tools: `package:test`, `flutter_test`, `package:mockito`; CLI `dart test`, `flutter test`; a 7-step checklist workflow ending in a fix-rerun loop.

## 5 most important rules
1. Test files mirror `lib/` and always end `_test.dart`; integration tests live in `integration_test/` and need the explicit path argument.
2. Group related cases with `group()`, give each a `test()`, assert with `expect()` + matchers (`equals`, `isTrue`, `throwsA`).
3. Async tests are just `async` test bodies — the runner waits for the Future.
4. Use `setUp()`/`tearDown()` for shared fixtures; use mockito only for injected dependencies.
5. Feedback loop is mandatory: run → read stack trace → fix implementation or assertions → rerun until green.

## Risks / things needing the owner
None operational; tests must reflect real behavior — don't write tests that merely mirror implementation bugs.

## Category / tags
build · dart, flutter, testing, unit-tests

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-add-unit-test\SKILL.md` (with examples/ dir). Only gemini-plugin holds it.
