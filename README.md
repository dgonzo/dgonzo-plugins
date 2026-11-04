# dgonzo plugins

Plugins by David Gonzalez for Claude and Antigravity, plus Codex and ChatGPT. Three plugins cover personal skills, house writing and Principal Engineer code review.

## Install

Claude.ai and Cowork: open Customize > Plugins > Add > Add marketplace. Enter `dgonzo/dgonzo-plugins` and add dgonzo, Writing and Code Review.

Claude Code:

```
claude plugin install dgonzo --marketplace dgonzo/dgonzo-plugins
claude plugin install writing --marketplace dgonzo/dgonzo-plugins
claude plugin install code-review --marketplace dgonzo/dgonzo-plugins
```

Antigravity CLI:

```
agy plugin install ./plugins/dgonzo
agy plugin install ./plugins/writing
agy plugin install ./plugins/code-review
```

Antigravity App and IDE setup is in [INSTALL.md](INSTALL.md). Team repos, older Claude Code versions and installs without GitHub are there too.

## Codex and ChatGPT desktop

```sh
codex plugin marketplace add dgonzo/dgonzo-plugins --ref main
codex plugin add dgonzo@dgonzo
codex plugin add writing@dgonzo
codex plugin add code-review@dgonzo
```

Start a new chat after installation. Hook trust and global style loading are covered in [INSTALL.md](INSTALL.md). That guide also covers updates and ChatGPT workspace imports.

## Plugins

| Plugin | Contents |
|---|---|
| [dgonzo](plugins/dgonzo/README.md) | working style, voice, reasoning lenses, judgment and leadership skills |
| [Writing](plugins/writing/README.md) | writing standard, readability review, prose linter, lint hook |
| [Code Review](plugins/code-review/README.md) | Principal Engineer code review router and webapp, API and data science skills |

The Writing plugin cuts linter findings by about 75 percent against a bare session. See [the plugin-vs-naked eval](evals/plugin-vs-naked/README.md).
