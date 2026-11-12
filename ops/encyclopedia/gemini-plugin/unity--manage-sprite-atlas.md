# manage-sprite-atlas

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\manage-sprite-atlas\SKILL.md`
- SKILL.md size: 18343 chars

## What it does

Manages SpriteAtlas assets through a prebuild pipeline, covering master and variant atlases, packing settings, and platform overrides. Use when asked to create or optimize sprite atlases.

## When to use (from skill text)

- - Use this if you want to keep current setup

## Structure (headings inside SKILL.md)

- Unity SpriteAtlas V2
- 🚨 CRITICAL: Required Checks and User Inputs Before Implementation
- Read the shipped resources before writing code (REQUIRED)
- 0. Check for Existing Scripts (REQUIRED FIRST STEP)
- 1. Delivery Mechanism (REQUIRED)
- 2. SpritePacker Mode (REQUIRED)
- 🚨 CRITICAL: Default Approach is Prebuild Generation
- ❌ DO NOT Create Manual Menu Item Scripts
- 🚨 CRITICAL: Sprite Source Location Restriction
- Critical V2 Architecture
- Forbidden Cross-Context Usage (Common Error Sources)
- Core V2 Workflow (Reference Only - Use Prebuild Instead)
- Prerequisites
- Quick Start: Automated Prebuild Generation (DEFAULT APPROACH)
- Overview
- Workflow Steps
- Option A: Built-in Data (Immediate Loading)
- Option B: Late-Binding via Addressables (On-Demand Loading)
- Common Categorization Patterns
- Variant Generation in Prebuild
- Advanced: Manual Authoring (NOT Default - Use Only When Explicitly Requested)
- Key Requirements (V2-Specific)
- Detailed Reference
- Namespaces
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Suitable for**: Core UI, main gameplay sprites, always-needed assets
2. - **🚨 REQUIRED**: Build Addressables content as build step
3. - **🚨 REQUIRED**: Create late-binding runtime loader script
4. - **Cons**: Requires Addressables package, async loading, network dependency
5. 1. **🚨 ALWAYS check for existing scripts FIRST**: Before generating code, scan for scripts with `[UNITY-SKILL:SPRITEATLAS]` identifier and prompt user to update or create new

## Files inside the skill

- `references/addressables-delivery.md` — "Late-Binding via Addressables (On-Demand Loading)"
- `references/api.md` — "SpriteAtlas V2 API Reference"
- `references/best-practices.md` — "SpriteAtlas V2 Best Practices"
- `references/common-errors.md` — "Common Errors and Invalid Patterns"
- `references/custom-packing.md` — "Custom Sprite Packing with ScriptablePacker"
- `references/manual-authoring.md` — "Manual Authoring (Advanced - Not Default)"
- `resources/authoringvsruntime.cs`
- `resources/buildaddressablespostprocess.cs`
- `resources/cacheloadedatlases.cs`
- `resources/cleanupbatchoperations.cs`
- `resources/createandconfiguremasteratlas.cs`
- `resources/custompackersetup.cs`
- `resources/deprecatedmethods.cs`
- `resources/dontmodifywithoutsaving.cs`
- `resources/dontpackinruntimebuilds.cs`
- `resources/dontscriptspriteatlasineditor.cs`
- `resources/editorconfiguration.cs`
- `resources/enablespritepacking.cs`
- `resources/gridspritepacker.cs`
- `resources/handlelatebinding.cs`
- `resources/handlenullcases.cs`
- `resources/migratev1tov2.cs`
- `resources/multipagepacker.cs`
- `resources/optimizetexturesettings.cs`
- `resources/packerdebugging.cs`
- `resources/packtransform.cs`
- `resources/platformnames.cs`
- `resources/queryspritesefficiently.cs`
- `resources/registercallbacks.cs`
- `resources/runtimeatlasloader.cs`
- `resources/runtimespriteaccess.cs`
- `resources/savespriteatlasasset.cs`
- `resources/scriptablepacker.cs`
- `resources/setincludeinbuild.cs`
- `resources/sizeoptimizedpacker.cs`
- `resources/spriteatlaslatebinding.cs`
- `resources/spriteatlasprebuildgenerator.cs`
- `resources/spritedata.cs`
- `resources/spritepack.cs`
- `resources/texturedata.cs`
- `resources/updatebuildscripts.cs`
- `resources/updatesettingsconfiguration.cs`
- `resources/usevariantswisely.cs`
- `resources/variantatlas.cs`
