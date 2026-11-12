# dart-build-cli-app (Flutter plugin)

## Summary
Comprehensive architecture guide for Dart CLI applications: thin `bin/` entrypoints over `lib/src/` logic, POSIX exit codes via `exitCode`/CommandRunner (never `exit(N)`), stdout= data / stderr= diagnostics with usage-on-error rules, terminal capability detection (`NO_COLOR`, `hasTerminal`, `supportsAnsiEscapes`), `package:args` parsing with typed accessors, no `Chain.capture` (VM preserves async stacks), `cli_util` for SDK discovery under AOT, Windows-safe signal/terminal teardown, two-layer testing (in-memory unit + test_process integration), and modern `dart run`/`dart install`/`dart compile exe` distribution.

## When to use / when NOT
Use when building CLI tools, console utilities, scripts, or compiling native CLI binaries — argument parsing, exit codes, subprocess spawning. Do NOT use for Flutter UI, web apps, or standalone HTTP servers.

## Inputs, outputs, tools
- Inputs: the CLI's commands/options and output contract.
- Outputs: packaged CLI (`executables:` in pubspec, `dart install` AOT binary).
- Tools: `package:args` (ArgParser/CommandRunner, `package:build_cli` for complex options), `package:io` ExitCode, `package:stack_trace`, `package:cli_util`, `package:test_process`/`test_descriptor`, `package:build_version`; examples/ + references/ (aot_sdk_discovery, signals_and_terminal).

## 5 most important rules
1. Never call `exit(N)` — it kills the process before VM-service pause, coverage collection, and buffer flush; set `exitCode` or return from CommandRunner.
2. `bin/` is a trampoline only; all logic in `lib/src/` so it's unit-testable via package: imports.
3. stdout carries data/help-on-request only; errors+usage go to stderr with exit 64 (EX_USAGE).
4. Spawn Dart subprocesses via `cli_util.dartExecutable` — `Platform.resolvedExecutable` points at the app binary under AOT and causes recursive self-invocation.
5. Guard Windows (`sigterm` unsupported), restore echo/cursor state in finally, close servers on signals; unit-test logic in-memory, e2e via TestProcess.

## Risks / things needing the owner
AOT/native compilation and `dart install` affect the user's global toolchain. ANSI/terminal handling bugs can leave users' terminals broken — teardown paths matter.

## Category / tags
build · dart, cli, devtools, packaging, best-practices

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-build-cli-app\SKILL.md` (with examples/, references/). Only gemini-plugin holds it.
