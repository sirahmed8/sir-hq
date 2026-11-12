# dart-generate-test-mocks (Flutter plugin)

## Summary
Guide for mock-based unit testing in Dart: design for DI (inject `http.Client` etc. via constructors, URLs as `Uri`), declare `@GenerateNiceMocks([MockSpec<Dependency>()])` in the test file (NiceMocks preferred over GenerateMocks to avoid unstubbed-call exceptions), generate via `dart run build_runner build`, then stub with `when().thenReturn` for sync and **`thenAnswer((_) async => ...)` for Futures/Streams — never thenReturn on async**, and verify with `verify()`/argument matchers.

## When to use / when NOT
Use when unit-testing classes dependent on external services (APIs, databases, http clients). Do NOT use for widget tests that can use fakes, or for integration tests hitting real services.

## Inputs, outputs, tools
- Inputs: the class under test and its injected dependencies; pubspec dev deps (`test`, `mockito`, `build_runner`).
- Outputs: generated `*.mocks.dart`, passing mocked test suites.
- Tools: `package:mockito` + `build_runner`, `package:test`; `dart pub add dev:test dev:mockito dev:build_runner`; examples/ dir.

## 5 most important rules
1. Always `@GenerateNiceMocks`, never `@GenerateMocks` — unstubbed calls on strict mocks throw.
2. CRITICAL: `thenAnswer` for any Future/Stream-returning method; `thenReturn` on async throws ArgumentError.
3. Inject dependencies through constructors; represent URLs as `Uri.parse` objects.
4. Import http with a prefix (`as http`) to avoid namespace collisions.
5. After build_runner, check `.mocks.dart` import matches the file name exactly; fix loop = run → review errors → fix → repeat.

## Risks / things needing the owner
Over-mocking tests implementation details; mocks drift from real API changes. Generated files must be regenerated after interface changes.

## Category / tags
build · dart, flutter, testing, mockito, unit-tests

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-generate-test-mocks\SKILL.md`. Only gemini-plugin holds it.
