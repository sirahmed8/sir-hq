# ci-integration

## Summary
Skill for wiring Postman API checks into CI pipelines: it maps each kind of guarantee (behavioral assertions, structural lint, workspace governance, AI-readiness score) to the exact `postman` CLI command that proves it, and explains how to keep PR gates read-only while letting post-merge jobs publish reviewed artifacts to the shared workspace.

## When to use / when NOT
Use when adding collection runs, lint rules, or publish steps to a PR pipeline, or when a teammate asks for "tests on every PR" against a Postman collection. Do NOT use to author the API contract itself (that is api-testing / api-discovery) or to decide which workspace governance rules should exist.

## Inputs, outputs, tools
- Inputs: a collection/spec path or id, a workspace id, a score threshold, CI secret `POSTMAN_API_KEY`.
- Outputs: gate results with distinguishable failure categories, JUnit/HTML reports, and (post-merge only) pushed workspace entities.
- Tools: `postman collection run`, `postman collection lint`, `postman spec lint`, `postman workspace lint`, `postman collection ai-readiness`, `postman dependency install`, `postman login --with-api-key`, `postman workspace push`.

## 5 most important rules
1. Pick the gate by the guarantee it establishes; never let a green job blur behavior vs structure vs governance vs readiness failures.
2. Never suppress nonzero exits (`-x`/`--suppress-exit-code`) — that deletes the gate.
3. Authenticate CI jobs that touch workspace resources with `POSTMAN_API_KEY` from the CI secret store; unauthenticated runs lose their results.
4. Publish only after merge checks pass — a PR-triggered `workspace push` publishes an unmerged contract.
5. Avoid `--push-strategy force-sync` unless exact mirroring is required; it can delete workspace entities managed elsewhere.

## Risks / things needing the owner
Live collection runs send real requests and can write data — the target and credentials must be isolated. Push strategy and binding diffs need explicit approval. CI secrets are owner-managed.

## Category / tags
ops · ci, postman, api-testing, automation, governance

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\postman\skills\ci-integration\SKILL.md`. Only the gemini-plugin tool holds it.
