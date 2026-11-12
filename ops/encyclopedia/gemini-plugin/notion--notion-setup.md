# notion-setup

Tools: gemini-plugin (Notion plugin). Source: C:\Users\a7med\.gemini\config\plugins\notion\skills\notion-setup\SKILL.md (6 lines, read in full)

## Summary
A tiny bootstrap skill for connecting the Notion MCP: it instructs the agent to call the connection's `notion-get-setup-guide` tool (or `get-setup-guide` on some connections) and walk the user through the returned guide, falling back to fetching https://developers.notion.com/prompts/setup when the tool is absent.

## When to use / not use
Use once when setting up Notion MCP integration for the first time. Not a content skill — every other notion-* skill assumes this connection already works.

## Inputs, outputs, dependencies
Input: a Notion MCP connection (or its absence). Output: a guided setup walkthrough for the user. Needs: the `notion-get-setup-guide` MCP tool, or web fetch of the Notion developer setup prompt.

## Key rules
1. Call the setup-guide tool first; only fall back to the URL when the tool is not exposed.
2. Follow the guide it returns rather than improvising configuration steps.

## Risks / owner items
- Requires the Notion MCP server to be connected in the host client; without it the skill can only point at documentation.
- Setup typically involves OAuth/account authorization — an owner action.

## Category and tags
ops — notion, mcp, setup, onboarding.

## Revision note
Single plugin revision; deliberately minimal — it delegates all substance to Notion's own setup guide.
