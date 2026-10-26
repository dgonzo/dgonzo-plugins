# Voice samples

These are verbatim excerpts of David's writing. Read them before drafting. Match the rhythm and the stance. Never copy the stories or the numbers into new text unless David supplies them for that text.

## Sources and trust

| Source | Trust | Reason | Quoted |
|---|---|---|---|
| `gwrk/docs/product/FOXTROT-CHARLIE.md` | High | His own essay, first person, his stories | All 10 samples |
| `gwrk/.gwrk/rules/operating-model.md` | Medium | His rules, written as orders to agents, with emoji | No |
| `gwrk/docs/product/GWRK-PRD-PRFAQ.md` | Medium | One quote is his, the body is AI-assisted | No |
| `gwrk/docs/product/WHAT_IS_GWRK.md` | Low | AI-drafted structure that reuses his lines | No |
| `gwrk/README.md` | Low | AI-drafted, with emoji and badges | No |
| gwrk commit messages | Low | 64 of his last 80 carry a Claude co-author line | No |

Paths are relative to `/Users/dgonzalez/Projects/MyTools/`. Line numbers refer to `FOXTROT-CHARLIE.md`. Trailing spaces used as Markdown line breaks are removed. An ellipsis marks a cut.

## 1. The thesis, stated flat

Lines 13 to 17.

```text
After almost two decades doing this, the cleanest truth I’ve earned is this:

**What gets built is 1,000% more important than how it gets built.**

Not rhetorically. Literally.
```

## 2. One-line beats

Lines 31 to 37.

```text
All the “best practices” finally showed up.

And it still didn’t matter.

Because no amount of flawless process can salvage a bad bet.
You cannot cargo-cult your way into product-market fit.
You can have immaculate sprints and still sprint straight into irrelevance.
```

## 3. Concede, then strike

Line 11.

```text
I will grant that for established leaders in the market, the marginal gains of building things correctly do matter—at least until someone else builds the right thing for right now and ships it quickly.
```

## 4. A company story as evidence

Lines 25 to 27.

```text
Meanwhile, companies like DataRobot had every chance to win. If they’d built the right thing, they’d be worth billions today. Shortly after I arrived we were autopsying tech debt, identifying product gaps, play-testing PLG, and fretting timing failures. But the postmortems miss the point. The brutal reality is:

**They didn’t build the right product, and for most of their life, they didn’t build it well.**
```

## 5. Naming the unpopular part

Lines 71 to 73.

```text
Here’s the part people avoid because it’s politically incorrect:

**When the landscape is dominated by unknown unknowns, high command-and-control communication isn’t authoritarian—it’s literally battle-tested best practice.**
```

## 6. A causal chain

Lines 63 to 65.

```text
Velocity gives you **reps**.
Reps give you **truth**.
Truth gives you **direction.**
```

## 7. Edge, kept work-safe

Lines 4 and 69.

```text
Also, a work-friendly euphemism for **Fuck Ceremony**.

... But if the biggest unknown is **exactly what the hell you should be building**, then no amount of sprint discipline, story-point virtuosity, or retrospective poetry will save you. You’ll simply execute beautifully—in the wrong direction.
```

## 8. Invariants and their diagnosis

Lines 106 to 120.

```text
2. **Reality is expressed as state, not narrative.**
   If it cannot be pointed to, it does not exist.

3. **All commitments exist as written artifacts.**
   If it is not written, it is not committed.

4. **Shipping happens frequently enough to surface truth.**
   Long cycles hide error. Short cycles reveal it.

5. **Value is measured in adoption or outcome, not effort.**
   Activity without impact is noise.

When any invariant breaks, ceremony rushes in to compensate.

This is not ideological. It is diagnostic.
```

## 9. Tools are not the work

Lines 54 to 59.

```text
Tools don’t extract truth—people do.
Tools don’t make decisions—leaders do.
Tools don’t create clarity—precision does.

Tool choice is second-order.
Truth extraction and clear thinking are first-order.
```

## 10. Mantra, verdict and no consensus

Lines 89 to 91, then line 368.

```text
**Truth → Clarity → Throughput → Value.**

Everything else is decoration.

...

Foxtrot Charlie scales by **compressing decision latency**, not by managing consensus.
```

## Work register patterns

These come from David's Slack and email between August and October 2026. Names and figures are replaced with placeholders. The verbatim messages are in `~/.claude/dgonzo/voice-samples.md` on David's machine only.

### 11. One-line Slack asks

```text
would you drop the link <Name> shared. I'm going to do a trial run of <task> so we're prepared for tomorrow.

<Name> I've already got <thing>. Let me get you an api key.

I defer to <Name> what he can do and what needs to be on <Name>.
```

### 12. Short email, name first, signed

```text
<Name>, looks very good. Let's work with <Name>'s process to get some interviews scheduled. --dg

These will be done.

<Name> I put 30 minutes tomorrow. Really appreciate it. --dg
```

### 13. Point, owner and next step

```text
<Name>, I'm working this week on <work> but based on this we need <thing>. I'll draft a spec with <Name> to deliver this so that <system> doesn't have to <cost>. --dg

<Vendor> and <Customer> are our biggest reasons to <goal>. <Name>, would you grab these requirements and we'll discuss prioritizing <work>.
```

### 14. Numbers as receipts

```text
We compared your <items> with ours and got almost <n>% coverage, which we're ok with, we have avenues to fill the remainder.
```

### 15. Structured approval request

This layout got a yes within three hours. A long email that reasoned out loud on a similar topic did not land with the same reader.

```text
<Name>,

I need your approval for a <term> <thing> at <amount>. <Name> is reviewing <item>. <Party> wants <action> by <date>.

WHAT WE ARE BUYING
   - <fact>
WHY
   - <fact with a number>
WHEN
   - <date>
COST
   - <amount>, and how it was negotiated
ASK

Approve the <amount> spend. Once <condition>, we will <action>.

Thank you,

--dg
```

### 16. Team post

```text
Team, now that <change> I want to communicate <what> and what I would like from everyone in terms of <practice>:

<who reports to whom, one line each>

I would like for <names> to <action> at least <cadence>.

Our goal is to, by <date>, be <state>.

Thank you each for how you've worked to get us moving in a good direction.

--dg
```

## Add samples here

David: add verbatim messages to `~/.claude/dgonzo/voice-samples.md`. Add a pattern here with names and figures replaced by placeholders.
