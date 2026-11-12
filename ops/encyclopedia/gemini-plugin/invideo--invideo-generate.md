# invideo-generate (invideo plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\invideo\skills\invideo-generate\SKILL.md` (1.2 KB; invideo plugin — generation sub-skill; `references/models.md` exists).

## Summary
The generation arm of invideo: producing images, video, voice-over, music, SFX, and 3D for a project when the person's files and stock can't supply them. Procedure: pick the model from the live list (`invideo gen models` / `find_models`, it changes as models ship), price with `--dry-run`, state the cost, run with `--max-credits`, generate ONE sample, review it, then produce the rest. With narration, generate voice first and read its length (`invideo media metadata`) so picture is generated to fit. Max three tries per asset, changing something each time, then stop and tell the person; redo only what failed.

## When to use / when NOT
Use only for assets neither uploads nor stock can provide. Not for sourcing existing media (`/invideo-media` handles uploads/stock/rights) and not as a general-purpose image/video API — output lands in an invideo project.

## Inputs, outputs, tools
- Inputs: asset specs (type, model choice, prompt, duration/fit constraints like voice length).
- Outputs: generated media assets attached to the project timeline.
- Tools: `invideo gen models|run` CLI / `find_models`, `dry_run`, `media metadata`; invideo credit balance.

## 5 most important rules
1. Read `/invideo` first; generate only what files+stock can't give.
2. Model list is live — always query it, never hardcode model IDs.
3. Always dry-run price → say cost → cap with `--max-credits` → sample first → then batch.
4. Narration before picture: voice length determines video length.
5. Three tries max per asset with a changed parameter each time; then escalate to the person and redo only failures.

## Risks / owner notes
Every generation spends real invideo credits — the dry-run/cap/sample discipline is the cost control. Failed-asset retries burn budget if the cap is set loosely.

## Category and tags
Category: media. Tags: invideo, generation, credits, dry-run, voice-over, cost-control.
