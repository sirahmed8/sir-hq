# vercel-agent (codex revision)

## Summary
vercel-agent documents Vercel's platform-level AI tool suite (configured at project Settings > AI, no npm package): automated PR code review (triggered on push or `@vercel` mention, multi-step reasoning for security/logic/perf, generates and validates patches inside Vercel Sandbox), anomaly investigation (queries logs/metrics for root cause, requires Observability Plus subscription), and free SDK installation (auto-installs Web Analytics and Speed Insights, opens a PR). Pricing: $0.30 per review/investigation plus token costs, $100 promo credit for Pro teams, installation free.

## When to use / when NOT
Use when the user asks about Vercel Agent features, PR review automation, anomaly investigation, or auto-installing Vercel analytics SDKs. Do NOT use it to configure the agent itself locally — it is a Vercel platform service configured in the dashboard; the agent can't toggle it from code.

## Inputs, outputs, tools
- Inputs: questions about Vercel Agent capabilities, pricing, configuration location.
- Outputs: factual answers about the service; optionally PR-based SDK installation happens platform-side.
- Tools: none locally — references https://vercel.com/docs/agent.

## 5 most important rules
1. Vercel Agent is dashboard-configured (Settings > AI), not code — there is no local install step.
2. Code Review runs on push or `@vercel` PR mentions and validates patches in Vercel Sandbox before proposing.
3. Investigation requires the Observability Plus subscription; reviews/investigations cost $0.30 + tokens.
4. SDK installation (Analytics, Speed Insights) is free and opens its own PR.
5. Keep answers factual about platform behavior; don't promise features not in the docs.

## Risks / things needing the owner
Costs money per use beyond the promo credit; investigation gated behind a paid add-on. Enabling/configuring it happens in the Vercel dashboard — an owner decision if billing is involved. No local side effects.

## Category / tags
cloud · vercel, ai-agent, code-review, observability

## Revisions
Single source read: `C:\Users\a7med\.codex\skills\vercel-agent\SKILL.md` (53 lines). The skill exists across codex/cursor/gemini-plugin/kilo/opencode/windsurf per the slice, but all are thin factual stubs of the same Vercel docs content; codex revision chosen as representative.
