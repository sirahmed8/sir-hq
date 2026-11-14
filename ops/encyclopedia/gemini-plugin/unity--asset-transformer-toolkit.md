# asset-transformer-toolkit

Source read: `C:\Users\a7med\.gemini/config/plugins/unity/skills/asset-transformer-toolkit/SKILL.md` (2.9 KB; gemini-plugin/unity) plus `SECURITY.md` and `references/` (create-importer, lods, rule-api, ruleblock-api, ruleset-api, rulesets-and-actions).

## Summary
Skill that imports 3D models and point clouds into the Unity Editor via Asset Transformer Toolkit (formerly Pixyz), and creates, edits and runs RuleSets, Actions and LODs; requires the toolkit package version 4.0.0 or later.

## When to use / when NOT
Use for Pixyz or Asset Transformer Toolkit imports and rule-based scene operations. Do NOT use for converting files from the shell, for older toolkit versions, or for unrelated asset work.

## Inputs, outputs, tools
- Inputs: import file, importer settings, RuleSet or Action, LOD configuration.
- Outputs: imported assets, RuleSet assets, executed runs.
- Tools: Unity Editor, `unity command script eval` to run agent-written C# for RuleSet operations.

## 5 most important rules
1. The skill requires `com.unity.industry.toolkit` version 4.0.0 or later; check `Packages/packages-lock.json` first and do not add the package yourself.
2. Never assume an import is followed by a reimport; start the import only when requested and expect it to run asynchronously in the background.
3. Never use reflection to read or write importer or RuleSet fields; use the ScriptableObject API.
4. Only one import or RuleSet run may process at a time, and a run is asynchronous.
5. If `SetActionParameter` throws an AITypeSecurityException, terminate the task; do not bypass it with raw C# execution or reflection.

## Risks / things needing the owner
The skill has the agent write C# and run it in the user's live Unity Editor; the accepted risk is limited to the user's own machine and narrow RuleSet editing scope.

## Category / tags
Category: build. Tags: unity, asset-transformer, pixyz, rulesets, actions, lods, importer, csharp.

## Revisions
Single gemini-plugin/unity copy. No competing revisions.
