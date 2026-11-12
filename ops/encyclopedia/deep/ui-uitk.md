# ui-uitk (gemini-plugin: unity)

## Summary
ui-uitk understands, edits and generates Unity UI Toolkit (UIElements) UXML/USS — the modern CSS-like UI system for runtime game UI (Unity 6+) and editor tools. It defines an understanding format (tree diagrams of elements), edit rules (change only what's asked, preserve formatting), a generation matrix (USS only / UXML only / screen = uxml+uss / "with code" adds .cs), naming conventions (camelCase `name`, kebab-case classes), a strict USS restriction table (no `border` shorthand, `gap`, `z-index`, `pointer-events`, gradients, attribute selectors, inline `style=""`, external `url()` — use `project://database/` paths), brevity rules, UXML requirements (namespace declaration, Style link, one root, no inline styles), event handling via Pointer Manipulators, asset/icon priority (reuse → generate SVG → image gen last), PanelSettings requirement, and TextCore (not TMP) types for C#. Eight reference files cover USS patterns, SVG icons, common issues, runtime binding, Painter2D, pointer manipulators, and custom elements.

## When to use / when NOT
Use for .uxml/.uss/UIDocument/PanelSettings/UIElements/CreateGUI requests and for NEW editor UI. Do NOT use for uGUI Canvas work (ui-ugui) or IMGUI (ui-imgui); route through the `ui` skill when the framework is unclear.

## Inputs, outputs, tools
- Inputs: UI request plus existing UXML/USS/project assets to match.
- Outputs: complete `.uxml`/`.uss` files (and `.cs` only when logic requested), PanelSettings asset if missing.
- Tools: file writes; references for deep topics. No external services.

## 5 most important rules
1. USS is a SUBSET of CSS — the banned-properties table is absolute; gradients need a custom VisualElement with Painter2D.
2. NEVER write partial/draft UXML — Unity parses on import and a half file is a parse error; finish ALL files before asking the user to check the Console (each round-trip costs a reimport).
3. No inline `style=""` in UXML and no external URLs; all styling lives in USS with `project://database/` asset paths.
4. C# styling goes through USS classes (`AddToClassList()`), never `element.style.*` (higher specificity, unoverridable, memory cost); use TextCore types not TMP.
5. PanelSettings is required for runtime UI to render; assign it to the UIDocument.

## Risks / things needing the owner
No external validation exists — Unity only reports UXML/USS errors in the Console after the user focuses the Editor, so the workflow depends on user round-trips; mistakes that parse but render wrong never appear in Console and need eyeballing (common-issues.md lists them). Draggable inventory/crafting systems need Pointer Manipulators — ask before assuming. Nothing else needs the owner.

## Category / tags
build · unity, ui-toolkit, uxml, uss, game-ui, editor-tools

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\unity\skills\ui-uitk\` with eight reference docs. No divergent copies.
