# access-protected-vercel-deployment

Source read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\access-protected-vercel-deployment\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/opencode).

## Summary
A Vercel plugin skill that enforces access control on deployments, ensuring that only authorized users or environments can preview, promote, or modify production builds. It integrates with Vercel's identity system to restrict deployment actions based on team roles, OAuth scopes, or IP allowlists, and can mask or redact sensitive environment variables from logs and error reports.

## When to use / when NOT
Use whenever a project has multiple contributors or integrates with external systems that should not modify production config. Do NOT disable for local development-only projects without team collaboration — the skill prevents accidental production changes. Do NOT rely on it as the sole security layer; complement with OAuth, IP allowlisting, and branch protection rules.

## Inputs, outputs, tools
- Inputs: Vercel project configuration, deployment requests, user OAuth tokens, team membership data.
- Outputs: approval/denial decision for each deployment action, updated project protections, masked log output.
- Tools: Vercel API, OAuth 2.0 flow, GitHub/GitLab integration, Vercel CLI `access` commands. MCP: vercel-plugin connector.

## 5 most important rules
1. **Require explicit approval for production deployments** by team leads or project owners.
2. **Restrict preview deployments to authenticated team members only** via OAuth session validation.
3. **Never expose environment variable values in build logs** — the skill redacts keys matching `SECRET_`, `TOKEN_`, `PASS_` patterns.
4. **Enforce branch-specific rules**: feature branches can only deploy to preview environments; main branch can promote to production.
5. **Log all access decisions** with user ID, timestamp, and reason for audit trails.

## Risks / owner notes
Over-restricting deployment access can stall urgent fixes or hot patches. The owner should regularly review the allowlist and adjust rules when team structures change. Misconfigured IP allowlists can lock out legitimate users working from new locations.

## Category / tags
deployment · security, vercel, ci-cd, access-control, oauth, infra

## Revisions
The gemini-plugin copy is the only revision available; it is newer and more comprehensive than any codex or kilo version. This is the canonical source for this skill.