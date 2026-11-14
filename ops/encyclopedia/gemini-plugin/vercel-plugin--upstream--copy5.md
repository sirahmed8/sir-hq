# upstream

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\react-best-practices\upstream\SKILL.md`
- SKILL.md size: 7251 chars

## What it does

React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

## Structure (headings inside SKILL.md)

- Vercel React Best Practices
- When to Apply
- Rule Categories by Priority
- Quick Reference
- 1. Eliminating Waterfalls (CRITICAL)
- 2. Bundle Size Optimization (CRITICAL)
- 3. Server-Side Performance (HIGH)
- 4. Client-Side Data Fetching (MEDIUM-HIGH)
- 5. Re-render Optimization (MEDIUM)
- 6. Rendering Performance (MEDIUM)
- 7. JavaScript Performance (LOW-MEDIUM)
- 8. Advanced Patterns (LOW)
- How to Use
- Full Compiled Document
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `rendering-hydration-suppress-warning` - Suppress expected mismatches

## Key rules (verbatim lines from SKILL.md)

1. - `async-cheap-condition-before-await` - Check cheap sync conditions before awaiting flags or remote values
2. - `bundle-barrel-imports` - Import directly, avoid barrel files
3. - `bundle-analyzable-paths` - Prefer statically analyzable import and file-system paths to avoid broad bundles and traces
4. - `bundle-defer-third-party` - Load analytics/logging after hydration
5. - `server-dedup-props` - Avoid duplicate serialization in RSC props

## Files inside the skill

- `AGENTS.md` — "React Best Practices"
- `metadata.json`
- `README.md` — "React Best Practices"
- `rules/advanced-effect-event-deps.md` — "t"
- `rules/advanced-event-handler-refs.md` — "t"
- `rules/advanced-init-once.md` — "t"
- `rules/advanced-use-latest.md` — "t"
- `rules/async-api-routes.md` — "t"
- `rules/async-cheap-condition-before-await.md` — "t"
- `rules/async-defer-await.md` — "t"
- `rules/async-dependencies.md` — "t"
- `rules/async-parallel.md` — "t"
- `rules/async-suspense-boundaries.md` — "t"
- `rules/bundle-analyzable-paths.md` — "t"
- `rules/bundle-barrel-imports.md` — "t"
- `rules/bundle-conditional.md` — "t"
- `rules/bundle-defer-third-party.md` — "t"
- `rules/bundle-dynamic-imports.md` — "t"
- `rules/bundle-preload.md` — "t"
- `rules/client-event-listeners.md` — "t"
- `rules/client-localstorage-schema.md` — "t"
- `rules/client-passive-event-listeners.md` — "t"
- `rules/client-swr-dedup.md` — "t"
- `rules/js-batch-dom-css.md` — "t"
- `rules/js-cache-function-results.md` — "t"
- `rules/js-cache-property-access.md` — "t"
- `rules/js-cache-storage.md` — "t"
- `rules/js-combine-iterations.md` — "t"
- `rules/js-early-exit.md` — "t"
- `rules/js-flatmap-filter.md` — "t"
- `rules/js-hoist-regexp.md` — "t"
- `rules/js-index-maps.md` — "t"
- `rules/js-length-check-first.md` — "t"
- `rules/js-min-max-loop.md` — "t"
- `rules/js-request-idle-callback.md` — "t"
- `rules/js-set-map-lookups.md` — "t"
- `rules/js-tosorted-immutable.md` — "t"
- `rules/rendering-activity.md` — "t"
- `rules/rendering-animate-svg-wrapper.md` — "t"
- `rules/rendering-conditional-render.md` — "t"
- `rules/rendering-content-visibility.md` — "t"
- `rules/rendering-hoist-jsx.md` — "t"
- `rules/rendering-hydration-no-flicker.md` — "t"
- `rules/rendering-hydration-suppress-warning.md` — "t"
- `rules/rendering-resource-hints.md` — "t"
- `rules/rendering-script-defer-async.md` — "t"
- `rules/rendering-svg-precision.md` — "t"
- `rules/rendering-usetransition-loading.md` — "t"
- `rules/rerender-defer-reads.md` — "t"
- `rules/rerender-dependencies.md` — "t"
- `rules/rerender-derived-state-no-effect.md` — "t"
- `rules/rerender-derived-state.md` — "t"
- `rules/rerender-functional-setstate.md` — "t"
- `rules/rerender-lazy-state-init.md` — "t"
- `rules/rerender-memo-with-default-value.md` — "t"
- `rules/rerender-memo.md` — "t"
- `rules/rerender-move-effect-to-event.md` — "t"
- `rules/rerender-no-inline-components.md` — "t"
- `rules/rerender-simple-expression-in-memo.md` — "t"
- `rules/rerender-split-combined-hooks.md` — "t"
