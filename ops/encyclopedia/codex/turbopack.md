# turbopack

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\turbopack\SKILL.md`
- SKILL.md size: 9605 chars

## What it does

Turbopack expert guidance. Use when configuring the Next.js bundler, optimizing HMR, debugging build issues, or understanding the Turbopack vs Webpack differences.

## Structure (headings inside SKILL.md)

- Turbopack
- Key Features
- Configuration (Next.js 16)
- CSS and CSS Modules Handling
- Global CSS
- CSS Modules
- PostCSS
- Sass / SCSS
- Common CSS pitfalls
- Tree Shaking
- Diagnosing large bundles
- Custom Loader Migration from Webpack
- Configuring custom rules (loader replacement)
- When migration isn't possible
- Production Build Diagnostics
- Build failing with Turbopack
- Build output too large
- Comparing webpack vs Turbopack output
- Turbopack build (default in Next.js 16)
- Webpack build
- Performance Profiling
- HMR profiling
- Build profiling
- Memory usage
- Turbopack vs Webpack
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Production**: Turbopack handles the production build (replaces webpack in Next.js 16)

## Key rules (verbatim lines from SKILL.md)

1. - **CSS ordering differs from webpack**: Turbopack may load CSS chunks in a different order. Avoid relying on source-order specificity across files — use more specific selectors or CSS Modules.
2. - **CSS-in-JS libraries**: `styled-components` and `emotion` work but require their SWC plugins configured under `compiler` in next.config.
3. - **ES module exports**: Only used exports are included — write `export` on each function/constant rather than barrel `export *`
4. 1. **Missing loader equivalent**: Some webpack loaders don't have Turbopack equivalents yet. Check Turbopack docs for supported transformations.
5. 3. **Custom aliases**: Use `turbopack.resolveAlias` instead of `webpack.resolve.alias`.

## Files inside the skill

- (SKILL.md only)
