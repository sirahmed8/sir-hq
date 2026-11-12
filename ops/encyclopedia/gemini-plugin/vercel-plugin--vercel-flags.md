# vercel-flags

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-flags\SKILL.md`
- SKILL.md size: 10774 chars

## What it does

Plan, configure, and evaluate feature flags.

## When to use (from skill text)

- Use this skill to decide how a feature should be flagged, to create and change flags, and to run rollouts and experiments. Write app code with the skill that matches the stack (see [Choose an approach](#choose-an-approach)). Do not leave CLI steps as "next steps" for the user; execute them yourself.

## Structure (headings inside SKILL.md)

- Vercel Flags
- Route the request
- Choose an approach
- Plan a flag
- Manage flags with the CLI
- Project targeting
- Common flows
- Credentials
- Flags Explorer
- Other frameworks
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Environments**: each environment serves its own value or targeting. Plan what Development, Preview, and Production serve at launch.
- - **OIDC**: on Vercel, the app authenticates with the project's OIDC token and evaluates the configuration of the current environment. `vercel env pull` writes the Development token to `.env.local` for local development ([Getting started](https://vercel.com/docs/flags/vercel-flags/quickstart#pull-lo

## Key rules (verbatim lines from SKILL.md)

1. - **Next.js or SvelteKit**: the Flags SDK (`flags` + `@flags-sdk/vercel`). It adds Flags Explorer integration and precompute for static pages. Load the `flags-sdk` skill. If it is not available, suggest `npx skills add vercel/flags@flags-sdk` (do not auto-install).
2. - **Variants**: name them after the behavior (`control`, `new-checkout`), not after the rollout step.
3. - **Targeting**: a percentage rollout or A/B split needs a stable identity to bucket by, such as `user.id`. Define the entity and attribute under Flags → Entities first; the app must return the same names from its evaluation context ([Entities](https://vercel.com/docs/flags/vercel-flags/dashboard/en

## Files inside the skill

- `overlay.yaml`
- `references/cli.md` — "`vercel flags` CLI"
