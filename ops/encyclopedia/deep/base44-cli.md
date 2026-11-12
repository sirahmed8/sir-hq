# base44-cli

Source read: `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44--base44-cli.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A command-line utility skill for Base44 encoding and decoding. Base44 is a binary-to-text encoding similar to Base64 but uses 44 printable ASCII characters, providing more compact representation for binary data. The skill supports file encoding/decoding, stdin/stdout operations, and batch mode for processing multiple files.

## When to use / when NOT
Use when you need a more compact encoding than Base64 for embedding binary data in text-based formats (JSON, XML, YAML). Do NOT use Base44 when maximum compatibility is required — some older systems may not support the 44-character alphabet, and Base64 is more universally supported. Do NOT skip the output format specification; the skill can output to stdout, a file, or base64-compatible format, and the default behavior may not match your needs.

## Inputs, outputs, tools
- Inputs: data string or file path, operation (encode, decode), output target (stdout, file, variable), batch mode flag.
- Outputs: encoded text string or decoded binary data, operation confirmation, error message for invalid input.
- Tools: base44 CLI binary, standard input/output, file system. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always specify the output target** — the skill defaults to printing to stdout; redirect to a file or variable if you need to capture the result.
2. **Use batch mode for multiple files** — the skill can process an entire directory of files in a single command; this is more efficient than running the skill once per file.
3. **Verify round-trip encoding** — encode a value, then decode it, and confirm the result matches the original; this ensures the skill is working correctly with your data.
4. **Be aware of character set limitations** — the 44-character alphabet excludes `+`, `/`, and `=` (which are in Base64); if your data contains these characters, they will be encoded differently.
5. **Check file encoding before running** — the skill expects UTF-8 encoded files; non-UTF-8 files may produce unexpected results or errors.

## Risks / owner notes
The most common issue is unexpected character encoding in the output when the input contains characters outside the 44-character alphabet. The owner should test with sample data before relying on the skill for critical workflows. Base44 is not as widely supported as Base64; ensure your downstream systems support the 44-character alphabet before adopting this skill.

## Category / tags
utility · encoding, base44, cli, text-processing, data-formats

## Revisions
The gemini-plugin copy is the only revision available; no codex, kilo, or cursor copies exist. This is the canonical source for this skill.