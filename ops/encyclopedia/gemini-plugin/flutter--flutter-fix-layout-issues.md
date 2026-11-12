# flutter-fix-layout-issues

## Summary
Diagnostic + fix playbook for Flutter constraint violations, built on the layout law "constraints go down, sizes go up, parent sets position". Catalogs error signatures and their causes: "Vertical viewport was given unbounded height" (scrollable inside unconstrained Column), "InputDecorator cannot have unbounded width" (TextField inside unconstrained Row), "RenderFlex overflowed" (child bigger than parent allocation, yellow/black stripes), "Incorrect use of ParentData widget" (Expanded outside Flex, Positioned outside Stack), and "RenderBox was not laid out" (cascading side-effect — ignore it, find the primary violation higher in the trace). Workflow: capture the debug-mode exception → identify primary error → apply the conditional fix → hot reload → visually verify stripes/error screen gone → repeat if new errors surface.

## When to use / when NOT
Use when hitting RenderFlex overflow, unbounded height/width, or ParentData errors. Not for designing adaptive layouts proactively (flutter-build-responsive-layout) or non-layout bugs.

## Inputs, outputs, tools
- Inputs: debug console exception text, offending widget tree.
- Outputs: minimal constraint fixes (Expanded/Flexible/SizedBox wrappers, ParentData reparenting).
- Tools: debug-mode error messages, hot reload, Flutter inspector implied.

## 5 most important rules
1. Fix the PRIMARY constraint violation; "RenderBox was not laid out" is always a cascade — scroll past it to the real error.
2. Unbounded height on ListView/GridView inside Column → wrap in Expanded (remaining space) or SizedBox (absolute height).
3. Unbounded width on TextField/TextFormField inside Row → wrap in Expanded or Flexible.
4. RenderFlex overflow → constrain the child with Expanded (force fit) or Flexible (allow smaller).
5. ParentData widgets must be direct children of their required ancestor: Expanded/Flexible only inside Row/Column/Flex, Positioned only inside Stack — otherwise restructure, don't wrap.

## Risks / owner needs
Minimal — local code fixes only. The real risk is fixing the symptom (e.g. hardcoded heights) instead of the constraint negotiation; Expanded/SizedBox choice should reflect intent.

## Category and tags
Category: mobile. Tags: flutter, layout, debugging, constraints, overflow, renderflex.

## Revisions
Single gemini-plugin flutter copy; no competing revisions.
