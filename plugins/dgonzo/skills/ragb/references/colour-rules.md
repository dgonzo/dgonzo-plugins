# RAGB colour rules

These rules decide the colour in pass 2 of the `ragb` skill. The source is the Foxtrot Charlie operating model. Reality is written as state. If it cannot be pointed to, it does not exist. Every initiative has one accountable owner.

## The four colours

| Colour | Meaning | What backs it |
|---|---|---|
| RED | At risk of not shipping | A blocker, a missed date, a failing check or no state at all |
| AMBER | Standard operating risk | An open PR, an active ticket or a dated plan |
| GREEN | Done done, and terminal | A release, a verification and a customer artifact |
| BLACK | Not doing or stopped | A decision with a name and a date |

## Honesty rating

Rate each initiative 1 to 10 for how far a reader can trust its status. A cycle is one week unless the input names another.

| Rating | What backs the status |
|---|---|
| 9 to 10 | An artifact the reader can open, dated this cycle |
| 6 to 8 | An artifact from an earlier cycle, or a metric with no link |
| 3 to 5 | A named person's word with no artifact |
| 1 to 2 | Activity words only |

A rating of 5 or lower means the status is narrative. Rule 6 below then decides its colour.

## Rules in order

Apply the first rule that matches. Stop there.

1. The work was stopped or dropped. The colour is BLACK. If no one wrote the decision down, list that as a gap.
2. A release, a verification and a customer artifact all exist. The colour is GREEN.
3. A date has passed with no new date. The colour is RED.
4. A blocker or a failing check threatens the date. The colour is RED.
5. The initiative has no owner or has two owners. The colour is RED.
6. The status is narrative, rated 5 or lower. The colour is RED, because its state is unknown.
7. Any other initiative. The colour is AMBER.

A merged PR, a passing test or a staging deploy does not meet rule 2. Neither does a claim of GREEN with no customer artifact. Such work falls through to the later rules.

GREEN is terminal. A GREEN initiative leaves the next report. If it comes back, it is a new initiative.

## Narrative tells

These phrases report activity, not state. Each one is a flag in pass 1. Quote it, then name the artifact that would replace it.

| Phrase | The fact to ask for |
|---|---|
| "making good progress" | Which PR merged or which ticket closed |
| "working on it" | The open PR or the active ticket |
| "had a great meeting with" | The decision written down, with its date |
| "almost done" | The remaining tickets and their count |
| "on track" | The date and the artifact that shows the pace |
| "aligned with stakeholders" | The written commitment and its owner |
| "spent the week on" | What shipped or what changed state |

## Good and bad lines

Bad: "Ingestion pipeline. GREEN. Team made great progress and the PR is merged."

Good: "Ingestion pipeline. Owner Ana Ruiz. AMBER. PR 412 for the loader rewrite merged and is not yet released. Next, Ana releases to production by Friday 30 October."

The bad line reports effort and calls a merge done. The good line names one owner, a fact a reader can open and a move with a date.
