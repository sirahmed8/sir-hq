# flutter-add-widget-test

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\flutter-add-widget-test\SKILL.md`
- SKILL.md size: 6381 chars

## What it does

Implement a component-level test using `WidgetTester` to verify UI rendering and user interactions (tapping, scrolling, entering text). Use when validating that a specific widget displays correct data and responds to events as expected.

## When to use (from skill text)

- 2. Call `await tester.pump()` to trigger a single frame rebuild.
- 1. Trigger the action (e.g., `await tester.drag(finder, Offset(500, 0))`).

## Structure (headings inside SKILL.md)

- Writing Flutter Widget Tests
- Contents
- Setup & Configuration
- Core Components
- Workflow: Implementing a Widget Test
- Task Progress
- Interaction & State Management
- Examples
- High-Fidelity Widget Test Implementation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - [ ] **Step 2: Build the widget.** Call `await tester.pumpWidget(MyWidget())` to render the UI. Wrap the widget in a `MaterialApp` or `Directionality` widget if it requires inherited directional or theme data.
2. - [ ] **Step 7: Verify updated state.** Use `expect()` to validate the UI after the interaction.
3. *   **If testing items in a dynamic or long list:** Call `await tester.scrollUntilVisible(itemFinder, 500.0, scrollable: listFinder)` to ensure the target widget is rendered before interacting with it.

## Files inside the skill

- (SKILL.md only)
