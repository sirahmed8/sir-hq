# USAGE POLICY: spend the plan like money (Ahmed, 2026-11-02)

Plan: Claude Pro, weekly limit resets Sunday 02:00 Cairo. On 2026-11-02 the week was 76% used after about 1 day (an even pace is about 14% per day). Quality stays; waste goes. Every chat and subagent follows this file.

## What burned the quota (7-day report, this machine)
- 87% of usage ran above 150k tokens of context; 81% came from subagent-heavy sessions; 57% from sessions open 8+ hours. Every turn re-reads the whole context, so a long chat costs more per message than a new one.
- Context window is 1M with auto-compact at 98%, so nothing shrinks a chat by itself. Rule below fixes that by hand.
- Biggest agent shares: ui-craftsman 13%, claude-in-chrome 7%, workflow subagents 6%, builder 6%, ccd_turn 5%.

## Rules (all chats)
1. **Small context.** At about 150k tokens (`get_usage` shows it): write the checkpoint, then `/compact` or start a fresh chat from `.sir/CHECKPOINT.md`. Never run one chat for hours on one huge context. Memory is files, not chat.
2. **Read ranges, not files.** `Grep` first, then `Read` with offset/limit. Never read a whole large file, a dashboard HTML, a lockfile or a log; use `tail`/`head`/`wc` or a haiku subagent that returns 10 lines.
3. **Model by level (MODEL_ROUTING.md), cheaper default.** Level 0-1 work is haiku. Sonnet is for design, review, security and hard debugging. Default effort is `medium`; `high` only for levels 2-3; `xhigh`/`max` need a written reason. Opus only when stuck twice.
4. **Fewer, bigger, better-briefed agents.** At most 3 agents at once (was 6). One agent per file set. A brief with files, edits allowed, done-when commands and a 15-line return format. No agent for work under about 8 tool calls. No second agent that re-reads what the first already read: pass it the summary.
5. **Scripts beat agents.** Anything deterministic (rename, count, generate files, run tests, grep reports, update checklists) is a script or one command, not a model loop. Generate from data (`plans/*.py`), do not hand-write 12 similar files.
6. **Free local workers for bulk.** Summaries, translation drafts, digests, first-pass reviews and classification go through `_SIR/scripts/ai/ask.ps1` (local qwen3:8b / qwen2.5-coder on `D:\Projects\AI_Models_Hub`, or free Gemini for non-private text). Private text stays local. Claude reviews the result; it does not produce it.
7. **Browser and screen work is expensive.** Prefer `get_page_text`/`read_page`/`find`/`javascript_tool` over screenshots; batch actions (`computer_batch`, `browser_batch`); no screenshot after every click; no polling loops; cap a UI check at 6 screenshots, then decide.
8. **No waiting loops and no polling.** Background commands notify on exit. Do not re-read the same bus file or status every turn; read it when a note says something changed.
9. **Fix once.** Run the failing test alone, not the whole suite, while iterating; run the full `verify` once before a push. Do not re-run a green check "to be sure".
10. **Short outputs.** Subagents return facts, not essays. Commit messages and reports are short. No recaps of finished work.
11. **Design agents (ui-craftsman, image/video work) only for a screen that will ship.** First write the spec and tokens once in `DESIGN.md`; builders implement from it. No repeated "redesign" passes; one review pass per screen.
12. **Pause rule.** Read `get_usage`. Weekly under 80%: normal. 80-90%: only tasks on the Now list, no new design or research, no new chats. 90%+: finish and push what is in flight, update checkpoints, stop; owner-only and free-local work only. The 5-hour limit hitting 100% means: stop all agents, write the checkpoint, resume after the reset.

## Weekly budget (shares of the weekly limit, to be re-split by HQ every Monday)
HQ manager 15% · the active project chat 60% · reviews and fixes 15% · reserve 10%. One project builds at a time (already the rule). Study, Jobs and Laptop Manager start only when the week has room.

## For HQ
- HQ runs at medium effort, reads `ops/bus` only when a note arrives, and never rebuilds files a project chat owns.
- Generators and dashboards are scripts: republish only when a report changes something.
- Each Monday HQ writes the used percent and the plan for the week at the top of `ops/OWNER_ACTIONS.md` "Optional" line (one line).
