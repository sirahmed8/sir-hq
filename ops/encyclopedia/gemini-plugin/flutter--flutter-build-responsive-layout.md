# flutter-build-responsive-layout

## Summary
Guide for adaptive Flutter layouts driven by actual window space, not device type. Core doctrine: measure with `MediaQuery.sizeOf(context)` for the whole app window and `LayoutBuilder` + `constraints.maxWidth` for the parent's allocated space; never branch on `MediaQuery.orientationOf`/`OrientationBuilder` near the tree root or on hardware type ("phone" vs "tablet") because Flutter runs in resizable windows, multi-window and PiP. Reminds the layout law "constraints go down, sizes go up, parent sets position"; space distribution via Expanded (tight fit) vs Flexible (fit up to limit, flex ratios); constrain wide content with ConstrainedBox maxWidth + Center; lists via ListView/GridView.builder only; `SliverGridDelegateWithMaxCrossAxisExtent` for auto column counts. Operational rules: never lock orientation (foldables letterbox; Android large-format tiers require both orientations — if business mandates it, use the Display API for physical size since MediaQuery fails in compatibility mode); support mouse/trackpad/keyboard; touch targets sized for all inputs.

## When to use / when NOT
Use when a UI must look right on mobile AND tablet/desktop/foldable/large-screen form factors. Not for single-form-factor apps or when the question is fixing an existing overflow (use flutter-fix-layout-issues).

## Inputs, outputs, tools
- Inputs: target widget, breakpoint choice, content type (list vs form/text).
- Outputs: LayoutBuilder-driven widget trees, ConstrainedBox/GridView adjustments.
- Tools: LayoutBuilder, MediaQuery.sizeOf, Expanded/Flexible/flex, ConstrainedBox/BoxConstraints, Center, ListView/GridView.builder, SliverGridDelegateWithMaxCrossAxisExtent, Display API (locked-orientation fallback).

## 5 most important rules
1. Layout decisions key off `constraints.maxWidth` inside LayoutBuilder — the app window, not the device; define an explicit breakpoint (e.g. 600) and return different trees per side.
2. Never use OrientationBuilder/orientation checks near the root, and never branch on hardware type — resizable windows and foldables break both.
3. Do not lock screen orientation; if forced, use Display API physical dimensions because MediaQuery misreports in compatibility mode.
4. Full-width components on large screens get constrained: wrap in ConstrainedBox(maxWidth) + Center, or convert ListView.builder → GridView.builder with MaxCrossAxisExtent for auto columns.
5. Lazy rendering always: ListView.builder/GridView.builder for unknown/large item counts; verify by resizing the window and checking overflow errors.

## Risks / owner needs
Orientation lock is sometimes a product requirement — that's an owner/product decision, not a layout detail; document it. Breakpoint choices affect all form factors; test on real resize, not just one device size.

## Category and tags
Category: mobile. Tags: flutter, responsive-layout, adaptive-ui, constraints, large-screens, foldables.

## Revisions
Single gemini-plugin flutter copy; no competing revisions.
