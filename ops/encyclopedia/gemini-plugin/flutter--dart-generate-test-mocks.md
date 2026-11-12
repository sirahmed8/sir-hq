# dart-generate-test-mocks

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-generate-test-mocks\SKILL.md`
- SKILL.md size: 6339 chars

## What it does

Define and generate mock objects for external dependencies using `package:mockito` and `build_runner`. Use when unit testing classes that depend on complex external services like APIs or databases.

## Structure (headings inside SKILL.md)

- Testing and Mocking Dart Applications
- Contents
- Structuring Code for Testability
- Managing Dependencies
- Generating Mocks
- Implementing Unit Tests
- Workflow: Creating and Running Mocked Tests
- Task Progress
- Feedback Loop: Test Failures
- Examples
- High-Fidelity Mocking and Testing Example
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Import HTTP libraries with a prefix to avoid namespace collisions: `import 'package:http/http.dart' as http;`.
2. - Always use the `@GenerateNiceMocks` annotation (preferable to `@GenerateMocks` to avoid missing stub exceptions).
3. - **Stubbing:** Configure mock behavior before interacting with the system under test.
4. - **CRITICAL:** Always use `thenAnswer((_) async => value)` for methods returning a `Future` or `Stream`. Never use `thenReturn` for asynchronous returns.
5. - [ ] 7. Stub required behaviors using `when()`.

## Files inside the skill

- (SKILL.md only)
