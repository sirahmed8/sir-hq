# ui (gemini-plugin: unity router)

## Summary
`ui` is the Unity plugin's ROUTER skill, not a framework skill itself. Its job: decide which of Unity's three UI systems a request belongs to and hand off to the right specialist skill (`ui-uitk`, `ui-ugui`, `ui-imgui`), or answer comparative/educational questions directly without routing. Routing is three-stepped: (1) explicit signals — `.uxml`/`.uss` files or "UI Toolkit/UITK/UIElements/CreateGUI" → ui-uitk; Canvas/RectTransform/uGUI → ui-ugui; OnGUI/OnInspectorGUI/IMGUI → ui-imgui; a Figma URL gets a honest "automated Figma import is not available here" plus an offer to build from description/screenshot; (2) project detection when ambiguous — search for uxml/uss files, UIDocument components, CreateGUI editor scripts, Canvas/RectTransform usage, OnGUI editor scripts; (3) defaults — existing projects follow whatever is in use, new runtime UI defaults to uGUI, new editor UI defaults to UI Toolkit, mobile/performance/pre-Unity-6 leans uGUI.

## When to use / when NOT
Use BEFORE writing any Unity UI code when the framework isn't named, and for UI comparison questions. Do NOT use it to actually write UI (it delegates), and do NOT route educational questions ("UITK vs uGUI?") — answer those directly.

## Inputs, outputs, tools
- Inputs: the user's UI request, project file search results.
- Outputs: a routing decision plus handoff to the correct sub-skill; or a direct conceptual answer.
- Tools: file/content search across the Unity project (uxml, uss, UIDocument, Canvas, OnGUI patterns). No scripts.

## 5 most important rules
1. Explicit file/keyword signals beat everything; detect project patterns before asking.
2. Figma import does not exist outside Unity AI Assistant — never promise it; offer description/screenshot-based rebuild instead.
3. Mixed projects are normal: route runtime UI to the runtime system in use; new EDITOR UI prefers UI Toolkit (CreateGUI), IMGUI only for legacy/exclusive-IMGUI projects.
4. Scope discipline applies to all sub-skills: a question gets an answer, a targeted edit changes only what was asked, "proper buttons" means styled buttons not scripts.
5. When still unclear on a new project, ask the user which framework — briefly explaining UITK is modern/CSS-like and uGUI is Canvas-based/mature.

## Risks / things needing the owner
Low risk; it is a decision layer. The main trap is misrouting (sending uGUI work to UITK or vice versa), which the detection step exists to prevent. Asking the user for framework preference is one of the few legitimate questions this skill allows.

## Category / tags
build · unity, ui, routing, uxml, ugui, imgui

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\unity\skills\ui\SKILL.md`. No divergent copies.
