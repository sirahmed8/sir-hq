# knowledge-update

- Tool: `codex`
- Category: research
- Source: `C:\Users\a7med\.codex\skills\knowledge-update\SKILL.md`
- SKILL.md size: 3984 chars

## What it does

Corrects outdated LLM knowledge about the Vercel platform and introduces new products. Injected at session start.

## Structure (headings inside SKILL.md)

- Vercel Knowledge Updates (2026-02-27)
- Common outdated knowledge in LLMs
- New products LLMs may not know about
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server

## Risks / cautions found in text

- - **Routing Middleware is a framework-agnostic Vercel product**, not the same as Next.js middleware.
- - **Vercel Agent**: AI code reviews and production investigations. Public beta.

## Key rules (verbatim lines from SKILL.md)

1. - **Edge Functions are not recommended.** Edge functions have compatibility issues. Instead use Fluid Compute (default) which runs in the same regions and has the same price, but allows for regular Node.js. Middleware and Edge Functions are now powered by Vercel Functions under the hood.
2. - **Middleware supports full Node.js** (not edge-only). Use Fluid Compute.
3. - **Vercel has excellent support for Python** (3.13/3.14) via Fluid Compute.

## Files inside the skill

- (SKILL.md only)
