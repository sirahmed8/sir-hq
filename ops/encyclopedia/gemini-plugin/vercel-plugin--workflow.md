# workflow (codex revision — Vercel Workflow DevKit)

## Summary
workflow is comprehensive guidance for Vercel's Workflow DevKit — durable, crash-safe orchestration via `"use workflow"` (durable function, runs in a sandboxed VM) and `"use step"` (full Node.js, auto-retry, persisted results) directives. CRITICAL first rule: your knowledge is outdated — ALWAYS search bundled docs in `node_modules/workflow/docs/` (and @workflow/ai, @workflow/core, @workflow/next docs) before writing code. Core patterns: put ALL logic in steps (full Node access, AI SDK works) and keep workflow functions orchestration-only; sandbox limitations table (no fetch/setTimeout/Node modules in workflow context — use `import {fetch} from "workflow"` + `globalThis.fetch = fetch`, `sleep("5s")`); `start()` from API routes but NEVER directly in workflow context (wrap in a step); Hooks (`createHook` deterministic token + `resumeHook` from routes; `createWebhook` random token only; hooks are AsyncIterable for multi-event); serialization rules (plain data only, no functions/class instances); streaming via `getWritable()` (callable in both contexts but I/O only in steps; namespaced streams for logs vs results); errors (`FatalError` no-retry vs `RetryableError` with retryAfter); DurableAgent for AI agents in workflows (handles fetch itself, tool executes needing Node go in steps); debugging (`npx workflow health/web/inspect runs|run|cancel`, `--backend vercel --project --team`); testing via `@workflow/vitest` plugin (waitForHook/waitForSleep/wakeUp/resumeWebhook, vi.mock doesn't work in integration tests).

## When to use / when NOT
Use for durable multi-step jobs, long-running processes, pause/resume on external events, AI agent orchestration, webhook ingestion — anything needing crash-safe retries beyond function maxDuration. Do NOT use for simple request/response (plain functions suffice), don't call start() inside workflow context, and don't trust memory — read the bundled docs first.

## Inputs, outputs, tools
- Inputs: workflow design (steps, hooks, streams, retries).
- Outputs: workflow/step functions, API routes calling start/resume, tests.
- Tools: `workflow` + `workflow/api` packages, `@workflow/ai` DurableAgent, `@workflow/vitest`, `npx workflow` CLI (health/web/inspect/cancel), framework integrations (next/vite/astro/nitro).

## 5 most important rules
1. READ `node_modules/workflow/docs/**/*.mdx` FIRST — the skill's own knowledge is declared outdated; docs match the installed version.
2. Steps = full Node.js + auto-retry + persisted results; workflows = sandboxed orchestration only. Logic goes in steps.
3. `start()` cannot run in workflow context — wrap in a step; it returns immediately (fire-and-forget), await via run.returnValue.
4. Only serializable data crosses workflow/step boundaries; FatalError stops retries, RetryableError retries (use retryAfter for 429s).
5. getWritable streams need step functions for actual I/O; namespaced streams separate verbose logs from replay-worthy results; only import APIs you use (unused imports → 500s).

## Risks / things needing the owner
Durable runs bill as function duration + workflow orchestration; long sleeps/hooks hold runs open. Hook tokens are security boundaries — deterministic tokens must be unguessable. Testing needs the vitest plugin config; vi.mock silently fails in integration tests. Deploy target config (--backend/--project/--team) needed for Vercel inspection. No other owner actions.

## Category / tags
cloud · vercel, workflows, durable-execution, orchestration, ai-agents

## Revisions
Single source read: `C:\Users\a7med\.codex\skills\workflow\SKILL.md` (553 lines). Six-tool skill; codex revision representative.
