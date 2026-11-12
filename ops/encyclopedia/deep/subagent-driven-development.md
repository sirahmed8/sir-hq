# subagent-driven-development (gemini-plugin: superpowers)

## Summary
subagent-driven-development is the execution half of the "superpowers" plugin: it runs an implementation plan by dispatching a FRESH implementer subagent per task, then a separate task reviewer per task, and one broad whole-branch review at the end. The controller (the main agent) never writes the code itself; it crafts minimal dispatch prompts, records a BASE commit before each dispatch, packages diffs into files via `scripts/review-package`, and keeps a `progress.md` ledger in a per-plan git-ignored workspace (`.superpowers/sdd/`) so progress survives context compaction. It pairs with sibling skills: using-git-worktrees for isolation, writing-plans/executing-plans for the plan itself, test-driven-development inside tasks, and finishing-a-development-branch at the end.

## When to use / when NOT
Use when you have a written implementation plan whose tasks are mostly independent and a subagent/agent-dispatch tool is available. Do NOT use for tightly coupled tasks, when the partner chose inline execution (use executing-plans), when there is no plan yet (brainstorm/writing-plans first), or when no subagent tool exists.

## Inputs, outputs, tools
- Inputs: a plan file (and optionally a spec it argues from), a git worktree, and the ability to dispatch subagents with explicit model selection.
- Outputs: committed code per task, a ledger (`progress.md`), review packages, task reports, and a final whole-branch review.
- Tools: bash helper scripts `sdd-workspace`, `task-brief`, `review-package`, `sdd-repo`; prompt templates `implementer-prompt.md`, `task-reviewer-prompt.md`, `re-review-prompt.md`; reference docs for preflight, fix-loop, batching, resuming, cannot-verify, handling-reports, final-review. Requires git and a harness with subagent dispatch.

## 5 most important rules
1. Fresh subagent per task with a crafted brief; never paste session history into dispatches (a real session hit 42k chars of pasted history).
2. Track progress in the ledger file, not memory: compaction has caused controllers to re-dispatch entire completed task sequences.
3. Never dispatch implementer subagents in parallel; implementers never spawn subagents or reviewers themselves.
4. Every task gets BOTH an implementer self-review AND an independent task review (spec compliance + quality); the final whole-branch review runs on the most capable model.
5. "Rulings, not stalls": decide ambiguities yourself, log each as `Ruling: <what> — <why> — <cost if wrong>`; only four things stop the loop (irreversible/destructive op, security-sensitive action, external side effect like push/merge, or a plan too broken to route).

## Risks / things needing the owner
Cost: one fresh context per task plus one per review; model selection guidance exists to control it (cheap tier for transcription tasks, mid-tier floor for reviewers, escalate on fix rounds 4-5). The four stop conditions include pushes to shared branches and merges, which per SIR rules go straight to main anyway — so the "ask before push" rule conflicts with the workspace no-PR law and the ledger ruling should note that. `git clean -fdx` destroys the workspace; recovery is via git log.

## Category / tags
build · subagents, orchestration, code-review, planning, superpowers

## Revisions
Only one revision exists: the gemini-plugin superpowers copy, which is the richest version (SKILL.md plus two prompt templates, seven reference docs and four helper scripts). No divergent copies elsewhere.
