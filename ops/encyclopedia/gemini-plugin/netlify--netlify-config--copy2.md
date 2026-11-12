# netlify-config (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-config\SKILL.md`. Build/routing config via netlify.toml, _redirects, _headers.

## Summary
Three config files: `netlify.toml` (build, contexts, plugins, functions, redirects, headers, dev — takes precedence over UI), `_redirects` and `_headers` (plain-text, saved to the PUBLISH directory). Paths in toml are absolute from base dir. Modern-vs-legacy: `node_bundler = "esbuild"` (zisi legacy; TS always esbuild); `status = 302` (307 unsupported); `NETLIFY_IMAGE_CDN` not deprecated `GATSBY_CLOUD_IMAGE_CDN`; `key = "$VAR"` env injection NOT supported in TOML (except signed proxy redirects) — use build-command sed or build plugin. `[build]` runs in Bash; context keys apply to `[build]` and `[[plugins]]` but NOT `[[redirects]]`/`[[headers]]` (always global). Precedence least→most: UI < toml < any-context < `[context.<name>]` < `[context.branchname]`. Redirects: `_redirects` processed first then toml, first-match-top-down wins (specific before general); edge functions run before redirects; SPA fallback `/* /index.html 200`. `_redirects` syntax: `from to [status] [conditions]` with splats `:splat`, placeholders `:param`, query `param=:id`, force `!`, conditions `Country=`, `Language=`, `Role=`, `Cookie=`. `[[redirects]]` keywords: from/to/status(301 default)/force/query/conditions/headers/signed. Gotchas cover monorepo base dirs, secrets handling, functions bundling, dev server.

## When to use / when NOT
Use for build command/publish dir, redirects/rewrites/proxies, SPA fallback, response headers/basic-auth, env vars/secrets, per-context vars, functions bundling, build ignores, monorepos/JS SPAs. NOT for deploy lifecycle (→ netlify-deploy) or caching headers specifically (→ netlify-caching).

## Inputs, outputs, tools
- Inputs: framework/build setup, routing rules, env vars, branch/deploy-context needs.
- Outputs: `netlify.toml`, `_redirects`, `_headers` files at repo root (or package dir for monorepos).
- Tools: Netlify build system, edge functions (run before redirects), build plugins.

## 5 most important rules
1. toml beats UI on conflicts; `_redirects`/`_headers` live in the PUBLISH dir, not repo root.
2. First matching redirect wins — order specific before general; edge functions precede redirects.
3. `[[redirects]]`/`[[headers]]` are global-only (no per-context); `[build]`/`[[plugins]]` are context-aware.
4. No `$VAR` injection in TOML; no `307` status; esbuild bundler; `NETLIFY_IMAGE_CDN`.
5. `[skip ci]`/`[skip netlify]` in commit message or PR title controls deploy skipping.

## Risks / owner notes
Secrets in toml env vars aren't deploy-env available and toml is committed — keep sensitive values out. Shadow (`200!`) redirects can mask real 404s. Monorepo base-dir mistakes break paths.

## Category and tags
Category: cloud. Tags: netlify, toml, redirects, headers, build-config, spa-fallback, monorepo, env-vars.
