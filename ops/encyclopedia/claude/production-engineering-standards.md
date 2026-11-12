# production-engineering-standards

Tools: claude, codex, cursor, kilo, opencode, windsurf (kilo copy used; identical across tools).
Source: C:\Users\a7med\.config\kilo\skills\production-engineering-standards\SKILL.md (30 lines) + references/{zero_mock_persistence_engines, runtime_schema_validation, defensive_zero_bug_engineering}.md (~254 lines total)

## Summary
An engineering-constitution skill mandating production-grade output: zero mock/in-memory persistence (real SQLite+Drizzle, Dexie, Prisma/Postgres, Supabase, Firestore, or validated localStorage), runtime schema validation at every boundary (Zod/Pydantic v2), defensive utilities (abortable fetch, debounce, optimistic UI with rollback, error boundaries), strictly modular multi-file architecture, and mandatory walkthrough.md/README/ARCHITECTURE documentation.

## When to use / not use
Use when building features that must work against real persistence and survive production — the anti-"vibe code" standard. Not for prototypes, throwaway scripts, or when mocks are explicitly acceptable; it conflicts with rapid scaffolding.

## Inputs, outputs, dependencies
Input: a feature/build task. Output: modular code with real persistence adapters, boundary validation, defensive hooks, and documentation files. Needs: references/ guides for adapter implementations and schemas; whichever DB/storage the project actually uses.

## Key rules
1. Zero hardcoded mock arrays — every data layer must be a real persistent implementation chosen from the reference list.
2. Validate at ALL boundaries: API inputs, DB results, IPC payloads, localStorage — with Zod or Pydantic v2 schemas.
3. Never monolithic single-file apps: decompose into Presentation / Domain-State / Data / Core layers.
4. Mandatory docs: walkthrough.md (chronological changes + verification) and README/ARCHITECTURE.md (setup, env vars, structure) on every major task.
5. Defensive utilities from the reference: abortable async, debouncing, optimistic updates with automatic rollback, global error boundaries.

## Risks / owner items
- "Mandatory documentation" can produce boilerplate walkthroughs if applied mechanically — quality bar is in the content, not file existence.
- Choosing among 6 persistence engines per project needs judgment; the skill lists options, doesn't pick.
- Strict modularity may fight small utilities — scope says "full applications or complex screens", so tiny scripts are exempt by its own wording.

## Category and tags
build, security — production, architecture, persistence, validation, zero-mock, standards.

## Revision note
Identical across tools; index file pointing to three reference guides (read structure confirmed, ~250 lines total).
