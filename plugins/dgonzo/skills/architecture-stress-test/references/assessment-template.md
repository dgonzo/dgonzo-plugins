# Assessment template

Scales, alternative definitions and the Markdown skeleton for `architecture-stress-test`.

## Blast radius

| Rating | What breaks if the phase fails |
|---|---|
| Low | Only this phase's work is redone. |
| Medium | Later phases or another team's work is redone. |
| High | Users, production systems or stored data are hit. |

## Alternatives

| Alternative | How to build it |
|---|---|
| Simplest | The fewest phases that still meet the plan's stated goal. |
| Most parallel | The same work reordered for the shortest critical path. |
| Most conservative | Every high blast radius step made reversible or staged behind a check. |

Each alternative must meet the plan's goal. If one cannot, say so in its row.

## Skeleton

```markdown
# Stress test: <plan name>

**Verdict: <APPROVE or REVISE>.** <Main reason in one sentence.> Blocked: <what, or "nothing">. Owner: <who, or "unassigned">.

## Required changes

REVISE only. Highest blast radius first.

1. <Change.> Phase: <phase>. Owner: <who>.

## Dependencies

| Phase | Depends on | Blast radius | Rollback |
|---|---|---|---|
| <phase> | <phases, or "none"> | <Low, Medium or High> | <stated rollback, or "none"> |

## Critical path

<phase> to <phase> to <phase>. Length: <total duration, or number of phases>.

## Failure scenarios

| Root cause | Phase | Prevention | Early signal |
|---|---|---|---|
| <cause> | <phase> | <change, or "none"> | <signal> |

## Alternatives

| Alternative | Critical path length | Top blast radius | Against the plan |
|---|---|---|---|
| Simplest | <length> | <rating> | <better, worse or equal, and why> |
| Most parallel | <length> | <rating> | <better, worse or equal, and why> |
| Most conservative | <length> | <rating> | <better, worse or equal, and why> |

## Assumptions

- <What the review took as given.>
```

Mark an inferred dependency with "(inferred)" in the Depends on cell.
