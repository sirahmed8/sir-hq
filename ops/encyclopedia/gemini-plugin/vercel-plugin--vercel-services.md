# vercel-services

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-services\SKILL.md`
- SKILL.md size: 9707 chars

## What it does

Configure multi-service architectures.

## Structure (headings inside SKILL.md)

- Vercel Services
- Choose the right structure
- Define services and public ingress
- Route requests correctly
- Serve a service on a subdomain
- Call services privately with bindings
- Develop and deploy
- Troubleshoot
- Related skills
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **A subdomain works in production but not in previews:** preview URLs have a single host, so host rules never match there. Keep a subpath rewrite to the same service and use the relative URL in the frontend.

## Key rules (verbatim lines from SKILL.md)

1. - Put service-local `headers`, `redirects`, `rewrites`, or `routes` inside a service only when they should run after public ingress selects that service.
2. - Set `runtime: "container"` when a service must build from a Dockerfile or OCI image. Use `entrypoint` for a nonstandard Dockerfile and `command` to override the image command.
3. - **A subdomain works in production but not in previews:** preview URLs have a single host, so host rules never match there. Keep a subpath rewrite to the same service and use the relative URL in the frontend.
4. - **Framework detection is wrong:** set that service's `framework` or `entrypoint` explicitly instead of changing the whole project.

## Files inside the skill

- `references/experimental-services.md` — "Experimental Services"
