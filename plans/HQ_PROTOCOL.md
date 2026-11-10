# HQ PROTOCOL: how this manager chat runs the projects (Ahmed, 2026-11-01)

HQ (the chat in `D:\Projects`) manages all projects and the waves. Project chats build (Gemini in Antigravity; the free CLI agents when its quota is out; Ahmed, 2026-11-09 and 2026-11-10). Ahmed is told on Telegram when a project finishes; nothing waits for him (Ahmed, 2026-11-01 and 2026-11-08).

## Lifecycle of one project
1. **Start:** HQ opens a project chat (start_session, cwd = the project folder) with the start prompt in `plans/START_PROMPT.md`.
2. **Work:** the project chat runs its tasks with subagents and reports to HQ through `ops/bus/sir-hq.md` (done, evidence, open questions) and through its turn notes.
3. **Review (the author never grades its own work):** HQ reads each report, checks the evidence (repo state, tests, deployed URL, screenshots, checkpoint), replies in the chat or in the bus with what is missing or wrong, and the project chat fixes it. This repeats until HQ can confirm all of: plan and tasks 100% done, verified; production deployed and checked; sites and apps built for every platform the plan lists; legal, security and quality checks green; Desktop shortcuts working; nothing left in the project's task list.
4. **Done:** HQ writes the result into `ops/PORTFOLIO.md` and the dashboard, sends Ahmed a short plain-language Telegram note, and lists anything only he can do (sign-in, 2FA, payment, identity) in `ops/OWNER_ACTIONS.md`. It does not wait for a reply.
5. **Next:** HQ opens the next project's chat in the order of `plans/WAVE_STUDY.md`. At most 2 project chats work at the same time while `plans/LOW_USAGE_MODE.md` is active (2026-11-10).

## Messaging a busy chat
A message sent to a chat that is mid-turn is queued and delivered only after that turn ends (Ahmed saw this with the AHome chat, 2026-11-01). So for anything that matters, also write it as an unread line in that project's inbox `ops/bus/<slug>.md`: the sir-context mod shows the unread count in the chat's prompt on every turn, and the chat reads the inbox at the start of each task. Do not expect an answer until its turn ends.

## Never overwrite a started project
Once a project chat has rewritten its `.sir/CHECKPOINT.md`, HQ must not regenerate or edit that project's `.sir` files (the generator now skips it). Changes to rules reach it through `AGENTS.md`, `ops/bus/<slug>.md` and the shared plans in `_SIR/plans`. (Lesson 2026-11-01: a regeneration wiped the AHome chat's task list.)

## Memory (HQ gets compacted often)
- Keep `ops/HQ_CHECKPOINT.md` current after every step: Now, exact next step, open promises, files to re-read. Keep `NEXT.md`, `plans/BUILD ORDER` (`WAVE_STUDY.md`) and `ops/OWNER_ACTIONS.md` true.
- After a compaction or resume: read START_HERE.md, NEXT.md, the checkpoint, then `ops/bus/*.md` and `list_sessions {linked: true}` before acting.
- Every decision that changes a rule goes into `D:\Projects\AGENTS.md` and memory, so every chat inherits it.

## What HQ does itself
Plans, kits, repos, accounts that can be done in the browser, keys and tokens, the dashboard, TickTick, desktop shortcuts, mods, and answering project chats. HQ does not build product code.
