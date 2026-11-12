# imagegen

- Tool: `claude`
- Category: design
- Source: `C:\Users\a7med\.claude\skills\imagegen\SKILL.md`
- SKILL.md size: 19476 chars

## What it does

Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

## When to use (from skill text)

- - **Fallback CLI mode:** `scripts/image_gen.py` CLI. Use when the user explicitly asks for or confirms the CLI/API/model path. Requires `OPENAI_API_KEY`.

## Structure (headings inside SKILL.md)

- Image Generation Skill
- Top-level modes and rules
- When to use
- When not to use
- Decision tree
- Workflow
- Transparent image requests
- Prompt augmentation
- Specificity policy
- Use-case taxonomy (exact slugs)
- Shared prompt schema
- Examples
- Generation example (hero image)
- Edit example (invariants)
- Prompting best practices
- Guidance by asset type
- gpt-image-2 guidance for CLI fallback
- Fallback CLI mode only
- Temp and output conventions
- Dependencies
- Environment
- Script-mode notes
- Reference map
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Generate a new image (concept art, product shot, cover, website hero)
- - Produce many assets or variants for one task
- - Creating simple shapes, diagrams, wireframes, or icons that are better produced directly in SVG, HTML/CSS, or canvas
- - For edits, preserve invariants aggressively and save non-destructively by default.

## Key rules (verbatim lines from SKILL.md)

1. - **Default built-in tool mode (preferred):** built-in `image_gen` tool for image generation, editing, and transparent-image requests. Does not require `OPENAI_API_KEY`.
2. - **Fallback CLI mode:** `scripts/image_gen.py` CLI. Use when the user explicitly asks for or confirms the CLI/API/model path. Requires `OPENAI_API_KEY`.
3. - Do not switch to CLI fallback for ordinary quality, size, or file-path control.
4. - Never silently switch from built-in `image_gen` or CLI `gpt-image-2` to CLI `gpt-image-1.5`; ask the user first unless they explicitly requested `gpt-image-1.5`.
5. - If the built-in tool fails or is unavailable, tell the user the CLI fallback exists and that it requires `OPENAI_API_KEY`. Proceed only if the user explicitly asks for that fallback.

## Files inside the skill

- `agents/openai.yaml`
- `assets/imagegen-small.svg`
- `assets/imagegen.png`
- `LICENSE.txt` — "A"
- `references/cli.md` — "CLI reference (`scripts/image_gen.py`)"
- `references/codex-network.md` — "Codex network approvals / sandbox notes"
- `references/image-api.md` — "Image API quick reference"
- `references/prompting.md` — "Prompting best practices"
- `references/sample-prompts.md` — "Sample prompts (copy/paste)"
- `scripts/image_gen.py`
- `scripts/remove_chroma_key.py`
