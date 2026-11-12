# ui-imgui

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\ui-imgui\SKILL.md`
- SKILL.md size: 6440 chars

## What it does

Generates and modifies Unity IMGUI editor code such as EditorWindows, custom Inspectors, PropertyDrawers, and OnGUI scripts. Use for IMGUI or OnGUI or maintaining existing IMGUI code.

## When to use (from skill text)

- ## When to Use This Skill
- **IMPORTANT:** This skill is for **legacy IMGUI code only**. Use this skill when:
- **Do NOT use this skill for:**

## Structure (headings inside SKILL.md)

- When to Use This Skill
- Scope
- Conventions
- Workflow
- Script Structure
- EditorWindow
- Custom Editor
- PropertyDrawer
- Key Rules
- Layout Basics
- Common Patterns
- Best Practices
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Requests that don't explicitly mention IMGUI or OnGUI
2. - **Cache GUIStyle objects** — never create new GUIStyle in OnGUI (causes memory allocation every frame)
3. - **Call ApplyModifiedProperties()** — after any serialized object changes
4. - **Begin/End pairs** — always match BeginHorizontal with EndHorizontal, etc.
5. - **Editor folder required** — scripts fail to build if not in Editor folder

## Files inside the skill

- `references/gui-elements.md` — "IMGUI Elements and Layout"
- `references/templates.md` — "IMGUI Templates"
