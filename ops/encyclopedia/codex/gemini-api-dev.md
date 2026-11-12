# gemini-api-dev

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\gemini-api-dev\SKILL.md`
- SKILL.md size: 21541 chars

## What it does

Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal understanding, image generation, video generation, speech generation (TTS), voice design, voice replication, streaming responses, background research tasks, function calling, structured output, or migrating from the old generateContent API. Covers SDK usage and best practices for Gemini models and agents in Python and TypeScript.

## Structure (headings inside SKILL.md)

- Gemini API Development Skill
- Critical Rules (Always Apply)
- Current Models (Use These)
- Current Agents
- Current SDKs
- Important Additional Notes
- Quick Start
- Python
- JavaScript/TypeScript
- Response Helpers
- Stateful Conversation
- Python
- Second turn — server remembers context
- JavaScript/TypeScript
- Deep Research Agent
- Python
- JavaScript/TypeScript
- Managed Agents
- Antigravity Agent
- Custom Agents
- Invoke — each call forks the base environment
- Streaming
- Python
- JavaScript/TypeScript
- Documentation Lookup & Pages
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP integration, MCP is, MCP server, MCP results, MCP tools, MCP provides, MCP tool

## Risks / cautions found in text

- - `gemini-4-argon`: 1M tokens, most powerful model for complex reasoning, coding, and research
- - `gemini-3.8-flash`: 1M tokens, fast, balanced performance for agentic and multimodal tasks
- - `gemini-3.5-flash-lite`: 1M tokens, fastest, lowest-cost 3.5 model for high-throughput execution
- - `gemini-nano-banana-2.1` (Nano Banana 2.1): 131k / 32k tokens, default high-efficiency image generation and conversational editing

## Key rules (verbatim lines from SKILL.md)

1. - **Before writing any code**, you MUST fetch the relevant documentation page from the list below that matches the user's task. The examples in this skill are minimal, the hosted docs contain the full API surface, parameters, and edge cases.
2. - **Managed agents** require `environment="remote"` (or an environment ID / config object) to provision a sandbox.
3. - **Migrating from `generateContent`**: Read `references/migration.md` for the scoping, checklist, and before/after code examples. Always confirm scope with the user before editing.
4. - **Model upgrades**: Drop-in, swap the model string. Deprecated models (`gemini-2.0-*`, `gemini-1.5-*`) must be replaced, see `references/migration.md`.
5. 3. **Trust MCP results** as source of truth for API details — they are always up-to-date.

## Files inside the skill

- `references/migration.md` — "Migration Reference"
