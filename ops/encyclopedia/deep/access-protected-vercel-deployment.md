# access-protected-vercel-deployment

Source read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\access-protected-vercel-deployment\SKILL.md`.

## Summary
This Vercel plugin skill explains how to reach protected preview or production deployments without weakening Deployment Protection. For HTTP checks it prefers `vercel curl` / `vc curl`, which uses the caller's existing Vercel authentication; for browser automation it injects a short-lived `x-vercel-trusted-oidc-idp-token` header so tools such as agent-browser or Playwright can load protected pages.

## When to use / when NOT
Use when a linked Vercel project returns a Deployment Protection, SSO, login, or Trusted Sources error during verification, smoke tests, or browser automation. Do not use it to disable protection, bypass app-level authentication, or change Trusted Sources without understanding the access-control impact.

## Inputs, outputs, tools
Inputs are the target deployment URL or path-only project target, the linked Vercel project context, and the caller's auth state. Outputs are authenticated HTTP responses or a browser session that can load the protected deployment, plus a diagnosis of whether the failure is Vercel protection or the app's own auth. Tools are the Vercel CLI (`vc curl`, `vc whoami`, `vc link`, `vc login`, `vc env run`, `vc env pull`), `VERCEL_OIDC_TOKEN`, and browser automation that supports origin-scoped headers.

## 5 most important rules
1. Use the caller's existing Vercel authentication first; do not ask for a long-lived bypass secret as the first move.
2. Use `vc curl` instead of raw `curl` for protected HTTP requests, and use full URLs when the exact deployment matters.
3. For browsers, send `x-vercel-trusted-oidc-idp-token` as an origin-scoped header and never print, commit, or log the token.
4. Do not confuse that header with `x-vercel-oidc-token`, which serves a different function inside Vercel Functions.
5. Treat Trusted Sources changes as access-control changes; a local development token can reach same-project Preview by default, but protected Production may require an authorized `development` to `production` rule.

## Risks / owner notes
The OIDC token is a secret even though it is short-lived; it must stay out of source, screenshots, logs, and shell output. `TRUSTED_SOURCES_ENVIRONMENT_MISMATCH` means the token is valid but not allowed for that environment, while an application `401` or `403` after protection is bypassed belongs to app auth. The owner should approve any Trusted Sources or protection change.

## Category / tags
cloud · vercel, deployment-protection, trusted-sources, oidc, curl, browser-automation, preview

## Revisions
Single gemini-plugin Vercel revision. No codex, kilo, claude, cursor, opencode, or windsurf copy was present for this skill.
