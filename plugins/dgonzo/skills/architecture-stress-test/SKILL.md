---
name: architecture-stress-test
description: Stress-test a plan before work starts. Maps phases, dependency edges and the critical path. Runs a pre-mortem. Compares the plan with a simpler, a more parallel and a more conservative version. Returns APPROVE or REVISE. Use for "stress-test this plan", "poke holes in this migration plan", "check the phase ordering", "will this rollout hold" or "stress-test this design doc before we build". Also for dgonzo:architecture-stress-test. Not for writing a plan (superpowers:writing-plans), reviewing code (code-review), choosing between two designs (decision-forge) or a bare pre-mortem with no plan review (lens).
---

# architecture-stress-test

This skill produces a plan assessment with an APPROVE or REVISE verdict. It counters plan fragility: phase ordering and sizing that nobody tested before the build started.

It works on any plan document. Design docs, migration plans and rollout plans all count. So does a gwrk `plan.md`.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Analytical: break the plan into its parts and show how they relate | Dependency edges, critical path and blast radius per phase on a 3-step scale |
| 2 | Pre-mortem: assume the plan failed and work backward to the causes | Failure at 6 months traced to at most 5 root causes |
| 3 | Comparative: judge the plan against alternatives, never alone | Plan against the simplest, most parallel and most conservative alternatives |

The blast radius scale, the alternative definitions and the table columns are in [the assessment template](references/assessment-template.md). The steps call it the template.

## Steps

1. If the user named a plan file or thread, read it. If not, ask once for the plan.
2. If the text has no sequence of work, say so in one sentence and stop.
3. Read the files the plan names that are in the repo. Read nothing else.
4. List every phase. Note each phase's inputs, outputs and owner as written. Write "unassigned" where the plan names no owner.
5. List each dependency edge between phases. Mark an edge the plan implies but does not state as inferred.
6. Flag every ordering error. An ordering error is a phase that uses an output before the phase that makes it.
7. Mark the critical path. It is the longest chain of dependent phases. Measure it in the plan's stated durations. If the plan states none, count phases.
8. Rate each phase's blast radius Low, Medium or High on the template's scale.
9. For each phase, record whether the plan states a rollback. Write "none" if it does not.
10. Assume the plan failed 6 months after start. Write at most 5 failure stories, most likely first.
11. Trace each failure story to one root cause in the plan. Cite the phase.
12. For each root cause, name the cheapest change that prevents it. If nothing prevents it, name the earliest signal that detects it.
13. Build the 3 alternatives from the template's definitions.
14. Compare each alternative with the plan on critical path length, top blast radius and root causes removed.
15. Apply the verdict rule below.
16. If the plan is a file in a repo, write the assessment as Markdown beside it. Name it `<plan-name>-stress-test.md` and link it.
17. If the plan came from a thread, write the file in the repo folder the user is working in. Link it.
18. If the session has no repo folder, give the assessment in the reply.

## Verdict rule

Return REVISE if any of these holds. Otherwise return APPROVE.

- An ordering error exists.
- A high blast radius phase has no rollback.
- A root cause has neither a prevention nor an early signal.
- An alternative meets the plan's goal and adds no root cause. It beats the plan on critical path length or top blast radius and loses on neither.

## Output

Write the prose to `writing:writing-standard`. Sections in this order:

1. Bottom line. APPROVE or REVISE and the main reason, in one sentence. Then what is blocked and who owns it. On APPROVE, write "Blocked: nothing."
2. Required changes. REVISE only. Ranked by blast radius, each with the phase and the owner.
3. Dependency table. One row per phase.
4. Critical path. The phases in order on one line.
5. Failure scenarios. One row per root cause.
6. Alternatives. One row per alternative.
7. Assumptions. What the review took as given and did not check.

Use the template's skeleton for the headings and table columns.

## Limits

- Never edits the plan file. It proposes changes only.
- Never writes a plan from scratch. That is `superpowers:writing-plans`.
- Never reviews code line by line. That is `code-review`.
- Never picks between two competing designs. That is `dgonzo:decision-forge`.
- Never runs a pre-mortem alone without the plan review. That is `dgonzo:lens`.
- Never presents an inferred dependency as stated.
- Never returns APPROVE while an ordering error is open.
- Never delivers the assessment as an HTML artifact.
