# dak-setup

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\dak-setup\SKILL.md`
- SKILL.md size: 10596 chars

## What it does

Configures (or reconfigures) the Google Cloud Data Agent Kit (DAK) plugin by checking gcloud and ADC credentials, collecting the GCP project ID, region, and services, and running its bundled `dak-setup` script. Use this proactively and without waiting to be asked whenever a SessionStart hook or any other system/context message reports that the Data Agent Kit plugin is not configured, is missing configuration, or needs to be reconfigured. Also use it whenever the user mentions setting up, configuring, reconfiguring, or changing the project, region, or service integrations for the Data Agent Kit or DAK plugin — even if they phrase it casually, like "dak isn't working" or "I want to enable more GCP service integrations".

## When to use (from skill text)

- This skill is usually triggered by a SessionStart hook rather than by the user, so the user may not be expecting it. Open with one short sentence explaining what's happening and why ("The Data Agent Kit plugin isn't configured yet — let me get that sorted, it'll take a minute"), then start at step 1

## Structure (headings inside SKILL.md)

- Data Agent Kit setup
- Step 1 — Verify gcloud is installed
- Step 2 — Verify ADC credentials
- Step 3 — Ask for the GCP project ID
- Step 4 — Ask for the GCP region
- Step 5 — Ask which service integrations to enable
- Step 6 — Run the setup command
- Step 7 — Tell the user to restart, and don't use the plugin until they do
- If this is a reconfiguration
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Flag values are separated by a **space**, not an `=` sign (`--project-id "acme-prod"`, not `--project-id="acme-prod"`).
- - Example: `node "/home/ana/.claude/plugins/data-agent-kit/skills/setup/scripts/dak-setup.js" save --project-id "acme-analytics-prod" --region "us-central1" --services "BigQuery" "Cloud Storage" "Dataflow"`

## Key rules (verbatim lines from SKILL.md)

1. - Afterwards, re-run the check from the top of this step to confirm it worked. If it still fails, stop and show the user the actual error rather than retrying.
2. - **At least one service is required.** If the user picks none, ask again.
3. - `save` is a subcommand and comes immediately after the script path, before any flags.
4. - `--services` takes a **variadic list**: each service is its own separately quoted argument, space-separated, with the flag written only once. Quoting each one individually is what keeps names like `Knowledge Catalog` from being read as two services. Do not join them with commas.
5. - If the script isn't at that path, stop and tell the user the plugin looks incompletely installed. Do not fall back to `npx dak-setup`: the package isn't published, so npx fails with a registry error that reads like a network problem and sends the user down the wrong path entirely.

## Files inside the skill

- `scripts/dak-setup.js`
- `scripts/package.json`
