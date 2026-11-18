---
name: voice
description: Use for any text sent under David's name, such as Slack, email, LinkedIn, an essay or a memo. Triggers are "in my voice", "reply as me" and "draft a Slack from me". Not for team documents, which follow writing:writing-standard.
---

# voice

This skill produces a draft that reads as David wrote it, ready for him to send under his name. It counters the generic voice: correct, polite prose that no reader would attribute to him.

David's voice is technically accurate and emotionally honest. Three ingredients carry it. Precision is the exact number, name or noun, never a category word. Honesty is the state as it is, the bad included, and how he feels about it in a few plain words. Ownership is who does the next thing, by name. The edge comes from the fact, never from the adjective.

David writes in two registers. The work register covers Slack and email, and it is the default. The essay register covers LinkedIn opinion posts and essays. Pick the register before drafting.

Read [references/samples.md](references/samples.md) before every draft. If `~/.config/dgonzo/voice-samples.md` is accessible, read it too. Otherwise use `~/.claude/dgonzo/voice-samples.md` when accessible. In a remote chat, use a private reference supplied by David if available. Do not assume access to files on his machine. Open the private file with a file read, never a shell test. A check that prints nothing does not prove the file is absent. Keep verbatim private messages out of this public repo.

## Work register

| Trait | Do | Pattern |
|---|---|---|
| Name first | Open with the reader's name and a comma, then the point or ask | "<Name>, looks very good." |
| Polite direct ask | Ask with "would you", one ask per person | "<Name>, would you grab these and we'll discuss." |
| Owner named | Say who does the next step, by name | "I'll draft a spec with <Name>." |
| Numbers as receipts | Give the figure that backs the claim | "85% coverage, which we're ok with" |
| Short replies | A one-line reply is enough when one line answers | "These will be done." |
| Plain warmth | One short line of thanks, no gushing | "Really appreciate it." |
| One real question | Ask the single question that unblocks him. Only when he is blocked, never as a closer in place of an ask | "Is there anything I can do from my end?" |
| Sign-off | `--dg` on email, none on Slack | `--dg` |
| Position he holds | State it once with "I think". No second softener | "I think <position>." |
| Dated ask | Give every ask a day | "<Name>, would you <verb> <thing> by <day>?" |
| Question with no view yet | Open with "I think" when the team has not settled it and he holds no view | "I think there may be <issue>." |
| Position, then delegate | In an ask to a lead, say what he wants true, then ask them to work it out | "We should make sure <outcome>. <Name>, would you work with folks here to determine <detail>." |
| Thing named in the ask | Repeat the noun in place of "that" | "is <thing> the right done for <team>?" |
| Structure for big asks | Ask, amount and deadline first, then capitalised labels | `WHAT`, `WHY`, `WHEN`, `COST`, `ASK` |

Slack may be lowercase and casual in a one-line DM. Never add typos. One Slack emoji code is fine in a warm internal message, such as `:slightly_smiling_face:`.

### Opening a team discussion

Use this section only when David holds no view yet. Ask him if it is unclear. When he holds a view, the post states it once with "I think" and no second softener. Then it gives each lead an ask with a day.

With no view yet, David opens a question for the team to work out. He does not announce a verdict. A flat verdict on an open question reads as the decision already made.

| Miss | Do not write | Write |
|---|---|---|
| Verdict on the team | "We've been using <wrong thing>." | "I think there may be <issue>." |
| Consequence framed for effect | "The answer changes how we read <number>." | "The answer must be aligned for <scope>." |
| Quiz question to a lead | "<Name>, which <items> count <x>?" | "We should make sure <outcome>. Would you work with folks here to determine <detail>." |
| Challenge to the room | "Everyone else, tell me where this is wrong." | No line |

Close a channel post with a thread request and its reason. "Please reply in thread to keep the main channel easier to work in."

In-message headings on Slack are numbered and italic, as in `_1. <heading>_`. Never bold.

A long email that reasons out loud does not land with executives. A structured ask with the decision in the first line gets a fast yes. For an exec, use `dgonzo:exec-brief`.

## Essay register

| Trait | Do | Sample |
|---|---|---|
| Flat conviction | State the claim with no hedge | 1 |
| One-line beats | Give a turn its own line, two or three per piece | 2 |
| Concede, then strike | Grant the other side in one sentence, then show its limit | 3 |
| Company stories | One named story per claim, with the outcome | 4 |
| Name the unpopular part | Flag the claim people avoid, then make it | 5 |
| Chains and mantras | One causal chain of three or four links | 6 |
| Work-safe edge | A euphemism or a mild word, never strong profanity | 7 |
| Invariants | Numbered rule, then a one-line consequence | 8 |
| Verdict close | End on a short line that judges, not a summary | 10 |

## What the voice is not

Five ways a draft misses while sounding strong. Each has a test.

| Miss | What it looks like | Test |
|---|---|---|
| Theatrical | Force from the adjective or the imperative. "Hunt down the uncomfortable truth" | Delete the adjective. If the sentence loses its force, it had none |
| Corporate | An abstract noun in place of the thing. "Operational contract", "architectural principle" | Point at it. A contract is a file. Name the file |
| Cute | Force from rhythm or word order. "Three conditions. Three legs. One owner each." | Rewrite as one plain sentence. If nothing is lost, it was rhythm |
| Coy | The noun withheld for effect. "One number is yours" | Put the noun in the first clause |
| Coined | An internal term standing in for a plain fact. "Envelope", "stubbed", "wrong-value target" | Could the reader say it back in their next email? If not, it is ours, not theirs |

