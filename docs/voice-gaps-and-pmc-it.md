# Voice gaps and the pmc-it skill

Written after the canon charter deck. The review of that deck read Peter correctly. The deck built against the review failed five times on voice and twice on design. This document says why the skills let that happen. It states David's voice in a form a skill can enforce. It lists the changes for this repo and for data-org.

## Bottom line

The skills describe the voice. Nothing forces a draft through it. `voice` has a traits table and a self-check. It has no per-sentence gate and no ban list for the failure modes the deck showed. It has no channel for a deck. `audience-model` writes a reader file that no other skill reads. `exec-brief` translates jargon the exec would look up and lets internal coinages through. The fix is one private readers folder and one generation gate in `voice`. Then one new skill, `pmc-it`, and four small edits elsewhere. Nothing is blocked. David owns the merge.

## What David's voice is

David's correction of Gemini is the definition: "My authentic voice moves through technically accurate and emotionally honest." Gemini's first attempt was theatrical. Its second was corporate. Neither was him.

Three ingredients, each with a sample from his own writing.

| Ingredient | What it does | His line |
|---|---|---|
| Precision | The exact number, name or noun. Never a category word | "We compared your UPCs with our scanned and got almost 85% coverage" |
| Honesty | The state as it is, the feeling about it in a few plain words | "which we're ok with, we have avenues to fill the remainder" |
| Ownership | Who does the next thing, by name | "I'll draft a spec with Tolga to deliver this" |

The edge in Foxtrot Charlie comes from the same three. "If it cannot be pointed to, it does not exist" is precision and honesty in nine words. The profanity is a work-safe euphemism used once. The strength is never in the adjective.

What he wrote on the deck, in order, is the clearest sample set we have.

| He rejected | He wrote |
|---|---|
| "A zero target is a wrong-value target." | "At 100% we publish wrong values." |
| "At 100% we publish wrong values." | "At 0% human we publish mistakes." |
| "One number is yours." | He called it obtuse. The fix was "You set one target." |

Each rewrite is shorter, has a plainer noun, and puts "we" first.

## The five voice failures, and the anti-pattern each one names

| Anti-pattern | What it looks like | Where it showed | Test that catches it |
|---|---|---|---|
| Theatrical | Strength from the adjective or the imperative. "Hunt Down the Uncomfortable Truth" | Gemini's first pass | Delete the adjective. If the sentence loses its force, it had none |
| Corporate | Abstract nouns in place of the thing. "Operational contracts", "architectural principles" | Gemini's second pass | Can you point at it? A contract is a file. Name the file |
| Cute | Force from rhythm or word order, not fact. "Three conditions. Three legs. One owner each." | Deck v1, slide 3 | Rewrite as one plain sentence. If nothing is lost, it was rhythm |
| Coy | Withholding the noun for effect. "One number is yours" | Deck v3, slide 2 | Name the noun in the first clause |
| Coined | An internal term standing in for a plain fact. "Wrong-value target", "envelope", "stubbed" | Deck v3, slide 2 | Could the reader say it back in their next email? If not, it is ours, not theirs |

Two more failures were not voice. They were design.

| Failure | What the skills said | Why it happened anyway |
|---|---|---|
| Uniform card grids, pretty over informative | Nothing. No skill covers slides | The Slides type's own guidance says "statement beats bullets, cards, one idea per slide". That is the opposite of David's "informative at a glance" |
| Numbers with no target and no verdict | `ragb` ties status to an artifact. Nothing says a measurement on a slide carries its target | The rule lives in the wrong skill |

## Why the review was right and the build was wrong

The review ran `audience-model` and `lens` and produced a correct read: six slides, his words, no IDs, lead with his own two documents. The build then produced eight slides, IDs, coined terms and card grids. The gap is structural. Analysis skills end in a file. Generation skills start from the prompt. Nothing makes generation read the analysis file line by line and check the draft against each row.

The fix is a gate, not more description. A gate is a list the draft must pass, row by row, with the row cited.

## Changes to the dgonzo plugin

### voice, 1.1.0 to 1.2.0

1. Add one line at the top: "David's voice is technically accurate and emotionally honest. Precision, honesty, ownership. The edge comes from the fact, never from the adjective."
2. Add the anti-pattern table above, with the five tests.
3. Add a generation gate, run on every sentence before output.

| Gate | Pass when |
|---|---|
| Subject | "We", "I" or a named person is the subject. No passive |
| Noun | A number, a name or a concrete noun is in the sentence |
| State | It says what is, including what is bad, in plain words |
| Owner | If it describes a next step, it names who |
| Repeat | The reader could say it back verbatim in their next email |
| Whole | A reader's own words appear whole. A mandate is never shortened into shorthand |

4. Add a Presentation channel row. Register work. Shape: the decision, the reader's words as headings, tables with a status column, an appendix for everyone else. Length: seven slides for the decider.
5. Require the full essay before an essay or a presentation: `~/Projects/MyTools/gwrk/docs/product/FOXTROT-CHARLIE.md`. The ten excerpts in samples.md are rhythm. The essay is posture.
6. Add samples 17 to 19 to the private samples file: the three deck rewrites above and "canon is our single most impressive and comprehensive moat. Working with it has challenges."

