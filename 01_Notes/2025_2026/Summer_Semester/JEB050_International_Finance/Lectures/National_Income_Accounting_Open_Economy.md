---
course: JEB050
topic: National Income Accounting for an Open Economy
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_3/week3_Slides.pdf
tags: [JEB050, national-income, current-account, twin-deficit, saving-investment]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_3/week3_Slides.pdf]]
Related: [[BOP_and_IIP]], [[DD_AA_Model]]

# National Income Accounting for an Open Economy

## The Open-Economy National Income Identity

The national income identity for a **closed economy** is $Y = C + I + G$. In an open economy, residents can also purchase goods produced abroad (imports $M$) and foreigners purchase domestically produced goods (exports $X$):

$$\boxed{Y = C + I + G + (X - M)}$$

The term $X - M$ is the **trade balance** (also referred to as the current account balance $CA$ in a simplified setting where $CA \equiv X - M$).

**Absorption** $A$ is defined as total domestic spending:

$$A \equiv C + I + G$$

Therefore:

$$CA = Y - A$$

A current account surplus ($CA > 0$) means the country produces more than it absorbs domestically — it is a net lender to the world. A deficit ($CA < 0$) means the country absorbs more than it produces — it borrows from abroad.

## The Saving-Investment Framework

**National saving** $S$ is income not consumed by the private sector or government:

$$S = Y - C - G$$

Combining with the income identity:

$$S = I + CA$$

$$\boxed{CA = S - I}$$

A current account surplus corresponds to national saving exceeding domestic investment — the surplus saving is lent abroad.

### Decomposition into Private and Public Saving

Define:
- **Private saving:** $S^P = Y - T - C$ (after-tax income minus consumption)
- **Government saving (fiscal surplus):** $S^G = T - G$

Then $S = S^P + S^G = (Y - T - C) + (T - G) = Y - C - G$ ✓

Substituting:

$$\boxed{CA = (S^P - I) + (T - G)}$$

### Interpretation

| Component | Meaning |
|---|---|
| $S^P - I$ | Private sector's net lending (+) or net borrowing (−) |
| $T - G$ | Government's fiscal surplus (+) or deficit (−) |

The CA balance is the sum of the private sector's financial balance and the government's fiscal balance.

## Twin Deficit Hypothesis

The identity $CA = (S^P - I) + (T - G)$ implies that if private saving and investment are relatively stable, a **fiscal deficit** ($T < G$) tends to be associated with a **current account deficit** ($CA < 0$) — the **twin deficit hypothesis**.

**Mechanism:** $\downarrow (T-G)$ → either directly reduces national saving → $CA$ deteriorates; or via higher interest rates if the fiscal deficit is monetised → $I$ falls, partially offsetting.

**Historical example — USA 1981–85:**
| Year | Fiscal deficit (% GDP) | Current account (% GDP) |
|---|---|---|
| 1981 | −2.6% | +0.2% |
| 1983 | −6.3% | −1.5% |
| 1985 | −5.4% | −3.0% |

The Reagan tax cuts created a fiscal deficit which coincided with a large CA deterioration, driven by dollar appreciation and capital inflows following the monetary contraction of Volcker.

**Limitations:** Private saving may respond endogenously (Ricardian equivalence argument). Empirically, the correlation is positive but not one-for-one.

## Current Account and External Indebtedness

A persistent CA deficit leads to accumulation of net foreign liabilities. The dynamic is:

$$\text{Net IIP}_t = \text{Net IIP}_{t-1} + CA_t + \text{Valuation changes}_t$$

For a country to maintain a stable debt-to-GDP ratio, the CA deficit cannot exceed:

$$|CA| \leq g \cdot |\text{Net IIP}|$$

where $g$ is the nominal GDP growth rate.

## Relevance for Exchange Rate Policy

The identity $CA = S - I$ shows that exchange rate policy alone cannot improve the CA without underlying changes in saving and investment. This insight is central to the [[DD_AA_Model]] and the [[Marshall_Lerner_Condition_and_Swan_Diagram]]:

- Depreciation raises $X$ and lowers $M$ (if Marshall-Lerner holds), improving $CA$
- But this works through stimulating $Y$, which raises $C$ and potentially $I$, partially absorbing the gain
- Sustainable CA improvement requires adjustment in the saving-investment balance
