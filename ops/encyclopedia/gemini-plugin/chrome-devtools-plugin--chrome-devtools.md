# chrome-devtools

- Tool: `gemini-plugin` (plugin: `chrome-devtools-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\chrome-devtools-plugin\skills\chrome-devtools\SKILL.md`
- SKILL.md size: 4164 chars

## What it does

Automate browsers.

## When to use (from skill text)

- 3. **Trigger Action**: Use `trigger_extension_action` to open the popup or side panel if applicable.
- 4. **Verify Service Worker**: Use `evaluate_script` with `serviceWorkerId` (omitting `pageId` and `args`) to check extension state or trigger background actions. When evaluating in a page, pass `pageId` (omitting `serviceWorkerId`).

## Structure (headings inside SKILL.md)

- Core Concepts
- Workflow Patterns
- Before interacting with a page
- Efficient data retrieval
- Tool selection
- Parallel execution
- Testing an extension
- Troubleshooting
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - For extension tooling, use the `--categoryExtensions` flag.
2. - For memory tooling, use the `--memoryDebugging` flag.
3. 1. Navigate: `navigate_page` or `new_page`

## Files inside the skill

- (SKILL.md only)
