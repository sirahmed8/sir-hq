# permissioned-github

- Tool: `antigravity-builtin`
- Category: design
- Source: `C:\Users\a7med\.gemini\antigravity\builtin\skills\permissioned-github\SKILL.md`
- SKILL.md size: 8293 chars

## What it does

Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agent environment.

## When to use (from skill text)

- - dispatch: to trigger a workflow run (`gh workflow run`). Also requires a `ref` field. No `git.read` grant is needed.

## Structure (headings inside SKILL.md)

- GitHub Skill
- How to Interact with GitHub
- Asking for Permissions
- Permission Format
- Examples
- Example 1: Creating an Issue
- Example 2: Commenting on a PR
- Example 3: Closing an Issue
- Example 4: Approving a PR
- Example 5: Pushing to an Existing Branch
- Example 6: Creating a New Branch
- Example 7: Fetching a Repository
- Example 8: Cloning a Repository
- Example 9: Deleting a Branch
- Example 10: Searching Pull Requests
- Example 11: Searching Commits
- Example 12: Searching Code
- Example 13: Searching Issues
- Example 14: Running (Dispatching) a Workflow
- Example 15: Listing, Viewing, or Watching Workflow Runs
- How and When to Ask for Permissions
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - delete: to delete a remote branch.
- 1. Construct the permission string as shown for the action (see the examples above).
- 2. Call the `ask_custom_permission` tool for the required permission.

## Key rules (verbatim lines from SKILL.md)

1. * Use the **gh** CLI. Always set the `-R ORG/REPO` argument.
2. * Do not use other commmands like curl.
3. * Do not write scripts to interact with the GitHub API servers directly.
4. * Git is supported over HTTPS. Do not use SSH.
5. - dispatch: to trigger a workflow run (`gh workflow run`). Also requires a `ref` field. No `git.read` grant is needed.

## Files inside the skill

- (SKILL.md only)
