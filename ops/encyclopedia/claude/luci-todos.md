# luci-todos

- Tool: `claude`
- Category: automation
- Source: `C:\Users\a7med\.claude\skills\luci-todos\SKILL.md`
- SKILL.md size: 3400 chars

## What it does

Read and write the user's per-project to-do lists in ~/.Life/todos/. Use when the user asks to add, tick, edit or list a to-do, asks what is left on a project, or when a distill run suggests to-dos from a daily report.

## Structure (headings inside SKILL.md)

- Project to-dos
- The files
- Luci Desktop
- Suggested by Luci
- Two kinds of write
- Reading
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - [ ] Fix Windows sign-in drop-off before 1.0.35
- - [ ] Remove the login token Luci stored in screen memory <!-- from: reflections/daily/2026-10-05.md -->
- - Tick, untick, rename, reword, delete: change only that line and its

## Key rules (verbatim lines from SKILL.md)

1. - [ ] Fix Windows sign-in drop-off before 1.0.35
2. - `## Suggested by Luci` is always the last section. Everything above it
3. - Add: append `- [ ] <title>` after the last to-do above `## Suggested by Luci`

## Files inside the skill

- `.luci-skill-manifest.json`
