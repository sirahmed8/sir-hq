# ui

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\ui\SKILL.md`
- SKILL.md size: 6717 chars

## What it does

Routes Unity UI requests to the right framework skill (UI Toolkit, uGUI, or IMGUI) and answers UI comparison questions. Use for menus, HUDs, panels, or editor UI when the request doesn't name a framework. Consult before writing any UI code.

## When to use (from skill text)

- - Only use when project has existing IMGUI editor code or user explicitly requests IMGUI

## Structure (headings inside SKILL.md)

- When to Route vs Answer Directly
- Routing Logic
- Request Types
- Available Sub-Skills
- UI Toolkit — `ui-uitk`
- uGUI — `ui-ugui`
- IMGUI — `ui-imgui`
- Figma design import — not available here
- Common Guidelines (All UI Systems)
- Scope Discipline
- Conventions
- Workflow
- Handling Mixed Projects
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Only use `ui-imgui` if project exclusively uses IMGUI or user explicitly requests it
2. - Only use when project has existing IMGUI editor code or user explicitly requests IMGUI
3. - Don't proactively add scripts unless explicitly asked
4. - Only use IMGUI if the project's existing editor tools use IMGUI exclusively, or user explicitly requests IMGUI

## Files inside the skill

- (SKILL.md only)
