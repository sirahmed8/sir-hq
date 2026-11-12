# typst-pdf-maker (codex/cursor/kilo/windsurf/opencode copies)

## Summary
typst-pdf-maker produces publication-quality PDFs — academic papers, executive resumes, technical reports — using Typst, the fast Markdown-inspired LaTeX alternative. The pitch: ~100x faster than pdflatex/xelatex, no `\begin{}` boilerplate, first-class grids/margins/headers/typefaces/math. The SKILL.md gives a ready A4 document template (`#set page` with 2.5cm margins, header/footer via `locate(loc => ...)` for "Page X of Y", Liberation Sans 10.5pt body, styled headings), math syntax (`$...$` inline, display equations, `mat()` matrices), and the compile command `typst compile document.typ output.pdf`.

## When to use / when NOT
Use when the owner needs a polished PDF: reports, resumes, papers, printable documents where Markdown→PDF converters look cheap. Do NOT use for simple text exports (pandoc/markdown may suffice), for pixel-perfect magazine layout (InDesign territory), or when the typst binary is not installed — check first or install it.

## Inputs, outputs, tools
- Inputs: document content/structure (sections, data, equations) and desired styling.
- Outputs: a compiled `.pdf` next to the `.typ` source.
- Tools: the `typst` CLI (`typst compile`, also `typst watch`/`typst query` exist though undocumented here), fonts installed on the system. No templates folder or scripts ship with the skill — the template is inline in SKILL.md.

## 5 most important rules
1. Author in `.typ` files, compile with `typst compile input.typ output.pdf`.
2. Start from the provided A4 template: margins, running header, `locate`-based page counter footer, base font/size.
3. Use Typst's native syntax: `#set`/`#show` rules for styling, `#grid`/`#table` for layout, `$...$` for math — not LaTeX commands.
4. Page numbers need `counter(page).at(loc)`/`final(loc)` inside `locate(loc => ...)` in the footer.
5. Keep styling in `#set`/`#show` rules at the top; content stays clean markup below.

## Risks / things needing the owner
Thin skill: only 76 lines, one template, no bibliography/citation handling (Typst uses hayagriva `.bib`/`.yml` — not covered here, so academic papers needing citations require the agent to know or fetch Typst docs). Font availability on Windows varies; Liberation fonts may need installing. Compilation errors surface in CLI output — iterate locally. Nothing needs the owner.

## Category / tags
media · typst, pdf, documents, typesetting, reports

## Revisions
Five copies exist (codex, cursor, kilo, windsurf, opencode; no claude copy). Identical content. Best revision: the codex copy (used here).
