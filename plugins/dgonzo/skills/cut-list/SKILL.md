---
name: cut-list
description: Force-rank a backlog, roadmap, quarter plan or list of asks against one stated goal. Then split it into keep, defer and cut, with each cut marked BLACK and a line to send. Use for "everything is P0", "what do we cut", "too many priorities", "rank this backlog" or "trim the quarter plan". Also for /dgonzo:cut-list. Not for one decision between options (decision-forge), status reports (ragb), vendor choices (build-vs-buy) or adding and completing tasks in TASKS.md (productivity:task-management).
---

# cut-list

Produces an evidence-backed keep list and defer list plus a cut list marked BLACK.

It counters the failure mode where everything is top priority, so nothing is.

BLACK means stopped on purpose, as in `/dgonzo:ragb`. A BLACK item gets no work this period.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Prioritizing: a forced rank that justifies the bottom and doubts the top | Rank 1 to N against the goal with tagged evidence and no ties |
| 2 | Counterfactual: trace the path forward as if the item had never existed | Loss if it never ships, scored 0 to 3 |
| 3 | Reductive: ground truth only, with inherited reasons removed | Drop "already promised" and "someone senior asked" as reasons, then keep what capacity covers |

## Steps

1. If the user named no list, ask once for it.
2. Otherwise read the file, issue list or thread the user named.
3. If the goal is not stated, ask once for the one goal this list serves.
4. If the goal is still missing, stop and say the list cannot be ranked without one.
5. If capacity is not stated, ask once for it in people-weeks or slots.
6. If capacity is still missing, assume the top third fits and say so.
7. Number every item and give it a plain name of 8 words or fewer.
8. Merge duplicates. Split any item that holds two pieces of work.
9. Record each item's owner and requester from the input. If either is not named, write "unassigned".
10. Tag each piece of evidence as measured, reported or assumed using [the evidence tags](references/output-template.md#evidence-tags).
11. Run pass 1. Rank every item by value to the goal. Give no two items the same rank.
12. Write the weakest case for the bottom item.
13. Write the 2 strongest reasons the top 3 could be wrong.
14. Run pass 2. For each item, record what happens if it never ships and who notices by when.
15. Score each loss from 0 to 3 using [the loss scale](references/output-template.md#loss-score).
16. If an item outside capacity scores 3, move it inside and say why.
17. If an item inside capacity scores 0, move it outside and say why.
18. Run pass 3. Strike any reason that rests only on a past promise, a title or habit. Re-rank if that changes the order.
19. Fill keep in rank order until capacity runs out.
20. If an item scoring 3 still does not fit, list it as a conflict. The goal owner must add capacity or name a kept item to drop.
21. If an item scores 2 or more and does not fit, defer it with the trigger that brings it back.
22. Cut everything else. Mark each cut BLACK.
23. Write one line per cut that the owner can send to the requester.
24. If the user named a repo folder or is working in one, write the result there as Markdown. Use [the output template](references/output-template.md) and link the file.
25. If there is no repo folder, reply inline in the same sections.

## Output

1. Bottom line: one sentence with the keep, defer and cut counts against the goal. Then each conflict from step 20 and its owner, or "no conflicts". Then who tells the requesters.
2. Keep: the kept items in rank order, with evidence and the loss if each never ships. Then the owner of each item.
3. Defer: each deferred item with its loss score and owner. Then the trigger that brings it back.
4. Cut (BLACK): item, why it goes and the line to send.
5. Where the rank could be wrong: the 2 strongest reasons and the evidence that would flip each.
6. Assumptions: capacity and goal wording. Then the inherited reasons struck in pass 3 and every piece of evidence tagged assumed.

Prose in the output follows `/writing:writing-standard`.

## Limits

- Never ranks without one stated goal.
- Never allows ties or a second "P0" tier.
- Never cuts an item without a reason a requester can read.
- Never defers an item without a trigger. A defer with no trigger is a cut.
- Never quietly defers an item that scores 3. It is a conflict with an owner.
- Never invents evidence or owners. Unknown value is tagged assumed.
- Never chooses between options for one decision. That is `/dgonzo:decision-forge`.
- Never reports status. That is `/dgonzo:ragb`.
- Never sends the cut lines. The owner sends them.
- Never writes the result as an HTML artifact.
