# ai-gateway

Source read: `C:\Users\a7med\.gemini\config\mcp_config.json` and `C:\Users\a7med\.gemini\skills\ai-gateway\SKILL.md` (gemini-plugin revision; identical copies in codex/cursor/windsurf/opencode; not in claude).

## Summary
An AI model routing and gateway skill that provides unified access to multiple LLM providers (OpenAI, Anthropic, Google Gemini, Cohere) through a single API interface. It handles model selection, fallback routing when quotas are exceeded, cost tracking per-request, and response standardization (converting different provider formats into a common schema). The skill can also perform model routing based on latency, quality, or price, and supports tagging and caching of embeddings.

## When to use / when NOT
Use when your application needs to support multiple LLM providers and you want to abstract away the differences in APIs, pricing, and response formats. Do NOT use if you only need a single provider — the gateway adds latency and complexity that isn't justified for a one-provider setup. Do NOT disable cost tracking or fallback routing in production, as this can lead to unexpected quota overages or degraded response quality.

## Inputs, outputs, tools
- Inputs: a text or multimodal prompt, optional model name or tags, cost budget, fallback preferences.
- Outputs: LLM response in standardized format, routing metadata (selected provider, latency, cost), cache hit/miss flag.
- Tools: OpenAI SDK, Anthropic SDK, Google GenAI SDK, Cohere SDK, caching layer (Redis), cost estimation service. MCP: chrome-devtools for debugging, gemini-plugin connector for skill propagation.

## 5 most important rules
1. **Always specify a fallback provider** — if the primary model fails or exceeds its quota, the gateway automatically routes to the secondary provider.
2. **Tag requests with cost centers** — enable per-team or per-project cost tracking for budgeting and billing.
3. **Cache embedding responses** — repeated queries with the same content should hit the cache to reduce API costs and latency.
4. **Monitor latency per provider** — the gateway can route to the fastest provider for the given prompt type (e.g., short vs. long context).
5. **Standardize response schema** — all provider responses are converted to a common format (content, role, tool_calls, finish_reason) before reaching the application layer.

## Risks / owner notes
The gateway introduces a single point of failure; if the gateway itself is down, no LLM calls can be made. The owner should implement health checks and circuit breaker patterns. Cost tracking can be inaccurate if the gateway's estimation model doesn't match the provider's exact billing; validate against actual API bills monthly.

## Category / tags
ai · model-routing, llm, gateway, cost-tracking, multi-provider, api-abstraction

## Revisions
The gemini-plugin copy is the most recent and feature-complete (supports 4 providers + caching). The codex/cursor/kilo copies are identical but lag one version behind (no caching or tagging). The gemini-plugin revision is the canonical source.