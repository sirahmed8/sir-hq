# vercel-functions

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-functions\SKILL.md`
- SKILL.md size: 37292 chars

## What it does

Configure and optimize serverless Vercel.

## Structure (headings inside SKILL.md)

- Vercel Functions
- Prefer Node.js over the Edge runtime
- The default to reach for
- Reasons people reach for Edge — and what to do instead
- What Edge actually costs you
- Migrating an existing Edge function
- Function Types
- Node.js (the default)
- Bun
- Python
- Rust
- Container images (Docker)
- Edge (legacy — not recommended)
- Choosing a Runtime
- Fluid Compute
- Instance Sizes (memory / CPU)
- Settings precedence
- Background Processing with `waitUntil`
- Next.js `after` (equivalent)
- Graceful shutdown and request cancellation
- Duration and Long-Duration Functions
- Duration limits
- Setting `maxDuration`
- Extended max duration (30 minutes) — Beta
- Keeping a long request alive
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Automatic cold start optimization**: function pre-warming plus **bytecode caching** on Node.js 20+. Bytecode caching applies to **production only** — not dev or preview, so don't benchmark cold starts in a preview deployment.
- - **With Fluid Compute enabled, memory cannot be set in `vercel.json`** — setting it there produces a build-time warning. Set it in the dashboard instead: Settings → Functions → Advanced Settings → **Function CPU**, then redeploy. (The `memory` key still exists for legacy non-Fluid deployments, whic
- - More memory also means more CPU, which can *reduce* Active CPU billing for CPU-bound work by finishing sooner — but it raises Provisioned Memory cost while requests are in flight.
- - **Scale to zero** after 5 minutes without traffic in production, 30 seconds in preview. Cold starts are real; do not assume a warm process.

## Key rules (verbatim lines from SKILL.md)

1. - No `fs`, no native modules, no `require()` — ESM only, and most npm packages with Node.js dependencies simply will not load
2. - **Code size limit after gzip: 1 MB (Hobby), 2 MB (Pro), 4 MB (Enterprise)** — versus 250 MB uncompressed (up to 5 GB) on Node.js
3. - Must begin sending a response within **25 seconds** (it may then stream for up to 300s). The 300s/800s/1800s duration limits below apply to the Node.js, Bun, and Python runtimes — **not** to Edge
4. - **Optimized concurrency**: multiple invocations share one instance instead of one microVM per request. Vercel prioritizes idle existing resources before allocating new ones. Available on the Node.js and Python runtimes.
5. - **Automatic cold start optimization**: function pre-warming plus **bytecode caching** on Node.js 20+. Bytecode caching applies to **production only** — not dev or preview, so don't benchmark cold starts in a preview deployment.

## Files inside the skill

- (SKILL.md only)
