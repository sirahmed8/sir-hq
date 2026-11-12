# gmail (gemini-plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\gmail\skills\gmail\SKILL.md` plus `scripts/gmail`, `scripts/gmail.cmd` (Go CLI wrappers; scripts dir contains only the CLI binaries).

## Summary
Gmail over a Go CLI that talks to the Gmail REST API, split into a strict `readonly` namespace (search, read, threads, drafts, labels, history, settings, attachment download) and a `mutate` namespace (send, reply, forward, drafts CRUD, labels, trash, batch-modify). It handles Gmail Web UI "Sapinto" IDs, emoji reactions, vacation responder, forwarding/send-as settings, and has explicit safety rails: `--max N` is the only result-limit flag, no shell grep/awk filtering, and all send-class commands are hard-blocked when `AGY_UNATTENDED` is set (use `create-draft` instead).

## When to use / when NOT
Use for reading/searching email, managing drafts and labels, sending/replying/forwarding with explicit user authorization, emoji reactions, attachments, and decoding `mail.google.com` URLs. Do NOT use for Google Chat or Calendar invites. Never use for unattended autonomous sending.

## Inputs, outputs, tools
- Inputs: Gmail search operators (`is:unread`, `from:`, `after:YYYY/MM/DD`, `has:attachment`, ...), message/thread/draft IDs, recipients, `--md`/`--html`/`--body-file` bodies, `--file` attachments.
- Outputs: plain-text reads by default (HTML boilerplate stripped), `--json` for machine output.
- Tools: the bundled `gmail` CLI (downloaded by `scripts/gmail --version` on first run, registered on agent PATH); auth either via Antigravity sign-in card or `gmail auth login` background flow.

## 5 most important rules
1. Run `scripts/gmail --version` once before anything; afterwards always call bare `gmail`, never the script path.
2. `readonly` vs `mutate` namespaces are strict; every send-class command needs explicit user authorization (recipient, subject, body confirmed first).
3. `AGY_UNATTENDED` hard-blocks all outbound sends; the only safe path is `mutate create-draft`.
4. Markdown bodies require `--md`; tables require `--html` with inline CSS (pipe tables render unstyled in Gmail).
5. Never pipe output to grep/awk — filter inside the Gmail query; use `--max N` (never `--max_results`/`--limit`/`-n`); avoid `--json` on `readonly read` because it dumps raw base64 payloads.

## Risks / owner notes
Sends email AS the user — highest-risk skill in this batch. `delete-draft` bypasses Trash and can remove an already-sent message inside the Undo Send window; re-check Sent first. Auth may require the owner to complete a browser sign-in.

## Category and tags
Category: automation. Tags: gmail, email, cli, google, readonly-vs-mutate, unattended-mode.
