---
name: pmc-it
description: Get any artifact in shape for Peter Castleman, CEO, before he sees it. A deck, a memo, an email or a Slack message. Leads with the one decision that is his, uses his own words whole, gives every number its target and a verdict, and strips everything he calls noise. Use for "get this ready for Peter", "pmc this", "will this land with Peter" or /dgonzo:pmc-it. Not for modelling him (audience-model) or for a generic executive (exec-brief).
---

# pmc-it

Produces a Peter-ready version of an artifact and predicts his reply. It counters the deck or memo organised by our structure instead of his.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Reductive: start from ground truth and drop inherited assumptions | The one decision that is his, the one number he needs, the two facts that make it his problem |
| 2 | Modeling: simulate how one named person responds, specifically | His first question and where he stops reading, from the reader file |
| 3 | Translator: rewrite for someone smart but outside the field | Every term replaced with his, every coinage cut |

## Steps

1. Read `~/.claude/dgonzo/readers/peter.md`. If it is missing, stop and say so. Never model him from memory.
2. Read the artifact.
3. Load `/dgonzo:voice`. Run its gate on every sentence you write.
4. Run pass 1. Write the decision as one sentence with a verb he performs. If the artifact asks him for a number nobody has measured, change the ask. Measure first, then he sets it.
5. Find his own documents the artifact should quote. Quote them whole. His conditions and mandates are never shortened.
6. Run pass 3. Cut every ID, tool name, repo name and internal coinage. Replace with his vocabulary from the reader file.
7. Give every number a target and a verdict word. Fails, passes or unmeasured. Never a number alone.
8. Cut to his length. Two lines before the ask. One page, or seven slides, for him. Everything else is an appendix for the room.
9. Run pass 2 on the result. Predict his first question and his first next action. If the first two lines do not answer the first question, go back to step 4.
10. Write the result beside the source as `<name>-pmc.md`, or edit the deck in place when asked.
11. Report the prediction and what you cut.

## Output

1. Bottom line: the one decision, and whether the artifact now leads with it.
2. The artifact, or the link.
3. His predicted first question and first next action.
4. What was cut, one line per item.

## Limits

- Never invents a number, a date or a quote of his.
- Never shortens his words.
- Never puts the reader file, or any quote from his email, into a team repo or this plugin.
- Never sends. David sends.
