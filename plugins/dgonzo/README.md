# dgonzo

David Gonzalez's personal skills. House prose rules are in the [writing plugin](../writing/README.md). This plugin covers how David works and how he sounds.

```
/plugin install dgonzo --marketplace dgonzo/dgonzo-plugins
```

Codex, ChatGPT, Cowork and older Claude Code versions are in [INSTALL.md](../../INSTALL.md).

## What loads when

| Tier | What | How it loads |
|---|---|---|
| Default | The stance, `working-style`, a router table and the gates | A SessionStart hook prints [card.md](card.md) and the `working-style` rules |
| Called by name | `lead-out`, `game`, `pmc-it`, `lens` | David types it |
| Routed | The other skills | The router table in the card names the situation for each |

David remembers four names. The card routes the rest, so no skill depends on its listing description.

Private files stay on David's machine and never enter a repo.

| File | Holds |
|---|---|
| `~/.claude/dgonzo/self.md` | His strengths, blind spots and standing feedback |
| `~/.claude/dgonzo/readers/<name>.md` | One reader each |
| `~/.claude/dgonzo/moves/` | Plans that name a colleague |

## Which style applies

| Text | Style |
|---|---|
| Team documents, repo docs, PR descriptions in team repos | `/writing:writing-standard` |
| Anything sent under David's name: Slack, email, LinkedIn, essays | `/dgonzo:voice` |
| A brief to an executive | `/dgonzo:exec-brief`, house structure in David's voice |
| Anything Peter will read | `/dgonzo:pmc-it`, after the draft exists |

## Skills

| Group | Skill | Job |
|---|---|---|
| Session | `working-style` | answer first, take a position, do the work, keep to the objective |
| Voice | `voice` | David's own voice for text sent under his name |
| Voice | `signal-cut` | posts, launches and threads without marketing-speak |
| Voice | `position-lock` | taglines, pitches and positioning |
| Voice | `audience-model` | model one reader before writing to them |
| Voice | `exec-brief` | a one-page ask for an executive |
| Voice | `pmc-it` | get any artifact in shape for Peter, the CEO, from his private reader file |
| Lead | `lead-out` | David's position, the order of conversations, an ask and a day per person |
| Lead | `game` | a game theory read with one move, as standoff, counterparty or commitment |
| Judgment | `lens` | run any of the 56 reasoning modes on a doc or decision |
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

Each compound skill names one failure mode and stacks three reasoning modes against it, in order. The rule and the modes come from gwrk, David's AI SDLC harness. The full mode list is in [lens/references/modes.md](skills/lens/references/modes.md). The Game category and two Reasoning modes come from David's market mode stack.

`game` holds three stacks under one name. Nine other skills carry a Game check, which is one conditional game theory step.

## Global instruction

Claude Code loads the card and `working-style` through the hook. Hooks do not run in Cowork, claude.ai, Codex or Antigravity. Put this in Cowork global instructions and claude.ai preferences, and keep it in `~/.claude/CLAUDE.md` for the `writing` line.

```markdown
Load the dgonzo:working-style and writing:writing-standard skills before the first reply in every session and follow them.

If a WRITING.md exists in the working folder, read it too.
```
