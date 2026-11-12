# netlify-ai-gateway (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-ai-gateway\SKILL.md`. Call LLM providers from Netlify compute without managing keys.

## Summary
Netlify AI Gateway injects provider credentials automatically — use each provider's OFFICIAL SDK instantiated with NO args (gateway injects `ANTHROPIC_API_KEY`/`BASE_URL`, `OPENAI_*`, `GEMINI_*`/`GOOGLE_GEMINI_*`, `TYPESAFE_*`, `OPENROUTER_*`). Never hand-roll fetch against the gateway URL and don't default to `NETLIFY_AI_GATEWAY_KEY`/`_URL` env vars (those are for third-party/unsupported libraries only). Footguns: NOT browser-callable (credentials only exist server-side — Functions/Edge Functions only); runtime-only (never from build scripts/prerender/SSG/build plugins — no credentials there; cache output to Blobs if it must look precomputed); 60-second sync function timeout — stream long generations (SDK streaming + ReadableStream) or use a background function persisting output for client fetch; requires ONE production deploy before the gateway activates (even for local dev — `netlify deploy --prod` once first); don't hardcode model lists — check live `api.netlify.com/api/v1/ai-gateway/providers/detailed`; OpenRouter SDK needs ≥1.2.43 (older ignores `OPENROUTER_BASE_URL`, hits openrouter.ai, 401s). Code lives in normal `netlify/functions/*.js` files with `config.path` exports — no AI-specific file type. Providers covered: Anthropic, OpenAI, Google Gemini, TypeSafe/Jev (structured decisions/routing), OpenRouter-hosted models (xAI/DeepSeek/Meta/Mistral/Qwen).

## When to use / when NOT
Use when adding an AI feature to a Netlify app (chatbot, summarizer, classifier, form routing) or wiring provider SDKs into Functions/Edge Functions. NOT for client-side AI calls, build-time generation, or third-party SDKs that can't take injected env vars.

## Inputs, outputs, tools
- Inputs: provider SDK + model name, function/edge-function handler, streaming needs.
- Outputs: LLM responses streamed or persisted; provider credentials auto-injected.
- Tools: `@anthropic-ai/sdk`, `openai`, `@google/genai`, `@typesafe-ai/sdk`, OpenRouter SDK ≥1.2.43, Netlify Functions/Edge Functions, Blobs for caching.

## 5 most important rules
1. Official provider SDK with zero config — gateway injects credentials; never hand-rolled fetch as default path.
2. Server-side only: Functions/Edge Functions; never browser, never build/prerender.
3. Requires one production deploy before gateway works — do `netlify deploy --prod` first.
4. Respect the 60s sync timeout: stream long generations or persist via background function.
5. Check the live providers endpoint for models — never bake in static lists.

## Risks / owner notes
AI calls consume plan/usage credits; unbounded generation can hit the 60s timeout or cost. First-deploy requirement surprises local dev. OpenRouter version pin matters (401s otherwise).

## Category and tags
Category: cloud. Tags: netlify, ai-gateway, llm, functions, streaming, credentials, openrouter.
