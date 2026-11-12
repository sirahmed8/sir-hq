# twg-setup

- Tool: `gemini-plugin` (plugin: `atlassian-twg-cli`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\atlassian-twg-cli\antigravity\skills\twg-setup\SKILL.md`
- SKILL.md size: 6465 chars

## What it does

Install, upgrade, authenticate, or repair `twg` for Antigravity, including missing CLI or skills and doctor/auth follow-up. TWG gives Antigravity grounded work context across Jira, Confluence, Bitbucket, JSM, Assets, Slack, Google Drive, and more, so it can connect tickets, docs, code, people, and decisions; surface risks and dependencies; summarize progress; and keep work moving.

## When to use (from skill text)

- Use this section only for a pre-existing install or after the user replies `done`. Run only the

## Structure (headings inside SKILL.md)

- TWG Setup
- Unix / macOS
- Windows PowerShell
- Common flow
- Doctor remediation
- Skill refresh
- Continue The Original Request
- Things To Try
- (none)

## Tools / MCPs it needs

- allowed-tools: Bash
- allowed-tools (frontmatter): `Bash`

## Risks / cautions found in text

- - What's the latest status of [project]? Include the owner, last update, blockers or risks, and next milestone.

## Key rules (verbatim lines from SKILL.md)

1. 3. After the user replies `done`, run the OS-specific **Inspect** block yourself so `doctor`
2. 4. After `doctor` is healthy, run the OS-specific **Antigravity skills** block unsandboxed.
3. - Give interactive auth and setup fixes to the user; never execute them yourself. Put the command

## Files inside the skill

- (SKILL.md only)
