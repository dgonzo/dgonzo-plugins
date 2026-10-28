# Owner brief template

Use the receiver’s agent CLI in the launch command, or give the prompt directly in their app. Copy this skeleton into the brief. Replace every angle-bracket field. Delete "How to start" when the receiver is a person. Delete "Assumptions" when no gap stayed open.

```markdown
# <Objective as a short title>

<What changes hands, in one sentence.> <Owner> owns it. <What is blocked, and who owns the blocker.>

## Owner

| Role | Name |
|---|---|
| Accountable owner | <one person> |
| Receiver | <person or "a fresh agent session"> |
| Deadline | <date or "none set"> |

## Facts the receiver needs

| Fact | Value |
|---|---|
| <fact> | <path, name, version or date> |

## How to start

    cd <absolute repo path>
    <agent-cli> "Read <absolute path to this brief> and do phase 1."

## Phase 1 <name>

1. <One imperative action.>
2. <If a condition holds, then the action.>

## Phase 2 <name>

Start only when <gate condition>.

1. <One imperative action.>

## Blockers

| Blocker | Owner | Cleared when |
|---|---|---|
| <what stops the work> | <one person> | <observable state> |

## Done when

1. <A state a second person can check with yes or no.>

## Assumptions

- <Gap that stayed open, and the value the brief assumed.>
```

## Done when items

Each item names a state, not an activity. A second person must be able to check it without asking the owner.

| Bad | Good |
|---|---|
| "Review the migration." | "`make test` exits 0 on `main`." |
| "Work on the dashboard." | "The dashboard shows October rows for all three regions." |
| "Coordinate with Ana." | "Ana has approved PR 42." |
| "Phase 1 is complete." | "`dgonzo:working-style` lists in a fresh session." |

## Good interview questions

Each question closes one gap and takes 5 words or fewer to answer.

| Gap | Question |
|---|---|
| Owner | "Who is accountable if this slips?" |
| Done when | "What do you check to call it done?" |
| Blocker owner | "Who clears the vendor access?" |
| Deadline | "Is there a date this must land by?" |
| Receiver | "Person or fresh agent session?" |