## Both registers avoid

- Hedges on a claim or a status, and consensus language. "I think" once on a view he holds is a position, not a hedge. A second softener is a hedge.
- A question where he holds a view.
- An ask with no day.
- Blame of a person, and doom. A problem comes with its next move.
- Motivational filler.
- Effort or tools offered as proof of progress.
- Status told as a story instead of a state.
- Praise openers and corporate warmth.

## Keep from the house standard

- Point first. In the work register, the name comes before it.
- Short sentences with one idea each.
- Plain words.
- No em-dash asides and no semicolons. Write the pivot with a full stop.
- No marketing adjectives and no hard-wrapped Markdown.
- Every number and name is true and traceable.

## Where the essay register departs from the house standard

| House rule | Essay setting |
|---|---|
| Rule 12 bans humour, drama and narrative voice | Dry edge, first person and his own stories allowed |
| Rule 12 bans metaphor and idiom | One common figure per piece |
| Rule 5 bans rule-of-three and "Not X, but Y" | One triplet or chain, one correction beat per piece |
| Rule 5 limits bold | One bold thesis line per piece |
| Rule 7 asks for short paragraphs | One-line paragraphs and fragments allowed as beats |

The work register departs only in small ways. It allows greetings and sign-offs. Slack may use lowercase and emoji codes.

## Channels

| Channel | Register | Shape | Length |
|---|---|---|---|
| Slack DM or thread | Work | Name, ask, owner | 1 to 4 lines |
| Slack team announcement | Work | Change, owners, goal date and thanks | Under 300 words |
| Slack team position | Work | His view once as "I think", numbered italic headings, one ask per lead with a day, thread request | Under 300 words |
| Slack team discussion | Work | Only with no view yet. The issue as "I think there may be", numbered italic headings, one ask per person, thread request | Under 300 words |
| Email | Work | Name, point, ask, `--dg` | 1 to 3 short paragraphs |
| Email asking approval | Work | Labelled sections, ask first | One screen |
| LinkedIn | Essay | Claim, story, verdict | Under 250 words |
| Essay | Essay | Thesis, story, rules, close | As long as the argument |
| Presentation to a decider | Work | The decision first, the reader's own words as headings, tables with a status column, an appendix for the room | Seven slides for the decider |

## Steps

1. Read the sample files named above. For the essay register or a presentation, read the full essay at `~/Projects/MyTools/gwrk/docs/product/FOXTROT-CHARLIE.md` as well. The excerpts give rhythm. The essay gives posture.
2. If the text is a team document, stop and apply `writing:writing-standard` instead.
3. If the reader has a file at `~/.claude/dgonzo/readers/<name>.md`, read it. Cite its rows when you check the draft.
4. If the user named a source to rewrite or reply to, read it first.
5. If the channel or the reader or the point is missing, ask once. Put all gaps in one message.
6. Pick the register and the channel row. For a Slack team post, decide first whether David announces a change, states a position or opens a question. He opens a question only when he holds no view.
7. Write the first line. In the work register it is the name, then the point or ask.
8. Use only facts David gave in this session or in the source he named. The samples set rhythm, never content.
9. If a claim needs evidence that is missing, insert `[FACT: what is needed]` and list it for David.
10. Draft with the traits of the chosen register. Use two to four essay traits, never all.
11. Run the gate and the self-check and fix every miss.
12. If the text is a message, return it in a fenced block ready to paste.
13. If the text is a document David keeps, write it as Markdown in his working repo folder. Link it.

### The gate

Run on every sentence before output. A sentence that fails a row gets rewritten, not excused.

| Gate | Pass when |
|---|---|
| Subject | "We", "I" or a named person is the subject. No passive |
| Noun | A number, a name or a concrete noun is in the sentence |
| State | It says what is, the bad included, in plain words. On an open question, "I think" and the issue named |
| Owner | If it describes a next step, it names who |
| Repeat | The reader could say it back verbatim in their next email |
| Whole | A reader's own words appear whole. A mandate is never shortened into shorthand |
| Position | Where David holds a view, the sentence states it. It does not ask it |
| Day | An ask names a day |
| Above the line | No blame of a person and no doom. A problem carries its next move |

### Self-check

1. Is the first line the name and the point, or the claim?
2. Would David send each sentence to this reader?
3. Does every name, number and story trace to David's input?
4. Does each next step have a named owner?
5. Is there a hedge on a claim or a status? A gush or a line that reads like a motivational post? Cut it.
6. Does a post that opens a question state a verdict, quiz a lead or challenge the room? Rewrite it from the discussion table.
7. Does David hold a view that the draft asks as a question? State it once with "I think".
8. Does every ask name a day? Does the draft close on an ask, not on an offer to help?
9. Is the length inside the channel row?
10. Does an email end with `--dg`?

## Output

1. Bottom line: one sentence that names the channel and the reader and says whether the draft is ready. List each placeholder that blocks sending, or write "Nothing blocks it".
2. The draft, in a fenced block or a linked file.

## Limits

- Never invent a story or a role.
- Never invent a name or a number.
- Never copy sample text or sample facts into new text.
- Never shorten a reader's own words into shorthand.
- Never carry a reader file, or a quote from a reader's email, into a team repo or this plugin.
- Never put profanity in external or customer text.
- Never send the text. Return the draft.
- Never copy text from the private samples file into this repo.
- Never deliver a document as an HTML artifact.
