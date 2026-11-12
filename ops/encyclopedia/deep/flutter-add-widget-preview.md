# flutter-add-widget-preview

## Summary
Guide for adding interactive widget previews via Flutter's `previews.dart` system (`@Preview` annotation from `package:flutter/widget_previews.dart`). Previews render widgets in isolation in a web-based Widget Previewer — no full app context. Covers valid targets (top-level functions, static methods, public parameterless widget constructors returning Widget/WidgetBuilder), preview parameters (name, group, size, textScaleFactor, wrapper, theme via PreviewThemeData, brightness, localizations), custom `Preview`/`MultiPreview` subclasses with `transform()` for runtime-generated configs, and the launch/iteration loop (IDE sidebar tab or `flutter widget-preview start` → Chrome; hot restart buttons for global vs per-preview state).

## When to use / when NOT
Use when creating new UI components or updating screens so design/behavior can be previewed and interactively tested in isolation. Do NOT use as a substitute for widget tests or screenshots in CI — the previewer is a dev tool, not an assertion harness.

## Inputs, outputs, tools
- Inputs: widget code, preview annotation config, IDE (Android Studio/IntelliJ/VS Code w/ Flutter 3.47+) or CLI.
- Outputs: annotated preview functions, `.widget_preview/` build cache, previewer session.
- Tools: `package:flutter/widget_previews.dart`, `flutter widget-preview start`, PreviewThemeData subclasses, MultiPreview.

## 5 most important rules
1. `@Preview` targets must be top-level functions, static methods, or public constructors with NO required arguments returning Widget/WidgetBuilder; callbacks passed to annotations must be public and const.
2. Web-environment constraints: no `dart:io`/`dart:ffi`/native plugins (use conditional imports to stub), assets must use package paths (`packages/pkg/assets/x.png`), unconstrained widgets need explicit `size`.
3. Always import `package:flutter/widget_previews.dart`; extract repeated config into custom Preview/MultiPreview classes instead of duplicating annotations.
4. `transform()` overrides enable runtime-dynamic names/config impossible in const constructors — build via `toBuilder()`/`build()`.
5. Iteration: code change → auto-update; global hot restart for static-initializer changes, per-card hot restart for local state; check IDE/CLI console for errors.

## Risks / owner needs
Previews run web-only — platform-specific behavior (native plugins, real assets) won't show; don't trust a green preview as proof of device behavior. `.widget_preview/` cache folder is generated, not source.

## Category and tags
Category: mobile. Tags: flutter, widget-preview, ui, design-review, dart, dev-tooling.

## Revisions
Single gemini-plugin flutter copy; no competing revisions.
