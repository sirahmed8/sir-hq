# gemini-api-dev

## Summary
gemini-api-dev is a Google-published skill for integrating the Gemini API into applications. It covers text generation with structured output, multi-turn chat, multimodal understanding (image + text), function calling, and agent workflows. The skill provides guidance on SDK setup (google-genai Python, @google/genai JavaScript/TypeScript), authentication via API keys or OAuth, prompt design for different model tiers, structured output schemas, tool calling patterns, and agent design with extended thinking. It also covers rate limiting, retry strategies, and cost optimization across models (flash vs pro). Reference files include auth, structured-output, function-calling, and agent-design guides.

## When to use / when NOT
Use when developers want to integrate Gemini text generation, chat, multimodal inputs, function calling, or agent workflows into their applications. Do NOT use for non-Gemini LLM providers, for general AI assistance without API integration, or for tasks that don't require structured output or function calling.

## Inputs, outputs, tools
- Inputs: Model selection (flash/pro), task type (text, chat, multimodal, function-calling, agent), SDK language (Python/JavaScript), authentication method, rate limit tolerance.
- Outputs: SDK code snippets, authentication setup, prompt templates, structured output schemas, rate limit config, agent workflow diagrams.
- Tools: `google-genai` Python SDK, `@google/genai` JS/TS SDK, API key management, rate limit configs. References: auth, structured-output, function-calling, agent-design .md files.

## 5 most important rules
1. Always authenticate before API calls: use API key for quick starts or OAuth for production; never hardcode keys in source.
2. For structured output, define JSON schema first; validate response matches schema before use.
3. Rate limit: start conservatively (10 rpm for flash, 5 rpm for pro); implement exponential backoff on 429 responses.
4. Multimodal: provide both image and text parts when using vision-capable models; image must be base64-encoded or URI.
5. Cost optimization: use flash model for prototyping; migrate to pro for production quality; cache identical prompts when possible.

## Risks / things needing the owner
API key or OAuth credential setup requires access to Google Cloud Console. Rate limit breaches may temporarily suspend access. No direct owner actions beyond console setup.

## Category / tags
google · gemini, api, llm, text-generation, chat, multimodal, function-calling, structured-output, agent, sdk

## Revisions
Single revision in `C:\Users\a7med\.config\kilo\skills\gemini-api-dev\SKILL.md` (Google-published, Apache-2.0, v1). Only kilo has this skill; scripts/references folders exist (scripts=False, refs=True per earlier check).