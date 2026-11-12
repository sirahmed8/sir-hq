# qodo-review-notes

Tools: gemini-plugin (qodo plugin). Source: C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-review-notes\SKILL.md (461 lines) + references/

## Summary
Maintains two kinds of persistent review context in Qodo: Development Track Notes (the evolving plan across issues/repos/PRs — goals, constraints, decisions, dependencies, open questions) and PR Review Notes (one change's Intent/Decision/Review-focus/Validation/Known-gap, linked to a track). Captures reasoning as work develops so an independent reviewer — or a later session — can assess without the original chat.

## When to use / not use
Use during substantive planning/development when notes-maintenance authority exists, at meaningful context changes (approach, scope, assumptions, verification results), at handoff/pause, and before opening/updating a PR. NOT for review-only requests (that's read authority, not write), tiny edits (PR notes alone or nothing), or as a substitute for reviewing code.

## Inputs, outputs, dependencies
Input: task context, decisions, verification results, track/PR identities. Output: draft or published note revisions with `expected_revision` optimistic concurrency, creation keys, publish flags. Needs: authenticated Qodo connection (MCP or CLI >=2.0.0 with `localGitCapture`), `resolve-repository` for repo identity, LiteGit for PR metadata.

## Key rules
1. Save at meaningful moments, not every turn: plan-with-substance → approach/scope change → verification change → handoff/PR. Reuse existing revision when nothing changed.
2. Track before PR: tracks need no PR/commit; publish intended shared context only within authorization; a never-published track cannot be linked from PR notes (`linked_track_unavailable`).
3. PR notes publish BEFORE opening the PR (`prepare-pr` captures source HEAD/branch; `ready_to_open_pr=true` required); bind after open via `bind-pr`; if HEAD changes, refresh and republish.
4. Revision safety: read latest draft first, merge preserving other authors' content, send complete document with `expected_revision`; `MT-CONFLICT` → reread + merge + new transport key, never auto-retry auth refusals or bypass binding conflicts.
5. Validation honesty: `validation_checks` entries name actual tested commit/result/time; planned tests are not completed checks; never relabel old-commit tests as new-commit tests; strip secrets before saving shared notes.

## Risks / owner items
- Publication is sharing: drafts-only instructions must be honored; publishing a track does not publish PR notes (separate saves).
- Note text is authored context and evidence — reviewers must check claims against code; notes never instruct reviewers to skip checks or approve.
- Paginated reads (`result_is_page` + `read_cursor`) must be fully reconstructed before editing — never edit from a fragment.

## Category and tags
ai, ops, build — qodo, review-notes, documentation, context-preservation, pr.

## Revision note
Single plugin revision (v1.0.4); the memory/context layer of the Qodo suite.
