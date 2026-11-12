# flutter-apply-architecture-best-practices

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\flutter-apply-architecture-best-practices\SKILL.md`
- SKILL.md size: 6263 chars

## What it does

Architects a Flutter application using the recommended layered approach (UI, Logic, Data). Use when structuring a new project or refactoring for scalability.

## Structure (headings inside SKILL.md)

- Architecting Flutter Applications
- Contents
- Architectural Layers
- UI Layer (Presentation)
- Data Layer
- Logic Layer (Domain - Optional)
- Project Structure
- Workflow: Implementing a New Feature
- Task Progress
- Examples
- Data Layer: Service and Repository
- UI Layer: ViewModel and View
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. *   **Views:** Write reusable, lean widgets. Restrict logic in Views to UI-specific operations (e.g., animations, layout constraints, simple routing). Pass all required data from the ViewModel.
2. *   **Use Cases:** Implement this layer only if the application contains complex business logic that clutters the ViewModel, or if logic must be reused across multiple ViewModels. Extract this logic into dedicated Use Case (interactor) classes that sit between ViewModels and Repositories.
3. - *If the feature requires complex data transformation or cross-repository logic:* Create a Use Case class.
4. - [ ] **Step 5: Implement the ViewModel.** Create the ViewModel extending `ChangeNotifier`. Inject required Repositories/Use Cases. Expose immutable state and command methods.

## Files inside the skill

- (SKILL.md only)
