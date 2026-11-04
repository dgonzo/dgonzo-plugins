---
name: review-data-science
description: Opinionated code review for data science that separates Insights code (notebooks, exploratory analysis, queries, metrics and statistical claims) from Modeling and Predictions code (feature pipelines, training, validation and inference). Checks join hygiene, row-count assertions and statistical validity for Insights, and checks data leakage, temporal/group splits, train-serve skew and baselines for Modeling. Returns GO or NO-GO with WHERE/EXPECTED/ACTUAL/FIX findings. Use for "review this notebook", "review this analysis", "review this ML pipeline", "check for data leakage" or /code-review:review-data-science.
---

# review-data-science

Opinionated Principal Engineer review for data science code. It splits data science into Insights code and Modeling code. It counters silent row corruption and bad statistical claims in Insights code. It also counters data leakage and train-serve skew in Modeling code.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Analytical: classify each file as Insights or Modeling and trace lineage | Separate insight generation from prediction pipelines and trace raw inputs to outputs |
| 2 | Forensic: audit mode-specific data invariants | Run the Insights checklist or the Modeling checklist from the rubric |
| 3 | Skeptic: assume the headline metric or model lift is an artifact | Identify the bug, bias or leakage that could fake the result and check if the code disproves it |

Read [data-science-rubric.md](references/data-science-rubric.md) before step 1. It defines the mode boundary and blocking anti-patterns. It also holds the Insights and Modeling checklists.

## Steps

1. Read [data-science-rubric.md](references/data-science-rubric.md) and [classification-and-output.md](../code-review/references/classification-and-output.md).
2. Collect the changed notebooks, queries and scripts from the caller or from `git diff`.
3. Classify each file into Mode A (Insights) or Mode B (Modeling) using the rubric. If one file mixes exploratory mutations with production training or serving, record `DS-01` (Mixed Mode File).
4. Trace data lineage from each source table or file through every filter, join and feature transform.
5. For every Mode A (Insights) file, audit these four gates:
   - population gate: every dataset states its date window and exclusion rules. Mixed populations require a sources table and named join key
   - join and row-count gate: every join states its expected cardinality (`1:1`, `1:M` or `M:M`). Code asserts row count and distinct entity count before and after each join or filter
   - statistical gate: parametric tests check skew and sample size first. Point estimates include uncertainty bounds, and every prose number traces to an executed cell
   - reproducibility gate: notebooks run top-to-bottom from a fresh kernel with zero out-of-order state or magic constants
6. For every Mode B (Modeling) file, audit these four gates:
   - leakage gate: data splits happen before any global calculation. Scalers and imputers fit on the training split only, and features exclude post-event columns
   - split strategy gate: temporal or event data uses chronological splits with `shuffle=False`, and multi-row entities use group-aware splits (`GroupKFold`)
   - train-serve parity gate: training and inference call the same feature functions. Historical joins are point-in-time safe, and inference handles unseen categories and nulls
   - baseline and evaluation gate: the model beats a naive baseline on a cost-matched metric. Hyperparameter tuning never touches the held-out test set, and random seeds are pinned
7. Run the Skeptic pass. State the single most plausible bug or leakage source that could produce the reported insight or model score. Check whether an assertion in the code rules it out. If none does, record a blocking finding.
8. Format every blocking defect with the `REVIEW FAIL (data-science:insights)` or `REVIEW FAIL (data-science:modeling)` block.
9. Set `NO-GO` if any blocking finding or failed mechanical check exists. Otherwise set `GO`.
10. When invoked directly rather than through `code-review`, write `code-review-ds-<slug>.md` in the repo folder using `writing:writing-standard`. Reply with the verdict and link.

## Output

Follow the report skeleton in [classification-and-output.md](../code-review/references/classification-and-output.md) and include a Data Lineage and Mode table:

| File | Mode | Primary sources and split | Status |
|---|---|---|---|
| `<path>` | `<Insights, Modeling or Mixed>` | `<tables joined or split method>` | `<PASS or FAIL>` |

## Limits

- Never approves a join or filter in Insights code that lacks before-and-after row and entity counts.
- Never approves a Modeling pipeline that fits a transform before splitting or shuffles temporal data.
- Never treats correlation in observational data as a causal finding without an explicit identification strategy.
- Never edits source files or notebooks to fix a finding.
- Never delivers the review as an HTML artifact.
