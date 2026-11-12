# vercel-flags (gemini-plugin: vercel)

## Summary
vercel-flags plans, configures and evaluates Vercel Flags — the platform feature-flag service switchable per environment (Dev/Preview/Prod) without redeploy. It routes requests: planning ("put behind flag", "roll out to 10%", "kill switch") → plan-then-choose-approach; pure flag management with no code → `vercel flags` CLI; apps already on Flags SDK → the flags-sdk skill; otherwise pick integration by stack: Flags SDK (`flags`+`@flags-sdk/vercel`) for Next.js/SvelteKit, `@vercel/flags-core` for other frameworks/servers, OpenFeature provider for portability, or KEEP an existing provider (Statsig/LaunchDarkly/PostHog) via adapter. Flag planning requires deciding kind (boolean vs string/number/json — immutable later), variants named by behavior, kebab-case stable key, per-environment values, targeting entity+attribute defined under Flags→Entities, and a fallback defaultValue. CLI lifecycle: inspect first, create/enable/set/rollout/split/rules/use-targeting, verify via inspect/versions/evaluations, retire code-first then archive then rm. Credentials: OIDC on Vercel, SDK keys (FLAGS) off-platform, FLAGS_SECRET for Flags Explorer overrides — never print secrets.

## When to use / when NOT
Use for any feature-flag planning, creation, rollout, A/B test or kill-switch work on Vercel. Do NOT use `vercel flags` for providers already in the app (configure in their dashboards), don't auto-install skills (`npx skills add` suggested, not run), and don't leave CLI steps for the user — execute them.

## Inputs, outputs, tools
- Inputs: flag intent, project/team (`--project`, `--scope`), environment targets.
- Outputs: flags created/configured via CLI, code integration guidance, evaluation context wiring.
- Tools: `vercel flags` CLI, `@vercel/flags-core`, Flags SDK, Flags Explorer, references/cli.md lifecycle doc.

## 5 most important rules
1. `inspect` before every mutation; adopt an existing flag key rather than creating a duplicate.
2. Kind is immutable after creation; key must match across CLI, dashboard and code.
3. Rollouts/A-B need a stable bucketing identity (e.g. user.id) whose entity/attribute names match Flags→Entities config.
4. Retire in order: remove code → verify no evaluations → archive → rm only archived flags.
5. `archive`/`rm`/`update --remove-variant` prompt — pass `--yes` only when the user approved; never rotate FLAGS_SECRET routinely, never print secrets.

## Risks / things needing the owner
Requires authenticated Vercel CLI (`vercel link`/whoami); unlinked dirs should use --project/--scope or ask. Flags Explorer override cookie signing uses FLAGS_SECRET — mishandling leaks override capability. Destructive flag ops are confirmation-gated. Auth/linking is owner territory.

## Category / tags
cloud · vercel, feature-flags, experimentation, rollout

## Revisions
Single revision read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-flags\SKILL.md` (107 lines + references/cli.md). Gemini-plugin only.
