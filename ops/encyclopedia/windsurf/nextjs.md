# nextjs

Tools: claude, codex, cursor, kilo, opencode, windsurf (claude copy used per preference rule; it has the fullest references set).
Source: C:\Users\a7med\.claude\skills\nextjs\SKILL.md + references/ (21 topic files, ~79 KB)

## Summary
A rulebook-style skill for writing and reviewing Next.js App Router code. The SKILL.md is an index: each section points to a dedicated reference file covering file conventions, RSC boundaries, async APIs, runtime selection, directives, functions, error handling, data patterns, route handlers, metadata/OG, image/font optimization, bundling, scripts, hydration errors, Suspense boundaries, parallel/intercepting routes, self-hosting, and debug tricks.

## When to use / not use
Use for any Next.js App Router implementation or review — the description explicitly triggers on Server Components, Server Actions, layouts, routing, deployment. Not for Pages Router apps, other frameworks, or infra work; it complements (does not replace) feature-specific skills like `next-cache-components` or `next-upgrade`.

## Inputs, outputs, dependencies
Input: Next.js code or questions about it. Output: correct App Router patterns (v15+/v16 semantics: async params/searchParams/cookies/headers, middleware renamed to `proxy` in v16). Needs: reading the relevant `references/*.md` file on demand — the skill is designed to be navigated, not memorized.

## Key rules (from the index)
1. Always read the matching reference file before answering — the SKILL.md itself contains no code rules, only pointers.
2. v15+ made `params`, `searchParams`, `cookies()`, `headers()` async — the async-patterns file covers migration.
3. Keep RSC boundaries clean: no async client components, no non-serializable props.
4. Default to Node.js runtime; Edge only when justified (runtime-selection.md).
5. Prefer `next/image`, `next/font`, `next/script` over raw HTML equivalents; see bundling.md for server-incompatible packages.

## Risks / owner items
- The skill is a large multi-file bundle; an agent that only reads SKILL.md gets pointers, not answers — must follow links.
- References cover up to v16 conventions (middleware→proxy rename); verify against the project's actual Next version.
- Some references are long (metadata.md 7 KB, self-hosting.md 8 KB); reading all 21 files costs significant context — read only the relevant one.

## Category and tags
build, web — nextjs, app-router, react-server-components, best-practices, reference.

## Revision note
claude copy chosen (has all 21 references). codex copy also exists with references; kilo/cursor/windsurf copies point to the same content family. claude revision is the most complete documented set.
