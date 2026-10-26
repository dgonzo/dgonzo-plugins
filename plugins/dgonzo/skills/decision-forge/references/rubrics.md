# decision-forge rubrics

Reference scales for the three passes and the verdict. The skill is in [../SKILL.md](../SKILL.md).

## Attack sources

Check every source. Skip one only when it cannot apply to this decision.

| Source | Question to ask |
|---|---|
| Evidence | What does the choice rest on that nobody has checked? |
| Rival | What does the rival option do better? |
| Cost | What does this cost in a year that it does not cost today? |
| People | Who has to run it, and can they? |
| Dependency | What outside party can break it? |
| Timing | What happens if this lands late? |
| Scale | What breaks at ten times today's volume? |
| Exit | What does leaving this cost later? |
| Motive | Is this chosen because it is familiar or someone's idea? |

Rate damage as if the attack is true. High means the decision fails or costs a quarter to recover. Low means a workaround exists inside one sprint. Medium is anything between.

## Attack status

| Status | Meaning |
|---|---|
| Survived | Evidence answers the attack |
| Landed | Evidence confirms the attack |
| Unresolved | No evidence either way. |

## Steel-man test

The steel-man passes when all three hold:

1. An advocate of the rival option would sign it as their own case.
2. It names at least one fact the decision cannot answer today.
3. It argues for the rival. It does not only argue against the decision.

If it fails, rebuild it once. If it still fails, say the rival has no strong case. That is a finding.

## Confidence scale

| Rating | Meaning |
|---|---|
| 9 to 10 | Measured or proven here |
| 7 to 8 | Strong evidence from a close case |
| 4 to 6 | Reasonable inference, untested here |
| 1 to 3 | Convention, hope or habit |

| Basis | Meaning | Ceiling |
|---|---|---|
| Known | Evidence the reader can check, with a source | 10 |
| Inferred | A pattern from similar cases | 7 |
| Assumed | Convention or belief, no evidence | 4 |

A rating above its basis ceiling is a calibration error. Lower it.

## Reversibility scale

| Door | Cost to reverse | Example |
|---|---|---|
| Two-way | Under a week of work | A library behind an interface |
| Sticky | Weeks, one team | A schema other teams read |
| One-way | A quarter or more, several teams | A vendor contract or a data platform |

Name the point of no return. It is the event after which the door type gets worse. A signed contract, a migration of live data and a public API release are typical.

## Verdict rules

Check the rows in order. The first match wins.

| Check | Verdict | When |
|---|---|---|
| 1 | Reopen | A high-damage attack landed |
| 2 | Reopen | A high-damage attack is unresolved and the door is one-way |
| 3 | Reopen | The steel-man's strongest point falls on the dimension most likely wrong, and no evidence answers it |
| 4 | Hold | Every high and medium attack survived, and no dimension is rated 4 or below |
| 5 | Hold with conditions | Any case the rows above do not match |

Under hold with conditions, each landed or unresolved attack and each dimension rated 4 or below becomes a condition. A condition names an owner, a test and a done-when before the point of no return. A condition with no known owner reads "owner: unassigned" and goes in the bottom line as blocked.
