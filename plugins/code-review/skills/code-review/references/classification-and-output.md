# Classification, gate authority and output format

Reference rules for `code-review` and its three specialist skills.

## Surface classification signals

| Kind | File and path signals | Import and symbol signals | Dispatched skill |
|---|---|---|---|
| Fullstack webapp | `app/`, `pages/`, `views/`, `components/`, `viewmodels/`, `stores/`, `hooks/`, `.tsx`, `.vue`, `.svelte` | Document Object Model (DOM) APIs, component state, view bindings, client routers, UI stores | `review-webapp` |
| API | `routes/`, `controllers/`, `handlers/`, `use-cases/`, `domain/`, `ports/`, `repositories/`, `openapi.yaml`, `.proto` | HTTP verbs, status codes, middleware, request schemas, database ports, Data Transfer Objects (DTOs) | `review-api` |
| Data science: Insights | `notebooks/`, `eda/`, `analysis/`, `reports/`, `.ipynb`, `.qmd`, SQL analysis scripts | `groupby`, `merge`, `join`, plotting libraries, hypothesis tests, summary tables | `review-data-science` (Mode A: Insights) |
| Data science: Modeling | `models/`, `features/`, `training/`, `inference/`, `pipelines/`, `evaluation/` | `train_test_split`, `Pipeline`, `fit`, `transform`, `predict`, `cross_val_score`, model persistence | `review-data-science` (Mode B: Modeling) |

If one file mixes UI rendering with HTTP persistence, classify it under both `webapp` and `api`. If one notebook mixes exploratory charts with model fitting, classify it under both Data Science modes and flag it.

## One-way gate authority

Derived from `gwrk` specification `028-review-finding-liveness`.

| Mechanical check | Review finding | Verdict and action |
|---|---|---|
| Passes | Blocking finding | `NO-GO` and record a gate coverage hole |
| Passes | None | `GO` |
| Fails | Blocking finding or none | `NO-GO` and cite the failing check |
| None exists | Blocking finding | `NO-GO` |
| None exists | None | `GO` and note the missing test coverage |

## Structured finding block

Every blocking finding uses this exact block from `gwrk` Principal Engineer reviews:

```markdown
REVIEW FAIL (<surface>): <rule-name>
  WHERE: <file_path>:<line_range>
  EXPECTED: <architectural rule, contract or invariant required>
  ACTUAL: <what the code does at that location>
  FIX: <concrete change required to restore the boundary or invariant>
  GATE: <test file or gate script that failed, or "MISSING (coverage hole)">
```

## Report skeleton

```markdown
# Code review: <target name>

**Verdict: <GO or NO-GO>.** <Primary finding or pass summary in one sentence.> Blocked: <what cannot ship, or "none">. Owner: <author or "unassigned">.

## Classification and scope

| Surface | Detected pattern or mode | Files | Specialist skill |
|---|---|---|---|
| <webapp, api or data-science> | <Clean, Hexagonal, MVVM, REST, Insights or Modeling> | <count> | <skill name> |

## Mechanical baseline

| Check | Command | Result | Notes |
|---|---|---|---|
| Build | `<cmd or "not run">` | <PASS, FAIL or SKIP> | <exit code or reason> |
| Lint | `<cmd or "not run">` | <PASS, FAIL or SKIP> | <error count> |
| Tests | `<cmd or "not run">` | <PASS, FAIL or SKIP> | <suite summary> |

## Blocking findings

<One REVIEW FAIL block per blocking defect, highest blast radius first. Write "None." on GO.>

## Gate coverage holes

| Finding | File | Why the test suite missed it | Required test |
|---|---|---|---|
| <rule-name> | `<path:line>` | <missing assertion or over-mocked boundary> | <test to add> |

## Non-blocking notes

1. `<path:line>`: <one-sentence structural or clarity improvement>.
```
