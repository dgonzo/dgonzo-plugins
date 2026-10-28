---
name: hiring-debrief
description: Turn interview notes or a scorecard for one candidate into a hire or no-hire recommendation. Every rating is tied to observed behaviour, confidence is rated per competency, and the opposite decision is argued in full. Use for "debrief this candidate", "hire or no hire", "review this candidate's interview notes", "write up the panel debrief" or "is this candidate a hire". Also for dgonzo:hiring-debrief. Not for headcount or other general decisions (decision-forge), comparing vendors (build-vs-buy), modelling a candidate as a reader (audience-model) or user-research interviews (truth-extract).
---

# hiring-debrief

Produces a hire or no-hire recommendation for one candidate. The evidence table, open risks and reference-check questions come with it.

It counters the failure where one strong impression decides the hire.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Forensic: work backward from each outcome to its cause | Each rating traced to a quoted or described behaviour, with unbacked ratings flagged |
| 2 | Calibration: rate confidence and name where you are most likely wrong | Confidence 1 to 10 per competency, the weakest call named, and every panel gap of 2 or more points on a 5-point scale |
| 3 | Devil's Advocate: argue the other side with full conviction and concede nothing | The strongest case for the opposite decision from the same supported evidence, in at most 5 ranked points |

## Steps

1. If the user names a file or thread, read it. If you cannot open it, ask the user to paste it.
2. If the user gave no notes or scorecard, ask for them once. Ask for the role and its competencies in the same message.
3. If the role's competencies are missing, take them from the scorecard headings. Say which ones you used.
4. List every rating in the input. Give the interviewer, the competency and the score for each.
5. If the notes carry no scores, record each interviewer's stated view per competency as the rating.
6. Run pass 1. Pair each rating with the behaviour that backs it, quoted as written or described in the note-taker's words.
7. Mark each rating with no behaviour behind it as unsupported. Exclude it from the recommendation.
8. If one interviewer's overall view rests on a single moment, flag it as a single-impression rating.
9. If one moment backs ratings in two or more competencies, flag each of those ratings as a single-impression rating too.
10. Run pass 2. Score confidence per competency. Two or more interviewers citing specific behaviour score 8 to 10. One scores 4 to 7. None scores 1 to 3.
11. Name the competency where the recommendation is most likely wrong, and why.
12. List each panel gap of 2 or more points on a 5-point scale. On another scale, use the same share of its range. Give both positions and the evidence each cites. If only one interviewer took part, say so instead.
13. Decide hire or no-hire from the supported evidence only. If that evidence cannot carry either call, say so and name what is missing.
14. Run pass 3 against that decision. Use only supported evidence.
15. If the opposite case cites supported evidence the decision missed, change the decision and say so. Rhetoric alone never changes it.
16. Write one open risk for each competency rated 3 or below and each unresolved gap.
17. Turn each open risk into a reference-check question.
18. Name what blocks the decision and its owner. If the input names no owner, give the role and mark the name unknown. Hiring manager is the usual role.
19. Write the debrief as Markdown to `hiring-debrief-<role>-<YYYY-MM-DD>.md` in the folder the user is working in. Link it with a relative Markdown link. Do not commit it.

## Output

Write the debrief in these sections, in this order. The prose follows `writing:writing-standard`.

1. Bottom line. One sentence gives hire or no-hire and the main reason. The next names what blocks the decision and who owns it. Example: "Blocked until two references reply. The hiring manager owns it."
2. Evidence table with the header `Competency | Interviewer | Rating | Behaviour`. One row per rating. An unsupported rating shows "No evidence" as its behaviour.
3. Confidence table with the header `Competency | Confidence 1 to 10 | Reason`. One row per competency. A last line names the competency where the call is most likely wrong.
4. Unsupported and single-impression ratings. One bullet each, with the interviewer and competency.
5. Panel disagreements table with the header `Competency | First position | Second position | What settles it`. Each position names the interviewer and the rating. It also names the evidence cited.
6. Case for the opposite decision. At most 5 Devil's Advocate points in ranked order.
7. Open risks. Each risk in one sentence with the competency it touches.
8. Reference-check questions. At most 7. Each names the behaviour it is probing.

## Limits

- Never infer or mention a protected trait. These include age, gender and ethnicity. Religion, disability and family status count too. If the notes raise one, flag the line for removal. Do not weigh it.
- Judge only job-relevant behaviour. Ignore remarks about accent or appearance. Ignore "culture fit" and likeability unless tied to a named job behaviour.
- Never invent a quote. If the notes paraphrase, write "described as" instead of quotation marks.
- Never fill a missing rating. Report it missing.
- Never debrief more than one candidate per run. Ranking candidates against each other is out of scope.
- Never decide headcount or whether to open a role. That is `dgonzo:decision-forge`.
- Never send the debrief to anyone or post it anywhere.
- The recommendation advises the panel. It does not make the decision.
