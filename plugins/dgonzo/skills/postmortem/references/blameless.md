# Blameless rewrites

A postmortem names conditions, not culprits. A person who made a mistake did what the system allowed. The fix changes the system.

## Rules

1. Name the role or the system as the actor. Name the person only in the source column.
2. State the action as a fact. Leave out judgment words such as "careless" or "should have".
3. State the condition that made the action reasonable at the time.
4. Ask what the person knew at that moment. Do not use what the team learned later.
5. If two accounts disagree, record both with their sources. Do not pick one.

## Rewrites

| Blame story | Blameless entry |
|---|---|
| "Ana pushed a bad config." | The deploy shipped a config with no validation step in the pipeline. |
| "Sales dropped the ball on the renewal." | The renewal date had no owner after the account changed hands. |
| "QA missed the bug." | The test plan had no case for an empty cart. |
| "Ops ignored the alert." | The alert fired into a channel with 200 other alerts that day. |
| "The PM promised a date engineering never agreed to." | The launch date went public before an estimate existed. |

## The test

Put any other competent person in the same seat. If the event would still happen, the cause is a condition. If it would not, ask what that person would have known or had. That difference is the condition to name.
