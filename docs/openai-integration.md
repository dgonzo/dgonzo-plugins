# Codex and ChatGPT integration assessment

Keep `plugins/dgonzo/skills` and `plugins/writing/skills` as the single source for every host. Start with OpenAI's Claude-compatible plugin support, then fix the few host-specific assumptions in the shared files. A separate skill library or MCP server would add maintenance without helping this workflow.

Assessment date: 2026-10-27. Repository baseline: `7a28948`. The assessment below records the initial findings. The implementation status supersedes the proposed changes and earlier verification boundary.

## Implementation status

Implemented in writing 3.1.0 and dgonzo 1.2.0. The existing Claude marketplace installs both plugins through Codex CLI 0.165.0-alpha.1.2 without another manifest. Shared instructions resolve resource paths and identify skills without Claude command expansion. The hook adapter now handles Codex patches. Five regression tests pass, all 21 skills pass frontmatter validation, Antigravity validates both plugins, and release archives build.

See [INSTALL.md](../INSTALL.md) for the maintained installation and update instructions. Hook trust and fresh-session behavior remain host-level checks. Desktop UI verification was unavailable because Computer Use blocked access to the ChatGPT application.

## Existing architecture

| Component | Current state | Integration consequence |
|---|---|---|
| Personal skills | 17 directories under `plugins/dgonzo/skills` | Keep their workflows and references together |
| Writing skills | Four directories under `plugins/writing/skills` | Keep the linter and card in the same plugin |
| Plugin identity | Root `plugin.json` symlinks to `.claude-plugin/plugin.json` | Already one metadata source per plugin |
| Marketplace | `.claude-plugin/marketplace.json` points to both plugin folders | Try the existing catalog first |
| Antigravity rules | `rules/AGENTS.md` links to `standard/card.md` | Already shares the writing card |
| Hooks | Separate host configurations, one linter implementation | Extend the event adapter, preserve the linter |
| Releases | Writing upload and whole-marketplace archives | Continue producing artifacts from source |

The Antigravity commit made useful changes: it exposed root manifests through symlinks, moved lint into a skill, and taught the lint hook a second event format. Those are appropriate seams for adding another host.

All 21 skill files have `name` and `description` frontmatter. A relative Markdown link check found no missing targets under `plugins/`. These checks establish basic structure, not successful OpenAI installation.

## Distribution routes

OpenAI documents support for Claude-compatible marketplaces and plugins. Its workspace importer explicitly accepts `.claude-plugin/marketplace.json`, including local plugin paths. That is the strongest reason to test the existing package before introducing another manifest. [Workspace plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management)

| Use | Recommended route | Update source |
|---|---|---|
| Personal Codex and desktop authoring | Register this local repository as a marketplace | Local checkout, followed by refresh |
| Personal installed release | Register the GitHub marketplace | Published repository revision |
| Wisecode ChatGPT workspace | Admin imports this GitHub marketplace | Repository sync |
| Freelance client workspace | Client admin imports the relevant plugins | Same repository or a selected release ref |
| Codex IDE extension | Link individual skill folders into its local discovery location | Local checkout |

Proposed local registration command, from this repo:

```sh
codex plugin marketplace add .
```

For the GitHub route:

```sh
codex plugin marketplace add dgonzo/dgonzo-plugins
```

