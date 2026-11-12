# google_maps_platform

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\google_maps_platform\SKILL.md`
- SKILL.md size: 25002 chars

## What it does

Architecture and implementation guidance for Google Maps Platform APIs, Places, Geocoding, Routes, and Street View across Web and Mobile.

## Structure (headings inside SKILL.md)

- Google Maps Platform Main Skill
- 1. Grounding and Routing Workflow
- Architecture and Logic
- MANDATORY FIRST ACTION — do this before reading anything else
- 2. Global Agent Directives / Reasoning Framework
- 3. Mandatory Compliance Checkpoints
- 4. Deprecated / Legacy APIs (Hard Failures)
- 5. Critical Failures (CF)
- 6. Use Case Product Mapping
- 7. Credentials Setup & Demo Key Quickstart
- Production: Standard API Keys
- Demo Key Quickstart
- 8. Required Response Verification
- Code Requirement
- Chat Response Appendix Checklist
- Completion checklist (self-verify before ending the task)
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP tool, MCP docs, MCP returns, MCP with

## Risks / cautions found in text

- *   **`PlaceAutocompleteElement`** (`<gmp-place-autocomplete>`): Drop-in web
- -   **OAuth / Application Default Credentials (ADC):** Required for Route
- -   **Security:** You MUST remind the user to restrict their production key by
- 2.  Sign in with a Google account (any personal account works; no billing

## Key rules (verbatim lines from SKILL.md)

1. 1.  **Retrieve Resources First:** Never start coding from memory. Always fetch
2. 4.  **Implement:** Generate the code while strictly avoiding the traps listed in
3. 5.  **Validate:** Before concluding your turn, verify that your response
4. -   **Doc Links:** All URLs linking to Google Maps Platform documentation must
5. *   **You MUST NOT** write new code against them.

## Files inside the skill

- (SKILL.md only)
