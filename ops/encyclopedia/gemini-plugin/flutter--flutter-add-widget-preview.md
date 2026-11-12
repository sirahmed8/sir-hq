# flutter-add-widget-preview

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\flutter-add-widget-preview\SKILL.md`
- SKILL.md size: 7987 chars

## What it does

Adds interactive widget previews to the project using the previews.dart system. Use when creating new UI components or updating existing screens to ensure consistent design and interactive testing.

## Structure (headings inside SKILL.md)

- Previewing Flutter Widgets
- Contents
- Preview Guidelines
- Preview Parameters
- Handling Limitations
- Workflows
- Creating a Widget Preview
- Interacting with Previews
- Examples
- Basic Preview
- Custom Preview with PreviewThemeData and Transformation
- MultiPreview Implementation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Target Elements:** Apply the `@Preview` annotation to top-level functions, static methods within a class, or public widget constructors/factories that have no required arguments and return a `Widget` or `WidgetBuilder`.
2. - **Imports:** Always import `package:flutter/widget_previews.dart` to access the preview annotations.
3. - **No Native APIs:** Do not use native plugins or APIs from `dart:io` or `dart:ffi`. Widgets with transitive dependencies on `dart:io` or `dart:ffi` will throw exceptions upon invocation. Use conditional imports or wrappers to mock or bypass these in preview mode.
4. - **Asset Paths:** Use package-based paths for assets loaded via `dart:ui` `fromAsset` APIs (e.g., `packages/my_package_name/assets/my_image.png` instead of `assets/my_image.png`).

## Files inside the skill

- (SKILL.md only)
