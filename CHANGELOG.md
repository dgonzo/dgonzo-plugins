# Changelog

## dgonzo 1.3.0 and writing 3.2.0

- `voice` states the voice in one line: technically accurate and emotionally honest. Precision, honesty, ownership. It names five misses that sound strong, theatrical, corporate, cute, coy and coined, each with a test. It adds a six-row gate run on every sentence. It adds a presentation channel. The essay register and any presentation read the full Foxtrot Charlie essay first.
- New skill `pmc-id`. Gets any artifact in shape for Peter from his private reader file. Reductive, Modeling and Translator passes.
- `audience-model` writes real people to `~/.claude/dgonzo/readers/<name>.md`, never a repo. It adds the reader's vocabulary, what loses them and what they do with the thing you send.
- `exec-brief` reads the reader file, cuts internal coinages as well as jargon, predicts the first question from the reader's behaviour, and has a seven-slide deck shape. No placeholder dates.
- `working-style` adds voice corrections: re-read the source, run the draft through the review's rows, never publish over a live edit.
- writing Rule 7: a measurement shows its target and a verdict word. A stakeholder's words appear whole. The check before you send hunts passives and checks measurements. The linter lints the text of `.html` slide files.

## writing 3.1.1

- The BLUF is one to three sentences and covers reports, notebooks and PR descriptions as well as documents and replies.
- A piece with no blocker says "Blocked: none". The writing card carries the same rule.
- Folds in the BLUF detail from the retired data-org `standards/writing.md` branch of 2026-10-12. The other rules on that branch were already here or in `dgonzo:working-style`.

## writing 3.1.0 and dgonzo 1.2.0

- Codex and ChatGPT use the same skill folders and Claude-compatible marketplace as the existing hosts.
- Shared skill references identify the owning plugin without requiring Claude slash-command syntax.
- Writing skills resolve the linter from the loaded skill location. Lint no longer depends on Claude argument expansion.
- The advisory lint hook handles Codex patches with multiple files, moves and deletes. Claude and Antigravity event formats remain supported.
- Voice accepts a neutral private sample path and keeps the existing Claude path as a fallback.
- Installation guidance covers local OpenAI clients, Git updates, hook trust and ChatGPT workspace sync.

## dgonzo 1.1.0

- `voice` has two registers. The work register covers Slack and email and is the default. It comes from David's own messages: name first, "would you" asks, named owners, numbers as receipts, `--dg` on email. The essay register keeps the Foxtrot Charlie traits.
- `voice` reads `~/.claude/dgonzo/voice-samples.md` when it exists. That file has David's verbatim messages and stays out of this repo. The public samples file has the patterns with placeholders.
- `exec-brief` gains an approval email template with WHAT, WHY, WHEN, COST and ASK labels.

## writing 3.0.0

- Breaking. The `working-style` skill moved to the new `dgonzo` plugin. `/writing:working-style` no longer exists. Install `dgonzo@dgonzo` and load `dgonzo:working-style` instead.
- The plugin now has three skills: writing-standard, improve-readability and review-prose.
- The CLAUDE.md snippet loads `dgonzo:working-style` and `writing:writing-standard`.

## dgonzo 1.0.0

- First release of David Gonzalez's personal plugin. Install ID `dgonzo@dgonzo`.
- Session: `working-style`, moved from `writing`. It now points at `/writing:writing-standard` for team documents and `/dgonzo:voice` for text sent under David's name.
- Voice: `voice`, `signal-cut`, `position-lock`, `audience-model`, `exec-brief`.
- Judgment: `lens` with all reasoning modes from gwrk, `decision-forge`, `truth-extract`, `architecture-stress-test`, `naming-forge`, `build-vs-buy`.
- Leadership: `ragb`, `owner-brief`, `cut-list`, `postmortem`, `hiring-debrief`.
- Compound skills follow the gwrk design rule. Each names one failure mode and stacks three reasoning modes against it.

## 2.0.1

- The repo is now `dgonzo/dgonzo-plugins`. The old name redirects. The install ID stays `writing@dgonzo`.
- Listings show "Writing" by David Gonzalez. The manifests also set a category and tags.
- One-command install for Claude Code. INSTALL.md covers Cowork, team repos and release files.
- Rule 10 bans "holds" and "carries" as vague verbs. Write "contains" or "applies" instead. The plugin's own text no longer uses them.
- The plugin-vs-naked eval compares the plugin with a bare session. Linter findings fall from 3.4 to 0.9 per 100 words. Its summary is in the plugin README.

## 2.0.0

- One standard. The writing-standard skill is the single source, 14 rules. It gained the plain-word swap table and the say-it-once rule. Never hard-wrap is its own rule. Sentence caps and condition-before-command steps are in. New rule on names and numbers.
- working-style gains the recommendations rule. Recommend only when asked for a decision. Then give one with the evidence beside it. Never a menu.
- A fallback card ships with the plugin and a SessionStart hook loads it. The global instruction shrinks to two lines.
- A surface note for hosts that show Mermaid as text, such as the VS Code extension chat.
- New review-prose skill for diffs and PR descriptions. New `/writing:lint <file>` command.
- The linter prints the standard's rule number on every finding.
- Release packaging: `make release` builds a `.plugin` file for Cowork and a marketplace zip for Claude Code.

## 1.0.0

- First release. Three skills: writing-standard, working-style and improve-readability. The prose linter and the PostToolUse lint hook.
