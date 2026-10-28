---
name: lint
description: Run the writing linter on one file and print its output. Use when asked to lint prose or run writing:lint with a file path. Reports findings without editing.
---

Run [writing_lint.py](../../scripts/writing_lint.py) with Python 3 on the file named by the user. Resolve the script relative to this skill file, following symlinks. Quote both absolute paths when invoking the shell.

If no file was named, ask for its path. If Python or file access is unavailable, report that limitation. Never invent linter output.

Reply with the linter output verbatim. Add nothing before it and nothing after it. Do not fix anything.
