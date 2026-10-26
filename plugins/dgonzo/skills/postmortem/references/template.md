# Postmortem template

Copy this layout. Replace each placeholder. The table rows are examples. Replace them too. Keep every section. If a section is empty, write "None found" and the reason.

```markdown
# Postmortem: <event in plain words>

Date of event: <yyyy-mm-dd>. Written: <yyyy-mm-dd>. Author: <name>.

## Bottom line

<Strongest cause in one sentence.> <What is still exposed.> <Who owns the fix.> <Every "Owner needed" or "Date needed".>

## Impact

<Who was affected.> <For how long.> <Cost in numbers: users, revenue, hours or deals.>

## Timeline

| Time | Event | Source | Status |
|---|---|---|---|
| 09:12 | Config change merged | PR #482 | Sourced |
| 09:40 | First customer report | Support ticket 1193 | Sourced |
| 09:55 | On-call paged | Recalled by <name> | Recalled |

## Contributing causes

| Cause | Rating | Timeline rows |
|---|---|---|
| No validation step for config | Prevents | 09:12 |
| Alert routed to a noisy channel | Shortens | 09:40, 09:55 |

<One short paragraph per cause if the table needs context.>

## Precedents

| Case | Shared condition | Fix then | Basis |
|---|---|---|---|
| <prior incident> | Config shipped without validation | Added schema check to CI | Sourced: <link> |
| Config drift | Config changed outside review | Validate config at deploy time | Pattern |

## Actions

| Action | Owner | Due | Cause |
|---|---|---|---|
| Add config schema check to the deploy pipeline | <one name> | <yyyy-mm-dd> | No validation step |
| Move the alert to the paging channel | <one name> | <yyyy-mm-dd> | Noisy channel |

## Evidence gaps

| Missing source | Question it would settle |
|---|---|
| Pager logs for 09:40 to 09:55 | Did the first alert reach anyone? |
```

## Rating scale

| Rating | Meaning |
|---|---|
| Prevents | Without this cause, the event does not happen |
| Shortens | The event happens but ends sooner or costs less |
| No effect | The outcome is the same, so the cause is dropped |

## Status and basis marks

| Mark | Meaning |
|---|---|
| Sourced | A log, PR, ticket, message or document backs it |
| Recalled | A named person remembers it and no record exists |
| Pattern | It comes from general knowledge, not a found document |
