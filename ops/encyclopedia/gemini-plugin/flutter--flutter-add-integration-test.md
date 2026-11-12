# flutter-add-integration-test

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\flutter-add-integration-test\SKILL.md`
- SKILL.md size: 7342 chars

## What it does

Configures Flutter Driver for app interaction and converts MCP actions into permanent integration tests. Use when adding integration testing to a project, exploring UI components via MCP, or automating user flows with the integration_test package.

## When to use (from skill text)

- - **Wait**: Always execute `waitFor` or verify state with `get_health` when navigating or triggering animations.
- - Trigger frames and wait for animations to complete using `await tester.pumpAndSettle();` after interactions like `tester.tap()`.
- // Trigger a frame and wait for animations.

## Structure (headings inside SKILL.md)

- Implementing Flutter Integration Tests
- Contents
- Project Setup and Dependencies
- Interactive Exploration via MCP
- Test Authoring Guidelines
- Execution and Profiling
- Workflow: End-to-End Integration Testing
- Examples
- Standard Integration Test (`integration_test/app_test.dart`)
- Host Driver Script (`test_driver/integration_test.dart`)
- Performance Profiling Driver Script (`test_driver/perf_driver.dart`)
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP tools

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1. Add required development dependencies to `pubspec.yaml`:
2. - Call `enableFlutterDriverExtension();` before `runApp()`.
3. - **Wait**: Always execute `waitFor` or verify state with `get_health` when navigating or triggering animations.
4. - **Troubleshoot Unmounted Widgets**: If a widget is not found in the tree, it may be lazily loaded in a `SliverList` or `ListView`. Execute `scroll` or `scrollIntoView` to force the widget to mount before interacting with it.
5. - Trigger frames and wait for animations to complete using `await tester.pumpAndSettle();` after interactions like `tester.tap()`.

## Files inside the skill

- (SKILL.md only)
