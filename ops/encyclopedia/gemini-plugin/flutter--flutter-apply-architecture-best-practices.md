# flutter-apply-architecture-best-practices

## Summary
Architecture blueprint for Flutter apps enforcing strict separation of concerns in three layers. UI layer = MVVM: lean Views (UI-only logic) + ViewModels extending ChangeNotifier exposing immutable state, repositories constructor-injected. Data layer = Repository pattern: stateless Services wrapping external APIs (HTTP, DB, plugins) return raw models/Result; Repositories are the single source of truth — consume services, transform API models to clean Domain Models, handle caching/offline/retry. Logic/Domain layer is OPTIONAL — Use Case classes only when business logic is complex or shared across ViewModels. Prescribes a hybrid folder layout (data/, domain/, ui/core + ui/features/<feature>/{view_models,views}) and an 8-step feature workflow: domain models (freezed/built_value) → services → repositories → conditional use cases → viewmodel → view (ListenableBuilder/AnimatedBuilder) → DI registration → run ViewModel/Repository unit tests.

## When to use / when NOT
Use when structuring a new project or refactoring for scalability. Do NOT apply dogmatically to tiny apps — the optional Domain layer and DI ceremony are skipped for simple CRUD (the skill itself says skip use cases for simple CRUD).

## Inputs, outputs, tools
- Inputs: feature requirements, existing codebase structure.
- Outputs: lib/ folder tree, model/service/repository/viewmodel/view classes, DI registrations, tests.
- Tools: ChangeNotifier, ListenableBuilder, freezed/built_value, provider/get_it, Result wrappers.

## 5 most important rules
1. Never mix UI rendering with business logic or data fetching — the layer boundary is the whole point.
2. Views stay dumb: only animations/layout/simple routing; all data arrives from the ViewModel; Views listen via ListenableBuilder/AnimatedBuilder, never setState business state.
3. Repositories are the single source of truth: they own caching, offline sync, retry, and API→Domain model transformation; ViewModels never see raw API models.
4. ViewModels expose immutable state snapshots + command methods and notifyListeners() on transitions (including loading flags in finally).
5. Hybrid structure: group UI by feature, group data/domain by type; register every new Service/Repository/ViewModel in DI, then run unit tests on VM+Repo before calling the feature done.

## Risks / owner needs
Architecture choice is a long-term commitment — retrofitting layers onto an existing anemic codebase is a refactor project, not a skill invocation. freezed/built_value add codegen steps (build_runner) the team must keep in the loop.

## Category and tags
Category: mobile. Tags: flutter, architecture, mvvm, repository-pattern, clean-architecture, dart.

## Revisions
Single gemini-plugin flutter copy; no competing revisions.
