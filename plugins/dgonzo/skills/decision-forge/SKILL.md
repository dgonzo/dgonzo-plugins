---
name: decision-forge
description: Test one pending decision for confirmation bias. Attacks it, builds the strongest case for the rival option, rates confidence by dimension and prices the cost of reversing it. For architecture choices, technology bets, a vendor already chosen, headcount calls and single priority calls. Use for "pressure-test this decision", "attack this choice", "steel-man the option we rejected", "am I fooling myself on this" or "how sure should we be about X". Also for /dgonzo:decision-forge. Not for choosing build, buy or a vendor (build-vs-buy), names (naming-forge), a plan before work starts (architecture-stress-test), ranking a backlog (cut-list) or judging a candidate (hiring-debrief). Never writes the decision record. That is data-org-cowork-plugin:draft-dadr.
---

# decision-forge

Produces a decision test that attacks one choice and rates how sure and how reversible it is.

It counters confirmation bias, where you defend the first idea instead of the best one.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Adversarial: attack the idea as a skeptic who must be convinced | Up to 5 attack vectors, ranked by damage if true |
| 2 | Steel-man: build the strongest version of the opposing position before answering it | One rival position a smart advocate would sign |
| 3 | Calibration: rate confidence per part and name where you are most likely wrong | 1 to 10 per dimension, each tagged known, inferred or assumed |

The scales and tests for each pass are in [references/rubrics.md](references/rubrics.md).

## Steps

1. Read [references/rubrics.md](references/rubrics.md). Every scale and rule below comes from it.
2. If the user named a source, read it. A source is a file, a thread or a PR.
3. If the user named no source, take the decision from the conversation.
4. If an input is missing, ask for all missing inputs in one question. Ask once. The inputs are the decision, the rival option and the deadline.
5. If the rival is still missing, use the strongest alternative in the material. If there is none, use "do nothing".
6. If the deadline is still missing, write "date unknown" and add a Timing attack for it.
7. Write the decision as one sentence: "We will do X instead of Y, by date D."
8. If the sentence holds two choices, split them. Test the one the user named first.
9. List every attack vector. Check each attack source in the rubric.
10. Rate each attack's damage high, medium or low with the rubric. Keep the 5 most damaging.
11. For each kept attack, look for evidence in the source and the conversation. Then search the repo.
12. Mark each attack with a status from the rubric. Survived means evidence answers it. Landed means evidence confirms it. Unresolved means neither.
13. Build the steel-man for the rival option. Argue it as its best advocate would.
14. Run the steel-man test in the rubric. If it fails, rebuild it once. If it fails again, record "no strong rival case" as a finding.
15. State what the steel-man gets right that the decision does not cover. Name the dimension that point falls on.
16. Pick 4 to 7 dimensions that carry the decision. Cost, delivery risk and lock-in are typical.
17. Rate each dimension 1 to 10 with the confidence scale. Tag it known, inferred or assumed. Cap it at its basis ceiling.
18. Name the dimension where you are most likely wrong.
19. Rate reversibility with the door scale in the rubric. Name the point of no return.
20. Set the verdict with the verdict rules in the rubric. Check the rules in order.
21. Name who owns the decision and who owns each condition. If an owner is unknown, write "owner: unassigned".
22. Load `/writing:writing-standard` before writing the result. If it is not installed, write point first in short sentences.
23. Write the result as Markdown named `decision-forge-<slug>.md`. Put it beside the source file, or else in the repo folder the user is working in.
24. Reply with the verdict sentence and a relative link to the file.
25. If the repo is data-org, add one line: the file can feed a DADR (data-org decision record) through `/data-org-cowork-plugin:draft-dadr`.

## Output

Sections in this order:

1. Bottom line. The verdict in one sentence. Then what is blocked and who owns it.
2. Decision. The one-sentence statement from step 7.
3. Attacks. One table row per attack with its damage, status and evidence. Status is survived, landed or unresolved.
4. Steel-man. The rival case in at most 5 sentences. Then one sentence on what it gets right and the dimension it hits.
5. Confidence. One table row per dimension with its rating, basis and reason. Basis is known, inferred or assumed. Then the dimension most likely wrong.
6. Reversibility. The door type and the cost to reverse. Then the point of no return.
7. Conditions. Only for hold with conditions. Each condition names an owner, a test and a done-when before the point of no return.

The prose follows `/writing:writing-standard`.

## Limits

- Never writes or edits the decision record, DADR or ADR.
- Never makes the decision. It tests the one in front of it.
- Never marks an attack survived or landed without evidence from the material.
- Never invents a weak rival to knock down.
- Never rates a dimension known without naming its source.
- Never tests more than one decision per run.
- Never writes an HTML artifact.
