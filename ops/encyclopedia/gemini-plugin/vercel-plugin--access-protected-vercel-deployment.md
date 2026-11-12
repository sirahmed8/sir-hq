# access-protected-vercel-deployment

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\access-protected-vercel-deployment\SKILL.md`
- SKILL.md size: 4906 chars

## What it does

Access and test protected Vercel preview or.

## Structure (headings inside SKILL.md)

- Access Protected Vercel Deployments
- Choose the access path
- HTTP requests: use `vercel curl`
- Browser automation: attach the development OIDC token as a header
- Trusted Sources rules
- Diagnose the response
- Avoid
- Related skills
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - the target is a protected Production deployment and the caller uses a local development token;
- - `TRUSTED_SOURCES_ENVIRONMENT_MISMATCH` means the token is valid but its caller environment is not allowed to reach the target environment.
- - A deployment marked `"target": "production"` can still be protected. Do not assume production is public.

## Key rules (verbatim lines from SKILL.md)

1. - An application-generated `401` or `403` after Vercel protection is bypassed belongs to the application's own authentication and must be debugged separately.
2. - A deployment marked `"target": "production"` can still be protected. Do not assume production is public.
3. - Do not disable Deployment Protection to make automation pass.
4. - Do not send raw unauthenticated `curl` repeatedly after receiving the protection page.
5. - Do not start an interactive SSO browser login when `vc curl` or an origin-scoped OIDC header can authenticate the request.

## Files inside the skill

- (SKILL.md only)
