---
name: voice
description: Draft or rewrite text in David's own professional voice for anything sent under his name. Covers Slack messages, emails, LinkedIn opinion posts, essays and memos. Name first, then the ask. Owners named, numbers as receipts, short and warm at work. Flat conviction in essays. Use for "write this in my voice", "make this sound like me", "draft a Slack reply from me", "reply to this as me" or "rewrite my email". Also for dgonzo:voice. Not for team documents or a plain PR description, which follow writing:writing-standard. Not for a launch post, blog post or demo about something built, which is dgonzo:signal-cut. Not for an internal Slack announcement, which is /slack:draft-announcement. Not for a brief that asks executives for a decision, which is dgonzo:exec-brief.
---

# voice

This skill produces a draft that reads as David wrote it, ready for him to send under his name. It counters the generic voice: correct, polite prose that no reader would attribute to him.

David writes in two registers. The work register covers Slack and email, and it is the default. The essay register covers LinkedIn opinion posts and essays. Pick the register before drafting.

Read [references/samples.md](references/samples.md) before every draft. If `~/.config/dgonzo/voice-samples.md` is accessible, read it too. Otherwise use `~/.claude/dgonzo/voice-samples.md` when accessible. In a remote chat, use a private reference supplied by David if available. Do not assume access to files on his machine. Keep verbatim private messages out of this public repo.

## Work register

| Trait | Do | Pattern |
|---|---|---|
| Name first | Open with the reader's name and a comma, then the point or ask | "<Name>, looks very good." |
| Polite direct ask | Ask with "would you", one ask per person | "<Name>, would you grab these and we'll discuss." |
| Owner named | Say who does the next step, by name | "I'll draft a spec with <Name>." |
| Numbers as receipts | Give the figure that backs the claim | "85% coverage, which we're ok with" |
| Short replies | A one-line reply is enough when one line answers | "These will be done." |
| Plain warmth | One short line of thanks, no gushing | "Really appreciate it." |
| One real question | End on the single question that unblocks him | "Is there anything I can do from my end?" |
| Sign-off | `--dg` on email, none on Slack | `--dg` |
| Structure for big asks | Ask, amount and deadline first, then capitalised labels | `WHAT`, `WHY`, `WHEN`, `COST`, `ASK` |

Slack may be lowercase and casual in a one-line DM. Never add typos. One Slack emoji code is fine in a warm internal message, such as `:slightly_smiling_face:`.

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

## Both registers avoid

- Hedges and consensus language.
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
| Slack team post | Work | Change, owners, goal date and thanks | Under 300 words |
| Email | Work | Name, point, ask, `--dg` | 1 to 3 short paragraphs |
| Email asking approval | Work | Labelled sections, ask first | One screen |
| LinkedIn | Essay | Claim, story, verdict | Under 250 words |
| Essay | Essay | Thesis, story, rules, close | As long as the argument |

## Steps

1. Read the sample files named above.
2. If the text is a team document, stop and apply `writing:writing-standard` instead.
3. If the user named a source to rewrite or reply to, read it first.
4. If the channel or the reader or the point is missing, ask once. Put all gaps in one message.
5. Pick the register and the channel row.
6. Write the first line. In the work register it is the name, then the point or ask.
7. Use only facts David gave in this session or in the source he named. The samples set rhythm, never content.
8. If a claim needs evidence that is missing, insert `[FACT: what is needed]` and list it for David.
9. Draft with the traits of the chosen register. Use two to four essay traits, never all.
10. Run the self-check and fix every miss.
11. If the text is a message, return it in a fenced block ready to paste.
12. If the text is a document David keeps, write it as Markdown in his working repo folder. Link it.

### Self-check

1. Is the first line the name and the point, or the claim?
2. Would David send each sentence to this reader?
3. Does every name, number and story trace to David's input?
4. Does each next step have a named owner?
5. Is there a hedge, a gush or a line that reads like a motivational post? Cut it.
6. Is the length inside the channel row?
7. Does an email end with `--dg`?

## Output

1. Bottom line: one sentence that names the channel and the reader and says whether the draft is ready. List each placeholder that blocks sending, or write "Nothing blocks it".
2. The draft, in a fenced block or a linked file.

## Limits

- Never invent a story or a role.
- Never invent a name or a number.
- Never copy sample text or sample facts into new text.
- Never put profanity in external or customer text.
- Never send the text. Return the draft.
- Never copy text from the private samples file into this repo.
- Never deliver a document as an HTML artifact.