Install both plugins through the supported plugin browser and test in a fresh chat. These commands are documented, but were not executed here. The local CLI version probe stalled, so installed CLI compatibility remains unverified. [Plugin packaging and marketplaces](https://developers.openai.com/plugins/build/plugins)

For a managed ChatGPT workspace, an admin can use **Admin > Plugins > Add > Import marketplace**. Use the repository URL and leave Path empty. Repository access is required. The documented sync defaults to daily, with **Sync now** available. Policies remain workspace-controlled. This route can use the existing Claude marketplace. [Workspace plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management)

ChatGPT and Codex share a plugin directory. Plugin skills are documented across Chat and Work on supported web, desktop, and mobile surfaces. The IDE extension supports standalone skills but not plugins. A local desktop installation does not establish that a personal web account has received the package. Test that account's distribution route separately. [Plugins](https://learn.chatgpt.com/docs/plugins?surface=app), [Build skills](https://learn.chatgpt.com/docs/build-skills)

For rapid local skill development, Codex supports symlinked skill folders under `~/.agents/skills`. Link each skill directory, not the outer plugin folder. Resolve resource links through the real skill location. Use this as an alternative to plugin installation in that environment, since installing both can expose duplicate skills. [Build skills](https://learn.chatgpt.com/docs/build-skills)

Installed caches and release archives are expected copies. They should remain disposable outputs. Only this repository should be edited.

## Required portability work

### Skill references and commands

The skills frequently refer to `/dgonzo:...` and `/writing:...`. Treat these as Claude invocation examples, not universal executable commands. In shared instructions, identify the skill by its name and owning plugin. Keep each host's invocation syntax in installation documentation.

`skills/lint/SKILL.md` contains Claude's dynamic shell block, `$ARGUMENTS`, and `allowed-tools: Bash(python3:*)`. It already has a useful relative-path fallback. Make the plain instruction to run the resolved linter the primary workflow. Do not depend on another host expanding the Claude block or enforcing that frontmatter permission.

The other writing skills use `${CLAUDE_PLUGIN_ROOT}` in shell examples. Resolve `../../scripts/writing_lint.py` from the loaded skill's actual location. OpenAI documents compatibility environment variables for plugin hooks; that does not establish their availability in arbitrary skill shell commands. [Plugin hook environment](https://learn.chatgpt.com/docs/hooks)

The handoff template also hardcodes a future Claude session and a `claude` launch command. Use the selected host in those examples. Preserve the handoff method itself.

### Lint hook input

The current `lint_hook.py` accepts either Antigravity's `toolCall.args` or Claude's `tool_input.file_path`. Codex's documented `apply_patch` input instead carries patch text in `tool_input.command`. Its `Edit` and `Write` matcher aliases can match that tool, so changing the matcher alone will not fix the parser. [Hook inputs and tool coverage](https://learn.chatgpt.com/docs/hooks)

A temporary-file probe produced these results:

| Input fixture | Exit code | Lint feedback |
|---|---|---|
| Claude Write | 0 | Present |
| Antigravity write_file | 0 | Present |
| Codex apply_patch | 0 | Absent |

Extend the shared adapter to extract added, updated, and moved file destinations from a Codex patch. Resolve relative destinations against the event's `cwd`. Lint surviving prose files, including multiple files in one patch. Skip deleted files. Preserve the current advisory behavior and shared `writing_lint.py` implementation.

Shell commands can also modify files. A patch adapter will not provide complete coverage of those writes. Keep explicit linting in the writing workflow, and document the hook's coverage accurately.

`session_hook.py` already emits the documented SessionStart context shape, and its output parsed successfully. A live Codex test must still verify loading and delivery. User-installed hooks require trust review. Cloud-orchestrated Work does not run local plugin hooks, so cloud writing must work through the skills themselves. [Hooks](https://learn.chatgpt.com/docs/hooks)

### Always-on style and local resources

Discovery does not guarantee that `working-style` and `writing-standard` load before every reply. Keep a short host-level instruction that names those two installed skills and asks the agent to read `WRITING.md` when available. Keep the full rules in this repo. Verify the first response in a fresh session, rather than only testing explicit invocation.

`voice` optionally reads `~/.claude/dgonzo/voice-samples.md`. Preserve that compatibility path, but allow a neutral local path or an explicitly supplied private reference. A remote ChatGPT session cannot assume access to the file on this Mac. The sanitized samples already shipped in the plugin provide the default. Keep private verbatim samples out of release packaging.

References to other plugins, such as `data-org-cowork-plugin`, `superpowers`, and Slack skills, are mostly routing boundaries. They should not become mandatory installation dependencies. Where a workflow delegates to an external skill, define what happens when it is absent.

### Metadata and packaging

The dgonzo manifest still describes one skill although it now contains 17. Update that description before exposing the catalog more widely. The writing manifest also describes its skill count indirectly as three skills plus a lint command, although lint is now a fourth skill.

Keep the current manifest symlinks for the initial compatibility test. If a loader rejects their layout or an importer handles symlinks differently, generate an installable package with regular manifest files from the existing metadata source. Do not manually maintain copied manifests.

Add a native `.agents/plugins/marketplace.json` only if testing identifies a need for OpenAI-specific catalog metadata or policy. Generate its entries from the existing catalog. Likewise, add an OpenAI manifest overlay only for settings that cannot be expressed through compatibility support. OpenAI documents a portable root manifest and optional OpenAI settings for future packaging. [Plugin packaging](https://developers.openai.com/plugins/build/plugins)

If a generated catalog is added, update `scripts/pack.sh`: its whole-marketplace archive currently includes only `.claude-plugin`, `plugins`, `INSTALL.md`, and `CHANGELOG.md`.

## Implementation sequence

1. Test the current marketplace in desktop Codex. Confirm both plugins and all 21 skills appear in a fresh chat.
2. Make the shared instructions portable. Keep the reasoning workflows, rubrics, templates, and writing rules intact.
3. Extend and test the hook adapter for Codex patches. Verify actual callback delivery after hook trust review.
4. Add Codex and ChatGPT installation instructions, including update behavior and the limits of local resources.
5. Import into an available ChatGPT workspace and verify skill execution without local hooks.
6. Add generated metadata only where those tests demonstrate a compatibility gap.

## Acceptance checks

- Resolve every reference and linter path from an installed cache, outside this checkout.
- Exercise `decision-forge`, `voice`, `exec-brief`, and `lint` through explicit selection and natural-language prompts.
- Confirm a first response uses the two global style skills when the bootstrap instruction is configured.
- Verify Claude and Antigravity hook fixtures still produce feedback after the adapter changes.
- Test a multi-file Codex patch, a moved file, a deleted file, and a filename containing spaces.
- Confirm hooks remain advisory and never edit the user's prose.
- Test missing Python, absent `gh`, unavailable private samples, and a cloud chat with no filesystem access. Report unsupported operations accurately.
- Change one source skill, refresh the installation, and verify the new content in a fresh chat.
- Compare the existing eval prompts on the target OpenAI environment. The current reported improvement measures Claude, not Codex or ChatGPT.

## Verification boundary

This assessment inspected the manifests, symlinks, all skill frontmatter, reference links, installation guidance, hook scripts, packaging, and evaluation method. It ran isolated hook fixtures and checked current official OpenAI documentation.

It did not install plugins, modify user configuration, trust hooks, publish a package, or access workspace admin settings. Personal ChatGPT account availability and end-to-end loader behavior remain installation checks. Only this assessment document was added.
