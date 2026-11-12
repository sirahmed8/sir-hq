# compose-preview

- Tool: `gemini-plugin` (plugin: `android-cli-plugin`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\android-cli-plugin\skills\compose-preview\SKILL.md`
- SKILL.md size: 12833 chars

## What it does

Render and review Jetpack Compose @Preview.

## Structure (headings inside SKILL.md)

- Android Compose Preview Skill
- Rendering previews
- Arguments
- Finding the server
- HTTP API
- Files
- Reading the component tree
- Guidelines
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 1. **The server info file**, written when the server starts and deleted when it stops:

## Key rules (verbatim lines from SKILL.md)

1. 4. **After changing the code** of a rendered preview, **re-render** with `POST /api/render` and `"wait": true`, **only after
2. - `POST /api/render` `{"wait": true}`: re-renders all the previews of the current session (e.g. after changing code). If a
3. 2. After each render, report failures with the relevant `output` lines instead of silently retrying.

## Files inside the skill

- (SKILL.md only)
