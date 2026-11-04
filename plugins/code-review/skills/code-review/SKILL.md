---
name: code-review
description: Principal Engineer code review router that identifies the kind of code under review and dispatches specialist skills for fullstack webapps, APIs and data science (insights vs modeling). Runs mechanical baseline gates under one-way gate authority and returns a GO or NO-GO verdict with WHERE/EXPECTED/ACTUAL/FIX findings. Use for "review this code", "code review", "review this PR", "review this diff" or /code-review:code-review. Not for reviewing prose (writing:review-prose), stress-testing a plan (dgonzo:architecture-stress-test) or testing a single architecture decision (dgonzo:decision-forge).
---

# code-review

Principal Engineer code review router. It identifies what kind of code changed, runs the mechanical baseline and dispatches the matching specialist review skills. It counters surface-level reviews that miss boundary leaks and silent data bugs.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Analytical: break the change into surfaces and architectural layers | Classify every changed file into Webapp, API or Data Science (Insights vs Modeling) |
| 2 | Audit: run the mechanical baseline and the specialist rubrics | Execute build, lint, tests and the dispatched specialist review skills |
| 3 | Integrative: merge surface findings under one-way gate authority | Return one `GO` or `NO-GO` verdict with `WHERE` remediation blocks and coverage holes |

Read [classification-and-output.md](references/classification-and-output.md) before step 1. It defines the classification signals and one-way gate authority. It also has the finding format and report skeleton.

## What the argument selects

| Argument | Target |
|---|---|
| none | `git diff` of the working tree against `HEAD` |
| a git ref or branch | `git diff <ref>...HEAD` |
| a PR number | `gh pr diff <n>` and `gh pr view <n>` |
| a file or directory path | the named files |

## Steps

1. Read [classification-and-output.md](references/classification-and-output.md).
2. Resolve the target files and hunks from the argument. If no code files changed, say so in one sentence and stop.
3. Read repo grounding if present. Check `docs/architecture.md` and `ARCHITECTURE.md`. Also check `.gwrk/ontology/domain.md`, `spec.md` and `plan.md`.
4. Classify each changed code file using the signals in the reference file. Group the files into `webapp` and `api`. Use `data-science:insights` and `data-science:modeling` for data science files.
5. If a single change spans multiple kinds, keep each group and review each with its specialist skill.
6. Detect the project's build, lint and test commands from repo config files. Check `package.json` or `pyproject.toml`, plus `Cargo.toml` or `go.mod` or `Makefile`.
7. Run the mechanical baseline on the changed scope:
   - run the build or typecheck command
   - run the linter in check mode
   - run the unit or integration tests covering the changed files
   - if `{feature_dir}/gates/run-all-gates.sh` exists in a `gwrk` repo, run it
   If local execution is unavailable in this environment, state that in the report. Never claim a command ran when it did not.
8. Record mechanical results as a baseline only. Apply one-way gate authority from the reference file. A passing test or gate never closes a defect found in step 9.
9. Load and run every specialist skill matched in step 4:
   - `webapp` files load [review-webapp](../review-webapp/SKILL.md)
   - `api` files load [review-api](../review-api/SKILL.md)
   - `data-science:insights` or `data-science:modeling` files load [review-data-science](../review-data-science/SKILL.md)
10. For every defect that survived a green test or gate, record a gate coverage hole alongside the finding.
11. Set the verdict. Any failed mechanical check or any blocking finding from a specialist skill forces `NO-GO`. Otherwise return `GO`.
12. Load `writing:writing-standard` before writing the report.
13. Write the review as Markdown in the repo folder open in the IDE. Name it `code-review-<slug>.md`. In a `gwrk` phase review, also follow the repo's `tasks.json` re-open rules if instructed.
14. Reply with the verdict sentence, the classification summary and a relative link to the report file.

## Output

Use the skeleton in [classification-and-output.md](references/classification-and-output.md). Sections in this order:

1. Bottom line. `GO` or `NO-GO` and the primary reason in one sentence. Then what is blocked and who owns it.
2. Classification and scope. A table of each detected code kind and its architectural pattern. Include the file count and dispatched skill.
3. Mechanical baseline. A table of build, lint and test results.
4. Blocking findings. `NO-GO` only. Rank findings by blast radius using the `WHERE` and `EXPECTED` block from the reference file.
5. Gate coverage holes. Any blocking finding where the existing test suite or gate stayed green.
6. Non-blocking notes. At most 5 structural or maintainability notes.

## Limits

- Never edits source code to fix a defect. Document the fix in `FIX` and return `NO-GO`.
- Never lets a passing test or gate erase a reproduced architectural or logic defect.
- Never reviews against personal framework or language taste when the code's boundaries hold.
- Never substitutes User Acceptance Testing (UAT) visual polish for code review.
- Never delivers the review as an HTML artifact.
