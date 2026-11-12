# swarm_monitor (antigravity-builtin)

## Summary
swarm_monitor is an Antigravity built-in skill for the "native swarm" multi-agent system, and it is explicitly restricted: only the swarm worker whose brief names it as the monitor may load it (slash command disabled). A swarm can deadlock — every member including the coordinator asleep on the board, each waiting for someone else, nobody posting, job unfinished. The monitor wakes on a cron timer regardless, reads the board, decides whether the swarm is stalled, diagnoses the cause (unaddressed result, unanswered mention, wait-chain, coordinator idle with unread posts), and posts at most ONE short message per tick to the single member who can unstick it. It never does the work itself.

## When to use / when NOT
Use ONLY inside a native-swarm run as the designated monitor worker. Do NOT load it as a coordinator or regular worker, do not use it outside the swarm system, and do not use it to do actual task work — its charter forbids editing files, builds, reviews or answering the user.

## Inputs, outputs, tools
- Inputs: the swarm board via `read_board` (paged by seq), member states via `read_board{status:true}`, its own cron via `manage_task`/`schedule`, and wake events via `swarm_wait`.
- Outputs: at most one board post per tick, addressed to one member by name, citing message seqs and how long the stall has lasted; plus its cron lifecycle (schedule on start, kill when dormant).
- Tools: swarm board tools (`read_board`, `swarm_wait`, `post_message`), `schedule`/`manage_task` for the `*/3 * * * *` daemon cron (IsDaemon must be true or the timer blocks idle detection). No file or shell tools by charter.

## 5 most important rules
1. Never do the work: no edits, builds, reviews, or user answers; only stall-breaking posts.
2. A stall = every live member except you (coordinator included) is waiting/stopped AND the job is not finished; anyone `working` means not a stall.
3. Post once per tick, to exactly one member, never `@all`, never to the narrator, never reply to replies; cite `#seq`s and durations.
4. Do not repeat alerts: re-alert only on change or after 3 ticks (~10 min); stop after 3 unanswered alerts on one stall.
5. Go dormant (kill cron, park on all messages) when the coordinator posts `[done]`, no live members remain, or 5 ticks pass with no board movement and no active stall alert; reschedule the cron on any wake if it is missing — never run two crons.

## Risks / things needing the owner
Runs every 3 minutes while active — token cost is bounded by its tiny reads but non-zero. Misdiagnosis could ping the wrong member or spam the board; the anti-repeat rules exist for that. Channel-aware: unaddressed posts in non-main channels reach only that channel's members. No owner action needed; it is internal swarm machinery.

## Category / tags
ops · swarm, multi-agent, monitoring, antigravity, orchestration

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\antigravity\builtin\skills\swarm_monitor\SKILL.md`. No divergent copies.
