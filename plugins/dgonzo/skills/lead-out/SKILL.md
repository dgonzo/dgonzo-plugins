---
name: lead-out
description: Use when David holds a view the room has not heard, before an exec meeting, a team post or a hard one-to-one. Returns his position in one sentence, the order of conversations, an ask and a date per person, and his first line.
---

# lead-out

Produces a plan to move a room: David's position, the order of conversations, one ask per person and the line he says first.

It counters deference, where David holds a view and the room hears a question.

## Passes

| Pass | Mode | Action |
|---|---|---|
| 1 | Reductive: ground truth only, with inherited assumptions removed | The position as one sentence David would say aloud, with a date |
| 2 | Sequential play: reason back from the end state to the first move | The order of conversations, from the last yes needed back to the first |
| 3 | Modeling: simulate how each named person responds, specifically | Per person, the predicted reply and one ask with a date |

A room check follows the passes. It covers what David's strengths skip.

## Steps

1. Read `~/.claude/dgonzo/self.md` with a file read. If it is missing, say so in one line and continue.
2. If David named a source, read it. A source is a thread, a doc or meeting notes.
3. Find four inputs. They are the situation, David's view, the people involved and the date of the room or the deadline.
4. If an input is missing, ask for all missing inputs in one message. Ask once.
5. If David gave no view, draft one from his material and mark it `[CONFIRM]`. Never present a drafted view as his.
6. Run pass 1. Write the position as "We will X by date D." or "I think X. I want Y by date D."
7. Test the position with the position test below. Rewrite it until every row passes.
8. Name the smallest outcome that counts as a win in this room. David stops pushing when he has it.
9. List every person the position touches. Include who decides, who must act, who is affected and who is not in the room.
10. For each person, read `~/.claude/dgonzo/readers/<name>.md` if it exists. Without a file, tag every claim about them assumed.
11. Run pass 2. Write the end state as who has said yes to what. Then work back to the first conversation.
12. Put a one-to-one before the room for every person whose yes the room depends on.
13. Put a one-to-one before the room for every person the position costs something.
14. Run pass 3. For each person, write what they gain, what they lose and their first reply.
15. Write one ask per person. Each ask has a verb they perform and a day.
16. If a person's reply is no, name the disagreement in plain words. Never soften the position to remove it.
17. If two or more people gain from the current pattern staying as it is, name `dgonzo:game` standoff in one line.
18. Run the room check below. Fill every row. Write "none" when a row is empty.
19. Run the above-the-line check. The position blames no person and predicts no doom. Each problem it names carries a next move.
20. Write the line David says first. It is the position, or the ask that opens the first one-to-one.
21. Load `dgonzo:voice`. Run its gate on the position, every ask and the first line.
22. Reply in the chat. Write a file only when David asks, and then to `~/.claude/dgonzo/moves/lead-out-<topic>.md`.

### Position test

| Test | Pass when |
|---|---|
| One sentence | It has one main verb and no "and also" |
| Sayable | David could say it aloud to the room without notes |
| Statement | It is not a question |
| Dated | It names a day |
| Owned | It says what David owns |
| One softener | "I think" appears at most once. No "maybe", "might" or "perhaps" |
| Two steps | The reason fits in two steps a listener can follow |

### Room check

| Check | Question |
|---|---|
| Left out | Who is affected and not in the room or on the thread |
| Criticism | Who will read the position as a verdict on their work |
| Time | Who needs to hear it one to one before the room |
| Same case | Whether two people get different treatment for the same case |
| Disagreement | What disagreement the position creates, and who holds it |
| Consult | Which one person David checks with first, if the call is hard to reverse |
| Input first | Whose view David asks for in the room before he gives his |

## Output

Sections in this order.

1. Bottom line. The position sentence. Then what is blocked and who owns it.
2. Win. The smallest outcome that counts in this room.
3. Moves. A table with Order, Who, Channel, Ask, Date and Predicted reply columns.
4. Room check. The seven rows with an answer each.
5. First line. In a fenced block, ready to say or paste.
6. Open. Every `[CONFIRM]` and every claim tagged assumed that would change the order.

## Limits

- Never invents David's position. A drafted one stays marked `[CONFIRM]`.
- Never softens the position to avoid a disagreement. It names the disagreement.
- Never writes an ask without a day.
- Never judges a colleague's character. It describes what they gain, lose and do.
- Never models private life or personality type. Work behaviour only.
- Never writes a plan that names a colleague into a repo.
- Never copies `self.md` or a reader file into a repo.
- Never sends anything. David speaks and sends.
- Never writes an HTML artifact.
