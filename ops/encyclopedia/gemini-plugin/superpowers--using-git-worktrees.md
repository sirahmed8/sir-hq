# using-git-worktrees

- Tool: `gemini-plugin` (plugin: `superpowers`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\using-git-worktrees\SKILL.md`
- SKILL.md size: 6803 chars

## What it does

Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback

## When to use (from skill text)

- **Only use this if Step 1a does not apply** — you have no native worktree tool available. Create a worktree manually using git.

## Structure (headings inside SKILL.md)

- Using Git Worktrees
- Overview
- Step 0: Detect Existing Isolation
- If this returns a path, you're in a submodule, not a worktree — treat as normal repo
- Step 1: Create Isolated Workspace
- 1a. Native Worktree Tools (preferred)
- 1b. Git Worktree Fallback
- Determine path based on chosen location
- Step 2: Project Setup
- Node.js
- Rust
- Python
- Go
- Step 3: Verify Clean Baseline
- Use project-appropriate command
- Report
- Quick Reference
- Common Rationalizations
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - On a branch: "Already in isolated workspace at `<path>` on branch `<name>`."
2. - Detached HEAD: "Already in isolated workspace at `<path>` (detached HEAD, externally managed). Branch creation needed at finish time."
3. 1. **Check your instructions for a declared worktree directory preference.** If the user has already specified one, use it without asking.

## Files inside the skill

- (SKILL.md only)
