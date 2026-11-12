# resize-for-social-media

- Tool: `gemini-plugin` (plugin: `canva`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\canva\skills\resize-for-social-media\SKILL.md`
- SKILL.md size: 5878 chars

## What it does

Resize a Canva design into multiple social media formats (Facebook post, Facebook story, Instagram post, Instagram story, LinkedIn post). Use this skill when users want to resize Canva designs specifically for multiple social media platforms in one operation, rather than resizing to a single format manually.

## Structure (headings inside SKILL.md)

- Canva Resize for Social Media
- Overview
- Workflow
- Step 1: Identify the Source Design
- Step 2: Retrieve Source Design Information
- Step 3: Ask Which Platforms and Formats
- Step 4: Resize to Selected Formats
- Step 5: Present Results with Edit Links
- Key Implementation Notes
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tools, MCP resize

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Extract the design ID from the URL (the part after `/design/` and before the next `/` or query parameter)
2. - **Compatibility**: Check if `resize-design` is available in the current MCP tools. If not, inform the user that this skill requires the Canva MCP resize tool in the current host
3. - **User confirmation**: Do not require user approval between steps - execute the full workflow automatically unless errors occur
4. - **Format accuracy**: Always use the exact pixel dimensions specified above for each platform

## Files inside the skill

- (SKILL.md only)
