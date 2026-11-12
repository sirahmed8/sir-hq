# react-best-practices

Tools: claude (also codex/cursor/opencode/windsurf copies; claude chosen). Source: C:\Users\a7med\.claude\skills\react-best-practices\SKILL.md (140 lines) + rules/ directory (64 rule files) + AGENTS.md

## Summary
Vercel's official React/Next.js performance rulebook: 64 rules across 8 impact-ordered categories — eliminating waterfalls (CRITICAL), bundle size (CRITICAL), server-side perf (HIGH), client fetching, re-render optimization, rendering, JS micro-perf, advanced patterns. Each rule has a dedicated file with wrong/right examples.

## When to use / not use
Reference when writing new React components/Next.js pages, implementing data fetching, reviewing for perf issues, or refactoring. Not for non-React frameworks or backend-only work; rule files are the detail layer, SKILL.md is the index.

## Inputs, outputs, dependencies
Input: React/TSX code to write or review. Output: code following the categorized rules. Needs: the rules/*.md files for specifics; targets React + Next.js App Router patterns (RSC, SWR, next/dynamic, Suspense).

## Key rules (top-impact subset)
1. Kill waterfalls first: parallelize independent awaits (Promise.all), defer awaits into branches, use Suspense boundaries — the two CRITICAL categories are waterfalls and bundle size.
2. Bundle discipline: no barrel imports, dynamic-import heavy components, defer third-party/analytics until after hydration.
3. Server-side: React.cache() per-request dedup, hoist static I/O to module level, minimize RSC→client serialization, use after() for non-blocking work.
4. Re-render hygiene: derive state during render not effects, functional setState, primitive effect deps, split hooks by dependency, startTransition for non-urgent updates.
5. JS micro-perf last: Set/Map lookups, combine filter/map passes, hoist RegExp, early exits — LOW priority, apply after structural wins.

## Risks / owner items
- 64 rules is a review checklist, not a mandate to apply all — impact ordering exists precisely to prioritize.
- Some rules are Next.js-specific (server-*, RSC props); pure client React only uses subsets.
- Rules assume modern React (Activity, useDeferredValue, toSorted) — check project's React version before applying advanced-* rules.

## Category and tags
web, build — react, nextjs, performance, best-practices, vercel.

## Revision note
Identical index across tools; authoritative revision is this compiled rule set with per-rule detail files.
