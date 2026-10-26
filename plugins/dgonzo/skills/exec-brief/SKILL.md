---
name: exec-brief
description: Write a one-page brief or a Slack message to an executive that opens with the ask and the deadline, then options only if the exec must choose, then the evidence. In David's voice with house structure. Use for "brief the CEO", "write the ask to the CTO", "I need a decision from the board", "exec summary for Slack" or "make this ask land with leadership". Also for /dgonzo:exec-brief. Not for testing the decision itself (decision-forge), a status report (ragb), a routine leadership update with no ask (internal-comms), a launch post (signal-cut) or modelling the reader (audience-model).
---

# exec-brief

Produces a brief or Slack message that gets an executive to decide or to know one thing by a date.

It counters detail that buries the ask, where the exec reads three paragraphs and still cannot say what you want.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Translator: rewrite for someone smart but outside the field | Replace every term, acronym or ticket ID the exec would have to look up, with zero left |
| 2 | Reductive: start from ground truth and drop inherited assumptions | Keep only the ask, the deadline and at most 3 sourced facts the exec needs to act |
| 3 | Modeling: simulate how one named person responds, specifically | Read only the first 2 lines as the exec and predict the reply in one sentence |

## Steps

1. If the user named a file, read it.
2. If the user pasted a thread or notes, use the pasted text.
3. If the user named a thread you cannot open, ask them to paste it.
4. If there is no source material, ask once for it.
5. If an `audience-<reader>.md` from `/dgonzo:audience-model` exists for this exec, read its Calibration section.
6. Find five items in the input. They are the exec by name and role, the ask and the deadline. Then what is blocked and who owns the work.
7. Find the channel. Slack means at most 150 words. A brief means at most 400 words. An approval email for spend or a contract fits one screen.
8. Classify the ask as a decision or as awareness.
9. If the ask is a decision, find David's pick.
10. If any item from steps 6 to 9 is missing, ask for all of them in one message. Do not ask twice.
11. Run pass 1. List every term the exec would have to look up. Replace each with plain words.
12. Run pass 2 on the ask. Write it as one sentence with a verb the exec performs. Use approve, pick or note.
13. Run pass 2 on the evidence. Keep at most 3 facts. Cut the rest.
14. If a kept fact has no source, mark it `(source needed)` in the draft.
15. If the ask is a decision, write at most 3 options. Give each its cost and its risk. Say once what happens if nobody picks by the deadline.
16. If the ask is awareness, write no options.
17. Run pass 3 with the check in [references/templates.md](references/templates.md#pass-3-check).
18. If the predicted reply is a question, move its answer into the first 2 lines. Then run pass 3 again.
19. Stop after 3 rounds of pass 3. Report any question that remains to David.
20. Load `/writing:writing-standard` for structure and `/dgonzo:voice` for voice.
21. If `/dgonzo:voice` is not installed, apply only the house standard and tell David.
22. If the channel is a brief, write it to `exec-brief-<topic>.md` in the repo folder the user is working in. Link it.
23. If the channel is Slack or an approval email, return the message in the reply ready to paste.

The skeletons for all three channels are in [references/templates.md](references/templates.md).

## Output

The brief itself has these sections, in this order.

1. Bottom line. The ask in one sentence, with its deadline. Then what is blocked and who owns it.
2. Options. Only for a decision. At most 3, with David's pick marked. Then what happens if nobody picks.
3. Evidence. At most 3 facts, each with its source.
4. Detail. A link to the long document, if one exists. Never the detail itself.

After the brief, tell David four things outside it.

1. The link to the file, or that the Slack text is above.
2. The predicted reply from pass 3.
3. What pass 2 cut, one line per item.
4. Every fact marked `(source needed)`.

## Limits

- Never test whether the decision is right. That is `/dgonzo:decision-forge`.
- Never report project status. That is `/dgonzo:ragb`.
- Never invent a deadline, an owner or a number. Ask for it.
- Never pick an option for David. Ask for his pick.
- Never write more than 3 options or more than 3 evidence facts.
- Never put background before the ask.
- Never send the message. David sends it.
- Never write an HTML artifact.
