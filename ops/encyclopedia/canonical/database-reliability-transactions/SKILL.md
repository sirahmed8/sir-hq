---
name: database-reliability-transactions
description: "Use when a feature needs atomic transactions with rollback, idempotency keys on mutations, query indexing, or keyset pagination."
---

# Database Reliability, Transactions & Idempotency Protocol

This skill enforces enterprise database durability, data consistency, query performance tuning, and safe file handling across all persistent operations.

---

## 1. Atomic Database Transactions & Rollbacks

- **Multi-Step Mutation Atomicity**:
  - Whenever an operation touches multiple tables or records (e.g., checkout + inventory decrement + payment record + audit log), wrap the entire sequence in an atomic transaction:
    ```typescript
    await db.transaction(async (tx) => {
      await tx.insert(orders).values(orderData);
      await tx.update(inventory).set({ stock: stock - 1 });
      await tx.insert(auditLogs).values(logData);
    });
    ```
  - If any step throws an error, the entire operation must automatically roll back without leaving orphaned rows or inconsistent state.

---

## 2. Idempotency & Duplicate Mutation Prevention

- **Client Idempotency Keys**:
  - Every financial transaction, order submission, or critical mutation must accept a unique client-generated `Idempotency-Key` header (UUID v4).
  - Check the database or Redis cache for existing idempotency records before executing. If found, return the cached successful response without re-processing.
- **Button Debouncing**:
  - Debounce all submit and payment CTAs on the client to prevent double-clicks.
  - Immediately set interactive buttons to `disabled` with an inline loading indicator upon initiation.

---

## 3. Query Indexing & Pagination

- **Database Indexes**:
  - Always index foreign keys (`user_id`, `organization_id`), status columns used in filters (`status = 'ACTIVE'`), and created timestamps used in sorting.
  - Avoid N+1 queries by using eager loading, joins, or dataloader batch fetching.
- **Keyset / Cursor Pagination**:
  - For high-velocity datasets, use cursor-based pagination (`WHERE id > :last_id LIMIT 20`) rather than expensive `OFFSET` queries.

---

## 4. Safe Cloud File Uploads

- **Client & Server MIME Verification**: Verify magic bytes on the server to prevent executable files from being disguised as images.
- **Direct-to-Cloud Uploads**: Upload directly to cloud object storage (S3 / Google Cloud Storage) via short-lived signed URLs; never stream large binaries through application compute.
- **Image Compression**: Automatically convert and compress uploaded images to WebP or AVIF formats before saving to storage buckets.
