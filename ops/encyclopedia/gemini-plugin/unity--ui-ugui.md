# ui-ugui (gemini-plugin: unity)

## Summary
ui-ugui understands, edits and generates Unity's Canvas-based uGUI hierarchies — the default runtime UI system. It covers three request types (understand a hierarchy, targeted edit, generate new Canvas UI) with strict scope rules (visual layout only unless "with code/logic/functional" is said). The technical core: every UI needs Canvas + CanvasScaler (Scale With Screen Size default, match 0.5) + GraphicRaycaster; Layout Groups (Vertical/Horizontal/Grid) control child sizing so manual anchors conflict — ContentSizeFitter on the same object as a Control-Child-Size Layout Group is a named conflict pattern; RectTransform anchoring order (preset → pivot matching anchor → offsets, verify non-zero size); component table (Image, RawImage, TMP text, Button, Toggle, Slider, ScrollRect, TMP InputField); interaction readiness checklist (exactly one EventSystem, GraphicRaycaster present, RaycastTarget correct, onClick wired only when logic requested); and ScrollRect setup delegated to references/scrollview-setup.md.

## When to use / when NOT
Use for Canvas/RectTransform/uGUI/prefab-UI requests — the default for new runtime/game UI when the user has no framework preference, and for mobile/performance/older-Unity projects. Do NOT use for UI Toolkit (.uxml/.uss → ui-uitk) or IMGUI editor tools (→ ui-imgui), and do not generate C# logic unless explicitly asked.

## Inputs, outputs, tools
- Inputs: UI request (layout, edit, fix) plus existing scene/prefab hierarchy to inspect first.
- Outputs: prefab or scene hierarchy edits, new Canvas structures, optionally scripts when requested.
- Tools: file writes to the Unity project; references/scrollview-setup.md for ScrollRect. Verification inside the Editor.

## 5 most important rules
1. Verify before modifying: read the hierarchy first, confirm parents/components exist, never assume state.
2. Incremental fixes over rebuilds — destroying hierarchies causes null-ref cascades; when a fix fails, revert before trying an alternative; one change at a time, no shotgun debugging.
3. Fully qualify UI types (`UnityEngine.UI.Image`) to avoid namespace ambiguity.
4. Honor exact user specs (pixel dims, hex colors, positions) precisely; minimize unrelated changes.
5. Interaction readiness: one EventSystem, GraphicRaycaster on Canvas, RaycastTarget true only on interactives — missing these fails silently.

## Risks / things needing the owner
Prefab/scene edits can break serialized references if objects are destroyed; the skill's core defense is surgical edits. TMP Essentials import must use `TMP_PackageResourceImporter.ImportResources()` — NEVER `EditorApplication.ExecuteMenuItem` (modal dialog blocks agents). CanvasScaler mode changes on existing canvases need user confirmation. Nothing else needs the owner.

## Category / tags
build · unity, ugui, canvas, layout, game-ui

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\unity\skills\ui-ugui\` with references/scrollview-setup.md. No divergent copies.
