# imagegen

Source read: `C:\Users\a7med\.claude\skills\imagegen\SKILL.md` (19.5 KB; claude revision — the only holder listed). Companion files: `scripts/image_gen.py` (CLI fallback), `references/{prompting,sample-prompts,cli,image-api,codex-network}.md`, `agents/`, `assets/`.

## Summary
Raster image generation/editing with two modes: the built-in `image_gen` tool (default, no API key; Codex saves under `$CODEX_HOME/generated_images/`) and a fallback CLI (`scripts/image_gen.py`, needs `OPENAI_API_KEY`, default model `gpt-image-2`) with `generate`/`edit`/`generate-batch` subcommands. It defines a generate-vs-edit decision tree (reference images = generate, edit target = edit), a use-case taxonomy (photorealistic, product-mockup, ui-mockup, infographic, ads, logo, illustration, edit slugs like text-localization/identity-preserve/background-extraction), a labeled prompt schema (Use case → Constraints → Avoid), prompt augmentation rules (normalize specifics, never invent characters/brands), save-path policy (project assets must be moved into the workspace, versioned filenames, never overwrite), transparent-background handling, and detailed `gpt-image-2` size/quality constraints for CLI mode.

## When to use / when NOT
Use for bitmaps: photos, illustrations, textures, sprites, mockups, cutouts, infographics. Do NOT use for SVG/vector/icon-system work, simple shapes/diagrams better done in code, or when the user wants deterministic code-native output.

## Inputs, outputs, tools
- Inputs: prompt(s), optional reference/edit-target images (built-in needs them visible via `view_image` first), exact verbatim text, constraints/avoid lists.
- Outputs: PNG/etc. files; final saved paths must be reported; project-bound assets moved into the workspace.
- Tools: built-in `image_gen` + `view_image` (default); fallback `scripts/image_gen.py` + `OPENAI_API_KEY` + optional `pillow`; `n` is variants-of-one-prompt, distinct assets need distinct calls or `generate-batch`.

## 5 most important rules
1. Built-in `image_gen` is the default for everything including transparency; CLI fallback only on explicit user request (and it needs `OPENAI_API_KEY`).
2. Never silently downgrade `gpt-image-2` to `gpt-image-1.5`; never modify `scripts/image_gen.py`.
3. Label every input image's role (reference / edit target / style insert); for edits repeat invariants every iteration to prevent drift.
4. Never leave a project-referenced asset only under `$CODEX_HOME/generated_images/` — move it into the workspace and report the path; don't overwrite, use `-v2` siblings.
5. `gpt-image-2` constraints (CLI): no `background=transparent`, no `input_fidelity`, quality low/medium/high/auto, edges multiple of 16, ratio <= 3:1, 655,360–8,294,400 px.

## Risks / owner notes
CLI mode spends the owner's OpenAI API quota — confirm before use. Generated images must not fabricate testimonials, logos, or likenesses of real people without consent. Verify text rendering in outputs (exact-text prompts often drift).

## Category and tags
Category: media. Tags: image-generation, gpt-image, prompt-engineering, assets, transparency, batch.
