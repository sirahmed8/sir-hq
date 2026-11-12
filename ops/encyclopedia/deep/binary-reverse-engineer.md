# binary-reverse-engineer

**Source:** `C:\Users\a7med\.claude\skills\binary-reverse-engineer\SKILL.md` (claude copy preferred; codex holds the same content)
**Category:** security
**Tags:** reverse-engineering, decompilation, apk, binary, frida, ghidra, jadx, clean-room

## Summary
A security skill for decompiling native binaries, Android APKs, iOS IPAs and desktop executables, tracing their execution, extracting assets, and recreating closed features cleanly in a modern stack. It lists a toolkit (jadx and apktool for Android; radare2, Ghidra, objdump, strings, file and nm for PE/ELF/Mach-O; Frida and mitmproxy for dynamic tracing) and a structured deconstruction protocol: metadata and string triage, decompilation, then clean-room feature recreation.

## When to use / when not to
Use it when decompiling a binary or APK, tracing its execution, or recreating a closed feature in TypeScript, Python, Go or Rust. Do not use it to copy proprietary bytecode, and do not apply it outside the legal and ethical scope of software the user owns or is authorized to study; the skill is explicitly clean-room.

## Inputs, outputs, tools
Inputs: a target binary, APK or IPA. Outputs: decompiled logic, extracted endpoints, keys and assets, and a clean typed reimplementation. Tools: jadx, jadx-gui, apktool, radare2, Ghidra, objdump, strings, file, nm, Frida and mitmproxy. No MCP.

## Five most important rules
1. Start with string and metadata triage (`strings -a` or `rabin2 -z`) to find hardcoded endpoints, keys, package names and schemas.
2. Decompile with the tool matched to the platform: jadx for Android, the Radare2 or Ghidra decompiler for C/C++/Rust control flow.
3. Recreate features clean-room: synthesize clean, typed, modular implementations that match the observed algorithm; never copy raw proprietary bytecode.
4. Use dynamic tracing (Frida for runtime hooking, mitmproxy for network inspection) to recover payloads and protocols.
5. Follow the protocol order: static analysis and dynamic analysis both feed logic and network extraction, which then feed the clean recreation.

## Risks and owner actions
Reverse engineering third-party software can raise legal and ethical questions; the skill's clean-room rule is the guardrail. No secrets are involved.

## Revisions
The claude copy (1923 bytes, 2026-10-28) and the codex copy (1905 bytes, 2026-10-11) differ only in the description line; the claude copy has the better "when to use" description and is the source per the rule.
