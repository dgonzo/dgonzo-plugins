---
name: review-api
description: Language-agnostic API code review focused on Clean Architecture, Hexagonal (Ports and Adapters), REST resource design and Domain-Driven Design bounded contexts. Checks inward dependencies, port isolation, boundary schema validation, error envelopes, idempotency and route test coverage. Returns GO or NO-GO with WHERE/EXPECTED/ACTUAL/FIX findings. Use for "review this API", "REST review", "hexagonal API review", "backend code review" or /code-review:review-api. Not for UI ViewModel review (code-review:review-webapp) or data science pipelines (code-review:review-data-science).
---

# review-api

Principal Engineer review for API code. It is non-language opinionated and enforces Clean Architecture, Hexagonal Architecture and REST resource rules. It counters transport and database leakage into core domain logic. It also stops unvalidated wire contracts from shipping.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Analytical: map bounded contexts, ports and dependency arrows | Assign every changed file to Driving Adapter, Use Case, Domain or Driven Adapter |
| 2 | Audit: check Hexagonal isolation and the six REST rules | Test each boundary against the API rubric |
| 3 | Stress-Testing: probe concurrency, retries, transactions and queries | Attack idempotency, transaction scope, N+1 queries and route test coverage |

Read [api-rubric.md](references/api-rubric.md) before step 1. It carries the layer map, the six REST governance rules from `gwrk` and the blocking anti-patterns.

## Steps

1. Read [api-rubric.md](references/api-rubric.md) and [classification-and-output.md](../code-review/references/classification-and-output.md).
2. Collect the changed API files from the caller or from `git diff`.
3. Identify the architecture pattern from repo docs or directory structure. Map each changed file to Driving Adapter or Use Case, or to Domain Core or Driven Adapter.
4. Check all imports in the changed files. Verify that dependencies point inward toward the Domain Core.
5. Audit the Domain Core and Application Use Cases:
   - Domain entities and value objects have zero HTTP, web framework or Object-Relational Mapping (ORM) imports
   - entities enforce their own domain invariants instead of acting as anemic data bags
   - each Use Case executes one business action and talks to external systems only through Outbound Ports
6. Audit the Driving Adapters (controllers, handlers and routers) against the six REST rules in the rubric:
   - routes respect Domain-Driven Design (DDD) bounded contexts without cross-domain reach-in
   - each resource has one owning route handler file with no scattered duplicate routes
   - URLs name resource nouns, never action verbs or user journeys
   - route files stay focused and under 400 lines
   - every route validates request and response Data Transfer Objects (DTOs) with explicit schemas at the boundary
   - all error responses map domain exceptions into one standard error envelope with zero SQL or stack-trace leaks
7. Audit the Driven Adapters against the rubric:
   - repositories, gateways and message publishers implement Outbound Ports defined inside the core
   - adapters map persistence rows to domain models and never leak ORM entities across the port
8. Run the stress-testing pass on runtime behavior:
   - state-changing endpoints handle retries safely or enforce idempotency keys
   - database transactions wrap one aggregate without holding locks across external network calls
   - list endpoints enforce pagination bounds and avoid N+1 query loops
   - authorization checks run in the Use Case or policy layer before any state mutation
9. Verify route test coverage across all four status classes in the rubric. Every route needs tests for success (`2xx`) and validation (`400`), plus auth (`401` or `403`) and missing resources (`404`).
10. Format every blocking defect with the `REVIEW FAIL (api)` block. Mark any defect where tests passed as a gate coverage hole.
11. Return `NO-GO` if any blocking finding or failed mechanical check exists. Otherwise return `GO`.
12. When invoked directly rather than through `code-review`, write `code-review-api-<slug>.md` in the repo folder using `writing:writing-standard`. Reply with the verdict and link.

## Output

Follow the report skeleton in [classification-and-output.md](../code-review/references/classification-and-output.md) and include a Port and Boundary table:

| File | Layer or port | Bounded context | Status |
|---|---|---|---|
| `<path>` | `<Driving, UseCase, Domain, OutboundPort or Driven>` | `<context name>` | `<PASS or FAIL>` |

## Limits

- Never enforces language-specific framework religion when port boundaries and wire contracts hold.
- Never edits source files to fix a finding.
- Never approves a route that serializes raw database rows or omits response schema validation.
- Never delivers the review as an HTML artifact.
