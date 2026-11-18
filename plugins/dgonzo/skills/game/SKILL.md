---
name: game
description: Use when the same argument comes round again, before an ask or a quote to a vendor, partner or customer, or before David promises a number or a date. Picks one of three game theory stacks, standoff, counterparty or commitment, and returns one move.
---

# game

Produces a read of the game David is in and the one move that changes it.

It counters the one-player view, where a plan treats other people's choices as fixed while each of them is choosing too.

## Stacks

The skill runs one stack of three modes. David may name it, as in `dgonzo:game standoff`.

| Stack | Use when | Modes in order |
|---|---|---|
| Standoff | The same argument comes round a third time. A number nobody is rewarded for stating honestly. A peer stuck below the line | Equilibrium diagnosis, Incentive compatibility, Mechanism design |
| Counterparty | Before an ask, an information request or a quote to a vendor, partner or customer | Information asymmetry, Signaling and screening, Bargaining and outside options |
| Commitment | Before David gives a number or a date. Before he relies on someone else's promise | Credible commitment, Sequential play, Reputation |

The prompt for each mode is in [../lens/references/modes.md](../lens/references/modes.md) under Game.

## Passes

| Stack | Pass | Action |
|---|---|---|
| Standoff | 1 | The pattern that repeats, and why each player's behaviour is their best reply to the others |
| Standoff | 2 | Per player, what they are rewarded for against what the goal needs |
| Standoff | 3 | At most 3 rule changes that make the wanted behaviour the best reply, with one picked |
| Counterparty | 1 | What they know that we do not, before and after signing. What we know that they do not |
| Counterparty | 2 | What our ask discloses, what to send in its place and what to ask that only a strong counterparty can answer |
| Counterparty | 3 | Our walk-away and theirs, how each moves with time and the deal shape that follows |
| Commitment | 1 | Per promise, what makes it costly to break. A promise with no cost is flagged as talk |
| Commitment | 2 | The later moves in order, reasoned back from the end date, with the point of no return |
| Commitment | 3 | What this move teaches each observer about David, and the precedent it sets |

## Steps

1. If David named a source, read it. Otherwise use the situation in the conversation.
2. If the situation or the goal is missing, ask once for both.
3. Pick the stack from the Stacks table. Say which one and why in one line.
4. If two stacks fit, run the one tied to the nearest dated move. Name the other in the Open section.
5. List every player. Include David, internal players and anyone watching.
6. For each player, read `~/.claude/dgonzo/readers/<name>.md` if it exists.
7. Fill the players table. The columns are what they want, what they are rewarded for, what they know that others do not and their outside option.
8. Tag every cell observed, stated or assumed. Never fill a gap with a guess presented as fact.
9. Run the three passes of the stack in order. Give each pass its own section.
10. In a standoff, describe each behaviour as a best reply to a rule or a reward. Never as a flaw in the person.
11. In a counterparty game, write the list of what David does not send.
12. In a commitment game, mark every number or date David has not yet measured. He does not promise an unmeasured number.
13. Run the falsification check. For each finding, name the observation that would prove it false. A finding nothing could prove false is tagged assumed.
14. Run the base rate check where a number exists. State how often this kind of move works, with its source. Otherwise write "base rate unknown".
15. Write the one move. It names what David does, to whom and by what day. It says which payoff it changes.
16. If the move needs a room moved, name `dgonzo:lead-out` in one line.
17. If the game names an internal colleague, reply in the chat. Write a file only when David asks, and then to `~/.claude/dgonzo/moves/game-<topic>.md`.
18. If the game names only outside parties, write `game-<topic>.md` in the folder David is working in. Link it.

## Output

Sections in this order.

1. Bottom line. The game in one sentence and the one move. Then what is blocked and who owns it.
2. Players. The table from step 7, with a status per cell.
3. One section per pass, headed with the mode name.
4. The move. What, to whom, by what day and which payoff it changes.
5. Do not send. Only for a counterparty game.
6. Open. Each assumed cell that would change the move, with who can settle it.

The prose follows `writing:writing-standard`.

## Limits

- Never judges a person's character. A player responds to rules, rewards and information.
- Never presents an assumed payoff as known.
- Never recommends a move that deceives a colleague or a counterparty. It changes what is rewarded, disclosed or committed.
- Never returns more than one move. Other candidates go in the Open section.
- Never writes a game that names a colleague into a repo.
- Never contacts a counterparty or sends a message.
- Never writes an HTML artifact.
