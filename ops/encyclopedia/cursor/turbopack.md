# turbopack (codex/cursor/kilo/windsurf/opencode copies)

## Summary
turbopack is an expert-guidance skill for Turbopack, Vercel's Rust bundler that is the DEFAULT bundler in Next.js 16 (webpack still supported via `bundler: 'webpack'`). It covers: key features (instant O(1) HMR, stable file-system dev caching up to 14x faster restarts in 16.1+, multi-environment builds, native RSC); Next.js 16 config shape (top-level `turbopack` key — `resolveAlias`, `resolveExtensions`, `rules`, moved out of `experimental.turbopack`); CSS handling (global CSS, CSS Modules, PostCSS/Tailwind v4 zero-config, Sass via the `sass` package, ordering pitfalls vs webpack); tree shaking (module-level, `sideEffects: false`, barrel-file optimization, `import()` chunk boundaries, bundle analyzers); migrating webpack loaders (built-in equivalents table, `turbopack.rules` for the rest like `@svgr/webpack`, `?raw` imports, native Workers); production diagnostics (env-boundary errors, `server-only` package, build comparisons); and performance profiling (`NEXT_TURBOPACK_TRACING=1` → trace.json for dev and build, OOM mitigations).

## When to use / when NOT
Use when configuring the Next.js bundler, optimizing HMR, debugging Turbopack build issues, migrating webpack config/loaders, or understanding Turbopack-vs-webpack differences. Do NOT use for non-Next.js bundling (Vite/esbuild projects), for React code issues unrelated to bundling, or for webpack-specific debugging while Turbopack is the bundler.

## Inputs, outputs, tools
- Inputs: a Next.js 16 project, its next.config, postcss/sass configs, and the build/dev symptoms.
- Outputs: corrected next.config, migrated loaders/rules, profiling traces, and diagnosed build failures.
- Tools: `next dev`/`next build`, `NEXT_TURBOPACK_TRACING=1`, `ANALYZE=true` or `experimental.bundleAnalyzer`, `server-only` package, chrome://tracing/Perfetto for trace.json. Pure guidance — no bundled scripts.

## 5 most important rules
1. Config moved: use top-level `turbopack` in Next.js 16, not `experimental.turbopack`; a leftover `webpack()` function is ignored and can mask real config.
2. Turbopack has no webpack loaders: use built-ins (CSS, sass, postcss, assets, `?raw`, native Worker) or `turbopack.rules`; if truly impossible, `bundler: 'webpack'` is the escape hatch.
3. Environment boundaries are enforced: `fs`/`path` etc. cannot appear in client/edge bundles — use `server-only` to fail fast on violations.
4. CSS ordering differs from webpack; don't rely on cross-file source-order specificity — use CSS Modules or more specific selectors.
5. Profile before optimizing: `NEXT_TURBOPACK_TRACING=1` produces trace.json; look for slow transforms, huge module graphs (barrel files) and cache misses from files that change every build.

## Risks / things needing the owner
`bundler: 'webpack'` opt-out exists but abandons the default path; loader-parity gaps are real (file issues upstream). Build caching is dev-only so far; don't promise production build-cache wins. Switching bundlers on a live product needs a full regression pass. Nothing needs the owner.

## Category / tags
web · nextjs, turbopack, bundler, webpack, performance, frontend

## Revisions
Five copies exist (codex, cursor, kilo, windsurf, opencode; no claude copy). Identical content. Best revision: the codex copy (used here).
