# invideo-pipeline

- Tool: `gemini-plugin` (plugin: `invideo`)
- Category: media
- Source: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\invideo-pipeline\SKILL.md`
- SKILL.md size: 4075 chars

## What it does

Use for scale and automation: a CSV to many videos, `--json`, idempotency keys, CI with device sign-in, outreach at scale, course batches, bulk orders, and several agents sharing one project.

## Structure (headings inside SKILL.md)

- Many videos at once
- Start from a brief
- What makes it work
- Craft
- Scripted runs
- Several agents in one project
- By type
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - The session lives on the machine that signed in (the keychain or keyring, else `~/.config/invideo/credentials.json`). For CI, use a persistent runner where someone signed in once with `INVIDEO_NO_BROWSER=1 invideo auth login`.

## Key rules (verbatim lines from SKILL.md)

1. - Fix the template or the data, never one video by hand.
2. - **Worst rows.** Before the batch, run the hardest rows: longest name, empty cells, ALL CAPS, other scripts, zero and one, a portrait photo in a wide slot, a white logo on white. Each should look designed, not just unbroken.
3. - **Text.** Leave room, then wrap, then shrink to a floor, then switch layout. Never truncate a name or split first from last. Hold time follows word count; the slack goes into a held background, never the beat that hits the music. Short labels grow most in translation.
4. - **Fallbacks.** Missing data gets a rewritten line ("Welcome aboard"), not "Hi Friend". Thin-data viewers get a warmer, shorter cut about a beginning, never a sad number. When wrong is worse than missing, skip the row.
5. - **Variation.** Variants are cousins, lessons are siblings. Vary the hook and first seconds hard, keep the brand thread; a caption swap is not a variant. Rotate two or three layouts so the set never looks machine-made. Your boredom is not the viewer's.

## Files inside the skill

- `references/collaborate.md` — "Several agents and a person in one project"
