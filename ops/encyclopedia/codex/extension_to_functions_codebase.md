# extension_to_functions_codebase (skill name: extension-to-functions-codebase)

## Summary
A migration playbook that converts a Firebase Extension into either a local Cloud Functions codebase (`functions/src/`) or a publishable npm package of V2 functions. It maps `extension.yaml` params/APIs/roles/lifecycle events onto modern `firebase-functions` v2 primitives (defineString/defineSecret params, requiresAPI/requiresRole, onInit, afterFirstDeploy/afterRedeploy hooks) and upgrades 1st Gen triggers to 2nd Gen with a destructuring compatibility shim so legacy handler bodies keep working.

## When to use / when NOT
Use when porting an existing Firebase Extension (or its resources) into app-owned functions or a reusable package. Do NOT use for writing brand-new functions with no extension source, or for non-Firebase/GCP serverless targets. The skill explicitly forbids running `npm publish` — packaging output stops at a ready-to-publish artifact.

## Inputs, outputs, tools
- Inputs: the extension's `extension.yaml` (params, apis, roles, lifecycleEvents, resources), its function source and tests, target choice A (local codebase) or B (npm package).
- Outputs: TypeScript under `functions/src/` or a package with `package.json` (exports map, `engines.node >=22`, peerDeps on firebase-admin ^11||^12 and firebase-functions >=6), converted triggers, lifecycle hooks in `src/index.ts`, and a README with install/re-export/.env/what-changed docs.
- Tools: `firebase-functions` v2 SDK (params, v2/firestore, v2/tasks, v2/https, v2 lifecycle hooks), TypeScript, jest preserved from the extension, npm packaging. References: configuration-migration.md, destructuring-shim.md, signature-mapping.md.

## 5 most important rules
1. Never call `.value()` on params at module top level — initialize SDK clients inside `onInit()` or lazy getters.
2. Use declarative IAM/APIs (`requiresRole`, `requiresAPI`) instead of gcloud scripts or console steps.
3. Keep V1 cost/concurrency parity on V2 by setting `cpu: "gcf_gen1"` (V2 defaults to concurrency up to 80).
4. Upgrade triggers to V2 and apply the destructuring shim — `{ change, context }`, `{ snapshot, context }`, `{ message, context }` map CloudEvent fields back to V1 shapes via lazy getters, so business logic stays untouched; scheduled functions moved from pubsub to scheduler namespace.
5. Map lifecycle events to hooks (`onInstall`→`afterFirstDeploy` task, `onUpdate`/`onConfigure`→`afterRedeploy` task), drop `EXT_INSTANCE_ID` when enqueueing tasks, and NEVER run `npm publish`.

## Risks / owner needs
Publishing is intentionally blocked; a human must publish. V2 trigger semantics differ subtly (task payloads, event shapes) — the shim covers common cases but edge handlers still need review. Requires firebase-functions >=6 and Node >=22.

## Category and tags
Category: cloud. Tags: firebase, cloud-functions, migration, typescript, serverless, v2-triggers.

## Revisions
Identical content across codex, cursor, gemini-plugin, kilo, opencode, windsurf per the kilo digest; kilo copy used (name field differs: `extension-to-functions-codebase` vs file slug `extension_to_functions_codebase`).
