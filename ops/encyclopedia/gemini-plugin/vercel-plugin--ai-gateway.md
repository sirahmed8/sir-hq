# ai-gateway

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\ai-gateway\SKILL.md`
- SKILL.md size: 12587 chars

## What it does

Configure Vercel AI Gateway for multi.

## Structure (headings inside SKILL.md)

- Vercel AI Gateway
- Start with current sources
- Vercel CLI inventory
- Route the request to the right guide
- Choose the integration surface
- Minimal AI SDK request
- Authentication decision
- Implementation workflow
- Routing invariants
- Verification checklist
- Current documentation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **BYOK provider credentials do not replace AI Gateway request authentication.** They decide how AI Gateway authenticates to a model provider.
- - Request-scoped provider credentials belong under `providerOptions.gateway.byok` and must remain secret.
- - [ ] No secret appears in source, logs, diffs, or the final response.

## Key rules (verbatim lines from SKILL.md)

1. 3. Fetch the complete live model list. Do not construct model variants by analogy:
2. 5. Run `vercel ai-gateway <command> --help` before documenting or scripting CLI flags.
3. - Use an **AI Gateway API key** for local scripts, CI, external servers, and non-Vercel deployments. Store it in `AI_GATEWAY_API_KEY` and never print or commit it.
4. - **BYOK provider credentials do not replace AI Gateway request authentication.** They decide how AI Gateway authenticates to a model provider.
5. 1. Establish the user's job, runtime, deployment target, current provider, and required capabilities.

## Files inside the skill

- `references/coding-agents.md` — "Coding agents through AI Gateway"
- `references/evaluation.md` — "Decision models"
- `references/routing.md` — "Models, routing, caching, BYOK, and timeouts"
- `references/setup.md` — "Setup and compatible APIs"
- `references/spend-observability.md` — "Credits, budgets, reporting, and observability"
- `references/virtual-models.md` — "Virtual Models"
