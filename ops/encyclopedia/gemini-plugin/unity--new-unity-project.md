# new-unity-project

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\new-unity-project\SKILL.md`
- SKILL.md size: 24508 chars

## What it does

Guides creating a new Unity project, gathering concept, platforms, and monetization before setting up the project, source control, and packages. Use when the user asks to start a new game or prototype. Runs an opinionated paved path by default; full interview on request.

## When to use (from skill text)

- it without this skill re-triggering.

## Structure (headings inside SKILL.md)

- New Unity Project
- Mode: paved by default, guided on request
- Sign-in and license (before your first question)
- The Defaults table
- The assumptions manifest
- Before Step 1: check the delegated skills are loaded
- The flow — and where the parallelism is
- Step 1 — Concept
- Step 2 — Platforms & monetization, then start installing
- Start in the BACKGROUND. Module names per platform are in the unity-cli skill.
- --bare only on the user's ask (see Mode).
- Step 3 — Join: project ready, result reconciled
- Step 4 — Source control
- Step 5 — Packages
- Step 6 — Player identity, then the craft floors
- Step 7 — Visual baseline
- Step 8 — Save & first commit
- Step 9 — Hand off
- Scope — what this skill does NOT do
- Checklist
- Common mistakes
- (none)

## Tools / MCPs it needs

- allowed-tools: - Bash - Write - Edit
- allowed-tools (frontmatter): `- Bash - Write - Edit`

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Never tell the user to sign in or activate a license themselves, and never hand them commands to
2. - Declining stops the run before the create only when nothing can license the Editor. A user who
3. 4. **UI stack.** HUD and menus use a uGUI Canvas + TextMeshPro or UI Toolkit — **never `OnGUI`**.
4. - [ ] Delegated skills checked before Step 1 (incl. `craft-game-floors`): a missing one offered, or named
5. - [ ] Mode decided once; in paved, the manifest printed before the create launches

## Files inside the skill

- `references/skill-setup.md` — "Skill setup — getting the delegated skills loaded"
- `SECURITY.md` — "Security notes: new-unity-project"
