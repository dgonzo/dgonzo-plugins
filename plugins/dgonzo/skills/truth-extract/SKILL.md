---
name: truth-extract
description: Use on notes, transcripts, interviews, vendor pitches or threads, such as "what do we actually know" or "separate fact from opinion". Sorts every claim into Grounded, Inferred or Asserted with its source.
---

# truth-extract

This skill produces a truth map that sorts every claim into Grounded, Inferred or Asserted with its source. It counters opinion as fact: a confident sentence in a note gets repeated until the team treats it as evidence.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Forensic: work backward from each claim to the evidence behind it | Each claim traced to its evidence, or to nothing, and put in 1 of 3 classes |
| 2 | Socratic: answer a claim with the question that gets closer to the truth | 1 grounding question per Asserted claim, with who can answer it |
| 3 | Uncertainty: separate what is known, what is inferred and what is assumed | Truth map in 3 tiers, plus at most 7 questions ranked by what rests on them |

The three classes are defined in [references/classification.md](references/classification.md). Read it before pass 1. It settles the hard cases, such as a vendor's own benchmark or a number with no origin.

## Steps

1. If the user pasted the source, use it. If the user named a file or link, read all of it.
2. If the user gave no source, ask once for it and stop until it arrives.
3. If no tool in this session can open the named link, ask once for the text. Stop until it arrives.
4. If the source is a Slack thread, read every reply before classifying anything.
5. Number the source by line or timestamp so every claim can cite a location.
6. List every claim as one sentence in plain words. Split compound sentences into one claim each.
7. Drop greetings, logistics and questions that assert nothing.
8. If a claim cites a file you can open, open it. Check the claim against it. Never search for support the source does not point to.
9. Classify each claim with the rules in the reference file. Record the speaker and the location.
10. If a claim is Inferred, write the premises it rests on. If any premise is Asserted, the claim is Asserted.
11. For each Asserted claim, write the question that would ground it and the person or data that can answer it.
12. Rank the Asserted claims by what depends on them. Put a claim first if a decision, a plan or a number in the source rests on it.
13. Keep the questions for the top 7 Asserted claims. Merge two questions if one answer settles both.
14. Write the report to a Markdown file in the repo folder the user is working in. Name it `truth-extract-<source-slug>.md`. If there is no repo folder, write it beside the source file. If the source was pasted, write it in the current working directory.
15. Reply with the bottom line and a relative link to the file. Do not paste the whole report into the reply.

## Game check

Run after step 9 when a speaker gains if the claim is believed. A vendor, a candidate and an owner reporting on their own work all do.

| Mode | The step |
|---|---|
| Evidence and falsification | Record what the speaker gains. Then name the observation that would prove the claim false |

A claim nothing could prove false stays Asserted. The falsifying observation becomes its grounding question.

## Output

The report has these sections, in this order.

1. Bottom line. One sentence giving Grounded claims out of all claims. Then what the top Asserted claim blocks. Then who owns the question that would ground it.
2. Counts. A table with columns Class and Claims, one row per class.
3. Grounded. A table with columns Claim, Source and Evidence.
4. Inferred. A table with columns Claim, Source and Premises.
5. Asserted. A table with columns Claim, Speaker and Source. Rank rows by what depends on them.
6. Questions to ask. A numbered list, at most 7. Each item gives the question, who can answer it and which claim it would ground.

Output prose follows `writing:writing-standard`. Every claim cites its location in the source. Name every person on first use. Add their role if the source gives it.

## Limits

- Never fills a gap with outside knowledge or a web search. A claim the source does not support stays Asserted, even if it is true.
- Never upgrades a claim because the speaker is senior, confident or repeats it.
- Never judges whether an Asserted claim is wrong. Asserted means unsupported, not false.
- Never recommends a decision. Use `dgonzo:decision-forge` or `dgonzo:build-vs-buy` for that.
- Never traces the cause of an incident. Use `dgonzo:postmortem` for that.
- Never edits the source.
- Never writes the report as an HTML artifact.
