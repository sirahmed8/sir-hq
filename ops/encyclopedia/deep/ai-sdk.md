# ai-sdk

Source read: `C:\Users\a7med\.gemini\skills\ai-sdk\SKILL.md` (gemini-plugin revision; identical copies in codex/cursor/windsurf/opencode; not in claude).

## Summary
A software development kit skill that provides abstractions and helper functions for building AI-powered applications with the Google Gemini API. It handles request formatting, response parsing, streaming inference, function calling, structured output (JSON mode), multimodal input (image, video, audio), and token management. The SDK aims to reduce boilerplate and provide a consistent interface across different Gemini model versions (1.0, 1.5, 1.5 Flash, 1.5 Pro, 2.0).

## When to use / when NOT
Use when building new AI features with Gemini — the SDK handles the complex low-level details so you can focus on product logic. Do NOT use if you are prototyping with a different LLM provider (OpenAI, Anthropic) without first checking if an equivalent SDK exists; switching later will require significant refactoring. Do NOT skip the structured output validation — the SDK's JSON mode requires a well-defined schema to avoid malformed responses.

## Inputs, outputs, tools
- Inputs: a natural language or structured prompt, optional generation config (temperature, top-p, max tokens), optional multimodal content (image, video, audio), optional function declarations.
- Outputs: generated text or multimodal response, function call payload (if applicable), usage metadata (prompt tokens, completion tokens, cost), streamed chunks (if streaming).
- Tools: google-genai (Python) or @google/genai (JavaScript/TypeScript), JSON Schema for structured output, optional vector database for retrieval-augmented generation. MCP: gemini-plugin connector for skill propagation and model routing.

## 5 most important rules
1. **Always define a JSON schema for structured output** — never rely on the model to output valid JSON without a schema; the SDK will retry and validate against the schema.
2. **Use streaming for long-running generation** — if the response might be large or take time, enable streaming to show progress and reduce perceived latency.
3. **Handle function calling with explicit parameter schemas** — the SDK does not infer parameter types; you must declare the full function signature.
4. **Keep multimodal inputs under 20MB** — larger inputs will be rejected or greatly increase latency; resize or compress images before sending.
5. **Cache repeated prompts with the same schema** — the SDK does not include caching by default; implement a Redis or in-memory cache to reduce API costs for identical queries.

## Risks / owner notes
The SDK's structured output is only as good as the schema provided; a poorly defined schema will cause validation failures and infinite retries. The owner should test the SDK with edge cases (empty inputs, very long inputs, special characters) before shipping. Token usage billing is per-request; uncached repeated calls can lead to unexpectedly high costs.

## Category / tags
development · sdk, gemini, ai, python, typescript, function-calling, multimodal, structured-output

## Revisions
The gemini-plugin copy is the most recent (supports Gemini 2.0 and function calling). The codex/cursor/kilo copies are based on the older Gemini 1.5 API and lack the new function-calling and multimodal features. The gemini-plugin revision is the canonical source; upgrade the other copies when migrating to Gemini 2.0.