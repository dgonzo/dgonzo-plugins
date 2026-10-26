# Reasoning modes

This file lists all 45 reasoning modes in 7 categories. Each entry gives the mode's lookup name and purpose. Then it gives the prompt and when to use it.

The `lens` skill reads this file. The lookup name is what follows `/dgonzo:lens`, as in `/dgonzo:lens skeptic`. Each prompt keeps the source wording in sentence case. Fill any placeholder such as `[X]` from the input before running the prompt.

| Category | Modes | Job |
|---|---|---|
| Reasoning | 8 | How to think |
| Evaluative | 6 | Find the cracks |
| Creative | 6 | Break the default answer |
| Persona | 8 | Decide who is in the room |
| Communication | 6 | Change how the answer lands |
| Operational | 6 | Move from thinking to doing |
| Meta | 5 | Question the reasoning itself |
| Total | 45 | |

## Reasoning

### Analytical

Lookup: `analytical`. Break the subject down and find its structure.

> "Break down to its core structure. What are the components and how do they relate?"

Use when the parts of a system or argument and the links between them are unclear.

### Synthetic

Lookup: `synthetic`. Connect separate ideas into one framework.

> "What do these things have in common at a deeper level? Build me a unified framework."

Use when several threads look separate and may share one cause.

### Dialectical

Lookup: `dialectical`. State the thesis and the antithesis. Then resolve them into a synthesis.

> "Argue both sides with full commitment, then resolve the tension into a single position."

Use when a choice has two real camps and you need one position at the end.

### Forensic

Lookup: `forensic`. Work backward from an outcome to its causes.

> "This failed. Work backward and identify the root causes, not the symptoms."

Use when something has already gone wrong and the current story names a symptom.

### Probabilistic

Lookup: `probabilistic`. Weight the uncertainty of each claim.

> "Give your confidence level on each. Separate what you know from what you're inferring."

Use for a forecast or a bet where the claims carry different weight.

### Counterfactual

Lookup: `counterfactual`. Explore what did not happen.

> "What if [X] had never existed? Trace the alternate path forward."

Use when you need to know what one factor contributed. Remove it and trace the result.

### Reductive

Lookup: `reductive`. Strip to first principles and drop the rest.

> "Ignore conventional wisdom. Remove inherited assumptions. Start from ground truth only."

Use when a proposal rests on habit and you want the ground truth.

### Expansive

Lookup: `expansive`. Widen the field before narrowing it.

> "Generate maximum surface area before filtering. Volume first, judgment second."

Use early in a problem, when the first option on the table is the only one anyone has considered.

## Evaluative

### Adversarial

Lookup: `adversarial`. Attack the idea and find every crack.

> "You're a skeptic who needs to be convinced. Attack this with everything you have."

Use on your own proposal before it meets a critical audience.

### Steel-man

Lookup: `steel-man`. Build the strongest form of the other side before critiquing it.

> "Build the strongest possible version of the opposing argument before you respond."

Use when you are about to dismiss an opposing view.

### Pre-mortem

Lookup: `pre-mortem`. Assume the plan failed and work back to the causes.

> "This failed 6 months from now. What were the most likely causes?"

Use on a plan or launch you are about to commit to.

### Audit

Lookup: `audit`. Map every assumption in a fixed order.

> "List every assumption this depends on. For each one, what breaks if it's wrong?"

Use when a plan rests on assumptions nobody has written down.

### Comparative

Lookup: `comparative`. Judge against alternatives, never alone.

> "Don't evaluate this alone. Compare it against the 3 most viable alternatives."

Use when one option is being judged with nothing beside it.

### Calibration

Lookup: `calibration`. Rate confidence for each part.

> "Rate your confidence 1-10 on each section. Where are you most likely to be wrong?"

Use on a doc or estimate that sounds equally sure about everything.

## Creative

### Generative

Lookup: `generative`. Produce ideas with no filter.

> "No filtering. Give me 15 ideas including the ones that seem too weird."

Use when there is one idea and you need options.

### Combinatorial

Lookup: `combinatorial`. Force a link between two unrelated fields.

> "Apply [X] principles to [Y]. What unexpected solutions emerge from that collision?"

Use when a problem is stuck in its own field's habits. Name the borrowed field in the section.

### Subversive

Lookup: `subversive`. Break the obvious approach on purpose.

> "What's the least expected solution that still actually works?"

Use when every option on the table looks like what everyone else does.

### Aesthetic

Lookup: `aesthetic`. Optimize for elegance as well as correctness.

> "What's the most beautiful version of this? Optimize for elegance over efficiency."

Use on a design or doc that works and is clumsy to use or read.

### Narrative

Lookup: `narrative`. Frame the subject as a story. Useful to persuade.

> "Turn this into a story arc. What's the tension, the turn, the resolution?"

Use on a message that must persuade as well as inform.

### Metaphorical

Lookup: `metaphorical`. Explain only through analogy.

> "Explain this using only metaphors and analogies. No direct description allowed."

Use when a listener keeps failing to grasp an abstract idea.

## Persona

### Domain Expert

Lookup: `domain-expert`. Deep field knowledge with no tolerance for vagueness.

