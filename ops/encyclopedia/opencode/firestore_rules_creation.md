# firestore-rules-creation (skill name: firestore-rules-creation)

## Summary
The production-grade authoring workflow for Cloud Firestore `firestore.rules`: a 4-phase process — (1) scan the whole codebase for collections, queries, data models, auth patterns; (2) generate rules under strict principles (default-deny, least privilege, validator-function pattern applied to BOTH create and update, UID protection, no public reads ever); (3) a mandatory "devil's advocate" attack phase trying ~22 exploit vectors until none succeed; (4) syntax validation via `firebase deploy --only firestore:rules --dry-run`. Output includes an assumed-data-model header, helper functions, domain validators, and an explicit "prototype, please review" disclaimer to the user.

## When to use / when NOT
Use when creating, refactoring or hardening firestore.rules. Delegation rule: if the `firestore-rules-author` subagent exists, hand the work to it; if inside that subagent already, or no subagents, author directly with this workflow. Not for Storage rules (different surface) or for auditing existing rules (firebase-security-rules-auditor).

## Inputs, outputs, tools
- Inputs: the app codebase (collections, document paths, all where/orderBy/limit queries — rules MUST allow them), auth model, data schemas.
- Outputs: complete `firestore.rules` with data-model comment block, helpers (isAuthenticated/isOwner/uidUnchanged/isValid*/isScopedPath/isRecent/isPositive/isValidList/hasOnlyAllowedFields/areImmutableFieldsUnchanged), domain validators, plus the mandated prototype disclaimer.
- Tools: `firebase deploy --only firestore:rules --dry-run` for syntax validation; no emulator required but recommended.

## 5 most important rules
1. Default deny + least privilege: the first generated file must NEVER contain `allow read: true`; auth required unless explicitly requested otherwise.
2. Validator Function Pattern is MANDATORY on BOTH create AND update — the "ownership-only update" trap (isOwner without isValidX) is a critical vulnerability; every string/list/map field needs size limits (1MB-string DoS); permission fields (roles/editors/ownerId) immutable for non-owners via areImmutableFieldsUnchanged.
3. RBAC absolutes: users can NEVER self-assign/escalate roles or grant access to others' data — role checks must not rely on user-writable document fields; prefer request.auth.token/custom claims.
4. PII rule: documents containing PII are owner-read ONLY; public profiles require denormalized public fields onto resources or a separate public collection — never mixed-content documents.
5. Devil's advocate is non-skippable: run all attack vectors (update bypass, ownership hijack, immutable-field change, type juggling, schema pollution, counter replay via getAfter(), query mismatch, mixed-content leak); fix and repeat until clean, then dry-run validate, then present as a PROTOTYPE needing user review — never claim the rules are perfect.

## Risks / owner needs
Rules mistakes = data breach; the skill itself insists on humility and user review. Query-mismatch (rules stricter than app queries) breaks the app — Phase 1 query scan prevents it. Denormalized identity fields carry spoofing risk unless validated against auth token.

## Category and tags
Category: security. Tags: firestore, security-rules, rbac, pii, validation, zero-trust.

## Revisions
Identical across the 7 tools; claude copy used.
