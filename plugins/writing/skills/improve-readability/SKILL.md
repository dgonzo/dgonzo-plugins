---
name: improve-readability
description: Review one Markdown, Quarto or text file for readability against the writing-standard skill. Use for "improve readability", "is this readable", "check the writing", "lint the prose" or "this doc is hard to follow". Also for a file path after writing:improve-readability. Reports findings and proposed rewrites. Never edits the file.
---

# improve-readability

Review one file against the `writing-standard` skill. Return findings and proposed rewrites. Do not edit the file.

## Steps

Resolve [writing_lint.py](../../scripts/writing_lint.py) relative to this skill file, following symlinks. Set `WRITING_LINTER` to that absolute path in the shell running the commands. If Python or file access is unavailable, report that limitation and perform only the manual review. Never claim the linter ran when it did not.

1. Load the `writing-standard` skill. If the repo has `WRITING.md`, read it too.
2. Run [writing_lint.py](../../scripts/writing_lint.py) and keep its output:

```
python3 "${WRITING_LINTER}" <path>
```

3. Read the file as a reader with no context. Check what the linter cannot:
   - is the first sentence the point
   - does each heading parse cold
   - does any paragraph want to be a table or diagram
   - is anything said twice
   - does every ID and person have a plain name on first use
   - does any sentence break the register rule
4. Report in this order:
   - one sentence on the biggest defect
   - a findings table with line, rule and proposed rewrite columns
   - the linter findings you judged false
5. Offer the rewrite of the whole file only if asked.

Leave thousands-separator commas, slashes inside paths and quoted examples of banned text alone. Those are the only linter findings to ignore without comment.
