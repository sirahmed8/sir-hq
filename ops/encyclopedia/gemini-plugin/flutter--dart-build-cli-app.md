# dart-build-cli-app

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-build-cli-app\SKILL.md`
- SKILL.md size: 13826 chars

## What it does

>- Architectural patterns, entrypoint structure, exit codes, stream routing, and subprocess spawning for Dart command-line interface (CLI) applications. Use when building CLI tools, console utilities, scripts, argument parsing with `package:args` (ArgParser or CommandRunner), handling exit codes, configuring executables in pubspec.yaml, spawning Dart subprocesses, or compiling native CLI binaries. Don't use for Flutter UI widgets, web applications, or standalone HTTP backend servers.

## Structure (headings inside SKILL.md)

- Building Dart CLI Applications
- Contents
- 1. Core Architecture & Process Lifecycle
- Avoid Destructive Exits (`exit(N)`)
- The Thin Entrypoint Pattern (`bin/` vs. `lib/src/`)
- 2. Output, Diagnostics & Formatting
- 3. Project Configuration & Packaging
- Scaffolding & Pubspec Executable Mapping (`executables:`)
- Single-Source Versioning (`package:build_version`)
- Caching Conventions
- 4. Argument Parsing & Command Routing
- 5. Native Async & Modern Stack Traces
- 6. Subprocess Spawning & AOT Resilience
- 7. Signal Handling & Terminal Teardown
- 8. Testing CLI Applications
- 9. Modern Compilation & Distribution
- 10. Workflows & Audit Checklist
- Implementation Workflow
- References & Examples
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- * **Buffer Truncation**: `stdout` and `stderr` are buffered asynchronous `IOSink` streams. `exit()` drops unflushed bytes.
- * **Data vs. Diagnostics**: Write intended program results and machine-readable data exclusively to `stdout`. Write warnings, error messages, and debug logs exclusively to `stderr`.
- - [ ] Direct errors, warnings, and usage on parse failure to `stderr`.

## Key rules (verbatim lines from SKILL.md)

1. * **Debugger Disconnect**: When launched with `--pause-isolates-on-exit`, the VM Service pauses isolates before shutdown to allow IDE inspection. `exit()` terminates the OS process before the VM Service can pause or inspect state.
2. * **Coverage Loss**: `package:coverage` queries execution lines over VM Service RPCs during the paused-on-exit state. `exit()` destroys the process before RPC extraction, yielding 0% coverage.
3. * **No `print()` in Error Handlers**: `print()` routes to `stdout`. Use `stderr.writeln()` for all failure notifications. For standard output, prefer `stdout.writeln()` over `print()` to comply with the [`avoid_print`](https://dart.dev/tools/linter-rules/avoid_print) lint rule (unless `analysis_opti
4. * **Terminal Capability Detection & `NO_COLOR`**: Verify `stdout.hasTerminal`, `stdout.supportsAnsiEscapes`, and `!Platform.environment.containsKey('NO_COLOR')` before emitting ANSI color or cursor escape codes:
5. * **Type-Safe Accessors**: Use `results.flag('name')`, `results.option('name')`, and `results.multiOption('name')` (available in `package:args` 2.5+) instead of map indexing `operator []` to eliminate manual type casts (`as bool`, `as String?`).

## Files inside the skill

- `examples/multi_command_runner.dart`
- `examples/single_command_tool.dart`
- `references/aot_sdk_discovery.md` — "Dart SDK Discovery and Subprocess Spawning in AOT & JIT"
- `references/signals_and_terminal.md` — "Signal Handling, Terminal Teardown, and Stream Resilience"
