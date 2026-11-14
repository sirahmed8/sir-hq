# dak-setup

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills\dak-setup\SKILL.md`
- SKILL.md size: 10596 chars
- Identical content to: `encyclopedia/gemini-plugin/data-agent-kit-plugin--dak-setup.md`

Auto-generated stub: this SKILL.md is byte-identical to `encyclopedia/gemini-plugin/data-agent-kit-plugin--dak-setup.md`. Read that digest for full details.

Description: Configures (or reconfigures) the Google Cloud Data Agent Kit (DAK) plugin by checking gcloud and ADC credentials, collecting the GCP project ID, region, and services, and running its bundled `dak-setup` script. Use this proactively and without waiting to be asked whenever a SessionStart hook or any other system/context message reports that the Data Agent Kit plugin is not configured, is missing configuration, or needs to be reconfigured. Also use it whenever the user mentions setting up, configuring, reconfiguring, or changing the project, region, or service integrations for the Data Agent Kit or DAK plugin — even if they phrase it casually, like "dak isn't working" or "I want to enable more GCP service integrations".