# auth0

Source read: `C:\Users\a7med\.gemini\config\plugins\auth0\skills\auth0\SKILL.md` (gemini-plugin auth0 2.6.0 installed copy; a newer 2.8.0 exists in the plugin cache — see Revisions), plus its references/ tree (~60 framework-*, feature-*, pattern-*, tooling-* hubs), scripts/, agents/, assets/.

## Summary
Auth0's official agent skill (Apache-2.0, by Auth0) for integrating and operating Auth0. Its core method is a four-step router: detect intent (integrate, feature:mfa, feature:passkeys, feature:organizations, feature:enterprise-connect, feature:universal-portals, feature:custom-domains, feature:acul, feature:branding, feature:dpop, feature:custom-token-exchange, feature:token-vault, audit, healthcheck, guidance, debug, debug:rate-limit, migrate, upgrade-sdk, tooling), detect the framework from installed SDK packages or workspace deps, detect tooling (CLI default, MCP if active, Terraform if .tf files, Vercel integration if requested), then load only 2-3 reference files from ~60 hubs instead of dumping everything into context.

## When to use / when NOT
Use for any Auth0 task: adding login to an app in ~45 supported frameworks (Next.js, React, Vue, Angular, Expo, Flutter, .NET, Java, PHP/Laravel, Python, Go, Swift, Android, KMP...), tenant features (MFA, passkeys, organizations, enterprise SSO, custom domains, branding/ACUL, DPoP, token vault, custom token exchange), migrations from other providers, tenant audits/health checks, SDK major-version upgrades, and CLI automation. Do NOT use it for non-Auth0 auth providers (use the `auth` skill for Clerk/Descope/Better Auth), and do NOT skip the intent/framework detection steps — loading the wrong reference hub produces wrong SDK calls.

## Inputs, outputs, tools
- Inputs: the developer's goal in plain language, the project's dependency files (package.json, requirements.txt, pom.xml, composer.json, *.csproj, pubspec.yaml, Package.swift, go.mod), presence of `terraform/` or an Auth0 MCP server.
- Outputs: a chosen intent + framework + tooling triple and 2-3 reference file paths to read; then SDK code/config produced by following those references.
- Tools: `auth0` CLI (brew install, macOS/Linux per metadata — not installed by default on this Windows machine), Auth0 MCP server (optional), Terraform provider, Vercel Marketplace integration. References live under `references/framework-{x}/`, `references/feature-{x}/`, `references/pattern-{x}/`, `references/tooling-{x}/`.

## 5 most important rules
1. **Detect intent first, from plain language** — the intent string is a lookup key; e.g. "second step after password" → `feature:mfa`, "work email routes to employer login" → `feature:enterprise-connect`.
2. **Framework detection is tiered**: Auth0 SDK package in deps → non-Auth0 workspace deps → framework named in the prompt; workspace signals outrank the prompt on conflict, and web-app vs API variant is chosen intent-first (ask if ambiguous).
3. **Load only 2-3 reference files** — never read the whole tree; each intent section in Step 4 lists exactly what to read.
4. **`tooling` intent skips framework detection** — CLI-only tasks (create apps/APIs, script tenant setup) load only `tooling-cli` unless a framework question appears.
5. **Audit/healthcheck have guardrails** — apply findings only with per-command confirmation, verify each change by re-fetch, and never quote Enterprise pricing.

## Risks / owner notes
The `auth0` CLI is required for tenant configuration and is declared for macOS/Linux only — on this Windows PC it likely needs WSL or manual install; MCP/Terraform paths need owner setup. Audit intent can change a live tenant — every mutation requires explicit per-command confirmation. Enterprise Connect/Organizations touch real customer identity; plan choice affects billing.

## Category / tags
security · authentication, auth0, oauth, oidc, mfa, passkeys, organizations, enterprise-sso, nextjs, migration, audit

## Revisions
Installed plugin copy is metadata version 2.6.0; a newer 2.8.0 exists in the plugin cache (per earlier slice notes). The 2.8.0 revision is preferable — same router design with updated references — but the installed 2.6.0 SKILL.md was the readable source here and the method is unchanged.
