---
name: lint
description: Run the writing linter on one file and print its output
argument-hint: <file>
allowed-tools: Bash(python3:*)
---

Linter output for `$ARGUMENTS`:

!`if [ -n "$ARGUMENTS" ]; then python3 "${CLAUDE_PLUGIN_ROOT}/scripts/writing_lint.py" $ARGUMENTS; else echo "Usage: /writing:lint <file>"; fi`

If the block above did not run, run [writing_lint.py](../../scripts/writing_lint.py) on the target file. Reply with the linter output verbatim. Add nothing before it and nothing after it. Do not fix anything.
