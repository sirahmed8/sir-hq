# knowledge-update

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\knowledge-update\SKILL.md`
- SKILL.md size: 10377 chars

## What it does

Corrects outdated LLM knowledge about the.

## Structure (headings inside SKILL.md)

- Vercel Knowledge Updates (2026-10-08)
- Common outdated knowledge in LLMs
- New products LLMs may not know about
- Current agent SDKs
- Next.js
- Integrations on Vercel
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server

## Risks / cautions found in text

- - **Streaming and SSE are NOT Edge-exclusive.** Streaming responses (`ReadableStream`, Server-Sent Events / `text/event-stream`, AI token streaming) work on the default Node.js runtime with zero config. You do **not** need `runtime = 'edge'` to stream — a common LLM misconception. Stay on Node.js (F
- - **Routing Middleware is a framework-agnostic Vercel product**, not the same as Next.js middleware.
- - **Edge Config is now Global Config** (July 2026). Same store, new name. `@vercel/global-config` replaces `@vercel/edge-config` as a drop-in (reads `GLOBAL_CONFIG`, falls back to `EDGE_CONFIG`); the CLI command is `vercel global-config`. The legacy package still works but cannot read newly connecte
- - **Vercel Daemons**: long-running background workers (queue consumers, Celery/Sidekiq/BullMQ workers, job runners) built from a Dockerfile and declared under the `daemons` key in `vercel.json`. No inbound traffic; production deployments only. Public beta on all plans.

## Key rules (verbatim lines from SKILL.md)

1. - **AI SDK 7** requires Node.js 22 or later and ESM. Verify APIs against the installed package docs under `node_modules/ai/docs/` instead of relying on remembered v6 patterns.
2. - **Official Next.js skills cover workflows, not reference knowledge**: `next-dev-loop`, `next-cache-components-adoption`, `next-cache-components-optimizer`, and the Partial Prefetching skills. Install with `npx skills add vercel/next.js --skill <name>`; propose them before installing.

## Files inside the skill

- (SKILL.md only)
