# shader-graph-create-custom-node

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\shader-graph-create-custom-node\SKILL.md`
- SKILL.md size: 1176 chars

## What it does

Generates custom Shader Graph nodes from HLSL code. Use when the user wants a new Shader Graph node or to make existing HLSL work as a reflected function node.

## Structure (headings inside SKILL.md)

- Generating a custom Shader Graph node
- Step 1: Generate an HLSL function definition
- Step 2: Decorate with Shader Graph hint tags
- Step 3: Write the code to an asset
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - The function must be preceded by the preprocessor define `UNITY_EXPORT_REFLECTION`
2. - Required function hints:
3. - If a matching asset exists, show the user its current contents and ask for confirmation before appending the new code

## Files inside the skill

- `resources/all_hints.hlsl`
