# distill-my-life

- Tool: `claude`
- Category: automation
- Source: `C:\Users\a7med\.claude\skills\distill-my-life\SKILL.md`
- SKILL.md size: 13212 chars

## What it does

Distill each day's raw activity into a daily report. Ensures ~/.Life exists, pulls the day's activity via Luci, writes an objective report under ~/.Life/reflections/daily/, and writes new entities under ~/.Life/entities/. Use when the user says "distill", "distill my life", "catch up on daily reports", "summarize the last few days", or first needs the life folders created.

## Structure (headings inside SKILL.md)

- Distill — daily distillation
- Step 0: ensure the life file system
- Step 0.5: read the user's rules
- Step 1: decide which days to process
- Step 2: write each daily file
- Pulling a day from Luci
- YAML (required)
- Body
- HH:MM–HH:MM
- HH:MM–HH:MM — title
- HH:MM–HH:MM — no samples ({duration})
- Step 3: write entities
- Microsoft-Luci-Electron
- Step 3.5: suggest to-dos
- Step 4: first-time notification
- Step 5: the profile
- Final output

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Never write to `RULES.md`.** Do not create it, tidy it, reformat it,
2. - Missing file, or a file you cannot read: continue with the defaults. Do not
3. - Before writing anything, check whether `~/.Life/reflections/daily/`
4. - Get today's date via Bash (never guess from memory).
5. - Only complete days — yesterday and earlier. **Never process today.**

## Files inside the skill

- `.luci-skill-manifest.json`
