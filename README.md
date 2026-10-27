# dgonzo plugins

Plugins by David Gonzalez for Claude and Antigravity. Two plugins: dgonzo has his personal skills, and Writing is a house writing standard.

## Install

Claude.ai and Cowork: open Customize > Plugins > Add > Add marketplace. Enter `dgonzo/dgonzo-plugins` and add dgonzo and Writing.

Claude Code:

```
claude plugin install dgonzo --marketplace dgonzo/dgonzo-plugins
claude plugin install writing --marketplace dgonzo/dgonzo-plugins
```

Antigravity CLI:

```
agy plugin install ./plugins/dgonzo
agy plugin install ./plugins/writing
```

Antigravity App and IDE setup is in [INSTALL.md](INSTALL.md). Team repos, older Claude Code versions and installs without GitHub are there too.

## Plugins

| Plugin | Contents |
|---|---|
| [dgonzo](plugins/dgonzo/README.md) | working style, voice, reasoning lenses, judgment and leadership skills |
| [Writing](plugins/writing/README.md) | writing standard, readability review, prose linter, lint hook |

The Writing plugin cuts linter findings by about 75 percent against a bare session. See [the plugin-vs-naked eval](evals/plugin-vs-naked/README.md).
