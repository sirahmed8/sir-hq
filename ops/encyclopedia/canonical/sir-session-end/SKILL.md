---
name: sir-session-end
description: End-of-session ritual for SIR work: update the checkpoint, append the mission log, push the mission repo, and answer the owner's questions. Use when a phase step, milestone or session finishes.
---

# SIR session end

1. **Checkpoint.** Update the right file so a fresh agent can continue without guessing:
   - HQ session (working folder D:\Projects or _SIR): `D:\Projects\_SIR\ops\HQ_CHECKPOINT.md` (format in `_SIR/core/04-memory.md`).
   - Project session: `<project>\.sir\CHECKPOINT.md` (template in `_SIR/standard/project-templates.md`).
   Keep it under about 100 lines. "Next step" names the exact command, file or task ID. Move finished items to the log.
2. **Log.** Append one dated line to `_SIR/ops/MISSION_LOG.md` (HQ) or the project's `CHANGELOG.md` (Unreleased) with what changed, the evidence, and any decision with its reason.
3. **Requirements.** If a request was completed or changed, update its row in `_SIR/REQUIREMENTS.md` (status and evidence only; never delete a row).
4. **Owner actions.** Anything only Ahmed can do goes to `_SIR/ops/OWNER_ACTIONS.md` with exact steps. It never blocks other work.
5. **Push.** If `D:\Projects\_SIR` changed: `git -C D:/Projects/_SIR add -A && git -C D:/Projects/_SIR commit -m "<what>" && git -C D:/Projects/_SIR push`. Run `gitleaks dir` first if any new file could hold a secret. Never commit secrets.
6. **Owner's questions.** Write down: Did we forget anything? What is missing compared with the best apps in this category? What should happen next? What would Ahmed think if he saw this now? What else might he need? Gaps become BOARD tasks; ideas go to `_SIR/ops/IDEAS_INBOX.md` marked `[agent]`.
7. **Report** in the A5 shape: outcome, changes, verification, upgrades applied, risks and unverified items, owner actions, next best step. State decisions; do not ask questions.
