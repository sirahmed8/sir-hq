# ui-plugin-navigation

- Tool: `antigravity-builtin`
- Category: design
- Source: `C:\Users\a7med\.gemini\antigravity\builtin\skills\ui-plugin-navigation\SKILL.md`
- SKILL.md size: 3801 chars

## What it does

Discover UI plugin panels relevant to the current task and surface a one-click pill in chat to open (toggle) them in the side pane. Use when a running UI plugin's panel would help with what the user is doing, or right after the user enables a new UI plugin pane and a shortcut to open it is handy.

## Structure (headings inside SKILL.md)

- UI Plugin Navigation
- When to surface a pill
- Step 1: Find UI plugin panes and their views
- Step 2: Emit the pill link
- Constraints & Tips
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 2.  **After a new UI plugin pane is enabled.** When the user has just created
2. *   **The pill toggles the aux pane.** Clicking opens the plugin's panel. DO NOT
3. *   **One pill per pane.** Don't emit multiple links to the same view.

## Files inside the skill

- (SKILL.md only)
