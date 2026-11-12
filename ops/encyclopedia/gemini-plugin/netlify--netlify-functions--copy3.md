# netlify-functions (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-functions\SKILL.md`. TypeScript/JS/Go serverless functions on Netlify.

## Summary
Modern default: `.mts` TS / `.mjs` JS default-export handler `(req: Request, context: Context) => Response` from `@netlify/functions`; legacy AWS Lambda shape only for Go/migration. Locations: `netlify/functions/` (outside publish dir or source ships as static assets); one file OR subdir whose entry is `index` or matches dir name — `hello.mts`, `hello/hello.mts`, `hello/index.mts` all → `hello`. Module format: `.mts`/`.mjs`=ESM, `.cts`/`.cjs`=CJS, `.ts`/`.js` follow package.json `"type"`. CRITICAL: same-name JS+TS → JS silently wins, TS ignored. Minimal function needs no config (serves at `/.netlify/functions/<name>`); env via `Netlify.env.get()` (needs Functions scope; toml vars NOT available; values frozen per deploy — change+redeploy); response headers set IN CODE on the Response — `[[headers]]`/`_headers`/redirect headers apply ONLY to static CDN responses, never function responses; don't add CORS unless asked. Custom routes: `config.path` (URLPattern syntax, `:param`→`context.params`, `excludedPath`, `preferStatic`, `method` restriction) — when set, function serves ONLY at that path. Also covers fetchable module shape, background functions (15min), scheduled/cron functions, event-triggered functions (deploy/form), rate limiting, region/memory config, Identity auth hooks, `netlify dev` local testing.

## When to use / when NOT
Use for API endpoints/backend routes, form handlers, auth/Identity hooks, streaming/AI proxies, cron jobs, long background jobs, deploy/form event reactions, rate limiting, env/secret access in functions. NOT for edge-runtime needs (→ netlify-edge-functions) or static-only sites.

## Inputs, outputs, tools
- Inputs: handler code, route config, env vars (Functions scope), method restrictions.
- Outputs: HTTP responses at `/.netlify/functions/*` or custom paths; scheduled/event-triggered runs.
- Tools: `@netlify/functions` types, `Netlify.env.get()`, `netlify dev`, URLPattern routing, background/scheduled function config.

## 5 most important rules
1. One file per function name — same-name `.js`+`.ts` silently deploys only the JS.
2. Keep `netlify/functions/` OUTSIDE the publish directory.
3. `config.path` reroutes exclusively — function then serves ONLY at that path.
4. Function response headers live in code; static header files don't apply; toml env vars invisible at runtime.
5. Env var scope must include Functions; values freeze per deploy — redeploy to change.

## Risks / owner notes
Silent TS-ignored-by-JS is a classic trap. Missing Functions scope = env vars undefined at runtime. `preferStatic`/`excludedPath` ordering bugs cause surprising routing. Background functions have 15-min cap.

## Category and tags
Category: cloud. Tags: netlify, functions, serverless, typescript, routing, env-vars, background-functions, cron.
