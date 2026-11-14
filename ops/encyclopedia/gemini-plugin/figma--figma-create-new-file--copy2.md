# figma-create-new-file

## Summary
A short deterministic procedure for creating a new Figma file (Design, FigJam, or Slides) via the `create_new_file` MCP tool: resolve the `planKey` (from the user or `whoami`), infer `editorType` from the requested file type, call the tool with `fileName`/`planKey`/`editorType` (optional `projectId`), then use the returned `file_key` for all subsequent calls. Includes one Slides-specific gotcha: a new Slides file has an empty grid, so `createSlide()` must be called before reading slide properties.

## When to use / when NOT
Use whenever a Figma MCP task needs a destination file that does not exist yet. Do NOT use to edit existing files (use the file key directly), and do not guess `editorType` — ask the user if the file type is unclear.

## Inputs, outputs, tools
- Inputs: requested file type (design/figjam/slides), optional file name, optional project, user's selected plan.
- Outputs: a new file plus its `file_key` for chaining into `use_figma` and other tools.
- Tools: Figma MCP `whoami` (plan discovery) and `create_new_file`; later `figma.getSlideGrid()`/`figma.createSlide()` for Slides.

## 5 most important rules
1. Resolve planKey first: user-provided, else `whoami`; zero plans = cannot proceed, multiple = ask the user to pick.
2. All three of `fileName`, `planKey`, `editorType` are required; pick a concise name if none given.
3. Infer `editorType` from the requested file type via the tool's enum; ask when unclear.
4. Use the returned `file_key` for every subsequent tool call — never reconstruct keys.
5. Slides files start with zero slides: call `figma.createSlide()` (first call creates row 0) before reading theme tokens or slide properties.

## Risks / owner needs
Needs an authenticated Figma MCP session and a plan seat that allows file creation; creating files consumes the team's plan. Low risk otherwise.

## Category and tags
Category: design. Tags: figma, mcp, file-creation, slides, figjam.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
