# troubleshooting

- Tool: `gemini-plugin` (plugin: `chrome-devtools-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\chrome-devtools-plugin\skills\troubleshooting\SKILL.md`
- SKILL.md size: 6978 chars

## What it does

Troubleshoot Chrome DevTools MCP connection.

## When to use (from skill text)

- You are acting as a troubleshooting wizard to help the user configure and fix their Chrome DevTools MCP server setup. When this skill is triggered (e.g., because `list_pages`, `new_page`, or `navigate_page` failed, or the server wouldn't start), follow this step-by-step diagnostic process:

## Structure (headings inside SKILL.md)

- Troubleshooting Wizard
- Step 1: Find and Read Configuration
- Step 2: Triage Common Connection Errors
- Step 3: Read Known Issues
- Step 4: Formulate a Configuration
- Step 5: Run Diagnostic Commands
- Step 6: Check GitHub for Existing Issues
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP configuration, MCP client, MCP initialization, mcp --search

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 3. **Once the user confirms both steps, your only next action should be to call the `list_pages` tool.** This is the simplest and safest way to verify if the connection is now successful. Do not retry the original, more complex command yet.
2. - **Check for flag typos:** For example, `--autoBronnect` instead of `--autoConnect`.
3. 2. **Make sure the MCP server in configured to launch Chrome instead of connecting to an instance**: Chrome before 149 is not able to load extensions when connecting to an existing instance (`--auto-connect`, `--browserUrl`).
4. - Missing `pageId`: Page-scoped tools require a `pageId` argument. Call `list_pages` to find active page IDs.
5. - `--autoConnect` handshakes, timeouts, and requirements (requires **running** Chrome 144+).

## Files inside the skill

- (SKILL.md only)
