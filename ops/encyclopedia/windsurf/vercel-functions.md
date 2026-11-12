# vercel-functions (codex revision)

## Summary
vercel-functions is expert guidance for Vercel's compute layer: Serverless Functions (full Node.js, 800ms-2.5s cold starts), Edge Functions (V8 isolates, <1ms cold starts, Web Standard APIs only — auth/redirects/simple transforms), Bun runtime (~28% lower CPU-bound latency, `"bunVersion"` in vercel.json), Rust runtime beta, and Node.js 24 LTS. Fluid Compute is the unified model: optimized concurrency (up to 85% cost cut), 300s default / 800s max Pro+Enterprise, Active CPU pricing, `waitUntil`/Next.js `after` for post-response work, instance sizes Standard(1vCPU/2GB)/Performance(2vCPU/4GB). Covers streaming (zero-config SSE/ReadableStream, AI SDK `toUIMessageStreamResponse`), Cron Jobs via vercel.json `crons` (endpoint must verify `Authorization: Bearer $CRON_SECRET`), per-function config (`maxDuration`, `memory`, `runtime`), timeout/500/invocation-failure/cold-start/edge-timeout diagnostic trees, and the now.json→vercel.json deprecation (removed 2026-03-31).

## When to use / when NOT
Use for any Vercel Function work: choosing runtime, configuring duration/memory, streaming, crons, or diagnosing function errors/timeouts. Do NOT use Edge for code needing fs/native modules/full Node APIs; don't put heavy deps in edge; hours-long work needs Workflow DevKit, not functions.

## Inputs, outputs, tools
- Inputs: function code/config questions, vercel.json edits, error symptoms.
- Outputs: runtime selection, config snippets, diagnostic verdicts.
- Tools: `vercel` CLI/env pull, Vercel dashboard Runtime Logs, `@vercel/functions` waitUntil, Next.js `after`, AI SDK streaming helpers.

## 5 most important rules
1. Runtime choice table is authoritative: nodejs for npm/native/heavy, edge for ultra-low-latency simple logic only (25s hard limit, no Node APIs), bun for CPU-bound latency, rust beta for systems perf.
2. Fluid Compute defaults: 300s all plans, 800s Pro/Enterprise — configure `maxDuration` per route glob in vercel.json.
3. Cron endpoints MUST verify `Bearer ${CRON_SECRET}` — the request is a normal HTTP call anyone could hit.
4. Post-response work goes in `waitUntil`/`after`, never after returning without it; streaming needs explicit ReadableStream/SSE headers.
5. Diagnostics order: check Runtime Logs → env vars (`vercel env pull` for local) → package in dependencies not devDependencies → memory limits (up to 3008MB Pro) → cold-start mitigations (pooling, dynamic imports).

## Risks / things needing the owner
Real deployments incur Active CPU billing; Hobby capped at 300s. Env vars and secrets managed via dashboard/`vercel env`. Cron secret must be set as env var. Choosing wrong runtime causes runtime crashes (edge + fs). No other owner actions.

## Category / tags
cloud · vercel, serverless, edge, functions, cron

## Revisions
Single source read: `C:\Users\a7med\.codex\skills\vercel-functions\SKILL.md` (279 lines). Exists across six tools with same content; codex revision representative.
