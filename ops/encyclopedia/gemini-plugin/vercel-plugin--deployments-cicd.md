# deployments-cicd

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\deployments-cicd\SKILL.md`
- SKILL.md size: 10737 chars

## What it does

Vercel deployment and CI/CD expert guidance.

## Structure (headings inside SKILL.md)

- Vercel Deployments & CI/CD
- Deployment Commands
- Preview Deployment
- Deploy from project root (creates preview URL)
- Equivalent explicit form
- Production Deployment
- Deploy directly to production
- Force a new deployment (skip cache)
- Build Locally, Deploy Build Output
- Build locally (uses preview env vars by default)
- Build with production env vars
- Deploy only the build output (no remote build)
- Promote & Rollback
- Stage a production deployment without assigning domains
- Promote it (instant, no rebuild)
- Show pending rollback status (no argument does not roll back)
- Rollback to a specific deployment
- Inspect Deployments
- View deployment details (build info, functions, metadata)
- List recent deployments
- View recent runtime logs for a deployment
- CI/CD Integration
- When to Add a CI Pipeline
- Required Environment Variables
- GitHub Actions
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. **Release only tested builds** — Deployment Checks (Git) or staged production builds (CLI)
- 4. **Use OIDC federation for runtime backend access** — lets Vercel functions auth to AWS/GCP without static secrets (does not replace `VERCEL_TOKEN` for CLI)
- - **Target**: production | preview
- - **Success (preview)** → "Visit the preview URL to verify. When ready, run `/deploy prod` to promote to production."

## Key rules (verbatim lines from SKILL.md)

1. 1. **Always use `--prebuilt` in CI** — separates build from deploy, enables build caching and test gates
2. 2. **Use `vercel pull` before build** — ensures correct env vars and project settings
3. - **No monitoring configured** → "Set up drains or install an error tracking integration before the next production deploy. Run `/status` for a full observability diagnostic."

## Files inside the skill

- `references/cli-pipelines.md` — "CLI Pipelines"
- `references/deployment-checks.md` — "Deployment Checks"
- `references/live-status.md` — "Deployment Status"
- `references/oidc-federation.md` — "OIDC Federation (Secure Backend Access)"
