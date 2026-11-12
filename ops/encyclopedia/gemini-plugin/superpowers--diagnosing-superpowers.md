# diagnosing-superpowers

- Tool: `gemini-plugin` (plugin: `superpowers`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\diagnosing-superpowers\SKILL.md`
- SKILL.md size: 6920 chars

## What it does

Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it took too long", "why is it so expensive", "what is it doing" — or wants to build a bug report for the superpowers maintainers, for the current session or a past one identified by id or path, on any harness.

## Structure (headings inside SKILL.md)

- Diagnosing Superpowers
- Overview
- Workflow
- Quick reference
- Hard rules
- Red Flags
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Read-only.** Never modify, move, or delete a session file.

## Key rules (verbatim lines from SKILL.md)

1. 6. **Export** — only when your partner asks for a bundle; never build one
2. - **Read-only.** Never modify, move, or delete a session file.
3. - **Approval gates.** No archive before your partner has seen the scrub
4. - **Intake before analysis.** Nothing in steps 2–7 starts until your

## Files inside the skill

- `prompts/analyst-common.md` — "Y"
- `prompts/cost-and-time.md` — "R"
- `prompts/plan-adherence.md` — "R"
- `prompts/quality-evidence.md` — "R"
- `prompts/repeated-work.md` — "R"
- `prompts/request-conflicts.md` — "R"
- `prompts/scrub-audit.md` — "R"
- `prompts/scrub.md` — "R"
- `prompts/similar-session.md` — "Y"
- `prompts/skill-timeline.md` — "R"
- `prompts/stumbles.md` — "R"
- `references/context-safety.md` — "Context safety for session transcripts"
- `references/github-issues.md` — "GitHub issues"
- `references/redaction-policy.md` — "Redaction policy"
- `references/session-discovery.md` — "Discover the session history"
- `templates/bundle-README.md` — "Superpowers session diagnosis bundle"
- `templates/case.md` — "Case: <session-id>"
- `templates/issue.md` — "T"
- `templates/report.md` — "Session diagnosis: <session-id>"
