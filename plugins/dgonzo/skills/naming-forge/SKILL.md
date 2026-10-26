---
name: naming-forge
description: Pick one name for a product, feature, CLI command, repo, plugin, skill or set of taxonomy categories. Argues for and against each candidate and scores the survivors on five criteria. Then it crosses the brief with an unrelated domain to find a wild card. Returns one recommended name with its scorecard. Use for "name this", "what should we call it", "is this a good name", "rename this command" or "help me name these categories". Also for /dgonzo:naming-forge. Not for variable, function or file names inside code, taglines (position-lock), word choice in prose, or decisions that are not about a name (decision-forge).
---

# naming-forge

This skill produces one recommended name, backed by a scorecard and a record of the names it beat. It counters generic naming, where a team settles on the first safe name nobody objects to.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Dialectical, which argues both sides in full and then resolves them into one position | Case for, case against and what survives for each candidate, cut to at most 5 survivors |
| 2 | Aesthetic, which asks for the most elegant version and puts how a name reads over how fast it came | Each survivor polished once, then scored 1 to 5 on five criteria, for a maximum of 25 |
| 3 | Combinatorial, which applies the principles of an unrelated domain to the brief to see what the collision produces | 2 domains far from the brief, at most 3 wild cards in total, each scored with the Pass 2 rubric |

Pass 2 scores five criteria. Their names and scoring anchors are in [references/rubric.md](references/rubric.md). The same file holds the generic-name test and the rules for each kind of name.

## Steps

1. If the user named a source for the brief, read it. A source can be a file, a thread or a spec.
2. Check the brief for four facts. Two are what the thing does and who says the name. Two are where it appears and which names sit beside it.
3. If any of the four facts is missing, ask once for all the missing ones in one message. Wait for the answers.
4. Read [references/rubric.md](references/rubric.md), which sits beside this file. Note the rules for this kind of name.
5. List the hard constraints. Include case style and the length limit. Include reserved words and every sibling name in the same namespace.
6. If the sibling names live in the repo, list them from the folder or manifest that holds them.
7. If the subject is a taxonomy, treat each full set of category names as one candidate. Check each set against the taxonomy rule in the rubric.
8. If the user brought candidates, keep the ones that meet the hard constraints. Move the rest to the cut list with the constraint each one breaks.
9. If more than 12 user candidates remain, keep the 12 the user listed first. Move the rest to the cut list.
10. If fewer than 12 candidates remain, add your own up to 12. Include at least 3 plain descriptive names as a baseline.
11. Run the generic-name test from the rubric on every candidate. Mark each one that fails.
12. Run Pass 1. A candidate that failed the generic-name test survives only if its case for outweighs that failure.
13. Run Pass 2 on the survivors. If a small change makes a survivor read better, score the changed form and note the change.
14. Run Pass 3. Pick 2 domains that share nothing with the brief. Name both domains in the output.
15. Run the generic-name test and a one-line case against on each wild card before you score it.
16. Search the repo for the top 2 names. Compare them with the sibling names from step 6.
17. If the name is a CLI command and a shell is available, run `command -v <name>` for each of the top 2 names.
18. If the brief names a registry or command list, search it for the top 2 names. Do this only when a web tool is available. Otherwise list the check as not done.
19. Pick one name. If two names are within 2 points, pick the one a new user would guess the meaning of.
20. If the name is for a product or a repo, write the assessment to `naming-<subject>.md`. Do the same for a plugin or a taxonomy. Put it in the repo folder the user is working in and link it.
21. Otherwise, reply inline with the same sections.

## Output

1. Bottom line. The recommended name and the reason in one sentence. For a taxonomy, give the recommended set. Then name each check that blocks shipping it, such as a trademark search. Say who owns each check. If the owner is unknown, write "owner: unassigned".
2. Scorecard. One row per survivor and wild card. Its columns are candidate and score out of 25. Two more give the weakest criterion and the verdict.
3. Head to head. One row per criterion. One column each for the top 2 names, with their scores from 1 to 5.
4. Dialectical record. One row per survivor. Its columns hold the candidate and the case for. Two more hold the case against and what survived.
5. Wild card. The best Pass 3 name and the domain it came from. Give its score and say why it lost or won.
6. Cut list. Each name cut by a constraint or in Pass 1, with the reason in one line.
7. Checks. What you verified and what you assumed. Then what you did not check.

Output prose follows `/writing:writing-standard`.

## Limits

- Never returns a list of names without one pick.
- Never says a name is clear of trademarks. Only a trademark search or a lawyer can say that.
- Never registers a domain, package or handle.
- Never renames files, code or manifests to apply the name.
- Never names variables, functions or files inside code.
- Never writes a tagline or a position. That is `/dgonzo:position-lock`.
- Never takes more than 12 candidates into Pass 1.
- Never lets a wild card win without a case against it.
- Never writes the assessment as an HTML artifact.
