# finishing-a-development-branch

## Summary
The integration gate at the end of a superpowers development cycle: verify the full test suite is green, detect the git environment (normal repo vs named-branch worktree vs detached HEAD), confirm the base branch, present a fixed 3-option (or 2-option detached) menu to the human, execute their choice (local merge, push+PR, or keep as-is), then clean up the worktree with provenance rules — never `--force` over uncommitted files.

## When to use / when NOT
Use when implementation is complete and all tests pass, to decide how work lands. Do NOT use with a failing suite (fix first), and never treat the menu as optional — the integration decision belongs to the human partner. Discarding work happens ONLY on an explicit typed "discard" confirmation.

## Inputs, outputs, tools
- Inputs: a finished branch/worktree, the project's test command, the confirmed base branch.
- Outputs: merged/pushed/kept branch per user choice, cleaned worktree, deleted feature branch (option 1), PR URL (option 2).
- Tools: git (rev-parse git-dir vs git-common-dir for environment detection, merge, pull, branch -d/-D, worktree remove/prune), the project test suite, forge CLI/PR URL for option 2.

## 5 most important rules
1. Tests must pass on the tree being integrated — run the suite fresh; a green run earlier proves nothing about the merged result (re-test after merge too).
2. Confirm the base branch before merging — merging into the wrong base is expensive to undo.
3. Present the menu exactly as written and wait; "obviously they want it merged" is a rationalization, not a decision.
4. Merge locally → verify tests on merged result → then remove worktree → then `git branch -d`; if tests fail post-merge, stop with everything in place (nothing pushed, fully recoverable).
5. Worktree cleanup is provenance-based: only remove worktrees under `.worktrees/`/`worktrees/`; on removal refusal show the uncommitted file list and ask — never `--force` on own initiative; detached HEAD worktrees are externally managed, leave them.

## Risks / owner needs
Every irreversible step (merge, push, PR, branch delete, worktree force-remove, discard) is gated on explicit human choice; push rejection means investigate, never force-push without request. In the SIR workspace the no-PR law overrides option 2 in practice (commit straight to main), but the skill's gating logic still applies.

## Category and tags
Category: build. Tags: git, workflow, superpowers, branch-integration, worktree, pr.

## Revisions
Single gemini-plugin superpowers copy; no competing revisions.
