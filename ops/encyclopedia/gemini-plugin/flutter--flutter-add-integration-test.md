# flutter-add-integration-test

## Summary
End-to-end guide for adding Flutter integration tests: add `integration_test`+`flutter_test` dev deps, inject `enableFlutterDriverExtension()` before `runApp()`, tag widgets with `ValueKey`s, optionally explore the live app via the Dart/Flutter MCP server (`launch_app` on `lib/main_test.dart`, `get_widget_tree`, `tap`, `enter_text`, `scroll`, `waitFor`, `scrollIntoView` for lazily-mounted slivers), then author `integration_test/*_test.dart` files with `IntegrationTestWidgetsFlutterBinding`, `pumpWidget`, `pumpAndSettle`, `find.byKey`/`scrollUntilVisible` assertions, plus a `test_driver/` host script calling `integrationDriver()`. Runs via `flutter drive` on Chrome (`chromedriver --port=4444 -d chrome`), headless web (`-d web-server`), Android locally, or Firebase Test Lab via debug+androidTest APKs. Includes a perf-profiling driver variant using `traceAction`/`TimelineSummary`.

## When to use / when NOT
Use when adding integration/E2E testing or converting explored MCP actions into permanent tests. Do NOT use for unit/widget tests (other flutter skills) — this is full-app driving, slow and device-bound.

## Inputs, outputs, tools
- Inputs: pubspec.yaml, app entry point, target widgets, MCP tool session.
- Outputs: integration_test/*.dart tests, test_driver/*.dart hosts, APKs for Test Lab, timeline summaries for perf tests.
- Tools: flutter pub/drive/build, chromedriver, gradlew assembleAndroidTest, Firebase Test Lab console, Dart/Flutter MCP (`launch_app`, `get_widget_tree`, `tap`, `enter_text`, `scroll`, `scrollIntoView`, `waitFor`, `get_health`).

## 5 most important rules
1. `IntegrationTestWidgetsFlutterBinding.ensureInitialized()` must be first in test main(); app loaded via `pumpWidget`, then `pumpAndSettle()` after every interaction.
2. Target widgets by `ValueKey` (e.g. `ValueKey('login_button')`), never by position or text alone; add keys to app code as part of setup.
3. `flutter drive` requires a host script `test_driver/integration_test.dart` with `integrationDriver()`; perf tests need a custom driver with `responseDataCallback` writing `scrolling_timeline`.
4. Widgets not found are usually lazily mounted in SliverList/ListView — `scroll`/`scrollIntoView` before interacting; `PumpAndSettleTimedOutException` means an infinite animation.
5. Legacy `flutter_driver` tests keep `driver.waitFor/tap/scroll` APIs — conditional, don't mix paradigms in one file.

## Risks / owner needs
Integration tests need a real device/emulator or Chrome+chromedriver; Firebase Test Lab path requires manual console upload. Adding `enableFlutterDriverExtension()` to main.dart ships test hooks in release builds — gate it or use a separate `main_test.dart` entry point.

## Category and tags
Category: mobile. Tags: flutter, integration-testing, e2e, flutter-driver, widget-keys, firebase-test-lab, mcp.

## Revisions
Single gemini-plugin flutter copy; no competing revisions.
