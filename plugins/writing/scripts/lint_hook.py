#!/usr/bin/env python3
"""Advisory prose lint feedback for Claude, Antigravity and Codex edits."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys

PROSE = (".md", ".qmd", ".mdx", ".txt")


def edited_paths(event):
    """Normalize host events without interpreting shell commands as patches."""
    if "toolCall" in event:
        args = (event.get("toolCall") or {}).get("args") or {}
        return [args.get("Path") or args.get("TargetFile") or ""]
    args = event.get("tool_input") or {}
    if event.get("tool_name") != "apply_patch":
        return [args.get("file_path") or ""]
    paths = []
    for line in args.get("command", "").splitlines():
        if line.startswith(("*** Add File: ", "*** Update File: ")):
            paths.append(line.split(": ", 1)[1])
        elif line.startswith("*** Move to: ") and paths:
            paths[-1] = line.split(": ", 1)[1]
    return paths


def feedback(event):
    cwd = Path(event.get("cwd") or os.getcwd())
    paths = []
    for value in edited_paths(event):
        if not value:
            continue
        path = Path(value)
        if not path.is_absolute():
            path = cwd / path
        path = path.resolve()
        if path.suffix.lower() not in PROSE or not path.is_file():
            continue
        if {"node_modules", ".git"}.intersection(path.parts):
            continue
        if path not in paths:
            paths.append(path)
    if not paths:
        return None
    lint = Path(__file__).resolve().with_name("writing_lint.py")
    out = subprocess.run(
        [sys.executable, str(lint), *map(str, paths)],
        capture_output=True, text=True, timeout=15,
    ).stdout
    lines = [line for line in out.splitlines() if re.match(r".+:\d+: [a-z-]+: ", line)]
    if not lines:
        return None
    more = f"\n... {len(lines) - 25} more" if len(lines) > 25 else ""
    noun = "finding" if len(lines) == 1 else "findings"
    msg = (
        f"writing-standard linter: {len(lines)} {noun}. Fix each real one before you finish. "
        "Leave only thousands-separator commas, slashes inside paths, and quoted examples of banned text.\n"
        + "\n".join(lines[:25]) + more
    )
    if "toolCall" in event:
        orig = event.get("result") or ""
        return {"overwriteResult": f"{orig}\n\n{msg}".strip()}
    return {"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}


def main():
    try:
        result = feedback(json.load(sys.stdin))
        if result:
            print(json.dumps(result))
    except (ValueError, TypeError, AttributeError, OSError, subprocess.SubprocessError):
        # Hook failures must not block the user's edit.
        return


if __name__ == "__main__":
    main()
