# ai-sdk

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\ai-sdk\SKILL.md`
- SKILL.md size: 4179 chars

## What it does

Vercel AI SDK guidance: streaming chat, structured output, tool calling, agents, and LLM integrations.

## Structure (headings inside SKILL.md)

- Prerequisites
- Critical: Do Not Trust Internal Knowledge
- Finding Documentation
- ai@6.0.34+
- Earlier versions
- When Typecheck Fails
- Building and Consuming Agents
- Creating Agents
- Consuming Agents (Framework-Specific)
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 4. Never rely on memory - always verify against source code or docs
2. 5. **`useChat` has changed significantly** - check [Common Errors](references/common-errors.md) before writing client code
3. 8. Run typecheck after changes to ensure code is correct

## Files inside the skill

- `overlay.yaml`
- `references/ai-gateway.md` — "Vercel AI Gateway"
- `references/common-errors.md` — "Common Errors"
- `references/devtools.md` — "AI SDK DevTools"
- `references/type-safe-agents.md` — "Type-Safe useChat with Agents"
