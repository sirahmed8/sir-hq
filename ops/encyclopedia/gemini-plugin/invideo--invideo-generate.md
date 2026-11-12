# invideo-generate

- Tool: `gemini-plugin` (plugin: `invideo`)
- Category: media
- Source: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\invideo-generate\SKILL.md`
- SKILL.md size: 1196 chars

## What it does

Generate images, video, voice-over, music, sound effects and 3D for an invideo video: picking and prompting a model, pricing, narration first, retries.

## Structure (headings inside SKILL.md)

- Generation in invideo
- How to generate
- What to read
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Pick the model from the live list (`invideo gen models` / `find_models`); it changes as models ship.
2. - Price it with `invideo gen run … --dry-run` / `dry_run`, say the cost, then run it with `--max-credits` / `max_credits`. Make one sample, review it, then make the rest.
3. - With narration, generate the voice first, read its length (`invideo media metadata` / `media`), then generate picture to fit.

## Files inside the skill

- `references/models.md` — "Models"
