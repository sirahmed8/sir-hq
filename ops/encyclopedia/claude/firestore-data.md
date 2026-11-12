# firestore-data

- Tool: `claude`
- Category: data
- Source: `C:\Users\a7med\.claude\skills\firestore-data\SKILL.md`
- SKILL.md size: 8310 chars

## What it does

Handles NoSQL document operations and collection hierarchy exploration. Use for CRUD tasks and data retrieval. Provides flexible document manipulation and structured querying.

## When to use (from skill text)

- Use this if you know the exact path of a collection and the filtering clause you would like for the document.

## Structure (headings inside SKILL.md)

- Usage
- Scripts
- add_documents
- delete_documents
- get_documents
- list_collections
- query_collection
- update_document
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. Delete fields using update mask: To delete fields, include them in the updateMask but omit them from documentData

## Key rules (verbatim lines from SKILL.md)

1. 1. Always use typed values in the documentData: Every field must be wrapped with its appropriate type indicator (e.g., {"stringValue": "text"})
2. 4. Validate data before sending: Ensure your data matches Firestore's native JSON format
3. 6. Base64 encode binary data: Binary data must be base64 encoded in the bytesValue field
4. 1. Use update masks for precision: When you only need to update specific fields, use the updateMask parameter to avoid unintended changes
5. 2. Always use typed values in the documentData: Every field must be wrapped with its appropriate type indicator (e.g., {"stringValue": "text"})

## Files inside the skill

- `scripts/add_documents.js`
- `scripts/delete_documents.js`
- `scripts/get_documents.js`
- `scripts/list_collections.js`
- `scripts/query_collection.js`
- `scripts/update_document.js`
