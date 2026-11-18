#!/usr/bin/env python3
"""SessionStart hook. Prints card.md, then the working-style skill body, as additionalContext.
The stance, the router table and the session rules then hold before any skill loads.
Exit 0 always. Prints nothing if both files are missing."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(*parts):
    try:
        with open(os.path.join(ROOT, *parts), encoding="utf-8") as fh:
            return fh.read().strip()
    except Exception:
        return ""


def body(text):
    """Drop YAML frontmatter from a SKILL.md."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].strip()
    return text


parts = [p for p in (read("card.md"), body(read("skills", "working-style", "SKILL.md"))) if p]
if not parts:
    sys.exit(0)
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n\n".join(parts)}}))
