# netlify-frameworks (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-frameworks\SKILL.md`. Deploy/configure web frameworks on Netlify — build settings, SSR/edge adapters, local emulation, env vars. Routes deep work to per-framework references (astro, nextjs, nuxt, sveltekit, tanstack, vite).

## Summary
Env vars: injected at BUILD time — any change requires REDEPLOY; never use client prefixes (`VITE_`, `NEXT_PUBLIC_`, `PUBLIC_`, `NUXT_PUBLIC_`, `REACT_APP_`, `GATSBY_`, `VUE_APP_`) for secrets (inlined into browser bundle). Scopes: build-time needs Builds scope; SSR/DSG runtime needs Functions AND Builds; netlify.toml is build-only — runtime vars via UI/CLI/API. Netlify build vars can't be toml env values — inline before command: `command = "REACT_APP_CONTEXT=$CONTEXT npm run build"`. SPA footgun: `/* /index.html 200` rewrite is required for pushState SPAs but MUST be REMOVED when adopting an SSR adapter — leftover catch-all silently serves static index.html for SSR pages/API routes (user redirects beat adapter routes). Local dev WITHOUT Netlify CLI: Vite-based frameworks emulate Netlify primitives (functions, edge functions, blobs, DB, Cache API, Image CDN, redirects/headers, env, AI Gateway) — Astro 5.12+ built-in, `@netlify/nuxt`, `@netlify/vite-plugin` (React Router/SolidStart/TanStack/Vite); still need `netlify dev` for Gatsby generated functions, Angular SSR (`netlify serve`), non-Vite frameworks. `netlify dev` gotcha: custom `command`+`targetPort` needs `framework = "#custom"` or detector silently ignores your command. Build table: per-framework command/publish (Next SSR `.next` vs static `out`+`NETLIFY_NEXT_PLUGIN_SKIP`, Nuxt3 `dist`, Gatsby `public`, Hydrogen `dist/client`, React Router `build/client`, etc.).

## When to use / when NOT
Use when setting up/fixing framework deploys, SSR/edge adapters, middleware on Netlify context, SPA catch-alls, build command/publish dir, env-var-not-updating bugs, framework build failures. NOT for framework-agnostic config (→ netlify-config) or env var management generally (→ env-vars skill).

## Inputs, outputs, tools
- Inputs: framework choice, SSR vs static, env vars, local-dev preference.
- Outputs: correct build/publish settings, adapter wiring, redirect rules, dev-server config.
- Tools: per-framework Netlify plugins/adapters, `@netlify/vite-plugin`, `netlify dev`, references/*.md per framework.

## 5 most important rules
1. Env changes need a redeploy; client prefixes expose secrets — never for secrets.
2. SSR needs Functions+Builds scopes; toml vars are build-time only.
3. Remove SPA `/*→index.html` catch-all BEFORE SSR adapter or it shadows SSR routes.
4. Vite-plugin frameworks emulate Netlify locally without the CLI; others need `netlify dev`.
5. `framework="#custom"` required when `[dev]` has custom command+targetPort.

## Risks / owner notes
Secret leakage via client-prefixed vars is the big one. Silent SSR shadowing by stale SPA redirects wastes hours. Build/publish mismatches are the most common deploy failure.

## Category and tags
Category: cloud. Tags: netlify, frameworks, ssr, env-vars, vite-plugin, spa-redirects, build-settings.
