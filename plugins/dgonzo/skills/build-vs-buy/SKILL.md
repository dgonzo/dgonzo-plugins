---
name: build-vs-buy
description: Compare building, buying, partnering and doing nothing on the same criteria, then recommend one option with the evidence behind every score. Weighs who runs it at 2am, the integration and exit cost and the 18-month outlook. Marks every vendor claim unverified until someone checks it. Use for "should we build or buy", "pick a vendor", "should we adopt this tool", "is this SaaS worth paying for" or "build, buy or partner". Also for /dgonzo:build-vs-buy. Not for testing a vendor choice already made or a choice between two designs the team builds itself (decision-forge). Not for sorting the claims in one vendor pitch (truth-extract).
---

# build-vs-buy

This skill produces a scored recommendation to build, buy or partner against a do-nothing baseline. It counters the failure mode where a vendor demo or a team's enthusiasm stands in for evidence.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Comparative: judge each option against the others, never alone | Score every option on fit, time to value and three-year cost, 1 to 5 |
| 2 | Operator: turn the choice into what happens on Monday and at 2am | Score run, integration and exit cost, 1 to 5, with a named 2am owner per option |
| 3 | Futurist: trace what follows the obvious outcome, three steps out | Score the 18-month outlook, 1 to 5, from a three-step trace per option |

## Steps

1. Read [references/scoring.md](references/scoring.md) for the criteria, evidence grades and checks.
2. If the user named a file, read it.
3. If the user pasted a thread, read it. If the user linked one and no tool can open it, ask for the text.
4. Ask once for any missing need, options or decider. Put every question in one message.
5. If no decider is named after that, write "Unassigned" as the owner and make naming one the first next action.
6. Write the need as one sentence with a done-when.
7. Always include build and do nothing as options.
8. Add at most three vendors, plus a partner if one is in play.
9. Run pass 1. Score each option on the three Comparative criteria.
10. Run pass 2. Score each option on the three Operator criteria.
11. If no named person or team will run an option at 2am, score its run cost 1.
12. Run pass 3. Score each option on the outlook criterion.
13. Write the evidence beside every score.
14. Grade every score as Verified, Claimed or Assumed.
15. If a score is Claimed or Assumed, cap it at 3.
16. Add every Claimed score to the unverified list with the check that would settle it.
17. Total the scores with equal weights, unless the user gave weights.
18. Recompute the leader's total with each Claimed score set to 1.
19. If the leader then loses its lead, recommend the checks before any purchase.
20. If do nothing scores within 2 points of the leader, recommend do nothing until the checks finish.
21. Write the result as Markdown in the folder the user is working in, named `build-vs-buy-<topic>.md`.
22. Reply with the bottom line and a link to the file. Do not paste the whole document.

## Output

The document has these sections, in this order. Its prose follows `/writing:writing-standard`.

1. Bottom line. The recommendation in one sentence. Then what is blocked and who owns it.
2. Scorecard. One row per option with its total and its count of Claimed scores.
3. Evidence by option. One table per option that gives each criterion its score, grade and evidence.
4. Unverified claims. One row per vendor claim with its source, check and owner.
5. Who runs it. One row per option with the 2am owner, upkeep hours a month and systems touched.
6. 18-month outlook. One row per option with the three-step trace and its effect on the score.
7. Next actions. At most five, each with an owner and a date.

## Limits

- Never grades a demo, a sales deck or an analyst ranking as Verified.
- Never counts a team's enthusiasm as evidence.
- Never scores a Claimed or Assumed item above 3.
- Never drops do nothing from the comparison.
- Never invents a decider, an owner or a number. A gap stays marked as a gap.
- Never contacts a vendor, starts a trial or sends a message.
- Never chooses between two internal designs or retests a vendor already chosen. That is `/dgonzo:decision-forge`.
- Never writes the result as an HTML artifact.
