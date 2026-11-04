---
name: review-webapp
description: Framework-agnostic code review for fullstack webapps focused on Clean Architecture, Hexagonal (Ports and Adapters), Model-View-ViewModel (MVVM), MVC and Vertical Slice boundaries. Flags Fat Views, View-Aware ViewModels, DTO bleed, inward dependency violations and missing UI state handling. Returns GO or NO-GO with WHERE/EXPECTED/ACTUAL/FIX findings. Use for "review this webapp code", "review frontend architecture", "MVVM review" or /code-review:review-webapp. Not for REST contract review alone (code-review:review-api), data science review (code-review:review-data-science) or browser User Acceptance Testing.
---

# review-webapp

Principal Engineer review for fullstack webapp code. It is non-framework opinionated and checks Clean, Hexagonal and Model-View-ViewModel (MVVM) boundaries. It counters boundary bleed between Views and ViewModels, and between Domain models and Adapters. Every layer keeps one job, and Document Object Model (DOM) details stay in the View.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Analytical: map layers and import directions | Identify the architecture pattern and assign every changed file to its layer |
| 2 | Audit: check boundary invariants and state completeness | Test each layer against the pattern rules in the rubric |
| 3 | Adversarial: attack state races, rollbacks and test holes | Probe async race conditions, optimistic rollback paths and gate coverage holes |

Read [webapp-rubric.md](references/webapp-rubric.md) before step 1. It defines the pattern detection signals, layer rules and blocking anti-patterns.

## Steps

1. Read [webapp-rubric.md](references/webapp-rubric.md) and [classification-and-output.md](../code-review/references/classification-and-output.md).
2. Collect the changed webapp files from the caller or from `git diff`.
3. Identify the active architecture pattern using the detection table in the rubric. State whether the pattern is declared in repo docs or inferred from directories and imports.
4. Assign every changed file to one layer in the rubric. The four layers are View and ViewModel or Use Case, plus Domain and Adapter. If one file spans two layers, record a layer-mixing finding.
5. Check every import statement in the changed files. Verify that dependency arrows point inward toward the Domain or Model layer.
6. Audit the View layer:
   - zero direct network calls, database queries or storage writes
   - zero domain calculations or multi-step business branching
   - binds to presentation state and dispatches user intents only
7. Audit the ViewModel, Presenter or Use Case layer:
   - zero DOM node references, window globals or UI component imports
   - unit-testable headlessly without mounting a UI tree
   - maps raw API Data Transfer Objects (DTOs) into presentation state before exposing them to the View
   - one cohesive flow per ViewModel or Use Case, never a God object
8. Audit the Domain and Adapter layers:
   - Domain models hold invariants and business rules with zero framework or transport imports
   - Driven adapters translate between external APIs or databases and domain ports without business decisions
9. Audit async state and lifecycle handling:
   - every async view state models `loading` and `empty` alongside `error` and `success`
   - optimistic mutations define an explicit rollback on failure
   - timers, listeners and inflight requests clean up on unmount
10. Run the adversarial pass on state synchronization and validation boundaries. Flag client-only security checks that lack server enforcement.
11. Format every blocking defect with the `REVIEW FAIL (webapp)` block. Mark any defect with a passing test suite as a gate coverage hole.
12. Set `NO-GO` if any blocking finding or failed mechanical check exists. Otherwise set `GO`.
13. When invoked directly rather than through `code-review`, write `code-review-webapp-<slug>.md` in the repo folder using `writing:writing-standard`. Reply with the verdict and link.

## Output

Follow the report skeleton in [classification-and-output.md](../code-review/references/classification-and-output.md) and add a Layer Map table after Classification:

| File | Assigned layer | Imports checked | Status |
|---|---|---|---|
| `<path>` | `<View, ViewModel, UseCase, Domain or Adapter>` | `<inward or violation>` | `<PASS or FAIL>` |

## Limits

- Never enforces framework-specific syntax preferences when architectural boundaries hold.
- Never edits source files to fix a finding.
- Never grades visual styling or pixel alignment. That belongs to User Acceptance Testing (UAT).
- Never delivers the review as an HTML artifact.
