# chrome-devtools

- Tool: `codex`
- Category: research
- Source: `C:\Users\a7med\.codex\skills\chrome-devtools\SKILL.md`
- SKILL.md size: 4345 chars

## What it does

Uses Chrome DevTools via MCP for efficient debugging, troubleshooting and browser automation. Use when debugging web pages, automating browser interactions, analyzing performance, or inspecting network requests. This skill does not apply to `--slim` mode (MCP configuration).

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
