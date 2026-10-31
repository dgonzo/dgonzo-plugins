---
name: audience-model
description: Model one specific reader before writing to them, such as an exec, a customer, a candidate or a team. Simulates their response to the ask, lists what is unknown about them and checks each claim against their past behaviour. Produces a reader model that dgonzo:signal-cut, dgonzo:position-lock and dgonzo:exec-brief build on. Use for "who am I writing for", "model this reader", "how will the CFO read this", "what does this audience care about" or "how will this reader take the ask". Also for dgonzo:audience-model. Not for writing the message, sorting claims from customer interviews (truth-extract) or judging whether to hire a candidate (hiring-debrief).
---

# audience-model

Produces a reader model. It says who the reader is, how they will respond to the ask and how to write to them.

It counters audience projection, which is assuming the reader cares about what excites the writer.

The model feeds `dgonzo:signal-cut`, `dgonzo:position-lock` and `dgonzo:exec-brief`. Hand them its Calibration section as input.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Modeling: simulate how one named person responds, specifically | Pick 1 of 4 responses to the ask, plus their first question and the line where they stop reading |
| 2 | Interviewer: ask the questions that get a better answer before answering | List at most 5 open questions about the reader, each with who can answer it |
| 3 | Forensic: work backward from what the reader did, not what they said | Tag every claim observed, stated or assumed against a record of past behaviour |

## Steps

1. If the user named a file, read it.
2. If the user pasted a thread or a draft, use the pasted text.
3. If the user named a thread you cannot open, ask them to paste it.
4. If the reader or the ask is missing, ask once for both. The ask is what David wants the reader to do.
5. If the reader is a group, model the person who decides. Also model one named member who will act on the message. Write one model per person.
6. Run pass 1. Fill the Reader fields listed under Output. Tag each field observed, stated or assumed.
7. Predict one response from the list under Output. If a draft exists, predict the response to the draft as written.
8. List what David wants the reader to care about. Mark each item the reader model does not share as a projection.
9. Run pass 2. List the open questions.
10. Answer from the source material each question it can answer.
11. If questions remain, ask David all of them in one message. Wait for the reply. Do not ask twice.
12. If David cannot answer a question, keep it open and name who can.
13. Run pass 3 with the sources in [evidence-sources.md](references/evidence-sources.md). Use only records open in this session or pasted by David.
14. If a record is out of reach, name where it lives in the Gaps section. Never claim to have checked it.
15. If a claim has no evidence, tag it assumed. Never fill it in.
16. If a stated preference contradicts behaviour, keep the behaviour and record the contradiction.
17. Rerun the pass 1 prediction using only observed and stated claims.
18. If the prediction changes, report both predictions and the claim that changed it.
19. Load `dgonzo:voice` for the output prose. If it is not installed, use `writing:writing-standard` and tell David.
20. Write the model to `~/.claude/dgonzo/readers/<name>.md` when the reader is a real person. Use the reader's first name in lower case. Write to the repo folder only when David asks, and never to a team repo. A real person's reading habits and quoted email stay on David's machine. Link the file.
21. Name the next skill. Use `dgonzo:exec-brief` for an ask to an exec. Use `dgonzo:signal-cut` for an announcement or outward post. Use `dgonzo:position-lock` for a one-line position.

## Output

The file has these sections, in this order. For a group, repeat sections 2 to 7 for each person.

1. Bottom line. One sentence on what the reader will do with the ask as it stands. Then the gap that most changes that prediction, and who can close it.
2. Reader. A table with Field, Value and Status columns. The fields are:
   - name
   - role
   - what they own
   - what they are measured on
   - their pressure this week
3. Predicted response. One of these:
   - reads and acts
   - reads and forwards
   - skims and parks
   - ignores

   Add their first question and the line where they stop reading. If the rerun in step 17 changed the prediction, give both and the claim that changed it.
4. Projections. What David cares about that the reader does not, one per row.
5. Evidence. A table with Claim, Evidence and Status columns.
6. Gaps. At most 5 open questions, each with who can answer it or where the record lives.
7. Calibration. A table with Item, Guidance and Evidence columns. Each row cites a claim from section 5. The items are:
   - lead with
   - leave out
   - words to use
   - words to avoid
   - length
   - channel
   - repeat test: one sentence the reader would say back verbatim
8. Their vocabulary. A table of the reader's own terms and what each means. Drafts use these.
9. What loses them. A table of signals that make the reader stop reading, each tied to a record.
10. What they do with the thing you send. Forward, assign, reply with actions, file. Write so that act needs no cover note.

## Limits

- Never writes the message. Calibration goes to the next skill.
- Never invents evidence. An unknown stays a gap.
- Never treats a stated preference as fact when behaviour contradicts it.
- Never averages a group into one persona. One named reader per model.
- Never models private life or personality type. Work behaviour only.
- For a candidate, uses only what the hiring process and their public professional work provide.
- Never produces an HTML artifact.
