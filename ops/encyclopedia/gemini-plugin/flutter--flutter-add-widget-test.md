# flutter-add-widget-test

## Summary
Guide for component-level Flutter widget tests with `WidgetTester`: dev-depend on `flutter_test`, place `*_test.dart` files under `test/`, then follow the pumpWidget → Finder → expect → interact → pump/pumpAndSettle → re-assert loop. Documents the core trio (WidgetTester auto-provided by `testWidgets()`, Finder via `find.text`/`byType`/`byKey`, Matchers like `findsOneWidget`/`findsNothing`/`findsNWidgets`/`matchesGoldenFile`), conditional guidance for static renders vs state changes vs animations/transitions vs text input vs lazy long lists (`scrollUntilVisible`), and a full TodoList worked example covering enterText, tap, drag-dismiss, pumpAndSettle.

## When to use / when NOT
Use to validate that a specific widget renders correct data and responds to taps/scrolls/text input — fast, no device needed. Do NOT use for full-app flows (use flutter-add-integration-test) or pure logic (use dart-add-unit-test).

## Inputs, outputs, tools
- Inputs: widget under test, flutter_test dependency, test file in test/.
- Outputs: `test/*_test.dart` files passing under `flutter test`.
- Tools: `testWidgets`, `WidgetTester` (pumpWidget, pump, pumpAndSettle, tap, drag, enterText, scrollUntilVisible), `find.*` finders, `expect` matchers incl. golden files.

## 5 most important rules
1. Wrap widgets needing inherited data in MaterialApp or Directionality inside pumpWidget — bare widgets crash without Directionality.
2. `pump()` rebuilds a single frame after state changes; `pumpAndSettle()` is required after animations/transitions or drags until no frames are scheduled — picking the wrong one is the #1 flaky-test cause.
3. Locate by stable finders (byKey > byType > byText); text finders break on copy changes, type finders break on refactors.
4. Lazy lists: call `scrollUntilVisible(itemFinder, delta, scrollable: listFinder)` before interacting — off-screen items don't exist in the tree.
5. Always end with the feedback loop: run `flutter test <file>`, read failing matchers, fix widget or assertion, re-run until green.

## Risks / owner needs
Golden-file tests (`matchesGoldenFile`) are font/platform-sensitive — regenerating goldens on a different OS produces false diffs; keep goldens platform-pinned. Widget tests mock nothing by default: real async work inside widgets needs `tester.runAsync` or fake_async awareness.

## Category and tags
Category: mobile. Tags: flutter, widget-testing, flutter-test, tdd, dart.

## Revisions
Single gemini-plugin flutter copy; no competing revisions.
