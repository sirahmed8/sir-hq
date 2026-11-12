# database-reliability-transactions

- Tool: `claude`
- Category: data
- Source: `C:\Users\a7med\.claude\skills\database-reliability-transactions\SKILL.md`
- SKILL.md size: 2614 chars

## What it does

Use when a feature needs atomic transactions with rollback, idempotency keys on mutations, query indexing, or keyset pagination.

## Structure (headings inside SKILL.md)

- Database Reliability, Transactions & Idempotency Protocol
- 1. Atomic Database Transactions & Rollbacks
- 2. Idempotency & Duplicate Mutation Prevention
- 3. Query Indexing & Pagination
- 4. Safe Cloud File Uploads
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Whenever an operation touches multiple tables or records (e.g., checkout + inventory decrement + payment record + audit log), wrap the entire sequence in an atomic transaction:
- - Debounce all submit and payment CTAs on the client to prevent double-clicks.

## Key rules (verbatim lines from SKILL.md)

1. - If any step throws an error, the entire operation must automatically roll back without leaving orphaned rows or inconsistent state.
2. - Every financial transaction, order submission, or critical mutation must accept a unique client-generated `Idempotency-Key` header (UUID v4).
3. - Check the database or Redis cache for existing idempotency records before executing. If found, return the cached successful response without re-processing.
4. - Always index foreign keys (`user_id`, `organization_id`), status columns used in filters (`status = 'ACTIVE'`), and created timestamps used in sorting.
5. - Avoid N+1 queries by using eager loading, joins, or dataloader batch fetching.

## Files inside the skill

- (SKILL.md only)
