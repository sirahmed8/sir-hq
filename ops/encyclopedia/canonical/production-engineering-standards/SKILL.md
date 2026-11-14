---
name: production-engineering-standards
description: "Use when implementing or refactoring production code that needs zero-mock persistence, atomic transactions, schema validation, and tests."
---

# Production Engineering Standards & Zero-Bug Protocols

This skill dictates core engineering protocols to ensure every feature built by the agent is complete, fully functional, resilient, and ready for immediate real-world use without lingering bugs or placeholders.

---

## Core Pillars & Detailed References

Read the corresponding reference guide for ready-to-use persistence adapters, validation schemas, and defensive utilities:

1. [Zero-Mock Persistence Engines & Data Layers](./references/zero_mock_persistence_engines.md)
   - Real persistent storage implementations: SQLite + Drizzle ORM, IndexedDB (Dexie.js), PostgreSQL/Prisma, Supabase, Firebase Firestore, and validated localStorage. Zero hardcoded mock arrays.
2. [Runtime Schema Validation & Data Contracts (Zod & Pydantic v2)](./references/runtime_schema_validation.md)
   - Runtime validation at all system boundaries (API inputs, DB results, IPC payloads, and localStorage).
3. [Defensive Zero-Bug Engineering & Utilities](./references/defensive_zero_bug_engineering.md)
   - Production hooks for abortable async requests (`useAbortableFetch`), debouncing, optimistic UI updates with automatic rollback, and Global Error Boundaries.

---

## Mandatory Documentation & Anti-Monolith Rules

- **Strictly Modular Multi-File Architecture**: Never build monolithic single-file scripts for full applications or complex screens. Always decompose into Presentation, Domain/State, Data, and Core layers.
- **Mandatory Documentation Protocol**: Never complete a major task, feature, or refactor without creating or updating:
  - `walkthrough.md`: Chronological breakdown of changes, architectural diagrams, and verification results.
  - `README.md` / `ARCHITECTURE.md`: Setup instructions, environment variables, dependencies, and architectural structure.
