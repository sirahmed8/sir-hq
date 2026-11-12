# firebase-firestore

## Summary
Router/edition-detection skill for Cloud Firestore: FIRST identify the instance edition via `firestore:databases:list`/`get` (STANDARD vs ENTERPRISE/native mode), pick the matching reference tree (references/standard/ vs references/enterprise/), and only then provision, model data, write SDK code or indexes. Security rules authoring is delegated: to the `firestore-rules-author` subagent if available, else the firestore-rules-creation skill. New databases default to Enterprise edition with a user-chosen location.

## When to use / when NOT
Use for ANY Firestore setup, querying, data modeling, compound indexes, or client SDK work — but ALWAYS run edition detection first because guides differ per edition. Not for Realtime Database or SQL Connect.

## Inputs, outputs, tools
- Inputs: existing database (or request for new one + location via `firestore:locations`).
- Outputs: selected edition → appropriate provisioning/data-model/security/SDK/indexes reference docs; optionally a new Enterprise database via `firestore:databases:create <id> --edition="enterprise" --location=<loc>`.
- Tools: `npx -y firebase-tools@latest firestore:databases:list|get|create|locations`; per-edition references (provisioning, data_model, web/android/ios/flutter/python sdk_usage, indexes); firestore-rules-creation skill / firestore-rules-author subagent.

## 5 most important rules
1. Edition detection is MANDATORY before dependencies, data models or rules — run databases:list/get first; guides under references/standard vs references/enterprise are not interchangeable.
2. No instance found → default to Enterprise edition and ASK the user for location (suggest colocating with other resources).
3. Ask the user which existing database to target before proceeding — never assume.
4. For Enterprise edition, you MUST read at least one platform SDK reference before writing any app code (pipeline initialization patterns differ).
5. Security rules: delegate to firestore-rules-author subagent when available, else follow firestore-rules-creation — never hand-wave rules.

## Risks / owner needs
Database creation is a real billable resource; edition choice affects pricing/capabilities. Location is permanent — confirm with user. Rules mistakes = data exposure.

## Category and tags
Category: cloud. Tags: firebase, firestore, database, nosql, security-rules, edition-detection.

## Revisions
Identical across the 7 tools; claude copy used.
