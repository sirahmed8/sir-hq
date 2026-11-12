# native_swarm (antigravity-builtin, file name `swarm`)

Source read: `C:\Users\a7med\.gemini\antigravity\builtin\skills\native_swarm\SKILL.md` (21 KB; antigravity-builtin; digest/file named `native_swarm` but frontmatter name is `swarm`; `logo.svg` sibling). Preview/quota-heavy multi-agent coordination.

## Summary
Coordinator manual for running a swarm: parallel agents, each in its own conversation, collaborating through one shared message board. The user talks only to the coordinator; workers talk via `post_message`/`read_board`/`swarm_wait` (free while asleep) and `swarm` tool actions (`status`, `models`, `add`, `model`, `kill`, `title`). Core doctrine: "Do not do the work" — technical work, research, builds, reviews all go to workers; the coordinator reads, judges, decides. Setup: size the swarm by genuinely independent pieces (one worker per file/target/question, plus one verifier per 2-4 workers; two workers editing the same file is the failure mode to design out), name it, `add` workers with complete standalone briefs (a worker starts fresh — state ownership, exclusions, context it can't find, and what "done" looks like; briefs are PUBLIC on the board), optionally add a `narrator` and `monitor` only if those skills exist, then show the user the board link. Operations: workers are `waiting` (free, needs @mention), `working`, `stopped` (post revives), `killed` (permanent — `add` fresh). Mentions are wakeup doorbells: `@name`, `@#channel` for channel broadcast, `@all`; workers may add/kill/model only their own helpers; quota exhaustion → `swarm{action:"model"}` switch (keeps conversation), check `models` for live quota. Board tools appear one turn AFTER first `add`; `kill` is permanent; `swarm_wait{since:N}` beats polling; channels only work if `main` stays quiet.

## When to use / when NOT
Use for parallelizable work (multi-file changes, parallel investigations, independent research) or adversarial verification (builder + verifier pairs). NOT for single-threaded tasks, tiny edits, or anything where coordination overhead exceeds the work; also quota-heavy — each worker burns tokens whether idle or not.

## Inputs, outputs, tools
- Inputs: a task decomposable into non-colliding pieces; per-worker briefs; optional model choices.
- Outputs: worker deliverables posted to the board, integrated and reported by the coordinator.
- Tools: `swarm` (status/models/add/model/kill/title), `post_message`, `read_board`, `swarm_wait`; optional `swarm_narrator`, `swarm_monitor` skills; board link/pill for the user.

## 5 most important rules
1. Coordinator never does technical work — brief, reply, end turn; unwatched swarms silently stall.
2. Design out file collisions upfront: one worker per file/target/question + verifiers; lean swarms (every worker costs tokens).
3. Briefs are public and are ALL a worker gets — complete context, ownership, exclusions, done-criteria.
4. `@mention` is a doorbell, not a CC — name only the next actor; workers report to coordinator on deliverable/blocker.
5. On quota failure: switch model via `swarm{action:"model"}` (never kill+re-add); board tools lag one turn after `add`; `kill` is forever.

## Risks / owner notes
High token cost — preview/quota-heavy by its own description. Killed workers can't be revived; helpers of a killed worker survive and must be cleaned up. Public briefs mean nothing secret goes in them. Model switching on quota is the designed recovery — check `swarm models` quota fields.

## Category and tags
Category: ai. Tags: multi-agent, swarm, coordination, message-board, parallel-agents, quota-management, antigravity.