### audience-model

1. Write the model to `~/.claude/dgonzo/readers/<name>.md` when the reader is a real person. The repo folder only when David asks. Real people's reading habits and their quoted email do not belong in a public plugin or a team repo.
2. Add three sections: "His vocabulary", "What loses him", "What he does with the thing you send". The Peter file in the readers folder is the model.
3. Add the Repeat test to Calibration.

### exec-brief

1. Step 5 reads `~/.claude/dgonzo/readers/<exec>.md` when it exists. Every pass cites rows from it.
2. Pass 1, the translator, gains a second list: internal coinages. Any term that exists only in our documents gets replaced or cut, even when the exec could guess it.
3. Pass 3, the modeling pass, predicts the exec's first question from the reader file, not from the brief. If the answer is "what is it today" and the brief has no today number, the ask is wrong in sequence. Say so.
4. Add the deck shape from the voice channel row.
5. Never a placeholder date. The deadline is the reader's own, or "set in the room".

### working-style

1. "When David corrects voice, re-read the source document before the next draft. Not the summary of it."
2. "Never publish over a file David is editing live. Wait, say so, or hand him the one-line change."
3. "A review that reads the audience correctly and a draft that ignores it is one failure, not a partial success."

### New skill: pmc-it

Get a thing in shape for Peter. The name is his initials. The skill is a gate over any artifact, a deck, a doc, an email or a Slack message, that makes it read the way he reads.

Draft SKILL.md:

```markdown
---
name: pmc-it
description: Get any artifact in shape for Peter Castleman, CEO, before he sees it. A deck, a memo, an email or a Slack message. Leads with the one decision that is his, uses his own words whole, gives every number its target and a verdict, and strips everything he calls noise. Use for "get this ready for Peter", "pmc this", "will this land with Peter" or /dgonzo:pmc-it. Not for modelling him (audience-model) or for a generic exec (exec-brief).
---

# pmc-it

Produces a Peter-ready version of an artifact and predicts his reply. It counters the deck or memo that is organised by our structure instead of his.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Reductive | The one decision that is his, the one number he needs, the two facts that make it his problem |
| 2 | Modeling | His first question and where he stops reading, from the reader file |
| 3 | Translator | Every term replaced with his, every coinage cut |

## Steps

1. Read `~/.claude/dgonzo/readers/peter.md`. If it is missing, stop and say so. Never model him from memory.
2. Read the artifact.
3. Load `/dgonzo:voice`. Run its gate on every sentence you write.
4. Run pass 1. Write the decision as one sentence with a verb he performs. If the artifact asks him for a number nobody has measured, change the ask: measure first, then he sets it.
5. Find his own documents the artifact should quote. Quote them whole. His three conditions are never shortened.
6. Run pass 3. Cut every ID, tool name, repo name and internal coinage. Replace with his vocabulary from the reader file.
7. Give every number a target and a verdict word. Fails, passes, unmeasured. Never a number alone.
8. Cut to his length. Two lines before the ask. One page, or seven slides, for him. Everything else is an appendix for the room.
9. Run pass 2 on the result. Predict his first question and his first next action. If the first question is answered nowhere in the first two lines, go back to step 4.
10. Write the result beside the source as `<name>-pmc.md`, or edit the deck in place when asked.
11. Report the prediction and what you cut.

## Output

1. Bottom line: the one decision and whether the artifact now leads with it.
2. The artifact, or the link.
3. His predicted first question and first next action.
4. What was cut, one line per item.

## Limits

- Never invents a number, a date or a quote of his.
- Never shortens his words.
- Never puts the reader file, or any quote from his email, into a team repo or a public plugin.
- Never sends. David sends.
```

The reader file is already written at `~/.claude/dgonzo/readers/peter.md`.

## Changes to the writing plugin

1. Rule 7, tables. Add: "A table that shows a measurement shows its target beside it and a verdict word. A number the reader cannot judge is decoration."
2. Rule 10, plain words. Add a passive hunt list to the check before you send: "is decided", "are marked", "is named", "is written", "is measured", "are recorded".
3. `writing:lint`. Accept a slide `.html` file and lint its text. Slide text with passives the Markdown linter would have caught.

## Changes to data-org

The team repo cannot depend on David's personal plugin and must not carry Peter's reading habits. These are the generic versions.

| File | Change |
|---|---|
| `standards/writing.md` | Add the measurement rule from writing Rule 7. Add: "Quote a stakeholder's words whole. Never shorten a mandate into a label" |
| `plugins/data-org/skills/report/SKILL.md` | Add a Reader line to the memo front matter. "Who reads it, what they decide." An exec memo is one page and the `Re:` block is the whole ask |
| `plugins/data-org/skills/improve-readability/SKILL.md` | Add two checks. Every measurement carries a target and a verdict. Every stakeholder quote matches its source |

## An eval worth running

Ten lines David wrote. Ten lines a skill wrote in his voice. Shuffle. He marks each as his or not. Below 8 of 10 correct on the generated set, the gate is not working. The `evals/` folder already has the harness shape.

## Order

1. Merge the reader file and the voice gate. One day.
2. Add `pmc-it`. Run it on the charter deck as the first test.
3. Then the writing rule 7 and the data-org standard, as one PR each.
