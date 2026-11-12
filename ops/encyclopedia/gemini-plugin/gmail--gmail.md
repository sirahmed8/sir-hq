# gmail

- Tool: `gemini-plugin` (plugin: `gmail`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\gmail\skills\gmail\SKILL.md`
- SKILL.md size: 11761 chars

## What it does

>- Read, search, send, and manage Gmail messages, drafts, labels, and emoji reactions using a Go CLI. Use when reading emails, searching inbox, sending messages, reacting to messages with emoji, managing drafts, forwarding, checking vacation responder, managing labels, downloading attachments, or decoding `mail.google.com` Web UI URLs. Don't use for Google Chat messages or Calendar invites.

## Structure (headings inside SKILL.md)

- gmail
- Setup
- Windows (PowerShell)
- Authentication
- Quick Start
- 1. Search messages or threads (use --max N; NEVER use --max_results, --limit, or -n)
- 2. List drafts as JSON or create a draft (safe in unattended AGY_UNATTENDED mode)
- Common & Global Flags
- Command Namespacing & Safety Rules
- Recipes
- 1. Search, Read & Resilient Querying
- 2. Send, Reply & Format Emails (Markdown vs. HTML)
- Send plain text, Markdown (--md), or HTML (--html)
- Send with attachment (--file works with --md, --html, and --body-file)
- Reply and forward
- 3. Emoji Reactions (`list-reactions`, `react`, `delete-reaction`)
- 1. List validated emoji reactions on a message (as JSON) or thread
- 2. React to a message with a single Unicode emoji (alias: create-reaction)
- 3. Remove an active reaction by message + emoji or reaction ID (alias: unreact)
- 4. Drafts
- 5. Labels, Organization & Batch Operations
- 6. Settings, History & Attachments
- Vacation responder (optional --timezone for timestamp display)
- Forwarding, Send-As, History & Attachments
- Handling Web UI (Sapinto) IDs
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   A 403 that names a missing permission or scope is not a sign-in problem.
- -   **`--page-token <TOKEN>`** (or `--page_token <TOKEN>`) — Pagination token
- -   **Explicit User Authorization Required for High-Risk Mutations**:
- -   **Deleting Drafts** (`mutate delete-draft`): Permanent (bypasses Trash).

## Key rules (verbatim lines from SKILL.md)

1. -   **Explicit User Authorization Required for High-Risk Mutations**:
2. -   **Trashing Messages** (`mutate trash`): Never use unless the user
3. -   **No Shell Filtering (`grep`/`awk`)**: NEVER pipe Gmail CLI output to
4. -   **Avoid `--json` on `readonly read`**: Default `readonly read` strips HTML

## Files inside the skill

- `scripts/gmail`
- `scripts/gmail.cmd`
