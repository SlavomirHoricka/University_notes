---
course: JEB050
topic: Exchange Rate Types, Quotation, and Triangular Arbitrage
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_4/week4_Slides.pdf
tags: [JEB050, exchange-rate, spot-rate, forward-rate, real-exchange-rate, triangular-arbitrage, NEER]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_4/week4_Slides.pdf]]
Related: [[UIP_and_CIP]], [[International_Fisher_Effect_and_REER]], [[PPP_and_Big_Mac_Index]]

# Exchange Rate Types, Quotation, and Triangular Arbitrage

## Quotation Conventions

An **exchange rate** is the price of one currency expressed in terms of another.

**Direct quotation** (domestic currency per unit of foreign):

$$E_{CZK/EUR} = 25 \quad \text{(25 CZK per 1 EUR)}$$

A **rise** in $E_{CZK/EUR}$ means the CZK has **depreciated** (more CZK needed to buy 1 EUR).

**Indirect quotation** (foreign currency per unit of domestic):

$$E_{EUR/CZK} = 1/25 = 0.04$$

In this course, $E$ denotes the **direct quotation** (domestic per foreign) unless otherwise stated. An increase in $E$ = depreciation of domestic currency.

## Spot vs. Forward Exchange Rates

| | Spot Rate | Forward Rate |
|---|---|---|
| **Settlement** | Typically T+2 (two business days) | Agreed today; settlement on a future date (30, 90, 180, 360 days) |
| **Price** | Current market price | Locked-in today via forward contract |
| **Purpose** | Immediate conversion | Hedging, speculation |

The **forward premium** (or discount) measures how the forward rate differs from the spot:

$$FP = \frac{F - S}{S} \approx R_{domestic} - R_{foreign}$$

In absolute terms:

$$FP = (R_{domestic} - R_{foreign}) \cdot S \cdot \frac{n}{360}$$

where $n$ = number of days to forward settlement. Forward points are often quoted in **pips** (multiply by 10,000).

**Example** (CNB forward rates, March 16, 2026): If spot CZK/EUR = 25.10 and 90-day forward = 25.30, the forward premium on EUR = $(25.30 - 25.10)/25.10 \approx 0.80\%$ per 90 days, annualised $\approx 3.2\%$.

## Real Exchange Rate

The **nominal exchange rate** $E$ measures the relative price of currencies. The **real exchange rate** $R$ (also written $q$) measures the relative price of goods:

$$\boxed{R = E \cdot \frac{P^*}{P}}$$

where $P^*$ = foreign price level, $P$ = domestic price level, $E$ = nominal ER (domestic per foreign).

**Interpretation:** $R$ is the price of a basket of foreign goods expressed in units of the domestic goods basket. If $R$ rises, foreign goods become relatively more expensive → domestic competitiveness improves.

Under absolute PPP, $R = 1$ (purchasing power parity). In practice, $R$ deviates substantially and persistently from 1 (see [[PPP_and_Big_Mac_Index]]).

## Effective Exchange Rates

A **bilateral** exchange rate (e.g., CZK/EUR) captures only one trade partner. The **effective exchange rate** is a trade-weighted average against a basket of currencies.

**Nominal Effective Exchange Rate (NEER):**

$$NEER_t = 100 \times \prod_{i=1}^{n} \left(\frac{S_{it}}{S_{i0}}\right)^{w_i}$$

where $S_{it}$ is the bilateral rate against currency $i$ at time $t$, $S_{i0}$ is the base-period rate, and $w_i$ is the trade weight (sum of weights = 1).

For the **Real Effective Exchange Rate (REER)**, the bilateral rates are adjusted for relative price levels. See [[International_Fisher_Effect_and_REER]] for the full derivation.

## Triangular Arbitrage

In a perfectly functioning FX market, bilateral exchange rates must be mutually consistent. If not, **triangular arbitrage** yields a riskless profit.

### No-Arbitrage Condition

$$S_{CZK/USD} = S_{CZK/EUR} \cdot S_{EUR/USD}$$

**Example:** Suppose:
- $S_{CZK/EUR} = 25.0$
- $S_{EUR/USD} = 1.10$
- $S_{CZK/USD}$ should equal $25.0 \times 1.10 = 27.5$

If instead $S_{CZK/USD} = 27.0$ (USD underpriced):
1. Buy USD with CZK: spend 27,000 CZK → receive 1,000 USD
2. Sell USD for EUR: receive $1,000/1.10 \approx 909.1$ EUR
3. Sell EUR for CZK: receive $909.1 \times 25.0 = 22,727.3$ CZK... 

Wait — that gives a loss. Let me re-check the direction: if USD is **underpriced** in the CZK/USD market (you only pay 27 CZK per USD instead of the implied 27.5):

1. Buy 1000 USD at 27,000 CZK (paying only 27 per USD instead of 27.5)
2. Sell 1000 USD for EUR at $1/1.10 = 0.909$ EUR/USD → receive 909 EUR  
3. Sell 909 EUR for CZK at 25 → receive 22,727 CZK

That's a loss. The correct direction:

1. Start with CZK; buy EUR at 25 → 1 EUR costs 25 CZK
2. Buy USD with EUR at 1.10 → 1.10 USD per EUR
3. Sell USD for CZK at (incorrect) 27 → receive $1.10 \times 27 = 29.7$ CZK per initial EUR

Since the implied CZK/USD = 27.5 but market quotes 27, there's no profit going EUR → USD → CZK (only 27 CZK per USD instead of 27.5). The arbitrage runs **CZK → USD → EUR → CZK** when USD is overpriced in the cross rate.

In liquid markets, triangular arbitrage is exploited by electronic traders within milliseconds, keeping cross rates aligned to the no-arbitrage condition.
