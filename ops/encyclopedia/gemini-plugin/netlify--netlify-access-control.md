# netlify-access-control (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-access-control\SKILL.md`. Routing/disambiguation skill for site-protection layers.

## Summary
Routes "auth" requests to the correct of Netlify's THREE unrelated layers users constantly conflate: (1) Netlify Identity = who the user is inside the app (issues `nf_jwt`, route to netlify-identity), (2) Password Protection / project visibility = whether the request loads the site at all, (3) Team/Org SAML SSO = dashboard login. Decision guide maps intents to layers: team-only site → Private project (Credit plans) or Team login protection; one shared password → Basic password protection (Pro) or Password visibility (Pro only, NOT on Credit Free/Personal — use Private instead); protect previews only → Non-production/Previews scope; SSO to view a site → Org SSO strict + team login protection; identify WHICH team member hit a private site → `context.user` in functions/edge functions. Key rules: NO public API/CLI/MCP exists for these settings — give dashboard paths, never curl api.netlify.com or read local tokens; on failure report and stop. Private project or team login gives functions `context.user` (the Netlify login IS the app identity when everyone can pass it — no second login). SSO tokens expire after ~1 hour → 401s; refresh via `Netlify-Site-Protection-Expires-In` header check + reload. Footguns: no bridge between perimeter session and Identity app session (no shared cookie/JWT — don't wire them); third-party webhooks can't reach private projects (must be public); making public needs a production deploy; basic-auth on ANY page disables caching site-wide; Advanced Web Security runs BEFORE password prompts; Free/Personal private projects are single-seat (Pro for more members); teams created on/after 2026-07-28 default to Private-for-new-projects.

## When to use / when NOT
Use when asked to password-protect a site/preview, make a project private/public, require SSO to view a site, or diagnose SSO 401s/expiry. NOT for wiring app-user login code (→ netlify-identity) or WAF specifics (referenced by URL only).

## Inputs, outputs, tools
- Inputs: which protection intent, plan tier, Credit-based vs legacy plan, production-deploy status.
- Outputs: correct dashboard path + checklist, plan-gating warnings, `context.user` guidance, SSO-refresh snippet.
- Tools: Netlify dashboard UI only (no API); functions/edge functions `context.user`; docs URLs.

## 5 most important rules
1. Disambiguate the three "auth" layers FIRST — Identity vs site-load gating vs dashboard SSO have separate sessions and providers.
2. These settings have NO API/CLI/MCP — dashboard paths only; never curl the API or read tokens.
3. Private project/team login already identifies visitors via `context.user` — often no second login needed.
4. Password Protection ≠ Private: shared password vs per-member Netlify credentials; plan gating differs sharply (Free/Personal has no Password option).
5. Report what you tried and stop on failure — no undocumented workarounds.

## Risks / owner notes
Wrong layer choice silently exposes a site or locks out users; plan gating surprises (Free/Personal private = owner-only). Webhook delivery requires public projects — a real integration constraint. Settings are dashboard-only so agent can't verify changes landed.

## Category and tags
Category: cloud. Tags: netlify, access-control, sso, privacy, password-protection, plan-gating, context-user.
