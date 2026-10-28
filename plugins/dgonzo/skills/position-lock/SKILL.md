---
name: position-lock
description: Turn a product, project or idea that is described as a list of features into one position and a headline of 10 words or fewer. Strips it to the one thing it makes possible. Tests that against the status quo, the closest competitor and the category. Then scores headline candidates. Use for "write a tagline", "sharpen our positioning", "elevator pitch for this", "landing page headline" or "how do we stand apart from X". Also for dgonzo:position-lock. Not for blog posts or announcements (signal-cut), product names (naming-forge) or choosing a vendor (build-vs-buy).
---

# position-lock

Produces one position statement, a territory map and a headline of 10 words or fewer. It counters feature-listing, which describes a product by its parts instead of its position.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Reductive | Ground truth only, with category convention and inherited claims removed: what it makes possible that was impossible before, in one sentence of 25 words at most |
| 2 | Comparative | Never alone, always against 3 alternatives (status quo, closest competitor, category), keeping only ground none of the 3 can claim |
| 3 | Aesthetic | Optimize for elegance, not only correctness: 5 candidates of 10 words at most, each scored 1 to 5 on rhythm, memorability, provocation and ownership |

## Steps

1. Load `dgonzo:voice`. The result is sent under David's name. If that skill is not installed, follow `writing:writing-standard` instead.
2. If the input is missing, ask once for three things. Ask what it is, who it is for and who it competes with.
3. Otherwise read the file, thread or pasted text the user named. If a reader model from `dgonzo:audience-model` is in the thread or folder, use it for who it is for.
4. List every feature and claim in the input. Count them.
5. Drop each claim the input does not show and each phrase that any product in the category would use.
6. Write the reductive sentence: what a user can now do that they could not do before.
7. If the sentence names a feature, rewrite it as the outcome the feature makes possible.
8. If the sentence holds more than one outcome, keep the one the target user would pay for.
9. Name the three alternatives: the status quo, the closest competitor and the category. If the user named no competitor, pick the closest one and mark it as your assumption.
10. For each alternative, ask whether it could say the sentence truthfully. If it could, narrow the sentence until it cannot.
11. If no sentence survives all three, stop. Report that there is no position yet and name the proof that would create one.
12. Write 5 headline candidates of 10 words or fewer from the surviving sentence.
13. Score each candidate with the rubric in [references/rubric.md](references/rubric.md).
14. Pick the top scorer. If two tie, pick the one with the higher ownership score.
15. If the winner scores below 5 on ownership, take the next candidate that scores 5. If none does, write 5 new candidates once and score them. If none of those scores 5 either, recommend the best and name the alternative that could also say it.
16. If the user asked for an elevator pitch, write one of 3 sentences at most. Use the headline, the position statement and the strongest proof point.
17. If the user is working in a repo folder, write the result to `positioning-<slug>.md` there and link it. Otherwise reply in the chat.

## Output

1. Bottom line. The recommended headline and the position it holds, in one sentence. Then what blocks it from shipping and who owns that. A claim that still needs proof is the usual blocker. If step 11 stopped the run, say there is no position yet and name the missing proof and its owner.
2. Position statement. The surviving reductive sentence.
3. Territory map. One row for each of the 3 alternatives. Columns are alternative, what it already owns and what it cannot claim.
4. Headline candidates. A table sorted by score. Each row gives the candidate and its word count. It also gives the total score and the weakest criterion.
5. Elevator pitch. Only if the user asked for one.
6. Cut features. Each feature that left the headline and where it goes now. Most become proof points under the headline.
7. Assumptions. Every competitor claim or user fact you did not get from a source.

The prose follows `dgonzo:voice`.

## Limits

- Never ships a headline over 10 words.
- Never presents a list of features as a position.
- Never claims a capability the input does not show.
- Never states a competitor's claim without a source. Unsourced claims go under Assumptions.
- Never names the product. That belongs to `dgonzo:naming-forge`.
- Never writes the blog post, announcement or page body. That belongs to `dgonzo:signal-cut`.
- Never picks between vendors to buy. That belongs to `dgonzo:build-vs-buy`.
- Never writes an HTML artifact.
