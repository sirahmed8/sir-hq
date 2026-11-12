# figma-spec

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-spec\SKILL.md`
- SKILL.md size: 5954 chars

## What it does

Read, create, review, and comment on.

## Structure (headings inside SKILL.md)

- Work with a Figma spec
- Discover and choose the Figma spec
- Create a Figma spec on a canvas
- Content methods
- Critical rules
- Style
- Images
- Comments
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Use destructive **`setContent`** only for an empty first draft or an explicit whole-document replacement.

## Key rules (verbatim lines from SKILL.md)

1. - Use **`getContent`** with the same `specNodeId` before edits and to verify writes; DON'T rely on screenshots.
2. 1. **`editContent` requires exactly one match.** Zero or multiple `oldText` matches fail without changes. Add surrounding context to make it unique.
3. 2. **Pass Markdown as plain strings.** Never encode it with `Buffer`/base64 or decode it with `atob()`. Base64 is only for image data URLs inside Markdown.
4. 5. **Use portable references.** Shared Figma specs must use links such as GitHub permalinks, never machine-local paths or `localhost` URLs.
5. - Keep the title block first and formatted as H1, even when its text is empty. Never remove it or insert blocks before it.

## Files inside the skill

- (SKILL.md only)
