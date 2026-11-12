# new-unity-project (unity plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\new-unity-project\SKILL.md` (24.7 KB; unity plugin; `SECURITY.md` + `references/` incl. skill-setup.md; `allowed-tools: Bash, Write, Edit`). Guided flow from idea to running, version-controlled Unity project — "paved by default, guided on request".

## Summary
Owns the FLOW (mode, defaults, ordering, background installs, handoffs) and delegates mechanics to sibling skills: `unity-cli` (install/auth/license/create/source-control/open — its "Bootstrap a new project" workflow is the backbone), `unity-package-management`, `urp-postprocessing`, `ui`, `2d-pixel-perfect`, `craft-game-floors` (look/camera/lighting/feedback/audio/shell/live floor/done gate), and end-stage `implement-in-app-purchases`/`levelplay-unity-integration`/`build-live-game`. Mode: paved unless the user asks for interview — parse the prompt, fill gaps from the Defaults table (latest editor, URP template 3D/2D, Desktop-only platforms unless implied, no monetization at creation, local git + Unity .gitignore, anonymous player accounts, craft floors on), print exactly one assumptions manifest block before create launches (every assumption named and reversible), proceed asking only on pushback/unruled forks. Bare/minimal asks get `--bare` (skips floors, states the cost). Sign-in/license comes FIRST: `unity auth status` + `unity license status` JSON, one combined question offering free Unity Personal (with EULA notice), never hand the user commands — agent runs `unity auth login`/`license activate` only after yes; declining sign-in but having serial/floating still yields a local `--no-cloud` project. Steps: concept → platforms/monetization + parallel background installs → join/reconcile result vs manifest → source control → packages → player identity + craft floors → visual baseline → save & first commit → handoff note. Human gates (sign-in, license, publishing) are never auto-consumed.

## When to use / when NOT
Use when the user asks to start a new Unity game/prototype from scratch. Not for working inside an existing project (use the domain skills directly) or for non-Unity engines.

## Inputs, outputs, tools
- Inputs: the game concept/prompt (platforms, monetization hints, 2D/3D), license preference.
- Outputs: created+opened Unity project, git repo with .gitignore, baseline packages/visuals, first commit, CLAUDE.md handoff note, monetization handoff.
- Tools: `unity` CLI (`auth`, `license`, project create/open), sibling skills listed above, Unity Editor.

## 5 most important rules
1. Check delegated skills are loaded BEFORE Step 1; missing `unity-package-management` stops the run at Step 2.
2. Auth/license status checked first; ONE combined question; agent runs auth commands only after explicit yes; Personal EULA disclosed in the choice.
3. Print the single assumptions manifest before create; reconcile the actual result against it at Step 3.
4. Paved = proceed on defaults, ask only on pushback; guided = ask current-step questions only.
5. Human gates (sign-in, license activation, publishing) always need the user's yes — never consume them silently; bare mode states its cost (no identity/saves/ranks).

## Risks / owner notes
Creates real Unity projects and may trigger license activation/EULA acceptance — the consent question is mandatory. `--no-cloud` projects lack cloud link/player accounts. Background installs run in parallel; Editor downloads are large.

## Category and tags
Category: mobile. Tags: unity, project-scaffolding, urp, license, paved-path, game-dev, onboarding.
