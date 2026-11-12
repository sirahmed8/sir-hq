# gemini-live-api-dev

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\gemini-live-api-dev\SKILL.md`
- SKILL.md size: 18646 chars

## What it does

Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migrating legacy Live models (2.0/2.5/3.1) to Gemini 3.8 Live. Covers WebSocket-based audio/video/text streaming, voice activity detection (VAD), background reasoning (extended thinking), asynchronous function calling, session management, ephemeral tokens, live transcription, and live translation. SDKs covered - google-genai (Python), @google/genai (JavaScript/TypeScript).

## Structure (headings inside SKILL.md)

- Gemini Live API Development Skill
- Overview
- Models
- Current Models (Use These)
- SDKs
- Partner Integrations
- Audio Formats
- Quick Start
- Authentication
- Connecting to the Live API
- Sending Text
- Sending Audio
- Sending Video
- frame: raw JPEG-encoded bytes
- Receiving Audio and Text
- Background Reasoning (Extended Thinking)
- Live Translation (Gemini Live Translate)
- Model
- Configuration (`TranslationConfig`)
- Live Streaming Transcription (Gemini Live Transcribe)
- Model
- Modes
- Python
- JavaScript
- Raw WebSockets
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP is, MCP results, MCP tools, MCP provides, MCP documentation

## Risks / cautions found in text

- - **Ephemeral tokens** — secure client-side authentication
- - [Voximplant](https://voximplant.com/products/gemini-client) — Connect inbound and outbound calls to Live API with Voximplant.
- - **Context window** — 128k input tokens / 64k output tokens
- 4. **Use ephemeral tokens** for client-side deployments — never expose API keys in browsers

## Key rules (verbatim lines from SKILL.md)

1. - `gemini-3.8-live-extended-thinking` — High-reasoning audio-to-audio model recommended when higher background reasoning is required during live interactions. Processes background reasoning and async tool calls (`behavior: NON_BLOCKING` required) while streaming continuous spoken conversational fill
2. - **Non-blocking tools**: All function declarations **must** set `behavior="NON_BLOCKING"`. Synchronous blocking mode is not supported and returns an error.
3. 4. **Use ephemeral tokens** for client-side deployments — never expose API keys in browsers
4. 3. **Trust MCP results** as source of truth for API details — they are always up-to-date.

## Files inside the skill

- `references/migration.md` — "Gemini Live API Migration & Upgrading Reference"
