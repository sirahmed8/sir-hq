# gcalendar

## Summary
CLI-driven Google Calendar manager built around a purpose-built `gcalendar` binary (scripts/gcalendar(.cmd) bootstraps it onto PATH). Two namespaces: `readonly` (events, today, search, get, instances, conflicts, calendars, colors, acl, freebusy, next-free, working-hours, workloc) and `mutate` (create, update, recurring, focus-time, quick-add, rsvp, move, delete, import-ics, workloc-set); flat commands work but are deprecated. Auth flow is prescribed exactly: run `auth status` first (the only login check — never hunt for tokens or run ops before login), then `auth login` as a background command that prints an OAuth URL for the user to approve. Heavy emphasis on write-safety because calendar writes email real guests.

## When to use / when NOT
Use for reading schedules, creating/editing/moving/deleting events, RSVPs, free/busy and conflict checks, focus time, OOO blocks, quick-add from phrases, ICS import, working-location queries. NOT for Gmail/Chat/Tasks.

## Inputs, outputs, tools
- Inputs: dates (YYYY-MM-DD), RFC3339 timestamps, calendar IDs (email addresses), event IDs, RRULEs, ICS files, attendee emails, `--send-updates`, `--json`, `--timezone`.
- Outputs: event tables/JSON, `Link:` URLs to created events, busy intervals, conflict lists.
- Tools: `gcalendar` CLI (readonly/mutate namespaces), references/recipes.md, commands.md, working_location.md.

## 5 most important rules
1. `mutate delete` is IMMEDIATE — no confirmation, no undo: only delete an event the user explicitly named, and announce which event first.
2. Writes reach other people: creating/updating/moving/deleting events with guests can email all attendees and invites can't be recalled — confirm title/time/guests BEFORE writing; never invite anyone unnamed or widen visibility on your own.
3. Read before write: check the day (`readonly events --date`), check every invitee (`readonly freebusy --email ... --start --end`), resolve relative dates to concrete dates in the user's timezone first, then create and report the printed `Link:`.
4. `--send-updates` defaults to `none` — guests are NOT notified unless you pass `all`; decide deliberately and say which you chose (silent for own blocks, `all` when actually inviting/cancelling on people).
5. Attendee flags MERGE on update (use `--remove-attendee` to drop); `--location` does NOT book rooms (rooms are resources invited as attendees); `--gvc` vs `--meet-code` are mutually exclusive; all-day `--end` is EXCLUSIVE (one-day event on the 15th = start 15 end 16).

## Risks / owner needs
Login requires the user to approve an OAuth URL in browser (owner action, may hit Google consent). Working-location ≠ time off — a recurring "office" location doesn't mean someone isn't on vacation; verify with freebusy. Mutations are irreversible-ish (delete has no undo).

## Category and tags
Category: automation. Tags: google-calendar, scheduling, events, rsvp, freebusy, ooo, ics, cli.

## Revisions
Claude copy used (skill description also present in windsurf list — same skill family; single authoritative claude source per selection rule).
