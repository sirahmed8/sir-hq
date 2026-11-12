# manage-sprite-atlas (unity plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\manage-sprite-atlas\SKILL.md` (18.5 KB; unity plugin; `resources/` has 38 C# files incl. spriteatlasprebuildgenerator, enablespritepacking, savespriteatlasasset, buildaddressablespostprocess, spriteatlaslatebinding, authoringvsruntime, deprecatedmethods; `references/` covers addressables-delivery, manual-authoring, common-errors, api, custom-packing, best-practices).

## Summary
Unity SpriteAtlas V2 authoring skill built on a strict editor/runtime split: `SpriteAtlasAsset`+`SpriteAtlasImporter` are editor-only, `SpriteAtlas` is runtime-only — never mix contexts. Mandatory pre-flight: (0) scan project for existing scripts tagged `// [UNITY-SKILL:SPRITEATLAS]` and ask update-vs-new-vs-abort; (1) ask delivery mechanism — Option A built-in (`includeInBuild=true`, immediate load, core UI/gameplay) vs Option B Addressables late-binding (`includeInBuild=false`, on-demand/DLC/levels/locales — requires ALL THREE scripts: prebuild generator, `IPostprocessBuildWithReport` Addressables builder, runtime late-binding loader); (2) enable Sprite Packer V2 mode and READ BACK `EditorSettings.spritePackerMode` (Disabled is the silent-failure default — atlas imports and looks done but never packs). Default approach is `IPreprocessBuildWithReport` generation — never manual `[MenuItem]` scripts unless explicitly requested. Sprites ONLY from `Assets/` (never Packages/built-ins). Two-step editor pattern: create via `SpriteAtlasAsset` → save → import → configure via `SpriteAtlasImporter` → SaveAndReimport; variants via `SetMasterAtlas` with a runtime atlas loaded via `LoadAssetAtPath<SpriteAtlas>`; `.spriteatlasv2` extension; `PackAtlases()` only for editor preview.

## When to use / when NOT
Use for creating or optimizing SpriteAtlas assets in a Unity 6000.3+ project. Not for texture compression generally, non-Unity engines, or hand-arranged atlases (manual authoring is explicitly non-default).

## Inputs, outputs, tools
- Inputs: sprite folders/naming rules in `Assets/`, delivery choice (built-in vs Addressables), platform format (e.g., ASTC_6x6 direct assignment).
- Outputs: prebuild generator script (+2 more for Addressables), generated `.spriteatlasv2` assets, Addressables entries/groups, late-binding loader.
- Tools: UnityEditor API (`SpriteAtlasAsset`, `SpriteAtlasImporter`, `IPreprocessBuildWithReport`, `IPostprocessBuildWithReport`, `ScriptablePacker`), Addressables, shipped `resources/` C# templates.

## 5 most important rules
1. Read the shipped `resources/` C# for your path BEFORE writing code — memory-based API use is the top cause of atlases that do nothing at runtime.
2. Check for existing `[UNITY-SKILL:SPRITEATLAS]` scripts first and ask update/new/abort; tag every generated script.
3. V2 context separation is absolute: editor = `SpriteAtlasAsset`/`SpriteAtlasImporter`, runtime = `SpriteAtlas`; the only allowed runtime use in editor is `SpriteAtlas.GetPackables()`.
4. SpritePacker mode must be enabled AND read back — `Disabled` produces silent no-op atlases.
5. Addressables delivery = all three scripts mandatory; sprites only from `Assets/`; atlases auto-generate in prebuild, never via menu items.

## Risks / owner notes
The failure modes are silent (atlas exists, packs nothing). Addressables path adds build-time content builds and async runtime loading complexity. Generated scripts may overwrite custom edits on "update" — flagged in the prompt.

## Category and tags
Category: mobile. Tags: unity, sprite-atlas, addressables, build-pipeline, editor-scripting, optimization.
