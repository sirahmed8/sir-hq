# auth0

- Tool: `gemini-plugin` (plugin: `auth0`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\auth0\skills\auth0\SKILL.md`
- SKILL.md size: 20584 chars

## What it does

Authenticate users and protect Next.js.

## Structure (headings inside SKILL.md)

- Auth0
- Step 1: Detect intent
- If nothing clearly matches
- Step 2: Detect framework
- Tier 1 — Auth0 SDK already installed (strongest signal)
- Node.js / JavaScript / TypeScript — check `package.json` → `dependencies`
- Python — check `requirements.txt` or `pyproject.toml`
- Java / Kotlin — check `build.gradle` or `pom.xml`
- .NET — check `*.csproj` or `NuGet.Config`
- PHP — check `composer.json`
- Go — check `go.mod`
- Mobile (native)
- Tier 2 — Framework from non-Auth0 workspace dependencies
- Tier 3 — Framework from the prompt
- Variant disambiguation (web app vs API)
- If nothing matched
- Conflicts
- Step 3: Detect tooling
- Step 4: Load reference files
- integrate
- feature:mfa
- feature:passkeys
- feature:organizations
- feature:enterprise-connect
- feature:universal-portals
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)


## Files inside the skill

- `agents/openai.yaml`
- `assets/acul/js-templates/login-id.js`
- `assets/acul/js-templates/login-password.js`
- `assets/acul/react-templates/login-id.tsx`
- `assets/acul/react-templates/login-password.tsx`
- `assets/acul/theme-templates/globals.css`
- `assets/acul/theme-templates/tailwind.config.ts`
- `assets/acul/theme-templates/theme-provider.ts`
- `assets/acul/theme-templates/tokens.css`
- `assets/audit/report-template.html`
- `assets/audit/report-template.md` — "Locked report skeleton (Auth0 Platform Development Review)"
- `assets/healthcheck/report-template.html`
- `assets/healthcheck/report-template.md` — "Auth0 Tenant Health Check — {{customer_name}}"
- `references/feature-acul/index.md` — "ACUL Screen Generator"
- `references/feature-audit/index.md` — "Auth0 tenant audit (CheckMate) — full workflow"
- `references/feature-audit-pricing/index.md` — "Auth0 Pricing"
- `references/feature-audit-remediation/index.md` — "Auth0 tenant audit — remediation reference"
- `references/feature-branding/index.md` — "Auth0 Branding"
- `references/feature-custom-domains/index.md` — "Auth0 Custom Domains"
- `references/feature-custom-token-exchange/auth0-android.md` — "Auth0.Android — Custom Token Exchange"
- `references/feature-custom-token-exchange/auth0-api-python.md` — "auth0-api-python — Custom Token Exchange (server-side / OBO)"
- `references/feature-custom-token-exchange/auth0-auth-js.md` — "@auth0/auth0-auth-js — Custom Token Exchange"
- `references/feature-custom-token-exchange/auth0-react.md` — "@auth0/auth0-react — Custom Token Exchange"
- `references/feature-custom-token-exchange/auth0-server-js.md` — "@auth0/auth0-server-js — Custom Token Exchange"
- `references/feature-custom-token-exchange/auth0-server-python.md` — "auth0-server-python — Custom Token Exchange"
- `references/feature-custom-token-exchange/auth0-spa-js.md` — "@auth0/auth0-spa-js — Custom Token Exchange"
- `references/feature-custom-token-exchange/auth0-swift.md` — "Auth0.swift — Custom Token Exchange"
- `references/feature-custom-token-exchange/index.md` — "Auth0 Custom Token Exchange"
- `references/feature-custom-token-exchange/nextjs-auth0.md` — "@auth0/nextjs-auth0 — Custom Token Exchange"
- `references/feature-custom-token-exchange/react-native-auth0.md` — "react-native-auth0 — Custom Token Exchange"
- `references/feature-dpop/index.md` — "Auth0 DPoP (Device-Bound Tokens)"
- `references/feature-enterprise-connect/auth0-angular.md` — "@auth0/auth0-angular — Enterprise Connect"
- `references/feature-enterprise-connect/auth0-express.md` — "@auth0/auth0-express — Enterprise Connect"
- `references/feature-enterprise-connect/auth0-react.md` — "@auth0/auth0-react — Enterprise Connect"
- `references/feature-enterprise-connect/auth0-server-js.md` — "@auth0/auth0-server-js — Enterprise Connect"
- `references/feature-enterprise-connect/auth0-server-python.md` — "auth0-server-python — Enterprise Connect"
- `references/feature-enterprise-connect/auth0-spa-js.md` — "@auth0/auth0-spa-js — Enterprise Connect"
- `references/feature-enterprise-connect/auth0-vue.md` — "@auth0/auth0-vue — Enterprise Connect"
- `references/feature-enterprise-connect/index.md` — "Auth0 Enterprise Connect"
- `references/feature-enterprise-connect/nextjs-auth0.md` — "@auth0/nextjs-auth0 — Enterprise Connect"
- `references/feature-healthcheck/index.md` — "Auth0 tenant health check (all plans) — full workflow"
- `references/feature-mfa/aspnetcore-api.md` — "ASP.NET Core API (Auth0.AspNetCore.Authentication.Api) — MFA (API-side scope gate)"
- `references/feature-mfa/auth0-android.md` — "Auth0.Android — MFA (API-driven, Flexible Factors Grant)"
- `references/feature-mfa/auth0-angular.md` — "@auth0/auth0-angular — MFA"
- `references/feature-mfa/auth0-api-python.md` — "auth0-api-python — MFA (API-side scope gate)"
- `references/feature-mfa/auth0-auth-js.md` — "@auth0/auth0-auth-js — MFA (API-driven, no redirect)"
- `references/feature-mfa/auth0-react.md` — "@auth0/auth0-react — MFA"
- `references/feature-mfa/auth0-server-js.md` — "@auth0/auth0-server-js — MFA"
- `references/feature-mfa/auth0-server-python.md` — "auth0-server-python — MFA"
- `references/feature-mfa/auth0-spa-js.md` — "@auth0/auth0-spa-js — MFA (step-up)"
- `references/feature-mfa/auth0-swift.md` — "Auth0.swift — MFA (API-driven)"
- `references/feature-mfa/auth0-vue.md` — "@auth0/auth0-vue — MFA"
- `references/feature-mfa/express-oidc.md` — "express-openid-connect — MFA (redirect step-up)"
- `references/feature-mfa/go-jwt-middleware.md` — "go-jwt-middleware — MFA (API-side scope gate)"
- `references/feature-mfa/index.md` — "Auth0 MFA"
- `references/feature-mfa/nextjs-auth0.md` — "@auth0/nextjs-auth0 — MFA (v4)"
- `references/feature-mfa/oidc-client-net.md` — "Auth0.OidcClient (.NET native/desktop) — MFA (client-initiated step-up)"
- `references/feature-mfa/react-native-auth0.md` — "react-native-auth0 — MFA (API-driven, Flexible Factors Grant)"
- `references/feature-mfa/spring-security-api.md` — "Spring Security (resource server) — MFA (API-side scope gate)"
- `references/feature-migration/index.md` — "Auth0 Migration Guide"
