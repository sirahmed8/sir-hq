# netlify-deploy

- Tool: `gemini-plugin` (plugin: `netlify`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\netlify\codex\skills\netlify-deploy\SKILL.md`
- SKILL.md size: 14586 chars

## What it does

Create, configure, and manage Netlify deploys from code — reach for this when setting up Git continuous deployment, running netlify deploy or netlify deploy --prod from the CLI, writing netlify.toml deploy contexts, adding a Deploy to Netlify button, wiring build hooks, configuring Deploy Previews or branch deploys, locking or skipping deploys, fixing a failed or secrets-scanning deploy, or when someone asks to "deploy my site", "set up preview deploys", "add per-branch build config", "keep staging out of Google", or "add a deploy button to my README".

## When to use (from skill text)

- **Continuous deployment vs manual deploys:** Deploy with Git and the Netlify CLI support continuous deployment — a push auto-triggers a build. Drag and drop and the API create one-off manual deploys. Manual deploys (`netlify deploy`) do **not** run a build command; drag-and-drop while logged in is t
- - **Build hooks** — unique URLs that trigger builds. (Deploys from build hooks are treated as trusted and bypass the deploy request policy.)

## Structure (headings inside SKILL.md)

- Netlify deploy
- Modern CLI
- Ways to create a deploy
- netlify.toml deploy contexts
- Deploy Previews & branch deploys
- Locking, skipping, and manual production deploys
- Managing deploys
- Deploy to Netlify button
- require/pre-fill env vars (hash, client-side only; values may be null)
- monorepo base dir (whole repo cloned, builds from blog/)
- clone only a subdirectory
- deploy a specific branch (sets it as production branch)
- install required SDK extensions before first deploy
- Secrets scanning failures
- Fixing a failed deploy — no rollbacks
- Deploy permissions (private repos)
- Constraints & gotchas
- Netlify house rules (deploy)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Git CD** — connect a repo; Netlify builds and deploys on every push (OAuth2 or the Netlify GitHub App). This is the default path. Production deploys come from pushes to the production branch — often the repo's default branch (e.g. `main`), changeable under Branches and deploy contexts.
- - **CLI** — `netlify create`, `netlify deploy`, `netlify deploy --prod`.
- - **Drag and drop** — https://app.netlify.com/drop. Logged in: builds if needed. Not logged in: publishes files as-is.
- - **Deploy Previews** auto-build for PRs/MRs (GitHub, GitLab, Bitbucket, Azure DevOps, Cursor Origin) and agent runs. The base branch must be a production branch or a branch-deploy-enabled branch. URL: `deploy-preview-<num>--<site>.netlify.app`. While the first deploy is pending the URL returns `Not

## Key rules (verbatim lines from SKILL.md)

1. - **Deploy Previews** auto-build for PRs/MRs (GitHub, GitLab, Bitbucket, Azure DevOps, Cursor Origin) and agent runs. The base branch must be a production branch or a branch-deploy-enabled branch. URL: `deploy-preview-<num>--<site>.netlify.app`. While the first deploy is pending the URL returns `Not
2. - **⚠ Manual `netlify deploy --prod` on a Git-CD site:** the next push to the production branch silently replaces your hand-shipped deploy. Warn the user; lock the published deploy if it must stay live.
3. - **Automatic deletion:** deploys are deleted after 30 days (90 days on paid plans); Enterprise can raise this up to 365 days. Never deleted: the published deploy, the most recent successful production deploy, and the most recent successful branch deploy per branch. Configure at Project configuratio
4. 1. Agents do not roll back deploys: never call `restoreSiteDeploy` or
5. 2. A failed deploy never publishes; on failure there is nothing to roll

## Files inside the skill

- `references/cli-commands.md` — "Netlify CLI Commands Reference"
- `references/deployment-patterns.md` — "Netlify Deployment Patterns"
- `references/netlify-toml.md` — "netlify.toml — Build Configuration for Deploys"
