---
course: JEB050
topic: Marshall-Lerner Condition, J-Curve, Swan Diagram, and Tinbergen's Rule
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_8/IF_2026_lecture_9_large_slides.pdf
tags: [JEB050, Marshall-Lerner, J-curve, Swan-diagram, internal-balance, external-balance, Tinbergen]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_8/IF_2026_lecture_9_large_slides.pdf]]
Related: [[BOP_and_IIP]], [[National_Income_Accounting_Open_Economy]], [[DD_AA_Model]], [[Fixed_Exchange_Rates_and_Impossible_Trinity]]

# Marshall-Lerner Condition, J-Curve, Swan Diagram, and Tinbergen's Rule

## Marshall-Lerner Condition

The **Marshall-Lerner (ML) condition** determines whether a currency devaluation/depreciation will improve the current account (balance of trade). It belongs to the **elasticity approach to the balance of payments** (Marshall, Lerner, Robinson, Machlup).

### Setup

Express the current account in units of domestic output (normalize $P = P^* = 1$):

$$CA = X - S \cdot M$$

where $X$ = export volume, $M$ = import volume, $S$ = nominal exchange rate (domestic per foreign).

A rise in $S$ (depreciation): domestic goods cheaper → exports increase, imports decrease. But the value of imports (in domestic currency) = $S \cdot M$, which may initially rise even if $M$ falls.

### Derivation

Differentiate with respect to $S$:

$$\frac{dCA}{dS} = \frac{dX}{dS} - M - S \cdot \frac{dM}{dS}$$

Define **elasticities** (both positive by convention):

$$\eta_x \equiv \frac{dX/X}{dS/S} = \frac{dX}{dS} \cdot \frac{S}{X}, \qquad \eta_m \equiv -\frac{dM/M}{dS/S} = -\frac{dM}{dS} \cdot \frac{S}{M}$$

Substituting into $dCA/dS$ and dividing by $M$:

$$\frac{dCA}{dS} \cdot \frac{1}{M} = \frac{\eta_x \cdot X}{S \cdot M} + \eta_m - 1$$

**Assuming balanced trade** ($X = S \cdot M$, i.e., $X/(S \cdot M) = 1$):

$$\boxed{\frac{dCA}{dS} = M \cdot (\eta_x + \eta_m - 1)}$$

### The Condition

Depreciation ($dS > 0$) improves the CA ($dCA > 0$) if and only if:

$$\boxed{\eta_x + \eta_m > 1}$$

The sum of the price elasticities of export demand and import demand must exceed 1.

**Intuition:**
- $\eta_x$: how much export volumes rise when domestic goods become cheaper (S rises)
- $\eta_m$: how much import volumes fall when foreign goods become more expensive (S rises)
- If both are very inelastic (each near 0), the volume responses are small but the price effect still raises the import bill → CA worsens

### Empirical Evidence on Elasticities

Long-run elasticities (2–3 year horizon, Pilbeam 1992, Gylfasson 1987):

| Country | $\eta_x$ | $\eta_m$ | Sum |
|---|---|---|---|
| USA | 1.19 | 1.24 | **2.43** |
| UK | 0.86 | 0.65 | 1.51 |
| France | 1.28 | 0.93 | 2.21 |
| Germany | 1.02 | 0.79 | 1.81 |
| **Industrial average** | **1.11** | **0.99** | **2.10** |
| **Developing average** | **1.1** | **1.5** | **2.6** |

Long-run elasticities generally satisfy the ML condition. However:
- **Rose (1991):** "Little evidence that the exchange rate significantly affects the trade balance" (5 OECD countries, various methods)
- **Bahmani et al. (2013)** meta-analysis (29 countries): ML condition is met at point estimates but **not** statistically met in ~half of cases
- **Giudici & Lima (2026):** Brazilian data, Bayesian SVAR — ML confirmed across sectors; J-curve probability high but not conclusive

## The J-Curve

After a real currency depreciation, the current account may **initially worsen** before improving — tracing a **J-shape** over time.

**Cause: time lags in quantity adjustment**

