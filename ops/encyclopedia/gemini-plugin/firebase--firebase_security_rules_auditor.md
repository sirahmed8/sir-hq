# firebase_security_rules_auditor

- Tool: `gemini-plugin` (plugin: `firebase`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\firebase\skills\firebase_security_rules_auditor\SKILL.md`
- SKILL.md size: 3579 chars

## What it does

Audit Firebase Firestore and Cloud Storage.

## Structure (headings inside SKILL.md)

- Overview
- Scoring Criteria
- Assessment: Security Validator (Red Team Edition)
- Mandatory Audit Checklist:
- Admin Bootstrapping & Privileges:
- Scoring Criteria (1-5):
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - email_verified is also checked (request.auth.token.email_verified == true).

## Key rules (verbatim lines from SKILL.md)

1. 1. **The Update Bypass:** Compare 'create' and 'update' rules. Can a user create
2. 1. **Authority Source:** Does the security rely on user-provided data
3. 1. **Business Logic vs. Rules:** Does the rule set actually support the app's

## Files inside the skill

- (SKILL.md only)
