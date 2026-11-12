# vercel-services (gemini-plugin: vercel)

## Summary
vercel-services configures Vercel's `services` model (Beta, all plans): multiple tightly-coupled components (frontend + backend) as independently-built services that ship as ONE deployment with skew protection, synced previews, atomic rollbacks, and private service-to-service bindings. Decision table first: use Services for coupled multi-component apps; one Next.js app with Route Handlers does NOT need it; independently-deployed services want separate monorepo projects; independently-deployed frontends rendering as one site want Microfrontends. Configuration: `services` map in vercel.json with per-service `root`/`entrypoint`/`framework`, top-level ordered `rewrites` as public ingress (a service with no top-level rewrite is private — reachable only via bindings), `bindings` for private service URLs injected as env vars (deployment-aware, skip Firewall/Protection/CDN, billed as Service Requests), `runtime:"container"` for Docker/OCI. Routing subtleties: rewrites evaluated in order, routing is FINAL (service 404 doesn't fall through), original path is preserved (strip prefixes with service-scoped rewrites), SPA deep-links need service-scoped catch-all to /index.html, host-matched rewrites for subdomains don't work on single-host previews (keep subpath rewrite + relative URLs). `vercel dev` injects local binding vars; `vercel dev -L` for local-only.

## When to use / when NOT
Use when one app genuinely needs multiple runtimes/frameworks deployed atomically. Do NOT split one framework into arbitrary processes, don't use for independent deploy cadences (separate projects), and don't confuse with `experimentalServices` (older model — read its reference before migrating; vercel.json accepts only one).

## Inputs, outputs, tools
- Inputs: app architecture decision, vercel.json service/rewrites/bindings config.
- Outputs: multi-service deployment config, binding env vars, routing rules.
- Tools: vercel.json, `vercel dev`, `vercel` deploy, references/experimental-services.md.

## 5 most important rules
1. Public exposure = top-level rewrites ONLY; bindings give network reachability, NOT app auth — add service-level authorization.
2. Rewrite order matters and is final: specific rules before catch-all; no fallthrough on service 404.
3. Service code sees the ORIGINAL path — strip `/api` prefixes via service-scoped rewrites or backend root_path.
4. Binding vars exist at runtime only — never in builds or Routing Middleware; declare on the CALLER service.
5. Go/Rust native runtimes can't consume bindings — use container services for those callers; Node/Python can.

## Risks / things needing the owner
Beta feature — say so when recommending. Misordered rewrites or missing catch-alls cause silent 404s; subdomain setups break previews if subpath fallback is forgotten. Deploys ship ALL services together (that's the point but also the constraint). `vercel link`/deploy auth is owner territory.

## Category / tags
cloud · vercel, microservices, deployment, beta

## Revisions
Single revision read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-services\SKILL.md` (183 lines). Gemini-plugin only.
