# best-practices

- Tool: `gemini-plugin` (plugin: `mobbin`)
- Category: ops
- Source: `C:\Users\a7med\.gemini\config\plugins\mobbin\skills\best-practices\SKILL.md`
- SKILL.md size: 6838 chars

## What it does

Tells your agent what Mobbin can and can't.

## When to use (from skill text)

- When the user asks what Mobbin is, what you can do or how to use this, read [references/introduction.md](references/introduction.md) and answer from it, not from memory.

## Structure (headings inside SKILL.md)

- Mobbin best practices
- What Mobbin can do
- What it can't do
- Using the skills well
- When the Mobbin MCP isn't working
- Connection check
- Out of scope
- Too broad
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP isn, MCP works, MCP should, MCP instead, MCP is, MCP doesn

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Search or compare before a redesign.** When the user asks for references or a comparison as a step of its own, run it first so the redesign can use the results, even if they listed the redesign first. If they said where to start, start there.
2. - **Don't name skills to the user.** Apart from the order line, write nothing before handing off.
3. - **Give the tool's reason, never a guess.** If it gave none, say so.
4. - **Don't work around it.** No answer from memory, web search or other connector in Mobbin's place.
5. - **Remember it.** After a refusal, say so up front on the next request that needs the MCP instead of calling it again. Carry on once the user says it's fixed.

## Files inside the skill

- `references/introduction.md` — "Introducing Mobbin"
- `references/reply-templates.md` — "Reply templates"
