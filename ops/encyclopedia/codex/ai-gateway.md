# ai-gateway

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\ai-gateway\SKILL.md`
- SKILL.md size: 19850 chars

## What it does

Vercel AI Gateway expert guidance. Use when configuring model routing, provider failover, cost tracking, or managing multiple AI providers through a unified API.

## When to use (from skill text)

- Use this to decide whether to route through AI Gateway or call a provider SDK directly:

## Structure (headings inside SKILL.md)

- Vercel AI Gateway
- Overview
- Packages
- Setup
- Model Slug Rules (Critical)
- Authentication (OIDC — Default)
- Setup
- Enable AI Gateway in Vercel dashboard: https://vercel.com/{team}/{project}/settings → AI Gateway
- How It Works
- Local Development
- Alternative: Manual API Key
- Set AI_GATEWAY_API_KEY in your environment
- The gateway falls back to this when VERCEL_OIDC_TOKEN is not available
- Auth Priority
- Provider Routing
- Routing Options
- Cache-Control Headers
- Caching strategies
- When to use caching
- Cache key composition
- Per-User Rate Limiting
- Rate limit configuration
- Handling rate limit responses
- Budget Alerts and Cost Controls
- Tagging for cost attribution
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2. The `@ai-sdk/gateway` package reads this token via `@vercel/oidc` (`getVercelOidcToken()`)
- 4. On Vercel deployments, OIDC tokens are auto-refreshed — zero maintenance
- - **Tokens per day per user**: Cap daily token consumption (e.g., 100K tokens/day)
- 2. Set monthly budget thresholds (e.g., $500/month warning, $1000/month hard limit)

## Key rules (verbatim lines from SKILL.md)

1. - `ai@^6.0.0` (required; plain `"provider/model"` strings route through the gateway automatically)
2. - Always use `provider/model` format (for example `openai/gpt-5.4`).
3. - Before hardcoding model IDs, call `gateway.getAvailableModels()` and pick from the returned IDs.
4. - Do not default to outdated choices like `openai/gpt-4o`.
5. 2. `VERCEL_OIDC_TOKEN` via `@vercel/oidc` (default on Vercel and after `vercel env pull`)

## Files inside the skill

- (SKILL.md only)
