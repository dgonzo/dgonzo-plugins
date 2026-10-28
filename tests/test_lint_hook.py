"""Exercise real hook output across host event formats."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

HOOK = Path(__file__).resolve().parents[1] / 'plugins/writing/scripts/lint_hook.py'
BAD = 'This is genuinely robust; it is seamless.\n'


class HookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(BAD)
        return path

    def run_hook(self, event):
        result = subprocess.run(['python3', str(HOOK)], input=json.dumps(event),
                                text=True, capture_output=True, cwd=self.root, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_claude_and_antigravity(self):
        path = self.write('file with spaces.md')
        for event in [
            {'tool_name': 'Write', 'tool_input': {'file_path': str(path)}},
            {'toolCall': {'args': {'Path': str(path)}}, 'result': 'written'},
            {'toolCall': {'args': {'TargetFile': str(path)}}, 'result': 'edited'},
        ]:
            with self.subTest(event=event):
                output = json.loads(self.run_hook(event))
                text = output.get('overwriteResult') or output['hookSpecificOutput']['additionalContext']
                self.assertIn('semicolon', text)
                self.assertEqual(path.read_text(), BAD)

    def test_codex_multiple_files_move_and_delete(self):
        for name in ['new file.md', 'existing.txt', 'moved.mdx', 'deleted.md']:
            self.write(name)
        # A deletion header must never select a file, even if a stale file exists.
        patch = '''*** Begin Patch
*** Add File: new file.md
+content
*** Update File: existing.txt
@@
-old
+new
*** Update File: old.mdx
*** Move to: moved.mdx
@@
-old
+new
*** Delete File: deleted.md
*** End Patch'''
        event = {'tool_name': 'apply_patch', 'cwd': str(self.root), 'tool_input': {'command': patch}}
        output = json.loads(self.run_hook(event))['hookSpecificOutput']['additionalContext']
        for name in ['new file.md', 'existing.txt', 'moved.mdx']:
            self.assertIn(name, output)
            self.assertEqual((self.root / name).read_text(), BAD)
        self.assertNotIn('deleted.md:', output)
        self.assertNotIn('old.mdx:', output)

    def test_skip_nonprose_dependencies_and_missing_files(self):
        for name in ['code.py', 'node_modules/readme.md', '.git/notes.md']:
            self.write(name)
        for name in ['code.py', 'node_modules/readme.md', '.git/notes.md', 'missing.md']:
            with self.subTest(name=name):
                self.assertEqual(self.run_hook({'tool_input': {'file_path': name}}), '')

    def test_shell_command_is_not_parsed_as_patch(self):
        self.write('sample.md')
        event = {'tool_name': 'Bash', 'tool_input': {'command': '*** Add File: sample.md'}}
        self.assertEqual(self.run_hook(event), '')

    def test_malformed_input_is_advisory(self):
        for event in [None, [], {'tool_input': 'wrong'}, {'tool_name': 'apply_patch', 'tool_input': {'command': None}}]:
            with self.subTest(event=event):
                self.assertEqual(self.run_hook(event), '')
        result = subprocess.run(['python3', str(HOOK)], input='{', text=True, capture_output=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
