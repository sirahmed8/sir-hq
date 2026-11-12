# flutter-build-responsive-layout

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\flutter-build-responsive-layout\SKILL.md`
- SKILL.md size: 6805 chars

## What it does

Use `LayoutBuilder`, `MediaQuery`, or `Expanded/Flexible` to create a layout that adapts to different screen sizes. Use when you need the UI to look good on both mobile and tablet/desktop form factors.

## Structure (headings inside SKILL.md)

- Implementing Adaptive Layouts
- Contents
- Space Measurement Guidelines
- Widget Sizing and Constraints
- Device and Orientation Behaviors
- Workflow: Constructing an Adaptive Layout
- Workflow: Optimizing for Large Screens
- Examples
- Adaptive Layout using LayoutBuilder
- Constraining Width on Large Screens
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. *   **Do not use `MediaQuery.orientationOf` or `OrientationBuilder`** near the top of the widget tree to switch layouts. Device orientation does not accurately reflect the available app window space.
2. *   **Do not check for hardware types** (e.g., "phone" vs. "tablet"). Flutter apps run in resizable windows, multi-window modes, and picture-in-picture. Base all layout decisions strictly on available window space.
3. *   **Lazy Rendering:** Always use `ListView.builder` or `GridView.builder` when rendering lists with an unknown or large number of items.
4. *   **Do not lock screen orientation.** Locking orientation causes severe layout issues on foldable devices, often resulting in letterboxing (the app centered with black borders). Android large format tiers require both portrait and landscape support.
5. *   **Fallback for Locked Orientation:** If business requirements strictly mandate a locked orientation, use the `Display API` to retrieve physical screen dimensions instead of `MediaQuery`. `MediaQuery` fails to receive the larger window size in compatibility modes.

## Files inside the skill

- (SKILL.md only)
