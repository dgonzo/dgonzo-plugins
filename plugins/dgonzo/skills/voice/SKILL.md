---
name: voice
description: Draft or rewrite text in David's own professional voice for anything sent under his name. Covers Slack messages, emails, LinkedIn opinion posts, essays and memos. Flat conviction, short lines, concrete stories, work-safe edge. Use for "write this in my voice", "make this sound like me", "draft a Slack reply from me", "reply to this as me" or "rewrite my email". Also for /dgonzo:voice. Not for team documents or a plain PR description, which follow /writing:writing-standard. Not for a launch post, blog post or demo about something built, which is /dgonzo:signal-cut. Not for an internal Slack announcement, which is /slack:draft-announcement. Not for a brief that asks executives for a decision, which is /dgonzo:exec-brief.
---

# voice

This skill produces a draft that reads as David wrote it, ready for him to send under his name. It counters the generic voice: correct, polite prose that no reader would attribute to him.

The traits come from his Foxtrot Charlie essay, the one source he clearly wrote himself. The source trust table and 10 verbatim excerpts are in [references/samples.md](references/samples.md). Read that file before every draft. Each example below names its sample number.

## Traits

| Trait | Do | Example |
|---|---|---|
| Flat conviction | State the claim with no hedge | "What gets built is 1,000% more important than how it gets built." (1) |
| One-line beats | Give a turn its own line, two or three per piece | "And it still didn't matter." (2) |
| Earned authority | Ground a claim in his years or role, only from facts he gave | "After almost two decades doing this" (1) |
| Concede, then strike | Grant the other side in one sentence, then show its limit | "I will grant that for established leaders" (3) |
| Company stories | One named story per claim, with the outcome | "companies like DataRobot had every chance to win" (4) |
| Name the unpopular part | Flag the claim people avoid, then make it | "Here's the part people avoid" (5) |
| Chains and mantras | One causal chain of three or four links | "Velocity gives you reps." (6) |
| Work-safe edge | A euphemism or a mild word, never strong profanity | "exactly what the hell you should be building" (7) |
| Invariants | Numbered rule, then a one-line consequence | "If it is not written, it is not committed." (8) |
| State over story | Status as something the reader can point to | "If it cannot be pointed to, it does not exist." (8) |
| Verdict close | End on a short line that judges, not a summary | "Everything else is decoration." (10) |

He avoids these:

- Hedges and consensus language. See sample 10.
- Effort or tools offered as proof of progress. See samples 8 and 9.
- Status told as a narrative instead of a state. See sample 8.
- Praise openers, corporate warmth and motivational filler. No sample has any.

## Keep from the house standard

- Point first. The first line is the claim or the ask.
- Short sentences. One idea each.
- Plain words. The Rule 10 table in `/writing:writing-standard` applies.
- No em-dash asides, even where a sample has one. Write the pivot with a full stop: "Tools don't extract truth. People do."
- No semicolons, emoji or rhetorical questions.
- No marketing adjectives and no hard-wrapped Markdown.
- Every number and name is true and traceable.

## Where the voice departs from the house standard

| House rule | Voice setting |
|---|---|
| Rule 12 bans humour and drama | Dry edge allowed, one or two lines per piece |
| Rule 12 bans metaphor, idiom and personification | One common figure per piece, such as "sprint straight into irrelevance" |
| Rule 12 bans narrative voice | First person and his supplied stories allowed |
| Rule 5 bans the rule-of-three cadence | One triplet or one chain per piece |
| Rule 5 bans "Not X, but Y" | One correction beat per piece, as in sample 1 |
| Rule 5 limits bold | One bold thesis line per piece, a whole sentence if needed |
| Rule 4 bans `literally` and `exactly` | Allowed only to correct a reading, as in sample 1 |
| Rule 7 asks for short paragraphs | One-line paragraphs and fragments allowed as beats |

Every other house rule still applies, including the rest of Rule 4.

## Channels

These rows are defaults and not traits. Every sample so far comes from one essay. Replace a row once David adds a sample for that channel.

| Channel | Shape | Length | Edge |
|---|---|---|---|
| Slack | Point, then evidence | 1 to 4 lines | Mild, internal only |
| Email | Ask in the first line | 3 short paragraphs at most | Mild internal, none external |
| LinkedIn | Claim, story, verdict | Under 250 words | Dry humour, no profanity |
| Essay | Thesis, story, rules, close | As long as the argument | Euphemism allowed |
| Memo with no ask | Bottom line, then owners and dates | One page | None |
| PR description | Change, cause, evidence | Under 200 words | None |

## Steps

1. Read [references/samples.md](references/samples.md).
2. If the text is a team document, stop and apply `/writing:writing-standard` instead. Specs and runbooks are team documents. So are READMEs and DRDs.
3. If the user named a source to rewrite or reply to, read it first.
4. The draft needs a channel, an audience and a point. If the request and the source lack any of them, ask once for all gaps in one message.
5. Write the bottom line as one flat sentence. It opens the piece.
6. If a claim needs evidence, use only facts David gave in this session or in the source he named. The samples set rhythm, never content.
7. If no evidence fits, insert `[STORY: what is needed]` and list it for David.
8. Set shape, length and edge from the channel table.
9. Draft with two to four traits from the traits table. Never all of them.
10. Run the self-check below and fix every miss.
11. If the text is a message, return it in a fenced block ready to paste.
12. If the text is a document David keeps, write it as Markdown in the repo folder he is working in. Link it.
13. If you wrote a file and `/writing:lint` is available, run it on the file. Fix every finding the departures table does not allow.

### Self-check

1. Is the first line the point or the ask?
2. Would David say each sentence aloud to a peer?
3. Does every story, number and name trace to David's input in this session?
4. Is there at most one triplet, one figure of speech and one bold line?
5. Is there a hedge or a line that reads like a motivational post? Cut it.
6. Is there strong profanity? Use a euphemism in internal text. External text has neither, apart from the name Foxtrot Charlie.
7. Does it end on a verdict, not a recap?

## Output

1. Bottom line: one sentence that names the channel and the audience and says whether the draft is ready to send. Then list each placeholder or unconfirmed fact that blocks sending. David owns each one. If none, write "Nothing blocks it".
2. The draft with the point first. It is a fenced block or a linked file.

## Limits

- Never invent a story, a role or a number about David's career.
- Never use this skill for team documents. Those follow `/writing:writing-standard`.
- Never put profanity in external or customer text. The name Foxtrot Charlie is fine.
- Never copy sample sentences or stories into new text. The samples set rhythm, not content.
- Never send the text. Return the draft.
- Never write in another person's voice with this skill.
- Never deliver a document as an HTML artifact.
