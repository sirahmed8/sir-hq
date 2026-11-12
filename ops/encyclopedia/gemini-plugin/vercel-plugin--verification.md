# verification

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\verification\SKILL.md`
- SKILL.md size: 5112 chars

## What it does

Full-story verification.

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

- 4. **External dependencies** — If the route calls a database, third-party API, or Vercel service (Blob, Marketplace storage, AI SDK): verify the client is initialized, credentials are present, and the call shape matches the SDK docs

## Key rules (verbatim lines from SKILL.md)

1. - You find the **first broken boundary** — report it with evidence and a specific fix, do not continue past the break
2. - Two consecutive layers return no useful signal (e.g., no logs, no errors, no output) — flag the observability gap and recommend adding logging before continuing

## Files inside the skill

- (SKILL.md only)
