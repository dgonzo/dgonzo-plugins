---
name: ragb
description: Write or audit a team status in RAGB. Every initiative gets one owner, one honest colour, one pointable fact and one next move. RED means at risk of not shipping. AMBER means standard operating risk. GREEN means shipped, verified and in the customer's hands. BLACK means stopped. Use for "write the team status in RAGB", "audit this status report", "is this status honest", "RAGB the weekly update" or "RAGB this thread". Also for dgonzo:ragb. Not for a standup of your own activity (slack:standup), a status update in the company comms format (internal-comms) or make and gh commands for the data-org board (data-org-cowork-plugin:handoff). Not for ranking priorities (cut-list), handing off work (owner-brief) or a postmortem on finished work (postmortem).
---

# ragb

Produces a RAGB status with one line per initiative, each tied to an artifact a reader can open. Counters activity reported as progress, where effort and meetings stand in for shipped work.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Forensic, from each claim back to its evidence | Trace each status to a PR, ticket, metric or release, else flag it as narrative |
| 2 | Calibration, trust rated 1 to 10 per claim | Rate each colour, then recolour by the ordered rules, with GREEN only if terminal |
| 3 | Reductive, ground truth only | Cut each initiative to one line of four fields with no activity words |

The four fields are the owner and the colour, then the fact and the next move. The [colour rules and narrative tells](references/colour-rules.md) hold the detail.

## Steps

1. If the user gave no input, ask once for it. A draft status or a Slack thread works. So does a file or a list of initiatives.
2. If the user named a file, read it. Do not ask again.
3. If the user named a Slack thread and a Slack read tool is available, read the thread. If no such tool is available, ask once for the text to be pasted.
4. Decide the job. A draft that states colours is an audit. A thread or a list without colours is a write.
5. Set the cycle. It is one week unless the input names another.
6. List every initiative in the input. Merge duplicates. Keep the input's names.
7. Name one owner per initiative. If the input gives none or gives two, mark the owner as missing.
8. Run pass 1. For each initiative, find the artifact in the input that backs its status. Record the link or the ID with a plain name.
9. If a read tool for the artifact is available, open it and check that it says what the status claims. Otherwise take it as given and say so in the Gaps.
10. If an initiative has no artifact, mark it as narrative. Quote the sentence that stands in for one.
11. Run pass 2. Rate each initiative 1 to 10 on the [honesty scale](references/colour-rules.md#honesty-rating).
12. Apply the [ordered colour rules](references/colour-rules.md#rules-in-order) to each initiative. The first rule that matches sets the colour.
13. If the input gave a colour and the rules give another, record both and the rule that decided.
14. Run pass 3. Write one line per initiative. The fact is a state a reader can check. The next move has an owner and a date.
15. If the next move has no date, write "no date" and list it as a gap.
16. Write the result to `status-<YYYY-MM-DD>.md` in the repo folder the user is working in. Use today's date. Link the file in the reply.
17. Put the bottom line and the RED table in the reply as well.

## Output

1. Bottom line. One sentence on the portfolio state with the count per colour. Then what is blocked and who owns the unblock.
2. RED. A colour table.
3. AMBER. A colour table.
4. GREEN. A colour table. The fact cell holds the release and the customer artifact.
5. BLACK. A colour table. The fact cell holds who stopped it and when.
6. Recoloured, in an audit only. A recolour table.
7. Gaps. One bullet per gap. A gap is a missing owner or a narrative status. It is also an unchecked artifact or a next move with no date.

A colour table has these columns.

| Initiative | Owner | Fact | Next move |
|---|---|---|---|

A recolour table has these columns.

| Initiative | Was | Now | Rule |
|---|---|---|---|

Each colour is a heading over its own table. RED always comes first. Leave out an empty colour.

The prose follows `writing:writing-standard`.

## Limits

- Never marks GREEN without a release, a verification and a customer artifact.
- Never invents an artifact, an owner or a date. A gap stays a gap.
- Never accepts two owners for one initiative.
- Never reports effort, meetings or hours as a fact.
- Never summarises one person's own activity. That is `slack:standup`.
- Never ranks priorities or cuts work. That is `dgonzo:cut-list`.
- Never writes a handoff. That is `dgonzo:owner-brief`.
- Never posts to Slack or edits a ticket. It writes the Markdown file and the reply.
- Never writes an HTML artifact.
