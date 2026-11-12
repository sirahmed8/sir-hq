# using-git-worktrees (gemini-plugin: superpowers)

## Summary
using-git-worktrees sets up an isolated workspace before feature work so the current branch stays untouched. Its core principle: detect existing isolation first, prefer the harness's native worktree tool, and only fall back to manual `git worktree add` when no native tool exists — "never fight the harness." Step 0 detects whether you are already in a linked worktree (`git rev-parse --git-dir` vs `--git-common-dir`, with a submodule guard via `--show-superproject-working-tree`), asks consent if the user hasn't declared a preference, then Step 1 creates the workspace (native tool or `.worktrees/<branch>` fallback after verifying the directory is git-ignored), Step 2 runs project setup (npm install / cargo build / pip / go mod download), and Step 3 verifies a clean test baseline before any implementation.

## When to use / when NOT
Use when starting feature work that needs isolation from the current workspace, or before executing an implementation plan (subagent-driven-development requires it). Do NOT create a second worktree if already inside one, do not use it for trivial single-file edits where isolation adds nothing, and do not skip the baseline test run.

## Inputs, outputs, tools
- Inputs: the repo, optional user preference for worktree location, and the project's package manifest.
- Outputs: a linked worktree at `.worktrees/<branch>` (or harness-managed path) on a new branch, dependencies installed, and a verified clean test baseline.
- Tools: git worktree commands, `git check-ignore` for safety, native harness worktree tools when present, and the project's own setup/test commands.

## 5 most important rules
1. Detect first: `GIT_DIR != GIT_COMMON` means already isolated — but check `--show-superproject-working-tree` because submodules fake the same signal.
2. Native worktree tools beat `git worktree add`; bypassing them creates phantom state the harness cannot see or clean up.
3. Verify the worktree directory is git-ignored (`git check-ignore`) before creating; if not, add it to .gitignore and commit first.
4. Always run the baseline test suite in the fresh worktree; a dirty baseline makes every later failure ambiguous — proceed past failures only with the human's call.
5. Sandbox fallback: if `git worktree add` is permission-denied, work in place and say so rather than fighting the sandbox.

## Risks / things needing the owner
Asks consent before creating a worktree unless a preference is already declared. Note the tension with SIR rules: the workspace law says background jobs work in a git worktree, but many SIR tasks commit straight to main — for those, isolation is optional, not mandatory. `git clean -fdx` in the worktree destroys uncommitted work; committed work survives via git log.

## Category / tags
build · git, worktree, isolation, workflow, superpowers

## Revisions
Only one revision exists: the gemini-plugin superpowers copy. No divergent copies.
