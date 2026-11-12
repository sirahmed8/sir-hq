# base44-sdk

- Tool: `gemini-plugin` (plugin: `base44`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44-sdk\SKILL.md`
- SKILL.md size: 16732 chars

## What it does

The base44 SDK is the library to communicate.

## When to use (from skill text)

- ## When to Use This Skill vs base44-cli

## Structure (headings inside SKILL.md)

- Base44 Coder
- ⚡ IMMEDIATE ACTION REQUIRED - Read This First
- When to Use This Skill vs base44-cli
- Quick Start
- ⚠️ CRITICAL: Do Not Hallucinate APIs
- Authentication - WRONG vs CORRECT
- Functions - WRONG vs CORRECT
- Integrations - WRONG vs CORRECT
- Actors - WRONG vs CORRECT
- Entities - WRONG vs CORRECT
- SDK Modules
- TypeScript and type registries
- Installation
- Creating a Client (External Apps)
- Module Selection
- Common Patterns
- Filter and Sort Data
- Protected Routes (check auth)
- Backend Function Call
- Realtime Room (Actor)
- Service Role Access
- Frontend vs Backend
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `token` (string) - Pre-authenticated user token
- - Create/read/update/delete records → `entities`

## Key rules (verbatim lines from SKILL.md)

1. - Do NOT use base44-cli unless user explicitly requests CLI commands
2. - Chat with AI agents → `agents` (requires logged-in user)
3. - Text-to-speech (TTS) or read-aloud → [speech guide](references/ai-gateway.md#generate-speech) for browser/Core/gateway selection; read it before implementing model-specific controls or editing existing gateway speech code

## Files inside the skill

- `references/actors.md` — "Actors Module"
- `references/ai-gateway.md` — "AI Gateway Module"
- `references/analytics.md` — "Analytics Module"
- `references/app-logs.md` — "App Logs Module"
- `references/auth.md` — "Auth Module"
- `references/base44-agents.md` — "Agents Module"
- `references/client.md` — "Client Setup"
- `references/connectors.md` — "Connectors Module"
- `references/entities.md` — "Entities Module"
- `references/functions.md` — "Functions Module"
- `references/integrations.md` — "Integrations Module"
- `references/QUICK_REFERENCE.md` — "Base44 SDK Quick Reference"
- `references/sso.md` — "SSO Module"
- `references/users.md` — "Users Module"
