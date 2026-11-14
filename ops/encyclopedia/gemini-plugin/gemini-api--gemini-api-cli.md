# gemini-api-cli

- Tool: `gemini-plugin` (plugin: `gemini-api`)
- Category: media
- Source: `C:\Users\a7med\.gemini\config\plugins\gemini-api\skills\gemini-api-cli\SKILL.md`
- SKILL.md size: 12730 chars

## What it does

Call the Gemini API from the shell with gemini-api. Use for media generation (images, TTS, music, video), file and YouTube analysis, audio/video transcription, Deep Research, and sandboxed agents.

## When to use (from skill text)

- | `environments` | `create`, `list`, `get`, `delete`, `files` (`list`, `upload`, `download`), `connect`, `poll`, `serve` | Remote sandboxes and workspace snapshots (`credentials`, `webhooks`, `triggers` for agent infra) |

## Structure (headings inside SKILL.md)

- CLI vs SDK
- Install and auth
- macOS / Linux (set GEMINI_VERSION=<tag> to pin a release)
- Command structure
- Global flags
- Output
- Input
- Media, analysis, and transcription
- Managed agents and sandboxes
- Multi-turn and structured output
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server

## Risks / cautions found in text

- - Active auth check: `gemini-api whoami` (add `-o json` for JSON) prints masked credentials and the winning source.

## Key rules (verbatim lines from SKILL.md)

1. - `-f` / `--file` reads prompt text from a file on `tts` and `music`. **Piped text needs `--stdin`:** when piping plain text into `generate`, `image`, `music`, or `video`, pass `--stdin` or piped input gets parsed as a JSON `--body`; `analyze` and `tts` ignore piped stdin unless `--stdin` is set (`a
2. - **Don't dump `--schema` raw:** it prints ~92 KB of minified JSON and exits before `--jq` runs. Pipe it to `jq`:

## Files inside the skill

- (SKILL.md only)
