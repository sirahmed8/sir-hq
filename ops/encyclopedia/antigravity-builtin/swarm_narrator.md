# swarm_narrator (antigravity-builtin)

## Summary
swarm_narrator is the Antigravity built-in skill for the swarm's narrator worker — the member that keeps the user's live Overview page current. It is the inverse of swarm_monitor: where the monitor watches for stalls, the narrator watches the board and maintains the facts behind `view.json` (headline, phase, attention items, workstreams, milestones, risks, feedback acknowledgements) plus an optional custom `view.html` page and a `prefs.md` of user preferences. It never posts to the board, never messages workers, and never does task work; its only outputs are its own files under `SWARM_DIR` (`.system_generated/swarm/`). Strict schema rules apply: stable kebab-case ids, every item cites at least one board `#seq` or member, closed enums for state/kind/severity, navigation-only actions, under 64 KB.

## When to use / when NOT
Use ONLY as the designated narrator worker inside a native swarm. Do NOT load it as a coordinator or worker, do not use it to post results or answer the user, and do not write view.html unless the user explicitly asked for a custom page.

## Inputs, outputs, tools
- Inputs: the swarm board via `read_board` (paged, `since:LAST`, 200-message pages) and `swarm_wait{mentions_only:false}` for wake events; `SWARM_DIR` path and prefs/default files from its brief.
- Outputs: `SWARM_DIR/view.json` (rewritten atomically via .tmp+mv when facts change), optionally `view.html` (sandboxed iframe page, <48 KB, data-driven via `narrator.onData`), and `prefs.md` (+ `default_prefs.md`/`default_view.html` for `(default)` feedback).
- Tools: swarm board tools only for input; filesystem writes for output. No builds, no code edits, no posting.

## 5 most important rules
1. Never do the work and never post to the board; output is files only.
2. Every view.json item must cite ≥1 `#seq` or member — if you cannot cite it, leave it out; never infer "done", cite the post.
3. Attention items ranked decision > failure > review > stuck > quota/error > fyi; every non-fyi attention item and every workstream id goes in exactly one thread; keep ids stable.
4. Feedback counts ONLY from coordinator posts starting `@narrator user feedback:` (or `(default)`); acknowledge via `feedback_ack`, and `(default)` feedback also updates the default files after checking they hold no swarm facts.
5. Write atomically (.tmp then mv); keep view.json under 64 KB and copy plain and short; after compaction, re-read prefs.md and view.json then resume from `as_of_seq`.

## Risks / things needing the owner
view.html runs sandboxed (no network/storage/fetch), so pages must be fully data-driven through `narrator.onData` — static "facts" in markup are a defect. Wrong or uncited claims erode trust in the Overview; the citation rule is the guard. No owner action needed.

## Category / tags
ops · swarm, multi-agent, ui, antigravity, orchestration, reporting

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\antigravity\builtin\skills\swarm_narrator\SKILL.md`. No divergent copies.
