# firebase-security-rules-auditor

## Summary
A red-team auditor persona for Firebase (Firestore) security rules: given a ruleset it actively tries to break it — update bypasses, self-assigned roles, missing size limits (DoS), type juggling, permission-field escalation — then returns a JSON assessment (score 1-5, summary, findings with check/severity/issue/recommendation). It encodes a specific scoring rubric and a mandatory checklist distinguishing real vulnerabilities from acceptable patterns (e.g. hardcoded admin email is OK only with email_verified and no self-escalation path).

## When to use / when NOT
Use after writing or modifying firestore.rules, before shipping — as the adversarial review pass. Do NOT use as the authoring tool (firestore-rules-creation does that) or as a substitute for the emulator test suite. Findings are advisory; it returns JSON, not fixed rules.

## Inputs, outputs, tools
- Inputs: the firestore.rules content (and ideally the app's data model/queries for context).
- Outputs: JSON `{score, summary, findings[]}` — score 1 Critical … 5 Secure; findings carry severity critical/major/moderate/minor.
- Tools: none — pure analysis persona; optionally paired with firestore emulator for exploit verification.

## 5 most important rules
1. Audit as an attacker, not a reviewer: actively seek an operation sequence that bypasses each rule — never assume complexity means security.
2. Mandatory checks: create-vs-update asymmetry, authority sourced from request.resource.data (user-writable) for sensitive fields, business-logic support, missing string/array size limits = Resource Exhaustion/DoS, type checks, and hasOnly()/diff() WITHOUT ownership check = integrity vulnerability.
3. Scoring anchors: 1 = unauthorized access/privilege escalation; 2 = broken business logic/self-assigned roles; 3 = PII exposure/inconsistent critical-field validation; 4 = self-data-only issues/missing minor checks; 5 = comprehensive validation + ownership + role ACLs.
4. Hardcoded single admin email does NOT lose points IF email_verified is checked AND no path lets others add themselves as admin.
5. Output is strictly the JSON structure — check, severity, issue, recommendation per finding.

## Risks / owner needs
Audit quality depends on having the real rules + data model; a ruleset audited without the app's queries can miss "rules don't allow the app's actual queries" failures. Still requires human sign-off before production.

## Category and tags
Category: security. Tags: firebase, firestore, security-rules, audit, red-team, vulnerability.

## Revisions
Identical across the 7 tools; claude copy used.
