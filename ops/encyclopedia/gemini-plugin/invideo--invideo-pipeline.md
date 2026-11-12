# invideo-pipeline (invideo plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\invideo-pipeline\SKILL.md` (4 KB; invideo plugin; `references/collaborate.md` exists).

## Summary
The scale/automation playbook for invideo: CSV-to-many-videos, scripted runs, CI, outreach at scale, course batches, bulk orders, and multi-agent collaboration on one project. Core doctrine: at scale you edit the SYSTEM that makes videos, not videos — the batch is only as good as its worst row. It prescribes cutting 3 very different rows by hand to isolate variables, locking story/pacing/music/type/color while data drives name/number/image/language/hook, designing fallbacks for missing/thin/edge data (rewritten lines, warmer shorter cuts, skip-when-wrong-is-worse), one voice per product line, variant-vs-lesson rules, pilot-then-batch checks, and stable per-row keys so reruns skip finished rows. Scripted runs use `--json`, per-step `--idempotency-key` (e.g. `row-42-voice`), `invideo status --wait`, and persistent sign-in for CI (`INVIDEO_NO_BROWSER=1`). Collaboration: register a role name, own one part, read inbox+timeline before every pass, write updates for the person.

## When to use / when NOT
Use for batches (CSV-driven), unattended/CI generation, outreach or course pipelines, bulk orders, or several agents sharing a project. Not for a single video (use `/invideo` directly).

## Inputs, outputs, tools
- Inputs: full data sheet (not the sample row), template/project, row-key scheme, idempotency keys, CI runner with prior sign-in.
- Outputs: N personalized videos/exports, deduplicated on rerun.
- Tools: `invideo` CLI with `--json`, `--idempotency-key`, `status --wait`; docs pages ci-and-servers and csv-to-videos; `references/collaborate.md`.

## 5 most important rules
1. Read `/invideo` first; get the WHOLE sheet — the sample row is always the nicest.
2. Cut 3 diverse rows by hand first; lock everything except the data variables; fix template/data, never one video by hand.
3. Stress-test worst rows before batching (longest name, empty cells, ALL CAPS, other scripts, 0/1, wrong-aspect images, white-on-white logos).
4. Every generation gets its own idempotency key (`row-N-step`); reruns must find earlier work, not redo it; stable row keys prevent duplicate deliveries.
5. Pilot 5–10 extreme rows, get approval, then run the rest; a repeating defect STOPS the batch.

## Risks / owner notes
Batch generation multiplies credit spend — pilot gating and idempotency are the cost controls. CI sign-in persists credentials on the runner (`~/.config/invideo/credentials.json` or keychain) — a shared CI machine is a credential-exposure surface.

## Category and tags
Category: media. Tags: invideo, batch-video, csv, idempotency, ci, personalization, multi-agent.
