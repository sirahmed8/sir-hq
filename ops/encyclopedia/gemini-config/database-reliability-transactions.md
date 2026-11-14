# database-reliability-transactions

## Summary
Doctrine skill for durable data layers: atomic multi-table transactions with automatic rollback, client idempotency keys (UUID v4) with cached-response replay, submit-button debouncing, index discipline (FKs, filter/sort columns, no N+1), keyset/cursor pagination over OFFSET, and safe file uploads (server-side MIME magic-byte checks, direct-to-cloud signed-URL uploads, WebP/AVIF compression).

## When to use / when NOT
Use when implementing any feature with mutations, payments/orders, uploads, or large lists. Do NOT use for read-only pages or as a DB engine tutorial — it states rules, not driver specifics.

## Inputs, outputs, tools
- Inputs: the feature's data model and mutation paths.
- Outputs: transactional code patterns, idempotency plumbing, indexes, pagination, upload pipeline.
- Tools: none — ORM/DB-agnostic guidance (examples in TypeScript/Drizzle-style syntax).

## 5 most important rules
1. Any multi-record mutation runs inside one atomic transaction — partial failure must roll back everything.
2. Every financial/critical mutation accepts an Idempotency-Key; replay returns the cached response, never re-processes.
3. Disable submit buttons immediately on click to kill double-submits.
4. Index FKs, status filters, and sort timestamps; paginate with keyset (`WHERE id > :last`) not OFFSET.
5. Verify upload MIME by magic bytes server-side; push files straight to object storage via signed URLs; compress images to WebP/AVIF.

## Risks / things needing the owner
Idempotency stores (Redis/DB table) and signed-URL buckets need infra the owner provisions. Choosing wrong index trade-offs on huge tables should be measured, not guessed.

## Category / tags
build · database, transactions, idempotency, pagination, uploads

## Revisions
Six tools hold it; bodies byte-identical, only `description` differs. Claude copy preferred for trigger-style description.
