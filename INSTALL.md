# Install

| Where you work | Route | Time |
|---|---|---|
| Claude.ai, Cowork and Claude Code | Add the marketplace in claude.ai | One minute |
| Claude Code only | One terminal command | One command |
| Codex and ChatGPT desktop | Register this GitHub marketplace | Once per machine |
| ChatGPT workspace | Admin imports this GitHub marketplace | Once per workspace |
| Antigravity | Add `plugins.json` or run `agy plugin install` | One minute |
| A team repo | Commit two settings to the repo | Once per repo |
| No GitHub access | Release files | One upload |

## Claude.ai and Cowork

1. Open Customize, then Plugins.
2. Select Add, then Add marketplace.
3. Enter `dgonzo/dgonzo-plugins` and select Sync.
4. Find dgonzo and Writing under Discover and select Add on each.
5. Turn on Sync automatically so new versions arrive on their own.

## Claude Code

Run this in a terminal:

```
claude plugin install dgonzo --marketplace dgonzo/dgonzo-plugins
claude plugin install writing --marketplace dgonzo/dgonzo-plugins
```

Inside a session, type the same as a slash command:

```
/plugin install writing --marketplace dgonzo/dgonzo-plugins
```

Both need Claude Code 2.1.275 or later. On an older version, add the marketplace first:

```
claude plugin marketplace add dgonzo/dgonzo-plugins
claude plugin install dgonzo@dgonzo
claude plugin install writing@dgonzo
```

## Antigravity

To load directly from a local clone across every Antigravity surface, add `~/.gemini/config/plugins.json`:

```json
{
  "entries": [
    { "path": "~/Code/dgonzo-plugins/plugins" }
  ]
}
```

To copy the plugins into `~/.gemini/config/plugins/` with the CLI instead, run:

```
agy plugin install ./plugins/dgonzo
agy plugin install ./plugins/writing
```

For a single project repo, add `.agents/plugins.json` at the repo root with the `entries` block above.

## A team repo

Add this to `.claude/settings.json` in the repo and commit it. Anyone who opens the repo in Claude Code and trusts the folder is offered the plugin.

```json
{
  "extraKnownMarketplaces": {
    "dgonzo": { "source": { "source": "github", "repo": "dgonzo/dgonzo-plugins" } }
  },
  "enabledPlugins": { "writing@dgonzo": true }
}
```

## Release files, without GitHub

Each release ships two files.

| File | Surface | How to install |
|---|---|---|
| `writing-<version>.plugin` | Cowork. The dgonzo plugin installs from the marketplace only. | Open the file, or Customize > Plugins > Add > Upload plugin |
| `dgonzo-plugins-<version>.zip` | Claude Code | Unzip to a folder you keep, then run the two commands below |

```
claude plugin marketplace add ./<folder>
claude plugin install writing@dgonzo
```

To upgrade, unzip the new zip over the same folder. Then start a new session or run `/reload-plugins`.

## Installs from before the rename

The repo was `dgonzo/claude-plugins` until version 2.0.1. GitHub redirects the old name, so old installs keep updating. The install ID stays `writing@dgonzo`. To point an old install at the new name, run:

```
claude plugin marketplace remove dgonzo
claude plugin install writing --marketplace dgonzo/dgonzo-plugins
```

## Check a new install

1. Ask "what is the writing rule on bold". The answer quotes Rule 5.
2. Type `/dgonzo:` and check that `working-style` lists.
3. In Claude Code, write a Markdown file with an em-dash aside. The lint hook reports it.

## Codex and ChatGPT desktop

Install from the tracked GitHub branch so future releases come from the same repository:

```sh
codex plugin marketplace add dgonzo/dgonzo-plugins --ref main
codex plugin add dgonzo@dgonzo
codex plugin add writing@dgonzo
```

These commands require a Codex CLI with `plugin add` support. The installation was checked with `0.165.0-alpha.1.2`. Both plugins use the existing Claude-compatible marketplace and shared skill folders. No OpenAI-specific skill copies are maintained.

Start a new chat in the desktop app or a new CLI session. If the desktop directory has not refreshed, restart the app. In the CLI, use `/skills` or `$` to select a skill. In ChatGPT, use `@` to select the installed plugin or skill. References such as `dgonzo:voice` inside a skill identify its owner and name. Use the host's selector to invoke it.

In the CLI, run `/hooks`, review the writing hooks, and trust them to enable session context and post-edit feedback. Installing a plugin does not automatically trust its hooks. The lint hook handles Codex patches and file edits from Claude or Antigravity. It does not detect every shell command that writes a file. Cloud-orchestrated ChatGPT Work does not execute these local plugin hooks.

Add this short bootstrap instruction to `~/.codex/AGENTS.md` for local Codex. Use the equivalent personal or project instructions for the ChatGPT surface you use:

```markdown
Load the working-style skill from dgonzo and the writing-standard skill from writing before the first reply. Follow them throughout the conversation.

If WRITING.md is accessible in the working folder or repository root, read it too.
```

The bootstrap names the skills. Keep their full rules in this repository. These user-level preferences remain subject to the host's system instructions.

To request an update explicitly:

```sh
codex plugin marketplace upgrade dgonzo
codex plugin add dgonzo@dgonzo
codex plugin add writing@dgonzo
```

Start a fresh session after updating. Version bumps identify new releases, but do not guarantee that every host refreshes at the same time. Installed plugin caches are generated copies. Never edit them.

For local development, replace the Git marketplace registration with this checkout's absolute path. Register only one source named `dgonzo` at a time. Use GitHub registration for normal use across projects.

## ChatGPT workspace

A workspace admin can open **Admin > Plugins > Add > Import marketplace** and enter `https://github.com/dgonzo/dgonzo-plugins`. Leave Path empty and use `main` for updates. The importer supports the existing `.claude-plugin/marketplace.json`.

Choose which workspace roles can install each plugin. New workspace marketplaces sync daily by default. Sync now requests an earlier update. A local desktop installation alone does not establish personal web or mobile availability.

Cloud chats use the same instructions and bundled references. Local tools and files may be unavailable. This includes Python and `gh`, plus private voice samples. The skills report those limits instead of claiming they ran local checks.

Private voice samples can live at `~/.config/dgonzo/voice-samples.md`. The older `~/.claude/dgonzo/voice-samples.md` remains a fallback. Neither file belongs in a release.

## Codex IDE extension

The IDE extension supports standalone skills rather than plugins. For that environment, link each skill directory into `~/.agents/skills` and preserve its real resource paths. Avoid installing the same skills through both routes in one environment.

## OpenAI references

- [Plugin packaging and marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Skill discovery](https://learn.chatgpt.com/docs/build-skills)
- [Hook trust and event formats](https://learn.chatgpt.com/docs/hooks)
- [ChatGPT workspace import and sync](https://learn.chatgpt.com/docs/enterprise/plugin-management)
