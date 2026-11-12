# workspaces (gemini-plugin: postman)

## Summary
workspaces defines how Postman context lives beside code: a workspace = one service's API work + evidence (contracts, collections, environments, mocks, runs/results), stored in Git so laptops and build agents share it. `.postman/resources.yaml` records the owner binding (one repo, or one remote URL + subpath in a monorepo) so every skill/CI/teammate resolves the same context — replacing a confirmed binding sends work to the wrong service. `postman init` is the safe-to-repeat starting point (files + optional workspace binding; `postman status` shows if done; "inferred" bindings are candidates to confirm, partial results are progress not failures). Other services' workspaces come in as dependencies via api-discovery — reuse without takeover, linked by the context graph. Session/plan handling: temporary/guest sessions lose work unless claimed via `postman signup`; usage-limit/quota/subscription errors mean STOP retrying — the CLI suggests next steps and the agent should relay them (signup link for guest, billing upgrade URL for paid accounts).

## When to use / when NOT
Use when initializing Postman in a repo, binding to a workspace, interpreting `postman init` output, or handling auth/plan/quota CLI suggestions. Do NOT create extra workspaces for dependent services (they come via api-discovery) or retry quota-blocked operations.

## Inputs, outputs, tools
- Inputs: repo/service identity, `postman init`/`status` output, CLI session state.
- Outputs: `.postman/resources.yaml` binding, workspace files in Git, user guidance on signup/upgrade.
- Tools: `postman` CLI (init/status/signup suggestions).

## 5 most important rules
1. One workspace per service (one repo or one monorepo subpath) — the binding in resources.yaml is the shared contract.
2. `postman init` is idempotent; check `postman status` first; inferred bindings need human confirmation.
3. Quota/plan-limit errors are NOT retryable — relay the CLI's suggested next step (signup for guests, billing for accounts).
4. Guest-session work is lost on expiry unless claimed — surface the signup option proactively when the reminder prints.
5. Depend on other services' workspaces via api-discovery, never duplicate their collections.

## Risks / things needing the owner
`postman signup` and plan upgrades are owner account actions — the skill's job is to explain and offer, not to perform. Wrong workspace binding scatters evidence across services. No other risks.

## Category / tags
ops · postman, api, workspaces, cli

## Revisions
Single revision read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\workspaces\SKILL.md` (64 lines). Gemini-plugin only.
