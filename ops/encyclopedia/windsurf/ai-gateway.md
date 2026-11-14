# ai-gateway

Source read: `C:\Users\a7med\.codex\skills\ai-gateway\SKILL.md`.

## Summary
This skill is a detailed Vercel AI Gateway guide for routing LLM calls through one API with provider selection, failover, caching controls, per-user tracking, budgets, audit logs, multimodal support, and Claude Code compatibility. It assumes the AI SDK is the main integration surface and repeatedly warns that model slugs, providers, pricing, and capabilities must be verified from live docs.

## When to use / when NOT
Use for production or multi-provider AI features that need failover, cost attribution, rate limits, audit logging, unified billing, or a single model string across providers. Do not use it as a reason to add gateway complexity for a tiny prototype already happy with one direct provider SDK, a self-hosted model absent from the catalog, or provider-specific features the gateway does not expose.

## Inputs, outputs, tools
Inputs are the target runtime, chosen `provider/model` slug, prompt or messages, optional `user`, `tags`, `order`, `only`, fallback `models`, cache headers, and budget or rate-limit preferences. Outputs are model responses, routing and usage metadata, cost-attributed logs, and handled gateway errors. Tools are `ai` and optionally `@ai-sdk/gateway`, Vercel CLI commands such as `vercel link` and `vercel env pull`, `VERCEL_OIDC_TOKEN` or `AI_GATEWAY_API_KEY`, the Vercel dashboard, provider SDKs when going direct, and the live model endpoint.

## 5 most important rules
1. Fetch current docs and the live model list before hardcoding model IDs; use `provider/model` format and call `gateway.getAvailableModels()` when available.
2. Prefer OIDC through `vercel link` plus `vercel env pull`; use `AI_GATEWAY_API_KEY` only for CI, scripts, or non-Vercel environments.
3. Configure `order`, `only`, fallback `models`, `user`, and `tags` deliberately for failover, per-user tracking, and cost attribution.
4. Handle gateway failures by status: `402` for budget exhaustion, `429` for rate limits, `503` or provider failure for failover, and use streaming for long generations.
5. Use the gateway for production, multi-tenant SaaS, cost accountability, and audit needs; choose a direct provider SDK only for provider-specific or self-hosted cases.

## Risks / owner notes
The skill itself warns that training data is outdated, so model names, prices, provider lists, and SDK syntax can drift. Local OIDC tokens are short-lived, budgets can stop spend with `402`, per-user limits can return `429`, and content logging is not enabled by default. The owner should configure budgets, keys, trusted environments, and dashboard alerts before production use.

## Category / tags
ai · vercel, ai-gateway, llm, model-routing, failover, cost-tracking, oidc, observability

## Revisions
The codex, kilo, cursor, and windsurf copies are identical and selected here because codex is the prescribed fallback and the file is the most complete standalone guide. The gemini-plugin Vercel copy is newer and more checklist-like, emphasizing live docs, CLI inventory, and reference files, but it is narrower than the codex revision.
