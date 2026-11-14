# upstream

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-flags\upstream\SKILL.md`
- SKILL.md size: 12560 chars

## What it does

> Feature flags, A/B tests, and gradual rollouts with Vercel Flags, in any app or framework. Use whenever the user is planning, adding, changing, or cleaning up a feature flag, toggle, kill switch, experiment, percentage rollout, or targeting rule, or wants to gate or hide a feature for some users, even before a library or provider is chosen. Covers choosing an integration (Flags SDK, `@vercel/flags-core`, OpenFeature), the Vercel dashboard, the `vercel flags` CLI (create, inspect, set, split, rollout, rules, segments, evaluations, archive, connections), Project Connections, OIDC vs SDK keys, `FLAGS_SECRET`, and Flags Explorer overrides. For `flag()` declarations, adapters, precompute, and the Flags Explorer endpoint in Next.js or SvelteKit code, load the `flags-sdk` skill.

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
- - **Datafile**: `datafile --environment <production|preview|development> --json` shows the current datafile used by SDKs for debugging.
- - **OIDC**: on Vercel, the app authenticates with the project's OIDC token and evaluates the configuration of the current environment. `vercel env pull` writes the Development token to `.env.local` for local development ([Getting started](https://vercel.com/docs/flags/vercel-flags/quickstart#pull-lo
- - **Project Connections**: read another same-team project's flags with the consumer project's OIDC token, without an SDK key. Follow [Project Connections](references/cli.md#project-connections) for setup and minimum versions.

## Key rules (verbatim lines from SKILL.md)

1. - **Clean up or remove a flag** ("remove this flag", "clean up stale flags", "inline this flag"): follow [references/cleanup.md](references/cleanup.md), then [Lifecycle and safety](references/cli.md#lifecycle-and-safety) before archiving.
2. - **Next.js or SvelteKit**: the Flags SDK (`flags` + `@flags-sdk/vercel`). It adds Flags Explorer integration and precompute for static pages. Load the `flags-sdk` skill. If it is not available, suggest `npx skills add vercel/flags@flags-sdk` (do not auto-install).
3. - **Variants**: name them after the behavior (`control`, `new-checkout`), not after the rollout step.
4. - **Targeting**: a percentage rollout or A/B split needs a stable identity to bucket by, such as `user.id`. Define the entity and attribute under Flags → Entities first; the app must return the same names from its evaluation context ([Entities](https://vercel.com/docs/flags/vercel-flags/dashboard/en
5. - **Targeting rules and segments**: `rules`, `segments`, and `targeting enable <key>` to switch an environment from a static value back to targets and rules (CLI versions before 65 call it `use-targeting <key>`).

## Files inside the skill

- `references/cleanup.md` — "Clean up a flag"
- `references/cli.md` — "`vercel flags` CLI"
