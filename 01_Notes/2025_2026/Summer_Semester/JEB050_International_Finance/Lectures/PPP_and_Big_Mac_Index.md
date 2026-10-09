---
course: JEB050
topic: Purchasing Power Parity and the Big Mac Index
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_5/week5_slides.pdf
tags: [JEB050, PPP, purchasing-power-parity, Big-Mac-index, real-exchange-rate, non-tradables]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_5/week5_slides.pdf]]
Related: [[Exchange_Rate_Types_and_Triangular_Arbitrage]], [[Balassa_Samuelson_Effect]], [[International_Fisher_Effect_and_REER]]

# Purchasing Power Parity and the Big Mac Index

## Historical Origins

**Purchasing Power Parity (PPP)** theory states that identical goods should trade at the same price when expressed in a common currency. The origins trace to the **University of Salamanca** (16th century Spanish scholastics), where it was used to explain exchange rate movements across the Spanish Empire.

The modern formulation was systematised by **Gustav Cassel (1922)** in the context of post-WWI exchange rate debates, proposing PPP as a basis for setting new parities after wartime inflation.

## The Law of One Price

The foundation of PPP is the **Law of One Price (LOOP)**: in competitive markets with no trade barriers, an identical good must sell at the same price everywhere when denominated in a common currency.

For a single good $i$:

$$P_i = E \cdot P_i^*$$

where $P_i$ is the domestic price, $P_i^*$ is the foreign price, and $E$ is the nominal exchange rate (domestic per foreign).

**Prerequisites for LOOP:**
- Perfect goods arbitrage (no trade costs, no tariffs)
- Identical goods (no quality differentiation)
- No entry/exit barriers
- No other motives for currency demand

## Absolute PPP

Aggregating LOOP across all goods to the price **level**:

$$P = E \cdot P^*$$

Solving for the equilibrium exchange rate:

$$\boxed{E_{PPP} = \frac{P}{P^*}}$$

This implies the **real exchange rate** $R = E \cdot P^*/P = 1$ under absolute PPP — all deviations from this are **misalignments**.

### Adjustment Mechanism

If $E > E_{PPP}$ (nominal depreciation beyond PPP level → domestic goods cheap → exports $\uparrow$, imports $\downarrow$ → demand for domestic currency $\uparrow$ → $E$ falls toward PPP).

## Relative PPP

The more empirically useful version deals with **changes** in exchange rates rather than levels:

$$\frac{\Delta E}{E} \approx \pi - \pi^*$$

where $\pi$ and $\pi^*$ are domestic and foreign inflation rates. A country with higher inflation will see its currency depreciate proportionally.

**Derivation:** Differentiating $P = E \cdot P^*$ with respect to time:

$$\hat{P} = \hat{E} + \hat{P}^* \implies \pi = \hat{E} + \pi^* \implies \hat{E} = \pi - \pi^*$$

## Deviations from PPP — Empirical Evidence

PPP fails systematically, especially in the short run:

| Cause of deviation | Mechanism |
|---|---|
| **Non-tradables** | Services (haircuts, restaurants) cannot be arbitraged across borders |
| **Imperfect substitutes** | French and German wine are not identical goods |
| **Trade costs** | Transport, tariffs, insurance create a price band |
| **Capital flows** | FX demand driven by finance, not just trade |
| **Index number problem** | Different consumption baskets across countries |

**Rogoff (1996) — the PPP Puzzle:** PPP deviations (deviations of $R$ from 1) have a **half-life of 3–5 years**. This is too slow for goods-market arbitrage to explain but too fast for financial market explanations. It remains an unresolved puzzle in international macroeconomics.

**Long-run PPP** holds reasonably well over periods of 10–30 years, especially when inflation differentials are large (hyperinflation episodes). 

**Engel & Rogers (1996):** Price differences across cities within the same country (e.g., Boston vs. Philadelphia) are far smaller than across the US-Canada border for identical goods — suggesting border effects are large.

## The Big Mac Index

Invented by **The Economist** in 1986, the Big Mac Index uses the price of a McDonald's Big Mac as a single-good PPP indicator. The Big Mac has the advantage of being a standardised product produced in ~100 countries.

**Formula:**

$$E_{BigMac} = \frac{P_{BigMac}^{domestic}}{P_{BigMac}^{USD}}$$

If $E_{BigMac} < E_{market}$, the domestic currency is **undervalued** relative to USD.

**January 2026 Czech example:**
| Measure | Value |
|---|---|
| Big Mac price (CZK) | 115 CZK |
| Big Mac price (USD) | \$6.12 |
| Implied PPP rate | 115/6.12 = **18.79 CZK/USD** |
| Actual market rate | 20.93 CZK/USD |
| CZK valuation | **10.2% undervalued** |

The CZK has been persistently undervalued on the raw Big Mac Index (around −25% historically), consistent with the **Balassa-Samuelson effect**: Czech prices (especially non-tradables) are systematically lower than US prices because of lower productivity levels.

### Adjusted Big Mac Index

The GDP-adjusted version accounts for the fact that richer countries systematically have higher price levels (Balassa-Samuelson). Regression of Big Mac price on GDP per capita (R² ≈ 0.56) gives an "adjusted" valuation correcting for income level. After this adjustment, the CZK undervaluation narrows considerably.

### McWages (Ashenfelter & Jurajda)

An alternative cross-country comparison using **entry-level McDonald's wages** (identical skill requirements, technology, and product worldwide). The **Big Macs Per Hour (BMPH)** metric (how many Big Macs a worker can buy per hour of work) captures real wage levels internationally.

## PPP with Non-Tradables — Generalisation

Let $\alpha$ = share of non-tradables in domestic basket; $(1-\alpha)$ = share of tradables.

$$P = \alpha P_N + (1-\alpha) P_T, \qquad P^* = \beta P_N^* + (1-\beta) P_T^*$$

If PPP holds for tradables: $P_T = E \cdot P_T^*$. Then:

$$E = \frac{P}{P^*} \cdot \frac{\beta(P_N^*/P_T^*) + (1-\beta)}{\alpha(P_N/P_T) + (1-\alpha)}$$

Higher relative price of non-tradables ($P_N/P_T$) in the domestic economy → lower equilibrium $E$ (domestic currency stronger than pure tradables PPP would suggest). This is the starting point for the [[Balassa_Samuelson_Effect]].
