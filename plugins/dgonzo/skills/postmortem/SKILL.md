---
name: postmortem
description: Write a blameless postmortem for an incident, a missed launch, a failed project or a lost deal. Builds a sourced timeline, tests which single changes would have prevented it, checks for precedent, and ends with dated actions that each have one owner. Use for "write a postmortem", "incident review for", "what went wrong with the launch", "why did we lose the deal" or "blameless review of". Also for /dgonzo:postmortem. Not for a pre-mortem on a plan that has not run yet (architecture-stress-test), a status report on work still in flight (ragb), debugging a live bug (superpowers:systematic-debugging) or a short incident notice to the company (internal-comms).
---

# postmortem

This skill produces a blameless postmortem with a sourced timeline, tested causes and dated actions. It counters the failure mode where a blame story stands in for the cause.

A blame story names a person and stops. The cause is the condition that let a normal person make that mistake. The passes replace the story with evidence. Then they test each cause and check whether it has struck before.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Forensic: work back from the outcome to root causes, not symptoms | Timeline from evidence only, each entry cited |
| 2 | Counterfactual: change one fact and trace the new path forward | At most 5 candidate causes, each rated Prevents, Shortens or No effect |
| 3 | Historian: find when this happened before and what those cases shared | At most 3 precedents, each with the shared condition and the fix then |

## Steps

1. If the user has not named the event, ask once for the event and where the evidence lives.
2. If the user named the event but no source, search the working repo for it. Check the git log, docs and past postmortems.
3. Read every source the user named, such as a PR or a log.
4. If no available tool reaches a source, ask the user once to paste it.
5. If a source is still missing, list it as an evidence gap. Do not fill the gap from memory.
6. Write one line that states the outcome as a fact with a number. Example: "Checkout returned errors for 47 minutes."
7. If no number is in the evidence, write the outcome without one and list the number as an evidence gap.
8. Build the timeline in time order. Give each entry a timestamp, the event and its source.
9. If an entry has no record behind it, mark it Recalled and name who recalled it.
10. If an entry names a person as the cause, rewrite it as the action and the condition around it. The rules are in [references/blameless.md](references/blameless.md).
11. List at most 5 candidate causes from the timeline. Include detection and response, not only the trigger.
12. Test each candidate. Change only that one fact, trace the outcome forward and give the rating.
13. Drop every candidate rated No effect. The rest are the contributing causes.
14. Search for precedent in the working repo first. Check past postmortems, closed issues and the git history.
15. Name a known industry pattern only if one fits. If you name a specific outside incident, cite a public source.
16. For each precedent, state the condition it shares with this event and the fix that worked then.
17. Mark each precedent Sourced if you found a document. Mark it Pattern if it comes from general knowledge.
18. If an old fix did not hold, state why. Then test that gap as a candidate cause.
19. Write one action per contributing cause. Give each action one named person as owner and a due date.
20. If the evidence names no owner or date, ask the user once with the action list.
21. If an owner or date is still unknown, write "Owner needed" or "Date needed". List it in the bottom line.
22. Write the document as Markdown with [references/template.md](references/template.md). Put it in the repo folder the user is working in. If the repo has a postmortems folder, use that.
23. Name the file `postmortem-<yyyy-mm-dd>-<slug>.md`, dated by the event.
24. If the `/writing:lint` command is available, run it on the file and fix every real finding.
25. Reply with the bottom line and a relative link to the file.

## Output

The document has these sections in this order.

1. Bottom line. The strongest cause in one sentence. A Prevents cause outranks a Shortens cause. Then what is still exposed, who owns the fix and every "Owner needed" or "Date needed".
2. Impact. Who was affected and for how long. Then the cost in numbers.
3. Timeline. One row per event in time order. Each row cites its source and is marked Sourced or Recalled.
4. Contributing causes. Each cause with its rating and the timeline rows behind it.
5. Precedents. Each prior case with the shared condition and the fix then. Each one is marked Sourced or Pattern.
6. Actions. One row per action. Each row names one owner, a due date and the cause it removes.
7. Evidence gaps. Each missing source and the question it would settle.

Prose follows `/writing:writing-standard`.

## Limits

- Never names a person as a cause.
- Never adds a timeline entry without a source or a Recalled mark.
- Never keeps a cause that fails the counterfactual test.
- Never presents a Pattern precedent as a sourced fact.
- Never invents an owner, a date or a number.
- Never gives an action two owners or a team as owner.
- Never rates individual performance. That belongs to a manager, not a postmortem.
- Never reviews a plan that has not run yet. That is `/dgonzo:architecture-stress-test`.
- Never writes an HTML artifact. The document is Markdown in the repo.
