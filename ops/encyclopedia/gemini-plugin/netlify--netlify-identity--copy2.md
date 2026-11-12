# netlify-identity

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\codex\skills\netlify-identity\SKILL.md`
- SKILL.md size: 14185 chars

## What it does

Add user authentication to a Netlify site with @netlify/identity — signup/login/logout, Google/GitHub/GitLab/Bitbucket OAuth, server-side getUser() checks, role-based access control, and Identity event functions. Use it when a task involves adding a login or signup form, gating content to members or roles, "auth middleware" or verifying users in Netlify Functions or Edge Functions, handling OAuth or email-confirmation callbacks, assigning roles at signup, or customizing Identity emails. For locking a whole site to your company or employees-only access, use netlify-access-control instead.

## Structure (headings inside SKILL.md)

- Netlify Identity
- Client auth (browser)
- Server-side auth (Netlify Functions & Edge Functions)
- Role checks
- CSRF: required for server-side auth endpoints
- Identity event functions
- Roles & the JWT
- CDN-edge RBAC (redirect rules)
- Multiple roles chained with commas:
- Configuration (dashboard-only)
- Emails (Pro plans or higher)
- Audit log (Pro plans or higher)
- External JWT providers (Enterprise)
- On failure — stop, don't guess
- Netlify house rules (identity)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Return `{ user: {...} }` to modify the record before persistence (canonical way to set roles at signup). Roles ride in the JWT, so a role change takes effect on the user's **next login or token refresh, not immediately** — see Roles & the JWT below.
- - **External providers** (`?tab=registration#external-providers`): Google/GitHub/GitLab/Bitbucket. For branded OAuth (your app name instead of "Netlify Identity"), register your app with the provider, get client ID + secret, and enter them **in the Netlify settings UI** — not in code.
- - **Password recovery**: user page → **Send reset password email**; link carries `recovery_token`.
- - Set the JWT secret at `Project configuration > General > Visitor access > JWT secret`. Project-level overrides team-level defaults.

## Key rules (verbatim lines from SKILL.md)

1. - Return `{ user: {...} }` to modify the record before persistence (canonical way to set roles at signup). Roles ride in the JWT, so a role change takes effect on the user's **next login or token refresh, not immediately** — see Roles & the JWT below.
2. - **Registration** (`?tab=registration#registration-preferences`): **Open** (default, anyone can sign up) or **Invite only** (all users, including external-provider logins, must be invited first).
3. - **External providers** (`?tab=registration#external-providers`): Google/GitHub/GitLab/Bitbucket. For branded OAuth (your app name instead of "Netlify Identity"), register your app with the provider, get client ID + secret, and enter them **in the Netlify settings UI** — not in code.
4. - JWT header must be `{"alg": "HS256", "typ": "JWT"}` (HS256 required). Payload `exp` is required and must be a future Unix Epoch time.
5. 3. Identity configuration has no public API — it is dashboard-only. Never curl

## Files inside the skill

- `references/advanced-patterns.md` — "Advanced Identity Patterns"
- `references/authorization-and-sessions.md` — "Netlify Identity — authorization and session gotchas"
