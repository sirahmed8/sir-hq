# workflow

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\workflow\SKILL.md`
- SKILL.md size: 35138 chars

## What it does

Vercel Workflow SDK expert guidance.

## When to use (from skill text)

- - `start()`: Trigger a workflow
- | Error Type | Use When | Behavior |

## Structure (headings inside SKILL.md)

- *Critical*: Always use correct `workflow` documentation
- Official resources
- Quick reference
- Prefer step functions to avoid sandbox errors
- Workflow sandbox limitations
- WorkflowAgent: AI agents in Workflow 5
- Starting workflows & child workflows
- Run size & concurrency: know when to split
- Hooks: pause & resume with external events
- Single event
- Multiple events (iterable hooks)
- Resuming from API routes
- Error handling
- Serialization
- Custom class serialization
- Validating serde compliance
- Streaming
- Namespaced streams
- Debugging
- Check workflow endpoints are reachable
- Visual dashboard for runs
- CLI inspection (use --json for machine-readable output, --help for full usage)
- For Vercel-deployed projects, specify backend and project
- Open Vercel dashboard in browser for a specific run
- Cancel a running workflow
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Build-time warnings** -- The builder automatically warns when serde classes have Node.js built-in imports remaining in the workflow bundle.
- - **Vercel:** `https://vercel.com/<team-slug>/<project-slug>/workflows/runs/<run_id>?environment=<production|preview>`
- - `waitForHook(run, { token? })` / `waitForSleep(run)`: Wait for workflow to reach a pause point
- - `resumeHook(token, data)` / `resumeWebhook(token, request)`: Resume paused workflows

## Key rules (verbatim lines from SKILL.md)

1. 1. **Define serde methods INSIDE the class body** as static methods with computed property syntax (`static [WORKFLOW_SERIALIZE](...)`). The SWC plugin detects them by scanning the class. Do NOT assign them externally (e.g., `(MyClass as any)[WORKFLOW_SERIALIZE] = ...`) -- the compiler will not detec
2. 2. **Serde methods must return only devalue-compatible types** (plain objects, arrays, primitives, Date, Map, Set, Uint8Array, etc.). No functions, no class instances, no Node.js-specific objects.
3. 4. **Do NOT manually register classes.** The SWC plugin automatically generates registration code (an IIFE that sets `classId` and adds the class to the global registry). Manual calls to `registerSerializationClass()` are unnecessary and error-prone.
4. 5. **Do NOT use dynamic imports to work around sandbox restrictions.** If a class method needs Node.js APIs, the correct solution is `"use step"`, not `/* @vite-ignore */ import(...)`.
5. - `getWorkflowRef(name)` / `listWorkflowRefs()`: Look a workflow up in the test build's manifest when the test cannot import the function (never hand-write `workflow//...` ids)

## Files inside the skill

- `overlay.yaml`
