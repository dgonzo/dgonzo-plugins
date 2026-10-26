---
name: signal-cut
description: Draft or rework outward content for a technical audience in David's voice about something built or shipped. Builds a story from a real problem, breaks the expected shape for the format and swaps every claim for something the reader can see or run. Use for "write the launch post", "draft a blog post about this", "turn this into a LinkedIn thread", "write the demo script" or "this launch post sounds like marketing". Also for /dgonzo:signal-cut. Not for taglines or positioning (position-lock), reader research (audience-model) or exec briefs (exec-brief). Not for opinion posts or plain rewrites in David's voice (voice). Not for an internal Slack announcement (slack:draft-announcement).
---

# signal-cut

This skill produces a draft of outward content in David's voice, such as a launch post or a demo script. It counters marketing-speak, which makes a technical reader stop at the first sign of a sell.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Narrative: turn it into a story with a tension, a turn and a resolution | 3-line arc of what broke, what changed and what is now possible, each line tied to a real event |
| 2 | Subversive: find the least expected approach that still works | 1 break of the default shape for the format, redone if a competitor could post it unchanged |
| 3 | Practitioner: keep only what gets done in the real world | Only sentences a reader could act on that day, each claim swapped for a demo or number, at least 1 demo |

## Steps

1. Load `/dgonzo:voice`. Every sentence of the draft follows it.
2. If `/dgonzo:voice` is not installed, say so in one line and follow `/writing:writing-standard` instead.
3. Read the reference file [marketing-tells.md](references/marketing-tells.md).
4. If the user named a source file or thread, read it.
5. If the user named no source, ask once for the facts and the target format.
6. If the target format is still unclear, ask once. If no answer comes, draft a blog post.
7. If the user has an audience model from `/dgonzo:audience-model`, read it and write for that reader.
8. If the source has no real event or number, ask once for one. If none comes, list it under Open items. Never invent one.
9. Run pass 1. Write the 3-line arc.
10. Run pass 2. Name the default shape in one line. Name the break in a second line.
11. Draft the piece in the target format from the arc and the break.
12. Run pass 3 on the draft. Cut or replace each sentence that fails the Monday morning test.
13. Check the draft against each tell in the reference file. Rewrite each hit.
14. End the draft with a call to action that asks for a concrete act, such as running a command. It is never "sign up" or "learn more".
15. If the user works in a repo, write the result as `<slug>.md` in the user's working folder and link it.
16. If the user works outside a repo, return the result in the reply.

## Output

1. Bottom line: the tension of the piece in one sentence. Then whether the draft is ready to publish, what blocks it and who owns each blocker.
2. Arc: the 3 lines from pass 1.
3. Break: the default shape in one line. The break in a second line.
4. Draft: the full piece in the target format, call to action last.
5. Cuts: a table with columns Removed and Replacement. One row per claim cut in pass 3 or step 13.
6. Open items: each missing fact the draft needs, with its owner.

## Limits

- Never invents a customer or a quote.
- Never invents an event or a metric.
- Never copies an example number from the reference file into a draft.
- Never writes a claim the source cannot back.
- Never writes taglines or positioning statements. Those belong to `/dgonzo:position-lock`.
- Never builds an audience profile. That belongs to `/dgonzo:audience-model`.
- Never writes a brief that asks an executive for a decision. That belongs to `/dgonzo:exec-brief`.
- Never posts or publishes. It returns a draft.
- Never returns an HTML artifact.
