# auth0

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\auth0--auth0.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An authentication provider skill for Auth0 that handles user sign-up, sign-in, password management, and social login integration. It configures Auth0 tenants, manages OAuth 2.0 and OpenID Connect flows, and provides user profile synchronization with your application. The skill can also handle multifactor authentication (MFA), breach password detection, and custom authentication actions.

## When to use / when NOT
Use when your application needs an identity provider with minimal custom development — the skill handles tenant configuration, OAuth flows, and user management out-of-the-box. Do NOT use Auth0 for applications requiring extremely customized authentication flows without evaluating the cost of custom actions — the skill's default MFA and breach password features may not cover all threat models. Do NOT skip the tenant domain verification step; the skill will verify that your custom domain is properly configured with Auth0 before allowing production sign-in.

## Inputs, outputs, tools
- Inputs: Auth0 tenant ID or domain, OAuth client ID/secret, OIDC client configuration, MFA enrollment settings.
- Outputs: authenticated user session, user profile data, MFA status, breach password notification, custom authentication action logs.
- Tools: Auth0 Management API, Auth0 Lock (deprecated but still supported), OAuth 2.0 / OIDC flows, email service integration. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always configure Email Verification** — the skill will not allow production sign-in without verified email domains; verify your domain in the Auth0 dashboard before going live.
2. **Enable Breach Password Detection** — the skill monitors the Have I Been Pwned database and will force password resets for compromised passwords; this is opt-in and must be enabled.
3. **Use Silent Authentication for single-page applications** — the skill can acquire tokens silently without requiring the user to re-enter credentials; this improves UX for SPA navigation.
4. **Configure MFA enrollment requirements** — the skill supports TOTP and SMS MFA; decide which methods your application requires and configure them in the tenant.
5. **Regularly review authentication logs** — the skill captures all authentication events; the owner should review weekly for suspicious activity (multiple failed logins, unusual geographic locations).

## Risks / owner notes
Over-reliance on default MFA methods may leave gaps in your threat model; the owner should evaluate whether SMS TOTP is sufficient or if app-based TOTP (Google Authenticator, Authy) is preferred. Breach Password Detection depends on the Have I Been Pwned database; if your organization has strict data privacy policies, verify that checking passwords against this service is compliant.

## Category / tags
authentication · identity-provider, auth0, oauth, oidc, mfa, breach-detection, user-management

## Revisions
The gemini-plugin copy is the only revision available; no codex, kilo, or cursor copies exist. This is the canonical source for this skill.