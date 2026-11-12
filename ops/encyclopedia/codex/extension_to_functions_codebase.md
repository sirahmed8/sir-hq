# extension_to_functions_codebase

- Tool: `codex`
- Category: data
- Source: `C:\Users\a7med\.codex\skills\extension_to_functions_codebase\SKILL.md`
- SKILL.md size: 4383 chars

## What it does

Convert Firebase Extensions into standalone Cloud Functions codebases or npm packages with V2 triggers.

## When to use (from skill text)

- Config, SDK Lifecycle Hooks) and modernizes 1st Gen triggers to 2nd Gen using
- - `resources` → Upgrade 1st Gen triggers to 2nd Gen (`onDocumentWritten`,
- ### Step 3: Upgrade Triggers from V1 to V2

## Structure (headings inside SKILL.md)

- Extension to Functions Codebase & npm Package Migration
- Overview
- Target Migration Workflows
- Core Rules & Constraints
- 1. Declarative IAM & APIs (Zero-Local-Overhead)
- 2. Global Parameter Access Restriction
- 3. V2 Concurrency & Cost Parity
- Step-by-Step Migration Execution
- Step 1: Inventory Extension Resources
- Step 2: Configure `package.json`
- Step 3: Upgrade Triggers from V1 to V2
- Step 4: Convert Lifecycle Events
- Step 5: Package README & Export Instructions
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Use `requiresRole("roles/...")` for required GCP IAM permissions.

## Key rules (verbatim lines from SKILL.md)

1. - Use `requiresRole("roles/...")` for required GCP IAM permissions.
2. - **Never call `.value()` at top-level module load scope.**
3. - `lifecycleEvents` → `afterFirstDeploy` & `afterRedeploy`.
4. - `onInstall` → `afterFirstDeploy({ task: { function: "initTask" } })`

## Files inside the skill

- `references/configuration-migration.md` — "Migrating Runtime Configurations (runWith)"
- `references/destructuring-shim.md` — "Architectural Deep Dive: Destructuring Compatibility Shim"
- `references/signature-mapping.md` — "Firebase Functions V1 vs V2 Signature Mapping"
