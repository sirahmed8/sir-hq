# vercel-firewall

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-firewall\SKILL.md`
- SKILL.md size: 20556 chars

## What it does

Configure DDoS protection.

## When to use (from skill text)

- The firewall sits in front of every request. A misconfigured rule can block real users, kill SEO crawlers, or break checkout. Treat changes like a production database migration: stage, review, and let the user pull the trigger.

## Structure (headings inside SKILL.md)

- Vercel Firewall
- Core Knowledge
- Overview
- Custom rules
- View
- Create — four modes
- AI — TTY only, BLOCKED FOR AGENTS/SCRIPTS
- Interactive wizard — TTY only, BLOCKED FOR AGENTS/SCRIPTS
- Flags — works in scripts and agents
- JSON — works in scripts and agents
- Multiple conditions (AND) and OR groups
- AND — multiple --condition flags in the same group
- OR — use --or to start a new group
- Edit and manage
- Condition format
- Operators
- Condition types
- Actions
- Rate limit example
- IP blocks
- System bypass
- Attack mode
- System mitigations
- Publishing
- Querying firewall traffic from the CLI
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Vercel does not bill for traffic blocked by DDoS mitigations or WAF.** Usage is only incurred for requests served before mitigation kicked in or not classified as an attack. You do not pay for requests or bandwidth for denies, challenges, or rate-limits from WAF custom rules or managed rules.
- - **Request shape**: `path`, `raw_path` (pre-rewrite), `target_path` (post-rewrite), `route` (e.g., `/blog/[slug]`), `server_action`, `method`, `host`, `protocol`, `scheme`, `environment` (preview|production), `region`
- - `--rate-limit-algo` — `fixed_window` (default), `token_bucket` (Enterprise only)
- 3. **Block in preview first.** Edit the rule to `deny` (or `challenge`) and add an `environment = preview` condition so production stays in log mode. This lets the user hit a preview deployment and confirm the block fires correctly without exposing real users:

## Key rules (verbatim lines from SKILL.md)

1. - **Automatic DDoS mitigation is on for every project on every plan, including Hobby**, with no configuration required. It covers L3/L4/L7 attacks.
2. - **Vercel does not bill for traffic blocked by DDoS mitigations or WAF.** Usage is only incurred for requests served before mitigation kicked in or not classified as an attack. You do not pay for requests or bandwidth for denies, challenges, or rate-limits from WAF custom rules or managed rules.
3. - **Headers / cookies / queries** — require `key`: `header`, `cookie`, `query`
4. - `log` — log without blocking (use to tune before enforcing)
5. - `--since` must fall inside your plan's retention, or the query requires Observability Plus. Shortening the window with `--until` does not help if `--since` is already too far back.

## Files inside the skill

- (SKILL.md only)
