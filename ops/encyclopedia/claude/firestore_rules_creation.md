# firestore_rules_creation

- Tool: `claude`
- Category: security
- Source: `C:\Users\a7med\.claude\skills\firestore_rules_creation\SKILL.md`
- SKILL.md size: 27662 chars

## What it does

Use when writing, refactoring, or hardening production Cloud Firestore Security Rules in firestore.rules.

## Structure (headings inside SKILL.md)

- Firestore Security Rules Creation
- Workflow
- Advanced Validation for Business Logic
- Critical Constraints
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - CRUD operations (create, read, update, delete)
- - Authentication patterns (Firebase Auth, custom tokens, anonymous)
- - **Least privilege:** Grant minimum permissions required
- - **NEVER** allow users to update their own roles or permissions.

## Key rules (verbatim lines from SKILL.md)

1. - Required vs. optional fields
2. 1. **Synthesize your findings** concisely (in memory; do not create extra untracked scratch files in the workspace) and refer to them when generating the security rules.
3. - **Least privilege:** Grant minimum permissions required
4. - **MANDATORY:** You **MUST** use the **Validator Function Pattern** described
5. - **MANDATORY:** For **ALL** creates **AND ALL** updates, ensure that after

## Files inside the skill

- (SKILL.md only)
