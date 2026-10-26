# dgonzo

David Gonzalez's personal skills. House prose rules are in the [writing plugin](../writing/README.md). This plugin covers how David works and how he sounds.

```
/plugin install dgonzo --marketplace dgonzo/dgonzo-plugins
```

Cowork and older Claude Code versions are in [INSTALL.md](../../INSTALL.md).

## Which style applies

| Text | Style |
|---|---|
| Team documents, repo docs, PR descriptions in team repos | `/writing:writing-standard` |
| Anything sent under David's name: Slack, email, LinkedIn, essays | `/dgonzo:voice` |
| A brief to an executive | `/dgonzo:exec-brief`, house structure in David's voice |

## Skills

| Group | Skill | Job |
|---|---|---|
| Session | `working-style` | answer first, do the work, keep to the objective |
| Voice | `voice` | David's own voice for text sent under his name |
| Voice | `signal-cut` | posts, launches and threads without marketing-speak |
| Voice | `position-lock` | taglines, pitches and positioning |
| Voice | `audience-model` | model one reader before writing to them |
| Voice | `exec-brief` | a one-page ask for an executive |
| Judgment | `lens` | run any of the gwrk reasoning modes on a doc or decision |
| Judgment | `decision-forge` | attack, steel-man and calibrate a decision |
| Judgment | `truth-extract` | sort claims into grounded, inferred and asserted |
| Judgment | `architecture-stress-test` | dependency, pre-mortem and alternatives review of a plan |
| Judgment | `naming-forge` | names for products, commands and taxonomies |
| Judgment | `build-vs-buy` | build, buy or do nothing, scored on evidence |
| Leadership | `ragb` | status as red, amber, green or black, each tied to an artifact |
| Leadership | `owner-brief` | a handoff with one owner and a done-when |
| Leadership | `cut-list` | rank a backlog and name what gets cut |
| Leadership | `postmortem` | a blameless timeline, causes and owned actions |
| Leadership | `hiring-debrief` | a hire or no-hire call from evidence |

## Design rule for compound skills

Each compound skill names one failure mode and stacks three reasoning modes against it, in order. The rule and the modes come from gwrk, David's AI SDLC harness. The full mode list is in [lens/references/modes.md](skills/lens/references/modes.md).

## Global instruction

Put this in `~/.claude/CLAUDE.md`, Cowork global instructions and claude.ai preferences.

```markdown
Load the dgonzo:working-style and writing:writing-standard skills before the first reply in every session and follow them.

If a WRITING.md exists in the working folder, read it too.
```
