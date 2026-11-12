# best-practices

**Source:** `C:\Users\a7med\.gemini\config\plugins\mobbin\skills\best-practices\SKILL.md` (+ `references/introduction.md`, `references/reply-templates.md`)
**Category:** design
**Tags:** mobbin, design-research, ui-references, redesign, mcp, reply-templates

## Summary
A companion skill for the Mobbin MCP that tells the agent what Mobbin can and cannot do and how to reply. Mobbin is a paid reference library of real apps and sites; through the MCP it can browse and find references, redesign a screen the user already has, and compare products. The skill defines exact reply templates for out-of-scope requests, too-broad requests, clones, connection checks and MCP failures, and it enforces short, answer-first replies.

## When to use / when not to
Use it whenever the user asks about Mobbin, its connection, or starts a design task Mobbin could help with, including tasks that are too large or outside Mobbin's scope. Do not use it for requests that are not Mobbin requests at all; those are answered normally.

## Inputs, outputs, tools
Inputs: the user's design question, screenshots or code or design files, and the Mobbin MCP tools. Outputs: short replies, reference search results, redesign directions, comparison results, or the prescribed refusal templates. Tools: the Mobbin MCP, which requires a paid Mobbin plan. No other MCP.

## Five most important rules
1. Pass the user's request and attachments to the skill unchanged, and do not name skills to the user.
2. Search or compare before a redesign when the user asked for references as a step; when they want references to fix their own screen, go straight to the redesign.
3. Work one step at a time and open with the order in one line, in the user's words.
4. When the MCP is not working, give the tool's reason and never a guess; do not work around it with memory or web search, and retry only once on an unexplained failure.
5. Use the exact reply templates for out-of-scope, too-broad and clone requests, and never offer to replicate a named app.

## Risks and owner actions
The Mobbin MCP requires a paid plan and an active connection; a refusal means stop, not retry. No secrets are involved.

## Revisions
The installed config copy (6838 bytes) and the marketplace cache 1.5.0 have identical bodies; only the description frontmatter differs.
