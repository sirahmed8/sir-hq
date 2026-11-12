# skill-installer

- Tool: `claude`
- Category: ops
- Source: `C:\Users\a7med\.claude\skills\skill-installer\SKILL.md`
- SKILL.md size: 3425 chars

## What it does

Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

## Structure (headings inside SKILL.md)

- Skill Installer
- Communication
- Scripts
- Behavior and Options
- Notes
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - If download fails with auth/permission errors, falls back to git sparse checkout.
- - Private GitHub repos can be accessed via existing git credentials or optional `GITHUB_TOKEN`/`GH_TOKEN` for download.

## Key rules (verbatim lines from SKILL.md)

1. - List skills when the user asks what is available, or if the user uses this skill without specifying what to do. Default listing is `.curated`, but you can pass `--path skills/.experimental` when they ask about experimental skills.
2. - Install from the curated list when the user provides a skill name.
3. - Install from another repo when the user provides a GitHub repo/path (including private repos).

## Files inside the skill

- `agents/openai.yaml`
- `assets/skill-installer-small.svg`
- `assets/skill-installer.png`
- `LICENSE.txt` — ""
- `scripts/github_utils.py`
- `scripts/install-skill-from-github.py`
- `scripts/list-skills.py`
