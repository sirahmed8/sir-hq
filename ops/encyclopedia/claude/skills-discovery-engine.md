# skills-discovery-engine

## Summary
skills-discovery-engine is the SIR-authored counterpart to skill-installer: it finds, vets and installs agent skills from the global `skills.sh` registry (Vercel Labs index, claimed 700,000+ skills) and from GitHub keyword searches. Its protocol is search, security audit, format validation, multi-platform deployment, parity check. Concretely it tells the agent to query skills.sh or GitHub for keyword matches, prefer repos with stars/maintenance/docs, inspect each SKILL.md for hidden shell payloads, obfuscated curls or credential scraping, validate frontmatter (`name` lowercase kebab-case, `description` under ~250 chars), strip prose to save tokens, then write the audited SKILL.md into every harness skills directory and run `sync_all_ai_skills.ps1` for parity.

## When to use / when NOT
Use when a task needs a capability no installed skill covers, or when the owner asks to find/install a skill from the internet. Do NOT use for skills already present, for repairing a broken skill (skill-repair), or for Codex-only curated installs (skill-installer). Do NOT skip the security audit step even for "trusted-looking" repos.

## Inputs, outputs, tools
- Inputs: a capability keyword or task description; optionally `npx skills add <repo>`.
- Outputs: one or more new `<skill-name>/SKILL.md` folders across the harness skill roots (`.gemini/config/skills`, `.claude/skills`, `.cursor/skills`, `.codex/skills`, `.config/opencode/skills`, `.config/kilo/skills`), plus a parity sync via `sync_all_ai_skills.ps1`.
- Tools: web/GitHub search, `npx skills`, git clone or direct file writes, and the local sync script. Needs network.

## 5 most important rules
1. Always audit before installing: look for hidden shell execution, obfuscated network calls and credential harvesting inside SKILL.md and any bundled scripts.
2. Validate frontmatter: kebab-case `name`, short high-signal `description` under ~250 characters.
3. Keep frontmatter concise; strip repetitive prose to preserve token budget.
4. Deploy to all target harness directories, not just the current one.
5. Run `sync_all_ai_skills.ps1` afterwards so every AI tool sees the same skill set.

## Risks / things needing the owner
This skill deliberately pulls third-party code/instructions onto the machine; a malicious SKILL.md can exfiltrate data in later sessions, which is why the audit step exists. `npx skills add` runs an npm package, so supply-chain risk applies. Nothing needs the owner unless an install requires an account or payment.

## Category / tags
ops · skill discovery, skills.sh, github, security-audit, automation

## Revisions
Six copies exist (claude, codex, kilo, cursor, windsurf, opencode) and they are the same document with only the frontmatter `description` wording differing (claude 2492 bytes, codex 2484). Best revision: the claude copy (used here); identical content, pick whichever harness is running.
