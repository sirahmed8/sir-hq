# production-engineering-standards

- Tool: `codex`
- Category: ops
- Source: `C:\Users\a7med\.codex\skills\production-engineering-standards\SKILL.md`
- SKILL.md size: 1995 chars

## What it does

Production-grade engineering standards: zero-mock persistence, atomic transactions, schema validation, and testing.

## Structure (headings inside SKILL.md)

- Production Engineering Standards & Zero-Bug Protocols
- Core Pillars & Detailed References
- Mandatory Documentation & Anti-Monolith Rules
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Production hooks for abortable async requests (`useAbortableFetch`), debouncing, optimistic UI updates with automatic rollback, and Global Error Boundaries.

## Key rules (verbatim lines from SKILL.md)

1. - **Strictly Modular Multi-File Architecture**: Never build monolithic single-file scripts for full applications or complex screens. Always decompose into Presentation, Domain/State, Data, and Core layers.
2. - **Mandatory Documentation Protocol**: Never complete a major task, feature, or refactor without creating or updating:

## Files inside the skill

- `references/defensive_zero_bug_engineering.md` — "Defensive Zero-Bug Engineering & Utilities"
- `references/runtime_schema_validation.md` — "Runtime Schema Validation & Data Contracts"
- `references/zero_mock_persistence_engines.md` — "Zero-Mock Persistence Engines & Data Layers"
