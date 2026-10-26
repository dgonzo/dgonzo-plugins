---
name: lens
description: Run one or more of 45 named reasoning modes on a doc, plan, decision or thread. Each mode gets its own section, then a short note on what changed in the user's view. Use for "run a pre-mortem on this", "steel-man this argument", "play devil's advocate", "look at this through a lens" or "what would a skeptic say". Also for /dgonzo:lens with an optional mode name, such as /dgonzo:lens skeptic. Not for a job a dgonzo compound skill owns, such as a full decision test (decision-forge), a plan review (architecture-stress-test), checking claims in notes (truth-extract), a candidate debrief (hiring-debrief), a postmortem (postmortem) or a status report (ragb).
---

# lens

Produces one section per reasoning mode applied to the input, then a note on what changed in the user's view. It counters the default lens: an unprompted model answers in the safe analytical mode, whatever the problem needs.

The 45 modes, their prompts and when to use each are in [references/modes.md](references/modes.md).

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | First lens, named by the user or picked in step 5 | Its modes.md prompt run on the input, with at most 5 findings or the output the prompt asks for |
| 2 | Second lens, if any | Same rules, with no finding from pass 1 repeated |
| 3 | Third lens, if any | Same rules, with no finding from earlier passes repeated |
| 4 | Integrative: merge the outputs of several modes into one view with no redundancy | Lens results merged with no repeats, then what changed in at most 3 bullets |

## Steps

1. If the user named an input, read it.
2. If the user named no input, use the target already in the conversation. If there is none, ask once what to look at.
3. If the input is a link or file you cannot open, say so in one sentence and stop.
4. If the user named one or more modes, look each up in modes.md by name or lookup name. Run every mode the user named, in the order given.
5. If the user named no mode, pick at most three from the table below or from modes.md. Prefer modes from different categories. Give one line per mode on why it fits.
6. If a mode name matches nothing in modes.md, name the closest mode and run it. Say which name you matched.
7. If the picked modes match a stack under Common stacks, name that skill in one line. Then run the lenses as asked.
8. Fill each placeholder in the prompt from the input, for example `[X]`. Name what you filled in.
9. If a prompt opposes "my position" and the user stated none, use the input's main claim. Say so.
10. Run each mode as its own section. Never blend two modes in one section.
11. If a mode's prompt asks for new output in place of a critique, treat it as a producing mode. Generative, Editor and Planning are examples. Treat every other mode as a finding mode.
12. For a finding mode, list findings and tie each to a quote or line.
13. For a producing mode, give the output its prompt asks for. Keep any count the prompt names, such as 15 ideas.
14. For Interviewer or Socratic, list the questions and stop that section. Never answer them for the user.
15. If a lens finds nothing, say so in one line. Never pad a section.
16. Run pass 4 when two or more lenses ran. After a single lens, state what changed in one line.
17. If the user asks to keep the result, write `lens-<topic>.md` in their working repo folder. Link the file. Otherwise answer in the chat.

## Which lens for which problem

| Problem | Lens |
|---|---|
| A plan you are about to commit to | Pre-mortem |
| An argument you want to dismiss | Steel-man |
| Claims with no source | Skeptic |
| A position nobody challenges | Devil's Advocate |
| A doc full of jargon for outsiders | Translator |
| More work than capacity | Prioritizing |
| A strategy with no next step | Operator |
| An estimate that sounds sure of everything | Calibration |
| A failure with a convenient story | Forensic |
| One option judged alone | Comparative |

## Common stacks

Three modes in a fixed order counter one failure mode. These stacks have their own skills in this plugin. Use the skill when the job matches.

| Job | Stack | Skill |
|---|---|---|
| Test a pending decision | Adversarial, Steel-man, Calibration | `/dgonzo:decision-forge` |
| Check claims in notes or transcripts | Forensic, Socratic, Uncertainty | `/dgonzo:truth-extract` |
| Review the phases of a plan | Analytical, Pre-mortem, Comparative | `/dgonzo:architecture-stress-test` |
| Name a product or command | Dialectical, Aesthetic, Combinatorial | `/dgonzo:naming-forge` |
| Choose to build or buy | Comparative, Operator, Futurist | `/dgonzo:build-vs-buy` |
| Write a status report | Forensic, Calibration, Reductive | `/dgonzo:ragb` |
| Hand off work | Reductive, Interviewer, Planning | `/dgonzo:owner-brief` |
| Cut a backlog | Prioritizing, Counterfactual, Reductive | `/dgonzo:cut-list` |
| Explain a failure | Forensic, Counterfactual, Historian | `/dgonzo:postmortem` |
| Debrief a hiring loop | Forensic, Calibration, Devil's Advocate | `/dgonzo:hiring-debrief` |
| Write a launch post | Narrative, Subversive, Practitioner | `/dgonzo:signal-cut` |
| Write a tagline or position | Reductive, Comparative, Aesthetic | `/dgonzo:position-lock` |
| Model a reader | Modeling, Interviewer, Forensic | `/dgonzo:audience-model` |
| Brief an executive | Translator, Reductive, Modeling | `/dgonzo:exec-brief` |

These stacks from the source have no skill. Run them as `/dgonzo:lens` with all three modes named.

| Job | Stack |
|---|---|
| Create something | Generative, Subversive, Aesthetic |
| Make a high-stakes call | Forensic, Audit, Pre-mortem |
| Say something hard | Adversarial, Editor, Calibration |
| Learn a topic fast | Reductive, Metaphorical, Teacher |

## Output

1. Bottom line. The strongest result across all lenses in one sentence. Then what it blocks and who owns it. Write "Nothing blocked" if nothing is. Write "owner not named" if the input names none.
2. Lenses. One line per mode with its name and why it ran.
3. One section per lens, headed with the mode name. A finding lens lists findings, each tied to a quote or line. A producing lens gives its output.
4. What changed. The user's view before and after, in at most 3 bullets.

Output prose follows `/writing:writing-standard`.

## Limits

- Never runs more than three lenses unless the user names more.
- Never edits the input. Editor output is a proposed rewrite.
- Never invents evidence. A finding with no quote or line behind it is labelled as inference.
- Devil's Advocate and Contrarian argue a side. Label their output as argument, not verdict.
- Never writes an HTML artifact.
- Never depends on gwrk or files under `~/.gwrk`.
