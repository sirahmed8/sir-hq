# sir-session-end

- Tool: `claude`
- Category: ops
- Source: `C:\Users\a7med\.claude\skills\sir-session-end\SKILL.md`
- SKILL.md size: 1880 chars

## What it does

End-of-session ritual for SIR work: update the checkpoint, append the mission log, push the mission repo, and answer the owner's questions. Use when a phase step, milestone or session finishes.

## Structure (headings inside SKILL.md)

- SIR session end
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. **Requirements.** If a request was completed or changed, update its row in `_SIR/REQUIREMENTS.md` (status and evidence only; never delete a row).
- 5. **Push.** If `D:\Projects\_SIR` changed: `git -C D:/Projects/_SIR add -A && git -C D:/Projects/_SIR commit -m "<what>" && git -C D:/Projects/_SIR push`. Run `gitleaks dir` first if any new file could hold a secret. Never commit secrets.
- 7. **Report** in the A5 shape: outcome, changes, verification, upgrades applied, risks and unverified items, owner actions, next best step. State decisions; do not ask questions.

## Key rules (verbatim lines from SKILL.md)

1. 3. **Requirements.** If a request was completed or changed, update its row in `_SIR/REQUIREMENTS.md` (status and evidence only; never delete a row).
2. 4. **Owner actions.** Anything only Ahmed can do goes to `_SIR/ops/OWNER_ACTIONS.md` with exact steps. It never blocks other work.
3. 5. **Push.** If `D:\Projects\_SIR` changed: `git -C D:/Projects/_SIR add -A && git -C D:/Projects/_SIR commit -m "<what>" && git -C D:/Projects/_SIR push`. Run `gitleaks dir` first if any new file could hold a secret. Never commit secrets.
4. 7. **Report** in the A5 shape: outcome, changes, verification, upgrades applied, risks and unverified items, owner actions, next best step. State decisions; do not ask questions.

## Files inside the skill

- (SKILL.md only)
