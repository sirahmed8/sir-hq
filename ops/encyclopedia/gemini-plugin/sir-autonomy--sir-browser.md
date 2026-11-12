# sir-browser

- Tool: `gemini-plugin` (plugin: `sir-autonomy`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\sir-autonomy\skills\sir-browser\SKILL.md`
- SKILL.md size: 1202 chars

## What it does

Zero-prompt autonomous Chrome browser bridge.

## Structure (headings inside SKILL.md)

- SIR Browser Autonomy
- Capabilities
- CLI Usage
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Read, navigate, and manage real Chrome tabs (`sir_browser_tabs`, `sir_browser_open`, `sir_browser_navigate`).
2. - Generate accessibility tree snapshots of any web page with numbered interactive element references (`[ref_1]`, `[ref_2]`, ...) via `sir_browser_snapshot`.
3. - Click buttons and links directly (`sir_browser_click(target="ref_1")` or CSS selectors).

## Files inside the skill

- (SKILL.md only)
