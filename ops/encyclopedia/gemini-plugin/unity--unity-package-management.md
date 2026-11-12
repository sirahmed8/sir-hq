# unity-package-management

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: research
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\unity-package-management\SKILL.md`
- SKILL.md size: 16368 chars

## What it does

Adds, removes, upgrades, and discovers Unity (UPM) packages from outside the Editor, with the Pipeline package commands first and a C# script as the fallback. Use for package installs, verifying package IDs and versions, or choosing which packages a game needs.

## When to use (from skill text)

- Use this section only when `package add` can't run: no Editor is open and you don't want one
- them; use this method when you need it **headless** (in a script or CI).

## Structure (headings inside SKILL.md)

- Unity Package Management (Pipeline commands first, C# script as the fallback)
- Use the package commands first
- When to use
- Choosing what to install
- Fallback: no Editor to ask (the C# Client API)
- The `-quit` problem — why NOT `unity run` for installs
- The installer script
- Discovering / verifying packages
- Run it headless (direct Editor invocation, no `-quit`)
- Install directory of that editor (Hub layout), via the unity CLI
- Resolve the executable per-OS (handles both "dir containing Unity.app" and the ".app" itself)
- Verify
- Every requested id should appear as a dependency
- Import & save headlessly (generate `.meta` files)
- Notes
- (none)

## Tools / MCPs it needs

- allowed-tools: - Bash - Write - Edit
- allowed-tools (frontmatter): `- Bash - Write - Edit`

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Verify a package id exists, or find its available versions, before depending on it.
2. - All scripts live under `Editor/` because they use `UnityEditor`; they never ship in a build.

## Files inside the skill

- `references/select-packages.md` — "Selecting packages"
