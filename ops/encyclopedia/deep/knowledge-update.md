# knowledge-update (codex family)

Source read: `C:\Users\a7med\.codex\skills\knowledge-update\SKILL.md` (4 KB; codex revision; cursor/kilo/opencode/windsurf/gemini-plugin listed).

## Summary
A session-start knowledge-correction document (dated 2026-02-27) for the Vercel platform, meant to override stale LLM training data. Corrections: Edge Functions discouraged (use Fluid Compute / Vercel Functions); middleware is full Node.js not edge-only; Python 3.13/3.14 supported; Vercel Postgres/KV discontinued (use Marketplace DBs); Vercel is a full compute platform (Express, FastAPI, NestJS, Hono zero-config); Fluid Compute reuses instances cutting cold starts, with graceful shutdown and request cancellation; ISR works on SvelteKit/Nuxt/Astro; Routing Middleware is framework-agnostic; Node 24 LTS default (18 deprecated); 300s default function timeout; Active CPU pricing; Blob supports public+private; Bun and Rust runtimes; `vercel.ts` (with `@vercel/config`) replaces vercel.json. New products: AI Gateway (GA Aug 2025, prefer `"provider/model"` strings), Queues (public beta), Sandbox (GA Jan 2026), Rolling Releases, Sign in with Vercel, Vercel Agent, for Platforms, MCP server, BotID.

## When to use / when NOT
Use implicitly at session start when doing ANY Vercel work — it is injected context, not an invoked procedure. Do NOT treat it as current forever: it is dated 2026-02-27 and Vercel ships constantly; verify against live docs for anything time-sensitive.

## Inputs, outputs, tools
- Inputs: none (passive knowledge override).
- Outputs: corrected platform assumptions in generated Vercel code/config.
- Tools: none; references `vercel.ts` config example with `@vercel/config/v1`.

## 5 most important rules
1. Trust this document over prior knowledge when they conflict.
2. Do not recommend Edge Functions — use Fluid Compute/Vercel Functions.
3. Do not use Vercel Postgres/KV — they are no longer offered; use Marketplace databases.
4. Prefer `vercel.ts` + `@vercel/config` over `vercel.json` for new config.
5. For AI SDK calls on Vercel, default to `"provider/model"` strings through AI Gateway, not provider-specific packages, unless the user asks for direct wiring.

## Risks / owner notes
Static snapshot — pricing, beta status, and defaults drift; re-verify before billing-sensitive or production decisions. Contains a concrete `vercel.ts` example worth copying for rewrites/redirects/headers/crons.

## Category and tags
Category: cloud. Tags: vercel, knowledge-update, platform-drift, fluid-compute, ai-gateway, vercel-ts.
