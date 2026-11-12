# xcode_project_setup

- Tool: `codex`
- Category: automation
- Source: `C:\Users\a7med\.codex\skills\xcode_project_setup\SKILL.md`
- SKILL.md size: 5949 chars

## What it does

Modify Xcode projects (.pbxproj) safely to add Swift Packages and link native dependencies.

## When to use (from skill text)

- Because this skill relies entirely on a native Swift script, you must verify the

## Structure (headings inside SKILL.md)

- Xcode Project Setup
- ⛔️ CRITICAL RULES & ENVIRONMENT CHECKS
- 1. The Anti-Ruby Mandate
- 2. Modern Xcode Folder Synchronization
- 3. Allowed Scripting Languages
- 4. Toolchain Verification
- 5. Mandatory Linker Flags for Static Frameworks (Firebase)
- Empty Directory Workflow
- Standard Xcode Workflow
- **CRITICAL: Always Use Latest SDK Version**
- Understanding the Script's Actions
- Usage
- Example 1: Generic Package (e.g., Alamofire)
- Example 2: Firebase (Requires Plist)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Run `swift --version` before proceeding.
2. - If the Swift command is not found, you must stop and recommend the user

## Files inside the skill

- `scripts/xcode_spm_setup/Package.resolved`
- `scripts/xcode_spm_setup/Package.swift`
- `scripts/xcode_spm_setup/Sources/main.swift`
