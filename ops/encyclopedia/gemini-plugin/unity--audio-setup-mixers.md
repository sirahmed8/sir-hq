# audio-setup-mixers

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: media
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\audio-setup-mixers\SKILL.md`
- SKILL.md size: 7521 chars

## What it does

Routes Audio Sources into existing Audio Mixer Groups, classifying each source by what it plays. Use when the user asks about cleaning up mixer assignments, routing audio through a mixer, or which group a sound belongs in.

## Structure (headings inside SKILL.md)

- Audio Mixer Setup
- Step 0: Confirm you can run C# in the Editor
- Passing C# to `script eval`
- Step 1: Pre-flight
- Step 2: Find scene references
- Step 3: Agree the group list, and get any missing groups created
- Step 4: Route the Audio Sources
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Do not fall back to editing `.mixer` files by hand.** Mixer routing is not safely
2. - **Types must be fully qualified.** A bare `AssetDatabase` or `Volume` does not resolve

## Files inside the skill

- `references/api.md` — ""
- `SECURITY.md` — "Security notes: audio-setup-mixers"
