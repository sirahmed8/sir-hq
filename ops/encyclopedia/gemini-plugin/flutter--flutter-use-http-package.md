# flutter-use-http-package

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\flutter-use-http-package\SKILL.md`
- SKILL.md size: 6456 chars

## What it does

Use the `http` package to execute GET, POST, PUT, or DELETE requests. Use when you need to fetch from or send data to a REST API.

## When to use (from skill text)

- *   **Error Handling:** Throw explicit exceptions for non-success status codes. Never return `null` on failure, as this prevents `FutureBuilder` from triggering its error state and causes infinite loading indicators.
- - [ ] 7. **Feedback Loop:** Run the app -> trigger the network request -> review console for unhandled exceptions -> fix parsing or permission errors.

## Structure (headings inside SKILL.md)

- Implementing Flutter Networking
- Contents
- Configuration & Permissions
- Request Execution & Response Handling
- Background Parsing
- Workflow: Executing Network Operations
- Examples
- High-Fidelity Implementation: Fetching and Parsing in the Background
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - [Configuration & Permissions](#configuration--permissions)
- 3. Configure Android permissions by adding the Internet permission to `android/app/src/main/AndroidManifest.xml`:
- *   **Headers:** Inject authorization and content-type headers via the `headers` parameter map. Use `HttpHeaders.authorizationHeader` for auth tokens.
- *   **Status Validation:** Evaluate `response.statusCode`. Treat `200 OK` (GET/PUT/DELETE) and `201 CREATED` (POST) as success.

## Key rules (verbatim lines from SKILL.md)

1. *   **URIs:** Always parse URL strings using `Uri.parse('your_url')`.
2. *   **Error Handling:** Throw explicit exceptions for non-success status codes. Never return `null` on failure, as this prevents `FutureBuilder` from triggering its error state and causes infinite loading indicators.

## Files inside the skill

- (SKILL.md only)
