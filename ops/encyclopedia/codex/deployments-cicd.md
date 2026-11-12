# deployments-cicd

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\deployments-cicd\SKILL.md`
- SKILL.md size: 10549 chars

## What it does

Vercel deployment and CI/CD expert guidance. Use when deploying, promoting, rolling back, inspecting deployments, building with --prebuilt, or configuring CI workflow files for Vercel.

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
- Build locally (uses development env vars by default)
- Build with production env vars
- Deploy only the build output (no remote build)
- Promote & Rollback
- Promote a preview deployment to production
- Rollback to the previous production deployment
- Rollback to a specific deployment
- Inspect Deployments
- View deployment details (build info, functions, metadata)
- List recent deployments
- View logs for a deployment
- CI/CD Integration
- Required Environment Variables
- GitHub Actions
- OIDC Federation (Secure Backend Access)
- GitLab CI
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Any runtime service-to-service auth where you want to avoid storing static secrets in Vercel env vars
- - vercel pull --yes --environment=production --token=$VERCEL_TOKEN
- - vercel build --prod --token=$VERCEL_TOKEN
- - vercel deploy --prebuilt --prod --token=$VERCEL_TOKEN

## Key rules (verbatim lines from SKILL.md)

1. - Any runtime service-to-service auth where you want to avoid storing static secrets in Vercel env vars
2. 1. **Always use `--prebuilt` in CI** — separates build from deploy, enables build caching and test gates
3. 2. **Use `vercel pull` before build** — ensures correct env vars and project settings
4. - **No monitoring configured** → "Set up drains or install an error tracking integration before the next production deploy. Run `/status` for a full observability diagnostic."

## Files inside the skill

- (SKILL.md only)