| Phase | What happens | Effect on CA |
|---|---|---|
| **Immediate (0–6 months)** | Existing contracts fixed; prices change but volumes do not adjust | Import bill rises (same volume, higher price in CZK); CA worsens |
| **Medium term (6–18 months)** | Importers and exporters gradually adjust volumes | Volumes start adjusting; CA begins improving |
| **Long run (18+ months)** | Full quantity adjustment; ML elasticities realized | CA improves to new long-run level |

The standard diagram shows CA on the y-axis and time on the x-axis: CA dips down immediately after depreciation (point 2) then recovers and improves above the original level (approaching the long-run effect) — the J shape.

**Evidence is mixed:** Some studies find clear J-curves; others find no systematic pattern. The ML condition and J-curve together suggest that the short-run effect of depreciation is unreliable (may even worsen CA), while the long-run effect is positive if ML holds.

## Swan Diagram — Internal and External Balance

The **Swan Diagram** (Trevor Swan, 1955) is a policy framework for simultaneously achieving **internal** and **external** equilibrium in an economy with a fixed exchange rate (or managed exchange rate).

### Policy Objectives

| Objective | Definition |
|---|---|
| **Internal balance (IB)** | Full employment + stable prices (no inflation or unemployment) |
| **External balance (EB)** | Current account equilibrium (sustainable BOP) |

### Policy Instruments

| Type | Examples |
|---|---|
| **Expenditure-changing** | Fiscal policy (G, T), monetary policy → affect level of domestic absorption $A = C + I + G$ |
| **Expenditure-switching** | Exchange rate changes (devaluation/revaluation) → shift spending between domestic and foreign goods |

### Diagram Structure

**Axes:** 
- Y-axis: Real exchange rate (higher = depreciation)
- X-axis: Domestic absorption $A = C + I + G$

**IB Schedule (Internal Balance):** Downward-sloping.
- Higher absorption → more inflation (overheating) → need real appreciation (lower $E$) to reduce net exports and cool demand → move down the IB curve.
- Left of IB: Unemployment (excess supply of domestic goods)
- Right of IB: Inflation (excess demand)

**EB Schedule (External Balance):** Upward-sloping.
- Higher absorption → more imports → CA deficit → need depreciation (higher $E$) to improve CA → move up the EB curve.
- Below EB: CA surplus
- Above EB: CA deficit

**The four zones** (IB and EB cross at the optimal point):

| Zone | Condition |
|---|---|
| Upper-left | Unemployment + CA surplus |
| Upper-right | Inflation + CA surplus |
| Lower-left | Unemployment + CA deficit |
| Lower-right | Inflation + CA deficit |

### Tinbergen's Instrument-Targets Rule

**Jan Tinbergen (1952):** To achieve $n$ independent policy targets, at least $n$ independent policy instruments are required.

- **Two targets** (internal + external balance) → **two instruments** needed
- Trying to achieve both with only one instrument (e.g., absorption alone, or exchange rate alone) will generally fail

**Application:** From any disequilibrium point in the Swan diagram:
1. Use **absorption** (fiscal/monetary) to move horizontally (toward IB)
2. Use **exchange rate** (devaluation/revaluation) to move vertically (toward EB)
3. Jointly adjust both to reach the intersection of IB and EB

### Greek Crisis Illustration

During the Greek sovereign debt crisis (2010–2015), Greece was in the **unemployment + deficit** zone (below both IB and EB): high unemployment (internal imbalance) and a large CA deficit (external imbalance).

**The constraint:** Greece was in the eurozone → could not devalue. The only available instrument was fiscal austerity (expenditure reduction). Austerity moved the economy toward EB (reduced imports by reducing income) and toward lower inflation, but at the cost of severe unemployment — moving along EB but not to the IB+EB intersection.

**Optimal policy** would have required **both** austerity **and** devaluation — but devaluation required exiting the eurozone. This illustrates the tension between monetary union membership and the ability to achieve internal+external balance simultaneously (connecting to [[Fixed_Exchange_Rates_and_Impossible_Trinity]]).
