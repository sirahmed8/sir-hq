# variables (gemini-plugin: postman)

## Summary
variables keeps one maintained Postman collection runnable across environments without forking requests. Scoping model: collection variables hold API defaults, environments hold target-specific values (`base_url` etc.), referenced as `{{key}}` in URLs/headers/params/bodies — parameterize only what actually varies. Precedence resolves surprises: local script values > iteration data > environment > collection > global; values can reference other variables and resolve at send time, so inspect the chain not just the final field. Runtime chaining uses `pm.environment`/`pm.collectionVariables` (intentional scope), `pm.variables.get` reads across scopes, `pm.variables.set` is run-local; transient sensitive values should NOT be persisted or logged. Secrets: durable credentials go in the shared vault via `postman secret create` (masked prompt — never through agent context or literal args) then `postman environment var set api_key --secret-id ... --vault-id ...` so the committed YAML carries vault/secret IDs, not values. Critical nuance: `type: secret` alone still leaves a literal readable value — it's masking, not protection. Lint with `postman environment lint <path> --fail-severity warning`; lint doesn't prove vault resolution — verify with an authenticated request + contract-derived assertion, credentials out of output.

## When to use / when NOT
Use when parameterizing requests across environments, choosing variable scopes, chaining response values in scripts, or referencing credentials without committing them. Do NOT use for one-off literals that never vary, and don't persist transient sensitive values to environments.

## Inputs, outputs, tools
- Inputs: environment YAML files, vault/secret IDs, script variable usage.
- Outputs: parameterized collections, environment files with vault references, lint reports.
- Tools: `postman environment new/var set`, `postman secret create`, `postman environment lint`, collection-schema-v3 reference for env file schema.

## 5 most important rules
1. Scope decides the winner: local > iteration > environment > collection > global — a correct env file can still lose to a script/row override.
2. Values resolve at SEND time and can chain — inspect the whole reference chain, not the rendered field.
3. Secrets via masked `postman secret create` prompt ONLY — never literal args or agent context; env file stores IDs not values.
4. `type: secret` in YAML is cosmetic masking — the literal is still readable; vault references are the real protection.
5. Verify resolution with an authenticated request + assertion; lint checks the artifact, not vault access; keep credentials out of output.

## Risks / things needing the owner
Vault operations need a signed-in Postman CLI (owner auth). Secret values must come from the user through the masked prompt — the agent must never see or echo them. Committing literal secrets is the failure mode this skill exists to prevent. Resolution-vs-view permission distinction means teammates can run requests without seeing credentials.

## Category / tags
security · postman, variables, secrets, environments, api

## Revisions
Single revision read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\variables\SKILL.md` (63 lines). Gemini-plugin only.
