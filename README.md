# dgonzo plugins

Claude plugins by David Gonzalez. Two plugins: dgonzo, his personal skills, and Writing, a house writing standard for chat, Cowork and Claude Code.

## Install

Claude.ai and Cowork: open Customize > Plugins > Add > Add marketplace. Enter `dgonzo/dgonzo-plugins` and add dgonzo and Writing.

Claude Code:

```
claude plugin install dgonzo --marketplace dgonzo/dgonzo-plugins
claude plugin install writing --marketplace dgonzo/dgonzo-plugins
```

Team repos, older Claude Code versions and installs without GitHub are in [INSTALL.md](INSTALL.md).

## Plugins

| Plugin | Contents |
|---|---|
| [dgonzo](plugins/dgonzo/README.md) | working style, voice, reasoning lenses, judgment and leadership skills |
| [Writing](plugins/writing/README.md) | writing standard, readability review, prose linter, lint hook |

The Writing plugin cuts linter findings by about 75 percent against a bare session. See [the plugin-vs-naked eval](evals/plugin-vs-naked/README.md).