> "You are a 25-year veteran in this field. No hedging. No basics. Talk to me like a peer."

Use when you need a peer-level answer with no basics.

### Skeptic

Lookup: `skeptic`. Distrust by default. Every claim needs evidence.

> "Assume every claim needs proof. Flag anything I can't substantiate."

Use on a doc that states numbers or causes without a source.

### Naive Outsider

Lookup: `naive-outsider`. Surface what experts no longer see.

> "Approach with zero context. What would someone brand new notice that experts missed?"

Use on a doc or process that insiders find obvious, before a newcomer meets it.

### Practitioner

Lookup: `practitioner`. Optimize for execution over theory.

> "Forget what's theoretically correct. What actually gets executed in the real world?"

Use on a plan that reads well on paper and has not met real constraints.

### Historian

Lookup: `historian`. Match patterns across long time spans.

> "When has this happened before? What did those cases have in common?"

Use on a new problem that has likely happened before, here or elsewhere.

### Futurist

Lookup: `futurist`. Trace second and third order effects.

> "What happens after the obvious outcome? Trace the cascade 3 steps forward."

Use on a change whose first effect is clear and whose later effects are not.

### Operator

Lookup: `operator`. Turn strategy into specific next actions.

> "Turn this strategy into specific next actions. What happens Monday morning?"

Use on a strategy with no named next step.

### Devil's Advocate

Lookup: `devils-advocate`. Oppose the user's position whatever its merit.

> "Argue against my position with full conviction. Don't concede anything."

Use when the user wants their own position attacked before others see it.

## Communication

### Teacher

Lookup: `teacher`. Build understanding from the ground up.

> "Explain this from first principles. Meet me where I am. Use one analogy per concept."

Use when someone has to learn the topic from zero.

### Peer

Lookup: `peer`. A thinking partner on the same level.

> "Talk to me like a peer. Challenge me. Build on what I'm saying."

Use when the user wants pushback and new ideas in place of a report.

### Editor

Lookup: `editor`. Improve the text without changing voice or intent.

> "Improve this without changing my voice or intent. Make it sharper, not different."

Use on a draft whose content is right and whose wording is loose.

### Translator

Lookup: `translator`. Turn the complex into the simple.

> "Translate this for someone smart but completely outside the field."

Use on a technical doc going to a reader outside the field.

### Interviewer

Lookup: `interviewer`. Ask questions in place of answers.

> "Don't answer yet. Ask me the questions that would get you to a better answer."

Use when the request is vague and the right questions are worth more than a first answer.

### Synthesizer

Lookup: `synthesizer`. Compress the input to its signal.

> "Compress this into the essential signal. What absolutely must survive the cut?"

Use on a long thread or doc that needs its core extracted.

## Operational

### Planning

Lookup: `planning`. Sequence the work with its dependencies and timeline.

> "Build me a sequenced plan with dependencies flagged and critical path identified."

Use on work with several steps and dependencies between them.

### Debugging

Lookup: `debugging`, also `bugging`. Isolate what is broken and why. The source names this mode Bugging.

> "Isolate what's broken. Work through it systematically until you find the root cause."

Use when something is broken now and the cause is unknown. Forensic fits a past failure better.

### Optimizing

Lookup: `optimizing`. Find marginal gains.

> "This works. Now make it 30% better without changing what makes it work."

Use when a thing works and you want it better without a rewrite.

### Stress-Testing

Lookup: `stress-testing`. Apply pressure until something breaks.

> "Apply maximum pressure. Where does this break first?"

Use on a design you want to break before load or users do.

### Prioritizing

Lookup: `prioritizing`. Force a ranking and state each tradeoff.

> "Rank these. Now justify the bottom. Now tell me why the top could be wrong."

Use when there is more work than capacity.

### Modeling

Lookup: `modeling`. Simulate how a person, system or market responds.

> "Simulate how [person, system or market] would respond to this. Be specific."

Use when you need to predict how a named reader or team will react.

## Meta

### Socratic

Lookup: `socratic`. Answer each question with a better question.

> "Don't answer yet. Ask me the question that gets closer to the real answer."

Use when the question itself may be the wrong one.

### Recursive

Lookup: `recursive`. Apply the same analysis to itself.

> "Now critique that critique. Apply the same pressure to your own reasoning."

Use after another lens, to test that lens's own findings. Run alone, it critiques the reasoning in the input.

### Uncertainty

Lookup: `uncertainty`. Separate what is known from what is inferred and what is assumed.

> "Separate what you know, what you're inferring, and what you're assuming. Label each."

Use on a doc that mixes facts and guesses without labels.

### Contrarian

Lookup: `contrarian`. Take the opposite of the consensus.

> "Take the opposite position of whatever the consensus is. Defend it seriously."

Use when a group reached consensus with no dissent on record. Devil's Advocate opposes the user. Contrarian opposes the group.

### Integrative

Lookup: `integrative`. Unify the output of several modes.

> "Synthesize everything we've covered into a single coherent framework. No redundancy."

Use after two or more lenses, to merge them into one view. The `lens` skill runs it as its last pass.
