# ui-imgui (gemini-plugin: unity)

## Summary
ui-imgui generates and modifies Unity IMGUI code — the legacy immediate-mode GUI used for EditorWindows, custom Inspectors (`Editor`/`PropertyDrawer`) and runtime `OnGUI` debug overlays. It is explicitly scoped to LEGACY code: the skill opens by telling the agent to recommend UI Toolkit (CreateGUI) instead for any NEW editor window/inspector unless the user explicitly asks for IMGUI or the project is IMGUI-exclusive. Content covers the three script shapes (EditorWindow with MenuItem+ShowWindow+OnGUI, CustomEditor with OnInspectorGUI+SerializedProperty caching, PropertyDrawer with OnGUI+GetPropertyHeight), hard rules (never allocate GUIStyle inside OnGUI, always use SerializedProperty/ApplyModifiedProperties for undo, EditorGUILayout for editor vs GUILayout for runtime, matched Begin/End pairs, Editor folder is mandatory or the build fails), layout patterns (BeginHorizontal/Vertical, scroll views, foldouts, disabled groups) and naming/folder conventions. References: templates.md and gui-elements.md.

## When to use / when NOT
Use when maintaining existing OnGUI/OnInspectorGUI code, when the user explicitly requests IMGUI, or when the project exclusively uses IMGUI for editor tools. Do NOT use for new editor UI (use ui-uitk), for runtime game UI (use ui-uitk or ui-ugui), or for any request that doesn't mention IMGUI — clarify which UI system first.

## Inputs, outputs, tools
- Inputs: the requested editor tool/debug overlay or existing IMGUI file to modify.
- Outputs: `.cs` files under an `Editor/` folder (EditorWindow/Editor/PropertyDrawer/MonoBehaviour debug overlay), or targeted edits to existing OnGUI code.
- Tools: none beyond file writes; references/templates.md and gui-elements.md carry the boilerplate. Verification happens inside the Unity Editor.

## 5 most important rules
1. Default-deny for new work: push UI Toolkit for new editor windows/inspectors unless IMGUI is explicitly requested or the project is IMGUI-only.
2. Scripts using `UnityEditor` MUST live in an `Editor` folder or the build fails.
3. Never create GUIStyle inside OnGUI (per-frame allocation); cache styles.
4. Use SerializedObject/SerializedProperty with ApplyModifiedProperties for undo/redo; Undo.RecordObject for direct changes.
5. Match every Begin* with its End*; use EditorGUILayout in editor code and GUILayout in runtime OnGUI.

## Risks / things needing the owner
Legacy tech debt: IMGUI editor tools look dated and don't scale; writing new ones is discouraged by the skill itself. Naming conventions must match the project (search existing editor scripts first). Requires Unity Editor to verify. Nothing needs the owner.

## Category / tags
build · unity, imgui, editor-tools, legacy, csharp

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\unity\skills\ui-imgui\` with references/. No divergent copies.
