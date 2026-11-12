# ui-uitk

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\ui-uitk\SKILL.md`
- SKILL.md size: 10960 chars

## What it does

Understands, edits, and generates Unity UI Toolkit UXML and USS with flex layouts. Use for requests involving UI Toolkit, UIElements, UIDocument, PanelSettings, custom elements, or UI runtime binding.

## When to use (from skill text)

- When explaining UI structure, use this format:
- 2. Ask the user to focus the Unity Editor. That triggers a reimport of the changed

## Structure (headings inside SKILL.md)

- References
- Understanding
- Editing
- Validation
- Generation
- Conventions
- USS Restrictions
- USS Brevity
- UXML
- Events and Interactivity
- Assets
- Scene Setup
- C# (Only When Requested)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - [references/pointermanipulator-guide.md](references/pointermanipulator-guide.md) — Patterns and guide to create and use Manipulators (only when requested or when manipulators are involved). This helps with setting up drag and drop features or simple event handling for a Visual Element.
- - Be careful not to accidentally drop existing elements, styles, or references when making edits
- - **Ensure text is readable by default:** When choosing colors, ensure text contrasts with its background — but respect intentional low-contrast uses (disabled states, placeholder text, decorative elements). When using design tokens, check that text and background variables provide adequate contrast
- - If drag and drop is requested then write a pointer Manipulator and attach it to the relevant Visual Element in UXML or via C#.

## Key rules (verbatim lines from SKILL.md)

1. - [references/common-issues.md](references/common-issues.md) — Common mistakes to avoid
2. - Don't "improve" unrelated code
3. - Don't add comments unless asked
4. - **When editing USS**, focus on the properties and selectors relevant to the request — avoid unnecessary reorganization, but restructure if the change genuinely requires it
5. 1. Write the complete file to its target path in the project. Do not write partial or

## Files inside the skill

- `references/common-issues.md` — "Common USS/UXML Issues"
- `references/custom-elements.md` — "Custom VisualElements in UI Toolkit"
- `references/painter2d.md` — "Custom Visuals with Painter2D"
- `references/pointermanipulator-guide.md` — "UI Toolkit Manipulator Reference"
- `references/svg-icons.md` — "SVG Icon Generation (Unity 6.3+)"
- `references/ui-runtime-binding.md` — "Runtime Data Binding Reference"
- `references/uss-guide.md` — "USS Patterns and Examples"
