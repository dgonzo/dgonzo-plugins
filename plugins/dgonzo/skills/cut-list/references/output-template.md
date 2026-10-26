# Cut list template

Use this layout when the result is a document the user keeps. Name the file `cut-list-<topic>-<YYYY-MM-DD>.md`. Replace every angle-bracket field.

```markdown
# Cut list: <list name>

<Keep K, defer D, cut C> against <goal>. Conflict: <item that scores 3 and does not fit>, owned by <goal owner>, or "no conflicts". <Owner> tells the requesters by <date>.

Goal: <one goal, as stated by the user>

Capacity: <people-weeks or slots, or "assumed: top third">

## Keep

| Rank | Item | Evidence | If it never ships |
|---|---|---|---|
| 1 | <plain name> | <measured / reported / assumed: fact> | <who notices, by when> |

Owner of each kept item:

| Item | Owner |
|---|---|
| <plain name> | <person or "unassigned"> |

## Defer

| Item | Loss (0 to 3) | Revisit when | Owner |
|---|---|---|---|
| <plain name> | <score> | <trigger> | <person> |

## Cut (BLACK)

| Item | Requester | Why it goes | Line to send |
|---|---|---|---|
| <plain name> | <person or "unassigned"> | <one reason> | <one sentence for the requester> |

## Where the rank could be wrong

1. <reason the top could be wrong>. Flips if <evidence>.
2. <reason the top could be wrong>. Flips if <evidence>.

## Assumptions

- <assumption and its source>
- Struck in pass 3: <inherited reason and the item it propped up>
```

## Loss score

| Score | Meaning |
|---|---|
| 0 | Nobody notices |
| 1 | One team notices and works around it |
| 2 | The goal slips or a commitment breaks |
| 3 | The goal fails or a customer or legal duty breaks |

## Evidence tags

| Tag | Meaning |
|---|---|
| measured | A number from a system or a test |
| reported | Someone said so, with a name and a date |
| assumed | No source, so treat it as a guess |
