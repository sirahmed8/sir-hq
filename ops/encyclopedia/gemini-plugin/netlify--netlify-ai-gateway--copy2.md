# netlify-ai-gateway

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\codex\skills\netlify-ai-gateway\SKILL.md`
- SKILL.md size: 14005 chars

## What it does

Use Netlify AI Gateway to call OpenAI, Anthropic Claude, Google Gemini, TypeSafe (Jev), or OpenRouter-hosted models (xAI/DeepSeek/Meta/Mistral/Qwen) from Netlify Functions or Edge Functions without managing provider accounts or API keys. Reach for this when adding an AI feature to a Netlify app — a chatbot, text summarizer, image generator, joke/content generator, form-submission routing or analysis, or any LLM call — or when wiring the OpenAI/Anthropic/Gemini/TypeSafe/OpenRouter SDK into a Netlify Function, choosing which env vars to use, streaming long generations, or debugging why gateway calls fail at build time or return 401.

## When to use (from skill text)

- **Explicit-config path:** `NETLIFY_AI_GATEWAY_KEY` and `NETLIFY_AI_GATEWAY_URL` are always injected and never collide with user-set provider vars. Use this pair only when a third-party or unsupported library needs explicit key/base-URL configuration — pass them as constructor arguments. It is not th

## Structure (headings inside SKILL.md)

- Netlify AI Gateway
- Footguns (read first)
- Where code goes
- Provider SDKs (instantiate with no args)
- Env vars — which to use
- Full example (Vite + React + Function)
- Local development
- Billing, limits, constraints
- References
- Netlify house rules (ai-gateway)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Not browser-callable.** Gateway calls belong in Functions or Edge Functions — never in client-side code. The browser has no injected credentials.
- - **Runtime-only credentials.** Never call the gateway from build scripts, prerender/SSG, or build plugins — those get no credentials and fail. Do AI work at request time; cache to Netlify Blobs if output must look precomputed.
- - **Requires one production deploy.** The gateway does not activate until a project has at least one production deploy. Even for local dev, run `netlify deploy --prod` once first.
- - **Cost:** tokens → USD (provider-published rates) → credits. **$1 USD = 180 credits.**

## Key rules (verbatim lines from SKILL.md)

1. - **Not browser-callable.** Gateway calls belong in Functions or Edge Functions — never in client-side code. The browser has no injected credentials.
2. - **Runtime-only credentials.** Never call the gateway from build scripts, prerender/SSG, or build plugins — those get no credentials and fail. Do AI work at request time; cache to Netlify Blobs if output must look precomputed.
3. - **60-second sync timeout.** A gateway call in a synchronous function is bound by the 60s function timeout. Stream long generations (SDK streaming + `ReadableStream`), or use a background function that persists output for the client to fetch. Never leave a slow generation unstreamed.
4. - **Requires one production deploy.** The gateway does not activate until a project has at least one production deploy. Even for local dev, run `netlify deploy --prod` once first.
5. - **Don't hardcode model lists.** Available models change. Check the live providers endpoint (`https://api.netlify.com/api/v1/ai-gateway/providers/detailed`) rather than baking in a static list.

## Files inside the skill

- (SKILL.md only)
