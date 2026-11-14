# mcp-app-development

- Tool: `antigravity-builtin`
- Category: design
- Source: `C:\Users\a7med\.gemini\antigravity\builtin\skills\mcp-app-development\SKILL.md`
- SKILL.md size: 12777 chars

## What it does

>- Build, package, and debug MCP Apps for Antigravity: MCP server tools whose results render as interactive UI in the conversation, in the side pane, or full-page from the sidebar. Use when adding a UI to an MCP tool, building or theming the app itself, packaging it as a plugin, or debugging an app that doesn't render or behave as expected.

## Structure (headings inside SKILL.md)

- Developing MCP Apps
- Server side
- 1. Declare the UI resource
- 2. Point tools at it
- Renders the app inline in the conversation.
- Also openable from the side pane "+" menu and full-page from the left sidebar
- Only the app may call it; the model never sees it.
- 3. Tool results
- App side
- Lifecycle
- What the app can ask for
- Host context and theming
- Sandbox and CSP
- Packaging and iterating
- Debugging checklist
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP Apps, MCP App, MCP tool, MCP Servers

## Risks / cautions found in text

- - `resourceUri` must start with `ui://`, or the tool's UI metadata is dropped.

## Key rules (verbatim lines from SKILL.md)

1. - `resourceUri` must start with `ui://`, or the tool's UI metadata is dropped.

## Files inside the skill

- (SKILL.md only)
