# gemini-live-api-dev

## Summary
gemini-live-api-dev is a Google-published skill for building real-time, bidirectional streaming applications with the Gemini Live API. It covers WebSocket-based audio/video/text streaming, voice activity detection (VAD), background reasoning (extended thinking), asynchronous function calling, session management with ephemeral tokens, live transcription, and live translation. The skill provides SDK usage guidance for both Python (google-genai) and JavaScript/TypeScript (@google/genai), session lifecycle (create/close with tokens), audio encoding (16kHz PCM, Opus), video frame handling, and resilience patterns (connection recovery, fallback). Reference files include VAD guide, function calling guide, session management, and resilience patterns.

## When to use / when NOT
Use when building real-time bidirectional streaming apps with Gemini (audio/video/text), real-time transcription/translation, or interactive voice assistant experiences. Do NOT use for non-real-time API calls, for static text generation, or for applications that don't require low-latency bidirectional streaming.

## Inputs, outputs, tools
- Inputs: Task type (audio, video, text, multimodal), SDK language (Python/JavaScript), session config (VAD, function calling, translation), audio/video parameters.
- Outputs: SDK code snippets, session management patterns, audio/video config, transcription/translation workflows, resilience patterns.
- Tools: `google-genai` Python Live SDK, `@google/genai` JS/TS Live SDK, WebSocket management, token handling. References: VAD, function-calling, session-management, resilience-patterns .md files.

## 5 most important rules
1. Always use ephemeral tokens for session management; never hardcode session IDs or tokens in source.
2. VAD must be enabled for voice applications; configure speech endpoints and silence timeout thresholds.
3. Audio: 16kHz PCM for microphone input; Opus encoding for transmission; always test VAD thresholds before deployment.
4. Function calling: use async/await pattern; never block the WebSocket thread during function execution.
5. Session lifecycle: create sessions with short-lived tokens; close sessions gracefully on exit; implement reconnect with exponential backoff.

## Risks / things needing the owner
WebSocket connection stability depends on network conditions; user must handle disconnect/reconnect gracefully. Token management requires secure storage. No direct owner actions beyond console setup.

## Category / tags
google · gemini, live-api, real-time, streaming, audio, video, websocket, vad, transcription, translation, sdk

## Revisions
Single revision in `C:\Users\a7med\.config\kilo\skills\gemini-live-api-dev\SKILL.md` (Google-published, Apache-2.0, v1). Only kilo has this skill; scripts/references folders exist (scripts=False, refs=True per earlier check).