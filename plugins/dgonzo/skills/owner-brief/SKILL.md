---
name: owner-brief
description: Turn work that is about to change hands into a brief with one accountable owner, a one-sentence objective, a facts table, ordered steps, owned blockers and a "Done when" checklist. The receiver is a person or a future Claude session. Use for "write a handoff brief", "brief the next session", "who owns this and when is it done", "pass this work to a teammate" or "set up a fresh session for this". Also for /dgonzo:owner-brief. Not for status reports (ragb), an implementation plan (superpowers:writing-plans) or gh and make commands that ship data-org docs (data-org-cowork-plugin:handoff).
---

# owner-brief

This skill writes a handoff brief that one named owner can act on without asking a question. It counters work handed off without a single owner or a test for done.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Reductive: strip to ground truth and drop inherited assumptions | One objective sentence and at most 12 facts |
| 2 | Interviewer: ask the questions that get a better answer instead of guessing | At most 5 questions, each answerable in 5 words |
| 3 | Planning: sequence the work with dependencies flagged and the critical path named | At most 3 phases, a one-sentence critical path and one owner per blocker |

## Steps

1. If the user named a file or thread, read it.
2. If the user named nothing and this conversation holds the work, use the conversation as the source.
3. If neither holds the work, ask once for the work and the receiver. Wait for the answer.
4. If `/writing:writing-standard` is available, load it. Otherwise write point first. Use one idea per sentence. Use no em dashes and no semicolons.
5. Write the objective in one sentence. If it needs two, the work is two briefs. Hold that as a gap for step 9.
6. List at most 12 facts the receiver needs to act. Give each fact a concrete value such as a path or a date. Drop any fact the receiver can find in under a minute.
7. Check for gaps. Who owns the work and who receives it? What is the done-when and the deadline? Who owns each blocker? Which brief comes first, if step 5 found two?
8. Fill each gap the source already answers. Never ask what you can read.
9. If gaps remain, ask at most 5 questions in one message. Each must be answerable in 5 words. Ask about the owner first and the done-when second. If the source names two owners or a team, ask which one person is accountable. Wait for the answers.
10. If a gap is still open after the answers, write it as an assumption in the brief. Never ask a second round.
11. If the answers still leave no single owner, mark the owner unresolved. Make naming one owner the first blocker, owned by the user.
12. Order the steps. If a step needs another to finish first, say which. If a gate separates two groups of steps, split them into phases. Use at most 3 phases.
13. Name the critical path in one sentence.
14. For each blocker, write who clears it and what state means it is cleared.
15. Write each "Done when" item as a state a second person can check with yes or no. Rewrite any item that describes activity.
16. If the receiver is a Claude session, add a "How to start" block with absolute paths and the exact `claude` command.
17. Write the brief as Markdown in the repo folder the user is working in. Use a `scratch/` folder if one exists. Name it `YYYY-MM-DD-<slug>-handoff.md`.
18. If `/writing:lint` is available, run it on the brief and fix every real finding.
19. Reply with a link to the brief and its bottom line. Do not paste the brief into the reply.

The section template and examples of good and bad "Done when" items are in [the brief template](references/brief-template.md).

## Output

The brief has these sections, in order.

1. Bottom line. One sentence on what changes hands and who owns it. Then what is blocked and who owns each blocker.
2. Owner. A table with the accountable owner, the receiver and the deadline.
3. Facts. A two-column table, Fact and Value.
4. How to start. Only when the receiver is a Claude session.
5. Steps or phases. Numbered. Blocked steps name their blocker.
6. Blockers. A table with Blocker, Owner and Cleared when.
7. Done when. A numbered checklist of verifiable states.
8. Assumptions. Only when a gap stayed open.

## Limits

- Never names two owners for one piece of work.
- Never writes a "Done when" item that is an activity, such as "review the PR" or "work on X".
- Never asks more than 5 questions or asks a second round.
- Never invents a fact, a path or a name. Unknowns become questions or assumptions.
- Never runs the steps it writes.
- Never reports progress or health. That is `/dgonzo:ragb`.
- Never packages gh or make commands for data-org docs. That is `data-org-cowork-plugin:handoff`.
- Never writes the brief as an HTML artifact.
