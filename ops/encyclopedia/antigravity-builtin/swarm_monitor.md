# swarm_monitor

- Tool: `antigravity-builtin`
- Category: build
- Source: `C:\Users\a7med\.gemini\antigravity\builtin\skills\swarm_monitor\SKILL.md`
- SKILL.md size: 5776 chars

## What it does

>- ONLY for the native-swarm worker whose brief says it is the monitor. On a timer, it checks whether the whole swarm has stalled and calls on the one member who can unstick it. Coordinators and other workers: do not load this.

## Structure (headings inside SKILL.md)

- You are the swarm's stall monitor
- Rules
- Start
- Each tick
- Stalled?
- Do not repeat yourself
- Going dormant
- Resuming
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. -   **Never do the work.** Do not edit files, run builds, review code, or
2. -   **A result went to nobody.** Someone posted after the coordinator's

## Files inside the skill

- (SKILL.md only)
