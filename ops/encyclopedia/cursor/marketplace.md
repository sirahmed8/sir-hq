# marketplace (vercel-plugin family)

Source read: `C:\Users\a7med\.codex\skills\marketplace\SKILL.md` (18 KB; codex revision; cursor/kilo/opencode/windsurf/gemini-plugin listed).

## Summary
Vercel Marketplace integration guide covering both consuming and building sides. Consuming: preflight `test -f .vercel/project.json` / `vercel link` (provisioning is project-scoped); discover via `vercel integration discover [--category]`, `guide <name> [--framework]` (agent-friendly structured setup steps), `add <name>` (auto-connects + auto env-sync), `list`/`ls`, `balance <name>`, `remove`, `open` for dashboard fallback. Auto-provisioned env vars are injected into all environments — Neon yields POSTGRES_* vars, Upstash KV_REST_API_*, etc. — with a documented 1-3 minute provisioning window where DB connections 500 (wait and retry, do NOT debug; `vercel env pull` after). Unified billing: single Vercel invoice, usage-based, team-level. Building: `npx create-vercel-integration`, `vercel-integration.json` manifest (slug, scopes, resourceTypes), webhook handlers for `integration.installed`/`uninstalled` verified via `verifyVercelSignature` from `@vercel/integration-utils`.

## When to use / when NOT
Use when installing/managing Vercel Marketplace integrations (DBs, auth, monitoring, CMS) or building a sellable integration. Not for plain env-var management or non-Vercel platforms.

## Inputs, outputs, tools
- Inputs: linked Vercel project, integration name/category, framework for guide steps.
- Outputs: installed integration, auto-provisioned env vars, unified billing line items; or a scaffolded integration app.
- Tools: `vercel integration` / `vercel mf`-adjacent CLI, `vercel link`, `vercel env ls/pull`, Marketplace dashboard, `create-vercel-integration`, `@vercel/integration-utils`.

## 5 most important rules
1. Verify the repo is linked (`.vercel/project.json`) before any `integration add`.
2. Default discovery flow is `vercel integration guide <name> --framework <fw>` — it returns structured env vars, SDKs, snippets.
3. After install, expect 1-3 min provisioning delay; DB 500s during that window are normal — wait, don't debug, then `vercel env pull`.
4. Never hand-edit `.env` for integration vars — they're auto-injected into Dev/Preview/Prod; verify with `vercel env ls`.
5. Building side: verify webhook signatures (`verifyVercelSignature`) and declare scopes/resourceTypes in the manifest; `add`/billing changes may require interactive confirmation (no `--yes` past free limits).

## Risks / owner notes
Marketplace installs create real billable resources on the owner's Vercel team — check `integration balance` and confirm spend. Removing an integration can delete provisioned resources; webhook handlers must be idempotent.

## Category and tags
Category: cloud. Tags: vercel, marketplace, integrations, env-vars, billing, webhooks, provisioning.
