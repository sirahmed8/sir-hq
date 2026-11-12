# build-live-game

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\build-live-game\SKILL.md`
- SKILL.md size: 18544 chars

## What it does

Builds and operates a live game's backend with Unity Gaming Services. Make sure to use this skill when the user wants trusted server-side game logic, player progress, remote configuration, sign-in, achievements, battle passes or leaderboards.

## Structure (headings inside SKILL.md)

- Build a Live Game With Unity Gaming Services
- Before You Start
- Glossary
- Documentation Map
- UGS Packages
- Initialization Pattern
- Architecture — How Packages Combine
- Core Services — Quick Reference
- Authentication
- Cloud Code
- Cloud Save
- Remote Config
- Tooling
- Deployment
- UGS CLI
- Services APIs
- Common Architecture Patterns
- Pattern 1: Config + State + Server Writes
- Pattern 2: Client-Direct Data
- Pattern 3: Competitive Features
- Validation
- Detailed References
- Service References
- Feature Blueprints
- Final Report
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **docs.unity.com**: the UGS product pages below are unversioned, so there is nothing to replace.

## Key rules (verbatim lines from SKILL.md)

1. 4. Before you go forward with a workflow or diagnosis, open and read the documentation pages for the service you will use (see [Documentation Map](#documentation-map)) and the matching file under `references/`, and name the pages you read in your response. This is because your training knowledge abo
2. 5. Do only what's asked. Don't change unrelated assets or files. Avoid long explanations.
3. - [Before You Start](#before-you-start)
4. 2. Check the initialization order in the code: search for `UnityServices.InitializeAsync()` and confirm it runs before the sign-in call, and that sign-in completes before any service call.
5. 5. Check Access Control by its effect: if the feature deploys an `.ac` policy that denies direct player writes, enter Play mode, run one direct client Cloud Save write to a key the policy covers (a temporary `SaveAsync` call), and confirm it fails with a `403`. Remove the temporary call afterwards. 

## Files inside the skill

- `references/achievements.md` — "Achievements Reference"
- `references/apis.md` — "Services APIs Reference"
- `references/authentication.md` — "Authentication Reference"
- `references/battlepass.md` — "Battle Pass Blueprint"
- `references/blueprints-and-samples.md` — "Blueprints, Building Blocks and Sample Projects"
- `references/cloud-code-cloudbehaviours.md` — "CloudBehaviours Reference"
- `references/cloud-code-modules.md` — "Cloud Code Scripts and Modules Reference"
- `references/cloud-code.md` — "Cloud Code Reference"
- `references/cloud-save.md` — "Cloud Save Reference"
- `references/deployment.md` — "Deployment Reference"
- `references/player-account.md` — "Player Account Reference"
- `references/remote-config.md` — "Remote Config Reference"
- `references/tooling.md` — "Tooling Reference"
- `references/ugs-cli.md` — "UGS CLI Reference"
