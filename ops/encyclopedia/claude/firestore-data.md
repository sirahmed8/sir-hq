# firestore-data

## Summary
A script-based Firestore data-operations skill (Google-published, Apache-2.0): six Node.js scripts under scripts/ for direct document/collection work — add_documents, delete_documents (bulk), get_documents (bulk by path), list_collections (root or subcollections under a parent doc), query_collection (typed filters + orderBy + limit + analyzeQuery explain metrics), update_document (full or updateMask partial, mask fields absent from data get deleted). All paths are RELATIVE collection/document paths, never absolute project/database paths. Scripts auto-load .env files.

## When to use / when NOT
Use for CRUD and structured queries against Firestore when you have concrete paths or filter clauses — including exploring collection hierarchies via list_collections. Do NOT use for rules/index/config management (other firebase skills) or when you only need a count — prefer narrow queries with limit.

## Inputs, outputs, tools
- Inputs: relative collectionPath/documentPath(s), Firestore native-JSON typed documentData (stringValue/integerValue/doubleValue/booleanValue/timestampValue RFC3339/geoPointValue/arrayValue/mapValue/nullValue/bytesValue base64/referenceValue), filters array ({field, op, value} with ops incl. array-contains, in, not-in), orderBy JSON, limit (default 100), updateMask array, returnData flag.
- Outputs: operation results; document data only when returnData=true (default false to save agent context).
- Tools: `node <skill_dir>/scripts/<script>.js '<json-params>'` (bash or PowerShell quoting), env auto-loaded from .env files.

## 5 most important rules
1. Every field value MUST be wrapped in its Firestore type indicator — raw JSON scalars are invalid; integers may be passed as strings; binary is base64 bytesValue; timestamps are RFC3339 strings.
2. Paths are RELATIVE ('users/userId/posts'), never 'projects/{pid}/databases/{db}/documents/...' absolute form.
3. update_document: use updateMask for precision — mask fields missing from documentData are DELETED; full updates omit the mask.
4. returnData defaults false — set true only when you must verify exact written data (context economy).
5. query_collection: filters need explicit op+value, orderBy is a JSON {field,direction}, analyzeQuery=true returns explain metrics for performance debugging; security rules must permit the operation.

## Risks / owner needs
Destructive ops (delete_documents bulk, field deletion via mask) are irreversible — confirm scope first. Writes depend on Firestore security rules allowing them; wrong project env vars silently target the wrong database — verify .env project before bulk ops.

## Category and tags
Category: data. Tags: firestore, nosql, crud, documents, query, google-cloud, scripts.

## Revisions
Only claude + gemini copies listed; claude copy used (gemini copy unchecked for diffs — flag if HQ wants a byte-diff audit).
