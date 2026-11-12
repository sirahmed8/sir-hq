# flutter-implement-json-serialization

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\flutter-implement-json-serialization\SKILL.md`
- SKILL.md size: 5650 chars

## What it does

Create model classes with `fromJson` and `toJson` methods using `dart:convert`. Use when manually mapping JSON keys to class properties for simple data structures.

## When to use (from skill text)

- Use this checklist to implement manual JSON serialization for a data model.
- Use this conditional workflow when retrieving and parsing JSON from a network request.

## Structure (headings inside SKILL.md)

- Serializing JSON Manually in Flutter
- Contents
- Core Guidelines
- Workflow: Implementing a Serializable Model
- Workflow: Fetching and Parsing JSON
- Examples
- High-Fidelity Model Implementation
- Synchronous Parsing (Small Payload)
- Background Parsing (Large Payload)
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Enforce Type Safety**: Always cast the `dynamic` result of `jsonDecode()` to the expected type, typically `Map<String, dynamic>` for objects or `List<dynamic>` for arrays.
2. - **Throw Exceptions on Failure**: When handling HTTP responses, throw an exception if the status code is not successful (e.g., not 200 OK or 201 Created). Do not return `null`.

## Files inside the skill

- (SKILL.md only)
