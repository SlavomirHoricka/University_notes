---
course: JEB044
topic: Inventory Cost Flow Assumptions (FIFO, LIFO, Average Cost)
source: 00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/03_Inventory_(act).pdf
tags: [JEB044, financial-accounting, inventory, FIFO, LIFO, average-cost, COGS, IFRS, US-GAAP]
created: 2026-04-20
---
Parent: [[JEB044_Financial_Accounting_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/03_Inventory_(act).pdf]]
Related: [[Expense_Recognition_and_Matching_Principle]], [[Income_Statement_Structure]], [[FIFO_vs_LIFO_Analysis]], [[Sales_Returns_and_Allowances]]

# Inventory Cost Flow Assumptions

## Inventory Definition

Inventory comprises assets:
- **held for sale** in the ordinary course of business (finished goods),
- **in the process of production** for such sale (work-in-process), or
- **in the form of materials** to be consumed in production (raw materials).

## The Cost Allocation Identity

At any period end, total costs must be fully allocated between what was sold and what remains:

$$\underbrace{Iv_{t-1} + \text{Purchases}_t}_{\text{Goods Available for Sale}} = \underbrace{COGS_t}_{\text{sold}} + \underbrace{Iv_t}_{\text{remaining}}$$

Therefore:

$$COGS_t = Iv_{t-1} + \text{Purchases}_t - Iv_t$$

The **cost flow assumption** determines which specific unit costs are assigned to $COGS_t$ versus $Iv_t$.

## Perpetual vs. Periodic Systems

| System | When COGS is recorded | Inventory balance |
|---|---|---|
| **Perpetual** | At each sale transaction | Updated continuously |
| **Periodic** | At period end (physical count) | Updated at period end |

Modern firms use perpetual systems; the periodic method is conceptually simpler for instruction.

## Three Cost Flow Assumptions

### FIFO — First In, First Out

The oldest units purchased are assumed to be the first units sold.

**In rising-price environments (inflation):**
- COGS reflects **old (lower) costs** → COGS is understated relative to current replacement cost.
- Ending inventory reflects **recent (higher) costs** → BS inventory is close to current market value.
- **Result:** Higher gross profit, higher reported NI, higher taxes.

### LIFO — Last In, First Out

The most recently purchased units are assumed to be the first units sold.

**In rising-price environments:**
- COGS reflects **recent (higher) costs** → COGS is a better approximation of economic cost.
- Ending inventory reflects **old (lower) costs** → BS inventory is significantly understated.
- **Result:** Lower gross profit, lower reported NI, lower taxes ("economic ideal").

**LIFO Reserve:** The difference between FIFO and LIFO inventory values:

$$LFR = Iv_{\text{FIFO}} - Iv_{\text{LIFO}}$$

The LIFO reserve grows in inflationary environments. Analysts can use it to convert LIFO statements to FIFO for comparability:

$$Iv_{\text{FIFO}} = Iv_{\text{LIFO}} + LFR$$

$$COGS_{\text{FIFO}} = COGS_{\text{LIFO}} - \Delta LFR$$

### Average Cost (AC) / Weighted Average

COGS and ending inventory are measured at the **weighted-average unit cost** of all units available for sale:

$$\bar{c} = \frac{\text{Total Cost of Goods Available for Sale}}{\text{Total Units Available for Sale}}$$

Results fall between FIFO and LIFO in inflationary periods.

## Comparative Summary (Inflation)

| Metric | FIFO | Average Cost | LIFO |
|---|---|---|---|
| COGS | Low (understated) | Middle | High (accurate economic cost) |
| Ending Inventory | High (close to market) | Middle | Low (understated — BS distortion) |
| Gross Profit | Overstated | Middle | Accurate |
| Taxes | High | Middle | Low |

## Regulatory Differences

| Standard | FIFO | LIFO | Average Cost |
|---|---|---|---|
| **IFRS** | Allowed | **Prohibited** (banned 2003) | Allowed |
| **US GAAP** | Allowed | Allowed (with conformity rule) | Allowed |

**IFRS prohibition of LIFO** was motivated by the BS distortion: LIFO inventory can become severely stale in long-held layers, making balance sheets non-comparable across firms.

**US GAAP LIFO conformity rule:** if a firm uses LIFO for tax purposes, it must also use LIFO for financial reporting. This links the tax benefit directly to the financial reporting choice.

## LIFO Liquidation Risk

If a firm using LIFO sells more inventory than it purchases (draws down old layers), old low-cost layers are expensed — artificially reducing COGS and inflating taxable income in that year. This creates a "LIFO liquidation" problem that can mislead analysts about underlying profitability.

For the broader economic and managerial considerations of FIFO vs. LIFO, see [[FIFO_vs_LIFO_Analysis]].
