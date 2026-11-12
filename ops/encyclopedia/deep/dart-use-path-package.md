# dart-use-path-package (Flutter plugin)

## Summary
Rules for cross-platform path handling in Dart: never treat paths as raw strings (`.split('/')`, `'$dir/$file'`, `.endsWith('.ext')` all break on Windows backslashes); use `package:path` (`p.join`, `p.split`, `p.extension`, `p.isWithin`, `p.normalize`/`p.canonicalize`, `p.toUri`/`p.fromUri`) and `package:file` for mockable filesystems. Includes nuance: 2-arg boundary joins on POSIX-only tools for greppability, strip `:line-col` suffixes before path ops, and list-pattern matching over `.first`/`.skip(1)`.

## When to use / when NOT
Use whenever joining, splitting, matching, or converting file paths or extensions. Do NOT use for HTTP URIs, DB strings, or non-path text processing.

## Inputs, outputs, tools
- Inputs: path strings/URIs in Dart code.
- Outputs: OS-correct path manipulation.
- Tools: `package:path` (`p.*`), `package:file` for injectable filesystems; examples/ dir.

## 5 most important rules
1. `p.join` for all joins — string interpolation injects `/` and `//` on Windows.
2. `p.split(path)` before segment inspection; list patterns (`['foo', ...rest]`) beat `.first`/`.skip(1)` (empty-list safe, binds tails).
3. `p.extension()` not `.endsWith()` — suffix match false-positives on `foo.wasm/` directories.
4. Strip `:line`/`:line-col` location suffixes via regex BEFORE path functions; `Uri.parse` misreads `C:` as a scheme on Windows — use `p.toUri`/`p.fromUri`.
5. `p.canonicalize` (not just normalize) when comparing physical identity across symlinks/case-insensitive FS.

## Risks / things needing the owner
Windows/POSIX divergence is the whole point — code "working on macOS" can silently corrupt paths on Windows. Review path code for raw-string ops in cross-platform packages.

## Category / tags
build · dart, paths, cross-platform, file-io

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-use-path-package\SKILL.md` (with examples/). Only gemini-plugin holds it.
