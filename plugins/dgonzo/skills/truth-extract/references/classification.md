# Claim classification

Every claim gets one class. When two classes seem to fit, pick the lower one. Asserted is lower than Inferred, and Inferred is lower than Grounded.

## The three classes

| Class | Test | Example |
|---|---|---|
| Grounded | The evidence is in the source, or in a file it cites that you opened and checked | "Churn was 4.2% in Q3, per the billing export attached" |
| Inferred | It follows from Grounded claims by a step of reasoning you can write down | "Q3 churn rose after the price change", when both dates and both churn figures are Grounded |
| Asserted | Nothing in the source supports it | "Customers love the new dashboard" |

## Hard cases

| Case | Class | Why |
|---|---|---|
| A customer says what they did, in their own words | Grounded, written as "<name> says they did X" | The transcript is the evidence of the statement, not of the fact |
| A customer says what other customers want | Asserted | Hearsay about third parties |
| A customer predicts what they will do | Asserted | A stated intention is not behaviour |
| A vendor quotes its own benchmark | Asserted | The vendor is the only source and has a stake in the result |
| A vendor names a customer reference you can call | Asserted until the call | The reference is the question, not the answer |
| A number with no origin | Asserted | A number is Grounded only when its source is named |
| A number with a named origin you cannot open | Asserted | The question asks for the origin |
| A competitor's price page included in the source | Grounded for the price on the date captured | Record the date |
| A competitor's claim about its own capability | Asserted | Same rule as a vendor |
| Several people repeat the same claim | Asserted | Repetition is not evidence |
| A senior person states it as settled | Asserted | Rank does not ground a claim |
| A claim built on one Asserted premise | Asserted | A chain is as strong as its weakest link |

## Writing the question

A good question is one a named person can answer with a fact, a document or a number. "Do customers like it?" is not a good question. "What share of the 40 pilot accounts used the dashboard weekly in October?" is a good question. Product analytics owns it.

Each question names three things:

- the claim it would ground
- the person, team or data source that can answer it
- the evidence that would count as an answer
