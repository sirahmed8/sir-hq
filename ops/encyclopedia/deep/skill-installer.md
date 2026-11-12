# skill-installer

## Summary
skill-installer is OpenAI's helper for installing Codex skills into `$CODEX_HOME/skills` (default `~/.codex/skills`). Its default catalogue is the curated and experimental skill folders of `openai/skills` on GitHub, but it also accepts any GitHub repo path, including private repos, via HTTPS token or git sparse-checkout fallback. It ships two Python helper scripts: `list-skills.py` (lists installable skills, marking ones already installed, with a `--format json` mode) and `install-skill-from-github.py` (downloads skill folders by repo/`--path`, `--ref`, `--dest`, `--name`, `--method auto|download|git`). It aborts if the destination skill directory already exists.

## When to use / when NOT
Use when the owner asks what Codex skills are available or wants one installed from the curated list or a specific GitHub repo. Do NOT use it for Claude/Kilo/Cursor skill folders (it targets `$CODEX_HOME/skills` only), for skills already installed (it aborts by design; repair or update instead), or for discovering arbitrary internet skills (that is skills-discovery-engine).

## Inputs, outputs, tools
- Inputs: a skill name, or `--repo owner/repo --path <path>` / `--url`, optional `--ref`, `--dest`, `--name`, `--method`.
- Outputs: a new directory `$CODEX_HOME/skills/<skill-name>/` containing the downloaded SKILL.md and its files; console list output for listing.
- Tools: Python 3 scripts that hit the GitHub API (`github_utils.py` uses a `codex-skill-install` user agent); `GITHUB_TOKEN`/`GH_TOKEN` or existing git credentials for private repos; git sparse checkout as fallback. Needs network and, in sandboxes, escalation.

## 5 most important rules
1. Listing defaults to `.curated`; pass `--path skills/.experimental` for experimental skills.
2. Install aborts if the target skill directory already exists; there is no overwrite flag.
3. Download is tried first; on auth/permission failure it falls back to git sparse checkout (HTTPS then SSH).
4. Private repos need `GITHUB_TOKEN`/`GH_TOKEN` or pre-configured git credentials.
5. `.system` skills are preinstalled; do not reinstall them unless the user insists.

## Risks / things needing the owner
Installing a third-party skill executes whatever instructions its SKILL.md contains in future sessions, so vet the source repo. Private-repo access needs a token the owner may have to provide or approve. Nothing else is owner-facing.

## Category / tags
ops · skill installation, codex, github, automation

## Revisions
Only one revision exists: the claude copy at `C:\Users\a7med\.claude\skills\skill-installer\` (includes LICENSE.txt, agents/openai.yaml, assets, and the three scripts). No other tool holds a copy, so there is nothing to compare.
