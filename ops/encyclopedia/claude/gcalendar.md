# gcalendar

- Tool: `claude`
- Category: design
- Source: `C:\Users\a7med\.claude\skills\gcalendar\SKILL.md`
- SKILL.md size: 10330 chars

## What it does

Read, create, and manage Google Calendar events. Use when the user shares a calendar.google.com URL, asks what is on their schedule, wants an event found, created, updated, deleted, or moved, wants to RSVP, wants free/busy or scheduling conflicts checked before proposing a time, wants focus time or an out-of-office block created, wants an event quick-added from a phrase or imported from an ICS file, or wants to know where someone is working from and which timezone they are in. Don't use for Gmail, Chat, or Tasks.

## Structure (headings inside SKILL.md)

- Google Calendar
- Setup and Authentication
- Windows (PowerShell)
- Usage
- Read the calendar before you write to it
- Times and timezones
- Reporting back
- Recipes
- Commands
- Notifications
- Meetings with other people
- Blocking time out
- Working Location
- Global Flags
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   `mutate` creates, updates, deletes, and RSVPs to events.

## Key rules (verbatim lines from SKILL.md)

1. -   `--json` — emit JSON instead of a table. Use it whenever you are going to

## Files inside the skill

- `references/commands.md` — "Command Reference"
- `references/recipes.md` — "Recipes"
- `references/working_location.md` — "Working Location"
- `scripts/gcalendar`
- `scripts/gcalendar.cmd`
