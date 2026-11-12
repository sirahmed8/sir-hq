# permissioned-github

Tools: antigravity-builtin. Source: C:\Users\a7med\.gemini\antigravity\builtin\skills\permissioned-github\SKILL.md (187 lines, read in full)

## Summary
Antigravity's authoritative rulebook for GitHub access: use `gh` CLI with `-R org/repo` (never curl or direct API scripts), use `git` over HTTPS only, and when a command fails on permissions, request a scoped grant via `ask_custom_permission` using a defined `<command-binary>.<action>(<resource_json>)` format, then retry.

## When to use / not use
This is environment governance, not a task skill — it activates whenever GitHub/git commands run inside Antigravity. Not relevant outside that harness.

## Inputs, outputs, dependencies
Input: GitHub operations (issues, PRs, branches, workflow runs, clones). Output: permitted command execution after scoped grants. Needs: `gh` CLI authenticated, `git` over HTTPS, and the `ask_custom_permission` tool for escalations.

## Key rules
1. `gh` for everything GitHub, always with `-R ORG/REPO`; no curl, no hand-written API scripts; `git` is HTTPS-only (no SSH).
2. Permission strings are lean: `gh.create/update/approve/read({org, repo, issue|pr})`, `git.read/create/update/delete({org, repo, branch?, contents?})`, `workflow.dispatch/read({org, repo, path, ref})`.
3. `contents:"*"` read grants the whole repo (clone/fetch/search commits/code); `workflow.read` is repository-wide only (path+ref must both be `*`) and covers run list/view/watch — NOT `gh run rerun` or workflow definitions.
4. Ask for permission ONLY after a command actually fails — each ask prompts the user; never pre-request.
5. Never pipe or redirect `gh` output — it doesn't work in this environment.

## Risks / owner items
- Unsupported operations have no grant path — the skill says stop and tell the user why rather than work around.
- `workflow.dispatch` needs an existing workflow file path at the target ref plus explicit `--ref`.
- Commit/code search reuses `git.read`, not `gh.*` grants — requesting the wrong permission family wastes a user prompt.

## Category and tags
ops, build — github, permissions, gh-cli, git, antigravity, governance.

## Revision note
Single antigravity-builtin revision; a permission grammar specific to that harness's sandbox.
