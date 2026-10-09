---
course: JEB050
topic: The DD-AA Model — Short-Run Exchange Rate and Output Determination
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_7/slides.pdf
tags: [JEB050, DD-AA, short-run-equilibrium, output, exchange-rate, asset-markets]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_7/slides.pdf]]
Related: [[UIP_and_CIP]], [[National_Income_Accounting_Open_Economy]], [[Policy_in_DD_AA]], [[Fixed_Exchange_Rates_and_Impossible_Trinity]]

# The DD-AA Model — Short-Run Exchange Rate and Output Determination

## Overview

The **DD-AA model** (Krugman, Obstfeld & Melitz, Chapter 17) provides a simultaneous short-run equilibrium for three markets:

1. **Output market** (goods and services) → **DD curve**
2. **Foreign exchange market** (UIP condition)  → jointly determine **AA curve**
3. **Money market** (LM condition)

The model is plotted in **(Y, E) space** — output on the x-axis, nominal exchange rate (domestic per foreign, so rise = depreciation) on the y-axis.

## The DD Curve

### Aggregate Demand

$$D = C(Y-T) + I + G + CA(EP^*/P,\; Y-T)$$

- $C(Y-T)$: consumption rising in disposable income (+)
- $I, G$: exogenous investment and government spending
- $CA(EP^*/P, Y-T)$: current account; rising in real exchange rate $(EP^*/P)$ and falling in domestic disposable income

Simplified:

$$\boxed{D = D(EP^*/P,\; Y-T,\; I,\; G)}$$

with partial derivatives: $(+,\; +,\; +,\; +)$ for $(EP^*/P,\; Y-T,\; I,\; G)$.

**Note on $CA$ and $Y$:** Higher $Y$ raises imports → $CA$ falls. But the direct consumption effect dominates: net effect of $\uparrow Y$ on $D$ is positive (MPC < 1, but MPC > 0).

### Output Market Equilibrium

$$Y = D(EP^*/P,\; Y-T,\; I,\; G)$$

### Derivation of the DD Curve

For fixed $T, I, G, P, P^*$: when $E$ rises (depreciation), $EP^*/P$ rises → $CA$ improves → $D$ rises → equilibrium $Y$ rises.

$$\boxed{\text{DD curve: upward-sloping in } (Y, E) \text{ space}}$$

Higher exchange rate (more depreciated) → higher output in goods market equilibrium.

### Shifts in the DD Curve (rightward)

| Shift factor | Direction | Mechanism |
|---|---|---|
| $\uparrow G$ | DD right | Higher government spending → higher aggregate demand at each $E$ |
| $\downarrow T$ | DD right | Lower taxes → higher disposable income → higher consumption |
| $\uparrow I$ | DD right | Higher investment → higher aggregate demand |
| $\downarrow P$ (or $\uparrow P^*$) | DD right | Lower relative domestic prices → improved competitiveness → $CA\uparrow$ |
| Demand shift to domestic goods | DD right | Consumers substitute away from imports |

Changes in $E$ cause movements **along** the DD curve; all other changes **shift** it.

## The AA Curve

### Asset Market Equilibrium

**Foreign exchange market — UIP:**

$$R = R^* + \frac{E^e - E}{E}$$

For given $R^*$ and $E^e$, a higher $R$ is associated with a lower $E$ (domestic currency appreciates when domestic interest rates are high).

**Money market — LM:**

$$\frac{M^s}{P} = L(R, Y)$$

where $L$ is money demand: decreasing in $R$ (opportunity cost) and increasing in $Y$ (transactions demand).

### Derivation of the AA Curve

For given $M^s, P, R^*, E^e$: when $Y$ rises:
1. Transactions demand for money $L\uparrow$
2. Excess money demand → $R\uparrow$
3. Higher domestic interest rate → capital inflow → $E\downarrow$ (appreciation)

$$\boxed{\text{AA curve: downward-sloping in } (Y, E) \text{ space}}$$

Higher output → lower exchange rate (appreciation) in asset market equilibrium.

### Shifts in the AA Curve

| Shift factor | Direction of shift | Mechanism |
|---|---|---|
| $\uparrow M^s$ | **AA up (depreciation)** | Excess money supply → $R\downarrow$ → $E\uparrow$ |
| $\uparrow P$ | **AA down (appreciation)** | Lower real money supply → $R\uparrow$ → $E\downarrow$ |
| Lower money demand | **AA up** | $R\downarrow$ → $E\uparrow$ |
| $\uparrow R^*$ | **AA up** | Foreign deposits more attractive → $E\uparrow$ |
| $\uparrow E^e$ (expected depreciation) | **AA up** | UIP: for given $R$, higher $E^e$ → higher $E$ today |

## Short-Run Equilibrium

**SR equilibrium** occurs at the **intersection of DD and AA**, where:
1. $Y = D(EP^*/P, Y-T, I, G)$ (goods market clears)
2. $R = R^* + (E^e - E)/E$ (FX market clears)
3. $M^s/P = L(R, Y)$ (money market clears)

### Adjustment Speed

- **Asset markets (AA) adjust instantly** (exchange rates and interest rates clear within seconds)
- **Output markets (DD) adjust slowly** (production plans change over weeks/months)

This asymmetry matters for dynamics: after a shock, the exchange rate jumps immediately to place the economy on the AA curve; output then adjusts gradually along the AA curve until DD is also satisfied.

**Graphical adjustment:** Starting from a disequilibrium point above AA — excess supply in money market → $R$ falls → $E$ rises → economy moves down along the AA direction; simultaneously, higher $E$ raises aggregate demand → $Y$ rises along DD → economy converges to the intersection.
