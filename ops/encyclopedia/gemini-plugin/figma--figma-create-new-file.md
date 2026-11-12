# figma-create-new-file

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-create-new-file\SKILL.md`
- SKILL.md size: 1764 chars

## What it does

Always use this skill when the user wants to.

## Structure (headings inside SKILL.md)

- Create a new file in Figma
- Step 1: Resolve the `planKey` and `editorType`
- Step 2: Call create_new_file
- Step 3: (Slides only) Handle the empty grid
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tool

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - `fileName`: Required. Choose a concise name if the user does not provide one.
2. - `planKey`: Required. Use the `planKey` resolved in Step 1.
3. - `editorType`: Required. Use the `editorType` selected in Step 1.

## Files inside the skill

- (SKILL.md only)
