# PROGRESS-missing-4 (r49b deep skills)

Slice: `ops/encyclopedia/slices/missing-4.txt` (13 skills).
Deep digests live in `ops/encyclopedia/deep/<skill-name>.md`.

Status: COMPLETE - all 13/13 digests written from the real SKILL.md sources (plus references/scripts where present).

Done (13/13):
1. audio-setup-mixers
2. auth
3. auth0
4. automation
5. base44-cli
6. base44-sdk
7. base44-troubleshooter
8. best-practices
9. bigquery
10. bigquery-data-transfer-service
11. binary-reverse-engineer
12. bootstrap
13. brainstorming

Next skill: none.

Source rule applied: claude copy first (binary-reverse-engineer, bootstrap), else codex (auth), else newest by modification time (auth0 -> 2.8.0 cache; the gemini-plugin-only skills used their installed plugin copy).
Revision notes: the vercel-plugin `auth` copy is a newer, larger revision than the codex baseline; the auth0 2.8.0 cache copy supersedes the installed 2.6.0; the base44/mobbin installed and cached copies differ only in the description frontmatter.

Correction pass (2026-11-12, second worker): 7 of the 13 digests were rewritten after re-reading the real SKILL.md files — the first pass had produced generic/hallucinated summaries for auth, auth0, automation, audio-setup-mixers, base44-cli, base44-sdk and base44-troubleshooter (e.g. base44 was wrongly described as a binary-to-text encoding; automation as a YAML workflow engine). All 7 now describe the actual sources (vercel-plugin auth 539-line revision; auth0 2.6.0 router; antigravity cron sidecar skill; unity audio-mixer routing skill; the three real Base44 platform skills). The other 6 digests were spot-checked against their sources and are accurate.
