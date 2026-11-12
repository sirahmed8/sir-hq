# diagnosing-superpowers

## Summary
Post-mortem skill for superpowers agent sessions: turn a vague complaint ("it took too long", "it ignored the plan", "skill X never fired") into a written problem statement, locate the session transcript(s) on disk, dispatch parallel analyst subagents across seven dimensions (skill-timeline, plan-adherence, repeated-work, stumbles, quality-evidence, request-conflicts, cost-and-time), and produce an evidence-cited report — optionally a GitHub issue or a scrubbed diagnostic bundle. It reports facts; it never diagnoses superpowers itself.

## When to use / when NOT
Use when a superpowers session went wrong and the user wants to know why, or wants a bug report for the maintainers (current or past session by id/path). Do NOT use for diagnosing your own non-superpowers code bugs, or to modify session files.

## Inputs, outputs, tools
- Inputs: the complaint, session id/path, turn range; transcript files on disk.
- Outputs: `templates/report.md` filled with path:line-cited findings, optional issue text, optional scrubbed bundle archive.
- Tools: session files under the harness's transcript dir, `references/` (session-discovery, context-safety, github-issues, redaction-policy), `prompts/` analyst+scrub prompts, `templates/` (case, report, issue, bundle-README), `gh` for issues, zip/tar for bundles.

## 5 most important rules
1. Every finding cites `path:line`; every number comes from the transcript or a command — never memory. No citation, no finding.
2. Read-only on session files — never modify/move/delete them.
3. One analyst subagent per dimension in parallel, each with absolute paths — a subagent's "current session" is its own.
4. Only human prompts count as the partner's words; hook output/system reminders/tool results are not.
5. Bundles/issues only on explicit request, after redaction-level approval; scrub loop (scrub + scrub-audit) must return CLEAN before archiving, and the user must review every file before sharing.

## Risks / things needing the owner
Transcripts can contain secrets/private data — the scrub pipeline exists precisely for that; never share unscrubbed bundles. Creating GitHub issues is an outward action needing approval.

## Category / tags
ai · debugging, agent-sessions, diagnostics, reporting

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\superpowers\skills\diagnosing-superpowers\SKILL.md` with references/, prompts/ (8 files), templates/ (4 files). Only gemini-plugin holds it.
