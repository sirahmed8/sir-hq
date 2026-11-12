# finishing-a-development-branch

- Tool: `gemini-plugin` (plugin: `superpowers`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\finishing-a-development-branch\SKILL.md`
- SKILL.md size: 7729 chars

## What it does

Use when implementation is complete, all tests pass, and you need to decide how to integrate the work

## Structure (headings inside SKILL.md)

- Finishing a Development Branch
- Overview
- Step 1: Verify Tests
- Step 2: Detect Environment
- Capture now, while still inside the workspace — Step 5 changes directory
- before cleanup (Step 6) needs this value
- Step 3: Determine Base Branch
- Step 4: Present Options
- Step 5: Execute Choice
- Option 1: Merge Locally
- Get main repo root for CWD safety
- Merge first — verify success before removing anything
- Verify tests on merged result
- Option 2: Push and Create PR
- From a detached HEAD, name the new branch on the remote:
- git push origin HEAD:refs/heads/<new-branch>
- Option 3: Keep As-Is
- If your human partner asks to discard the work
- Step 6: Cleanup Workspace
- Quick Reference
- Common Rationalizations
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. Delete them (unrecoverable)

## Key rules (verbatim lines from SKILL.md)

1. 1. Commit them to <branch> before cleanup

## Files inside the skill

- (SKILL.md only)
