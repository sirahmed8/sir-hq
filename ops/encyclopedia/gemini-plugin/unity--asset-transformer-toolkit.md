# asset-transformer-toolkit

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: ops
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\asset-transformer-toolkit\SKILL.md`
- SKILL.md size: 2951 chars

## What it does

>- In the Unity Editor, imports 3D models and point clouds with Asset Transformer Toolkit (formerly Pixyz), and creates, edits, and runs RuleSets, Actions, and LODs. Use for Pixyz imports in a Unity project, not for converting files from the shell.

## Structure (headings inside SKILL.md)

- Before you start: check the package version
- API Reference
- Technical Notes
- Importers
- RuleSets and Actions
- Levels of Detail
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 2. **Not installed:** tell the user this workflow needs Asset Transformer Toolkit 4.0 or later, which is an entitled Unity package they may need access to through their Unity plan, and stop. Don't add it to the manifest yourself.
2. 3. **Installed below 4.0.0:** tell the user which version you found and that 4.0 or later is required, and ask before upgrading. Don't fall back to older APIs, raw C# against internal types, or reflection.

## Files inside the skill

- `references/create-importer.md` — ""
- `references/lods.md` — "C"
- `references/rule-api.md` — ""
- `references/ruleblock-api.md` — ""
- `references/ruleset-api.md` — ""
- `references/rulesets-and-actions.md` — ""
- `SECURITY.md` — "Security notes: asset-transformer-toolkit"
