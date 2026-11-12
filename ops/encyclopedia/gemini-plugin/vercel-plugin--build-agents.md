# build-agents

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\build-agents\SKILL.md`
- SKILL.md size: 3179 chars

## What it does

Default guidance for building AI agents.

## When to use (from skill text)

- - `/eve/v1/slack` as the Connect trigger path.

## Structure (headings inside SKILL.md)

- Build Agents
- What eve is
- Getting started
- Slack Agents
- Boundaries
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP servers

## Risks / cautions found in text

- - `@vercel/connect` for Slack credentials and webhook verification.
- - Do not hardcode credentials, Slack bot tokens, signing secrets, or provider

## Key rules (verbatim lines from SKILL.md)

1. - Do not use Vercel Agent for generic agent building. Vercel Agent is the
2. - Do not duplicate the Slack Agent Skill's setup wizard in this skill.
3. - Do not hardcode credentials, Slack bot tokens, signing secrets, or provider

## Files inside the skill

- (SKILL.md only)
