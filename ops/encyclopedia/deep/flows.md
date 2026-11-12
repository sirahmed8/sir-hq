# flows (Postman Flows)

## Summary
Operational guide for running, deploying and debugging Postman Flows — API workflows saved as block graphs. Core doctrine: the artifact and execution path determine what a "pass" means. `postman flows run <path>` executes a local JSON graph; `postman flows trigger <flow-id>` calls the deployed webhook (auth + config included). Local View and Cloud View artifacts are isolated — local files are not assumed deployable, `workspace pull` does not fetch them, and the desktop app's Git-connected Local View produces them. Diagnosis must follow block-level run evidence (`flows get-run --run-id`, `--logs`), because an HTTP 200 trigger response only proves the Response block ran — other blocks may have failed.

## When to use / when NOT
Use when running, deploying, or debugging an existing Postman Flow ("why did this flow fail"). Not for authoring flow graphs from scratch (Postman app/other skills) or for plain single-request API testing.

## Inputs, outputs, tools
- Inputs: local flow JSON path OR hosted flow-id (resolve via `flows list --workspace <id>`; no local mapping in .postman/resources.yaml), named Start-block scenarios (`-s` payload/headers/query; `-i`/`-f` and explicit flags override), `--dry-run` for deployed side-effect flows.
- Outputs: run results/reports (persist them in CI with the failure exit code), Run IDs, failing block + cause.
- Tools: `postman flows run|trigger|update|get-run|list-runs|list`, `--workspace` (required even for connector blocks in local runs), reference/flow_cli_flags.md for reporters/dataset iteration/flag collisions; api-discovery skill for cross-workspace search.

## 5 most important rules
1. Pick the right artifact first: local `run` vs deployed `trigger` produce different evidence — a passing local run says nothing about the deployed webhook callers hit; never assume local files are deployable.
2. Reuse named Start-block scenarios for repeatable payloads; one-off inputs go on the invocation; secrets stay masked — use `trigger --dry-run` before side-effecting deployed runs.
3. Deployment needs canvas config the CLI can't repair: Start block set to API-request trigger + a Response block; resolve path suffix and auth first; deploy/auth changes affect other callers — unrequested public exposure or auth removal needs consent.
4. A deployed-but-disabled flow receives nothing — check enabled state (`flows update <id> --trigger on` to enable when intended); report URL, auth and enabled state separately from execution results.
5. Diagnose from run evidence, not the trigger response: HTTP 200 ≠ whole-flow success; `flows get-run --run-id <id> --logs` names the failing block; `list-runs` widens time range before concluding absence; access denials across workspaces = credentials/entitlement, not empty results.

## Risks / owner needs
Deployed flows are callable endpoints — auth/exposure decisions are owner-visible; check local-run entitlement before building CI on it. Secrets must never appear in reports.

## Category and tags
Category: automation. Tags: postman, flows, api-automation, webhooks, ci-cd, debugging.

## Revisions
Single gemini-plugin postman copy; no competing revisions.
