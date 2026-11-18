"""The dgonzo SessionStart hook prints the gonzo card and the working-style rules."""
import json
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'plugins/dgonzo'
HOOK = ROOT / 'scripts/session_hook.py'


class SessionHookTests(unittest.TestCase):
    def context(self):
        result = subprocess.run(['python3', str(HOOK)], text=True, capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        out = json.loads(result.stdout)['hookSpecificOutput']
        self.assertEqual(out['hookEventName'], 'SessionStart')
        return out['additionalContext']

    def test_card_and_working_style(self):
        text = self.context()
        self.assertIn('# Gonzo card', text)
        self.assertIn('# Working style', text)
        self.assertNotIn('\nname: working-style', text)

    def test_router_names_every_skill(self):
        text = self.context()
        skills = sorted(p.name for p in (ROOT / 'skills').iterdir() if (p / 'SKILL.md').exists())
        routed = set(re.findall(r'`dgonzo:([a-z-]+)`', text))
        # working-style is injected whole. voice is a gate row.
        self.assertEqual([s for s in skills if s not in routed and s != 'working-style'], [])

    def test_descriptions_stay_short(self):
        for skill in (ROOT / 'skills').iterdir():
            head = (skill / 'SKILL.md').read_text().split('---')[1]
            desc = re.search(r'^description: (.*)$', head, re.M).group(1)
            self.assertLessEqual(len(desc), 260, skill.name)


if __name__ == '__main__':
    unittest.main()
