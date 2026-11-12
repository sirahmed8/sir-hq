# omniroute-resilience-gateway

Tools: claude, codex, cursor, gemini-plugin, kilo, opencode, windsurf (kilo copy used; identical across tools).
Source: C:\Users\a7med\.config\kilo\skills\omniroute-resilience-gateway\SKILL.md (39 lines, read in full)

## Summary
A short architecture-pattern skill for resilient AI model gateways: route agent/app requests through a local or edge proxy that tracks provider health and quota, chains providers by cost/quality tier, opens a circuit on 429/quota errors honoring `Retry-After`, and normalizes payloads to OpenAI-compatible or Anthropic Messages schema so clients need zero code changes on failover.

## When to use / not use
Use when designing or operating a multi-provider LLM gateway that must survive rate limits and quota exhaustion (the SIR autopilot context). Not a code library — it describes the pattern; implementing it needs an actual gateway (OmniRoute or equivalent) plus provider API keys.

## Inputs, outputs, dependencies
Input: LLM requests from agents/applications. Output: responses from whichever healthy provider answers. Needs: multiple provider API keys, a gateway/proxy layer, a health+quota tracker, and a normalization layer.

## Key rules
1. Tier-chain providers: reasoning models for hard requests, fast cheap/free models (Gemini Flash, Groq, OpenRouter free tier) for lints and quick completions.
2. On 429/RESOURCE_EXHAUSTED, open the provider's circuit for the `Retry-After` duration and redirect pending+new requests to the next healthy provider.
3. Normalize request/response to OpenAI-compatible or Anthropic Messages schema — clients never change when models switch.
4. Keep a health/quota tracker as a first-class gateway component, not an afterthought.

## Risks / owner items
- Failover can silently change model quality/cost — tier assignment decides what answers; a "free tier" fallback may produce weaker output without the caller noticing.
- Provider API keys for several services must be configured and budgeted; quota exhaustion on the primary is the expected trigger, so free tiers should be vetted for data/privacy policy before routing user data.

## Category and tags
ai, build, ops — llm-gateway, failover, rate-limits, multi-provider, reliability.

## Revision note
Identical across all seven tools; single 39-line file — a pattern sketch, not an implementation.
