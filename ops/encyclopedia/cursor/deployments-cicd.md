# deployments-cicd (Vercel)

## Summary
Vercel deployment/CI-CD expert guide: `vercel`/`vercel deploy` preview, `--prod` production, `vercel build` + `deploy --prebuilt` for custom pipelines, `vercel promote` (instant alias re-point, no rebuild) vs `rollback`, `inspect`/`ls`/`logs`; CI needs VERCEL_TOKEN + ORG_ID + PROJECT_ID secrets; ready-made GitHub Actions/GitLab CI/Bitbucket Pipelines YAML (pull → build --prod → deploy --prebuilt --prod), PR preview + comment pattern, promote-after-e2e pattern, global flags (--token/--yes/--scope/--cwd), OIDC federation clarification (runtime backend auth only, NOT CLI auth), strategy matrix, common build errors, deploy summary format.

## When to use / when NOT
Use when deploying, promoting, rolling back, inspecting Vercel deployments or writing CI workflows. Do NOT use for app code, env var management (env-vars skill), or non-Vercel hosts.

## Inputs, outputs, tools
- Inputs: project dir, target env (preview/production), CI provider.
- Outputs: deployment URLs, promoted/rolled-back production, CI pipeline configs.
- Tools: Vercel CLI (vercel/vercel deploy/build/pull/promote/rollback/inspect/ls/logs/daemons scale), CI secrets VERCEL_TOKEN/VERCEL_ORG_ID/VERCEL_PROJECT_ID.

## 5 most important rules
1. CI pattern is always `vercel pull --environment=...` → `vercel build --prod` → `vercel deploy --prebuilt --prod`, all with `--token` and `--yes`.
2. `promote` re-points the alias instantly without rebuild — prefer it over re-deploying a validated preview; use rollback for instant revert.
3. `--prebuilt` separates build from deploy — enables CI build caching and test gates between them.
4. OIDC federation authenticates runtime functions to AWS/GCP — it does NOT replace VERCEL_TOKEN for CLI deploys.
5. Pin the CLI version in CI (`vercel@latest` can break); never commit tokens — secrets only.

## Risks / things needing the owner
Deploys hit production — promote/rollback are real-world side effects needing confirmation. Tokens are owner-managed secrets. `--force` skips cache.

## Category / tags
cloud · vercel, ci-cd, deployment, devops

## Revisions
Five tools hold it (codex, cursor, gemini-plugin, kilo, opencode, windsurf — no claude); codex copy chosen, all ~10549 bytes identical.
