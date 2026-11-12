# netlify-access-control

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\skills\netlify-access-control\SKILL.md`
- SKILL.md size: 14022 chars

## What it does

Picks the right Netlify site.

## When to use (from skill text)

- 8. The description's triggers must include the SSO-session symptoms users
- skill never triggers on the symptom.

## Structure (headings inside SKILL.md)

- Netlify access control — pick the protection layer
- First: disambiguate "auth" — three unrelated layers
- Decision guide (this skill's job)
- Key distinction: Private vs Password
- Identify the visitor: `context.user`
- SSO-session symptom: 401s after ~1 hour
- UI paths (the only path — no API)
- Constraints & footguns
- Netlify house rules (access-control)
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tool

## Risks / cautions found in text

- 2. **Password Protection / project visibility** — "can this request load the site at all." Covered here.
- - Restrict entire site to your team, invite by email → **Private project** (Credit-based) or **Team login protection** (Password Protection).
- - Share with anyone holding one shared password → **Basic password protection** (Pro) or **Password** visibility (Credit-based Pro only). **Not available on Credit-based Free/Personal** — make the project **Private** instead.
- - Keep production public, protect previews only → scope **Previews only** / **Non-production deploys only**.

## Key rules (verbatim lines from SKILL.md)

1. - **They can't** (e.g. employees without Netlify seats) → **Auth0 extension** federating to the corporate IdP, *before* the two-layer stack.
2. - Require SSO to *view a site* → Organization/Team SSO with **Only SSO allowed (strict)**, then Password Protection with **Team login protection**.
3. - **Private** already requires Netlify credentials — no shared password. Invite by email; recommended for team-only access.
4. - **Password** = one universal shared password anyone can use (including managing team members, who must also enter it). No SSO. Doesn't identify individual visitors.
5. - **Team login protection** = same mechanism as Private: a visitor must log in as a member of your Netlify team, and **Reviewers** you invite can get in too (unlimited and not counted toward the member count on legacy plans; Pro or higher on Credit-based plans). **Git Contributors cannot log in** — 

## Files inside the skill

- `references/two-layer-pattern.md` — "Two-Layer Pattern: Company-Only Access + Per-User Identity"
