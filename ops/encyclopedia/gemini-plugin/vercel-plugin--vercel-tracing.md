# vercel-tracing (gemini-plugin: vercel)

## Summary
vercel-tracing configures OpenTelemetry tracing on Vercel: register `@vercel/otel` once from the framework's server startup hook (Next.js `instrumentation.ts` `register()` → `registerOTel({serviceName})`), deploy, exercise a server route, then find/inspect spans with `vercel traces` CLI. Workflow: register SDK → exercise route → `vercel traces search` (team-wide, `--project`/`--scope` to narrow) → `inspect` (timeline/tree/waterfall). Investigation discipline is the heart: measure BEFORE optimizing — wrap suspected operations in `startActiveSpan` custom spans, deploy, read exact durations as baseline, fix the measured cause keeping its span, compare after. Only server-executed requests produce spans — static/prerendered/CDN-cache hits have NO application spans (optimize those with caching/CWV instead). 13 reference files: collection, instrumentation, nextjs, sveltekit, library-spans (AI SDK/Flags/Workflow/DB clients), custom-spans, context-propagation, configuration, capture, search, inspection, performance, troubleshooting.

## When to use / when NOT
Use for setting up or debugging Vercel tracing, finding slow/failed spans, or performance investigation of server routes. Do NOT use for static page performance (no spans exist), don't register a second OTel provider if Sentry v8+/existing setup found, and don't change sampling just to debug one issue.

## Inputs, outputs, tools
- Inputs: framework/version, existing telemetry setup, route/symptom to investigate.
- Outputs: `registerOTel` wiring, custom spans, `vercel traces` JSON results, before/after timing reports.
- Tools: `@vercel/otel`, `@opentelemetry/api`, `vercel traces` CLI (auto `--non-interactive` JSON for agents), 13 reference docs.

## 5 most important rules
1. Check existing setup first — extend an existing provider, NEVER register a second one.
2. Verify with DEPLOYED traces, not local exporter checks; span names/parents via inspect, service.name via search JSON.
3. Measure first: code reading finds candidates, traces show which dominates — report gains as estimates until deployed spans confirm.
4. Empty sampled results ≠ request never happened; distinguish auth/API failures from empty searches; don't alter sampling to investigate.
5. `search` is team-scoped (all projects) — use `--project`/`--scope`; `inspect`/`config` stay project-scoped; agent mode prints JSON and rejects `--columns`.

## Risks / things needing the owner
Tracing adds minor overhead; sampling config changes affect observability billing/retention (Observability Plus extends retention). Production capture needs `--yes`. Deploying instrumentation is a real deploy. Otherwise low risk.

## Category / tags
cloud · vercel, opentelemetry, tracing, observability, performance

## Revisions
Single revision read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-tracing\SKILL.md` (70 lines + 13 references). Gemini-plugin only.
