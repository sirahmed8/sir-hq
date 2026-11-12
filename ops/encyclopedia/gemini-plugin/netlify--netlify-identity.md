# netlify-identity (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-identity\SKILL.md`. User auth via `@netlify/identity`.

## Summary
`@netlify/identity` npm package replaces legacy `netlify-identity-widget`/`gotrue-js` for new projects. Client API: `signup` (confirmation email by default), `login`, `logout`, `getUser`, `oauthLogin('google'|'github'|'gitlab'|'bitbucket')`, `handleAuthCallback()` — MANDATORY on the landing page or OAuth redirects/email-confirm/invite/recovery links never complete; call on page load, returns falsy without token in URL hash. `refreshSession()`, `recoverPassword()`, `acceptInvite()` for single token types. Call `getSettings()` at startup and render providers from it — don't hardcode. Server-side `getUser()`/`login()`/`admin.*` need modern v2 functions (`export default`); v1 `export { handler }` unsupported. `getUser()` works in Functions AND Edge Functions; `admin.*` runs ONLY in Netlify Functions — never browser/edge. Identity config is DASHBOARD-ONLY (no public API — never curl api.netlify.com, never read local tokens, enable at app.netlify.com/projects/{site}/identity). NEVER build from-scratch OAuth beside Identity (no provider app registration, no client_id/secret in source, no custom callback exchange — `oauthLogin()`+`handleAuthCallback()` instead; raw OAuth is the top rework source). Two hard limits: Identity does NOT run under `netlify dev` — test auth on deploys/Deploy Previews only; and for whole-site company/employee gating use netlify-access-control instead.

## When to use / when NOT
Use for app-user signup/login/logout, OAuth providers, server-side user checks, RBAC roles, Identity event functions, customizing Identity emails. NOT for site-level gating (→ netlify-access-control) or local dev auth testing (impossible — test on deploys).

## Inputs, outputs, tools
- Inputs: user credentials/OAuth, role assignments, custom email templates.
- Outputs: authenticated sessions (`nf_jwt`), user records, role-gated content.
- Tools: `@netlify/identity` SDK, Netlify Identity dashboard, v2 Functions/Edge Functions `getUser()`, `admin.*` (Functions only).

## 5 most important rules
1. `handleAuthCallback()` on the landing page is mandatory — without it all token flows dead-end.
2. Dashboard-only config — no API, no token reading, no undocumented endpoints.
3. Never hand-roll OAuth alongside Identity — use `oauthLogin`+`handleAuthCallback`.
4. Server auth needs v2 function shape; `admin.*` is Functions-only (not edge/browser).
5. Identity doesn't work under `netlify dev` — verify on Deploy Previews.

## Risks / owner notes
No local auth testing = slower iteration; dashboard-only config can't be IaC'd; roles/permissions mistakes expose gated content; confirmation-email deliverability affects signup.

## Category and tags
Category: cloud. Tags: netlify, identity, authentication, oauth, rbac, jwt, serverless-auth.
