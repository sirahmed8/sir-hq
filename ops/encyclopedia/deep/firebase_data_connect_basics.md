# firebase-data-connect (skill name: firebase-data-connect; product now "Firebase SQL Connect")

## Summary
Guide for Firebase SQL Connect (renamed from Data Connect): a relational backend on Cloud SQL for PostgreSQL exposed through a GraphQL schema with auto-generated type-safe SDKs. Strict file layout (`dataconnect/` with dataconnect.yaml, schema/schema.gql, connector/{connector.yaml,queries.gql,mutations.gql}, local-only seed_data.gql), a fixed workflow (model → authorized operations → SDK generation), and a feature-capability map to 10+ reference files covering schema, operations, security, realtime, native SQL, search, config, functions, seeding, templates, examples.

## When to use / when NOT
Use for relational data needs with GraphQL + type-safe clients (web TS, Android Kotlin, iOS Swift, Flutter Dart, Node admin). Default to Native GraphQL operations; use Native SQL only when explicitly requested or for advanced Postgres features (PostGIS, window functions). Not for Firestore-style document needs (use firebase-firestore).

## Inputs, outputs, tools
- Inputs: data model requirements, target platforms, auth requirements.
- Outputs: schema.gql types with @table/@col/@ref, queries/mutations with @auth/@check/@redact/@transaction/@refresh, generated SDKs via connector.yaml `generate:` blocks, deployed Cloud SQL backend.
- Tools: `npx -y firebase-tools@latest init dataconnect`, `dataconnect:compile` (validation), `dataconnect:sdk:generate`, `emulators:start --only dataconnect`, `deploy --only dataconnect`; reference/ and examples.md, templates.md.

## 5 most important rules
1. Follow the strict workflow: schema/schema.gql first (@table types), then connector queries/mutations, then SDK generation — validate each with `dataconnect:compile` and review generated schema extensions in `.dataconnect/schema/main/`.
2. Secure by default: every operation needs @auth level (PUBLIC/USER/NO_ACCESS) plus @check/@redact row-level rules — never leave operations open.
3. Use `_upsert` for insert-or-update (critical for user profiles); `@transaction` + `_expr: "response.<prevStep>"` for multi-step atomic ops; `@refresh` + CEL for realtime subscriptions.
4. Native SQL is the exception: raw `_select`/`_execute` strings lack type safety — strict positional `$1` params, quoting rules; default to auto-generated GraphQL fields.
5. `seed_data.gql` is LOCAL ONLY (prototype/test) — production seeding uses Admin SDK bulk or migrations per data_seeding.md.

## Risks / owner needs
Deploy creates real Cloud SQL resources (cost). Vector/full-text search and realtime have dedicated reference docs — read before implementing. Admin SDK path exists for privileged operations.

## Category and tags
Category: cloud. Tags: firebase, sql-connect, postgresql, graphql, type-safe-sdk, database.

## Revisions
Identical across the 7 tools; claude copy used (name field `firebase-data-connect`).
