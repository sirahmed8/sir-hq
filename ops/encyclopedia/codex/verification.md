# verification

- Tool: `codex`
- Category: data
- Source: `C:\Users\a7med\.codex\skills\verification\SKILL.md`
- SKILL.md size: 5067 chars

## What it does

Full-story end-to-end verification across browser, API, data flow, and runtime environment.

## When to use (from skill text)

- ## When This Triggers
- Report what you find at each layer before proceeding. Use this reporting contract:
- Trace the feature's data path from trigger to completion:

## Structure (headings inside SKILL.md)

- Full-Story Verification
- When This Triggers
- Step 1 — Infer the User Story
- Step 2 — Establish Evidence Baseline
- Step 3 — Walk the Data Flow
- Step 4 — Report With Evidence
- Verification Report: [Feature Name]
- Flow Status
- Issues Found
- Verified Working
- Stop Conditions
- Suggest Verification After Implementation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 4. **External dependencies** — If the route calls a database, third-party API, or Vercel service (KV, Blob, Postgres, AI SDK): verify the client is initialized, credentials are present, and the call shape matches the SDK docs

## Key rules (verbatim lines from SKILL.md)

1. - You find the **first broken boundary** — report it with evidence and a specific fix, do not continue past the break
2. - Two consecutive layers return no useful signal (e.g., no logs, no errors, no output) — flag the observability gap and recommend adding logging before continuing

## Files inside the skill

- (SKILL.md only)
