---
course: JEB050
topic: International Fisher Effect, NEER, and REER
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_6/slides.pdf
tags: [JEB050, Fisher-effect, NEER, REER, nominal-exchange-rate, real-exchange-rate, convergence]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_6/slides.pdf]]
Related: [[UIP_and_CIP]], [[PPP_and_Big_Mac_Index]], [[Balassa_Samuelson_Effect]], [[Exchange_Rate_Types_and_Triangular_Arbitrage]]

# International Fisher Effect, NEER, and REER

## The International Fisher Effect (IFE)

The **International Fisher Effect** combines [[UIP_and_CIP|Uncovered Interest Parity]] with **relative PPP** to derive a relationship between nominal interest rate differentials and expected inflation differentials.

### Derivation

**Step 1 — UIP:**

$$R - R^* = \frac{E^e - E}{E} \quad \text{(expected depreciation)}$$

**Step 2 — Relative PPP (applied to expectations):**

$$\frac{E^e - E}{E} = \pi^e - \pi^{e*} \quad \text{(expected inflation differential)}$$

**Combining (1) and (2):**

$$\boxed{R - R^* = \pi^e - \pi^{e*}}$$

The nominal interest rate differential equals the expected inflation differential. This means that **real interest rates are equalised** across countries in equilibrium:

$$R - \pi^e = R^* - \pi^{e*} \quad \Leftrightarrow \quad r = r^*$$

### Counter-Intuitive Implication

The IFE implies a **negative relationship** between nominal interest rates and exchange rates: a country experiencing an **increase in expected inflation** will see:
1. Nominal interest rates rise (Fisher equation)
2. Currency **depreciate** (higher inflation → loss of competitiveness)

This is the opposite of the naïve intuition that "high interest rates attract capital → currency appreciates." Under IFE, high nominal rates simply reflect high expected inflation and the currency will still depreciate.

### Empirical Status

The IFE holds approximately over long horizons in countries with large inflation differentials. In the short run, deviations are large because PPP does not hold (see [[PPP_and_Big_Mac_Index]]).

## Nominal Effective Exchange Rate (NEER)

The **NEER** is a multilateral index measuring the value of a currency against a **trade-weighted basket** of partner currencies:

$$\boxed{NEER_t = 100 \times \prod_{i=1}^{n} \left(\frac{S_{it}}{S_{i0}}\right)^{w_i}}$$

where:
- $S_{it}$ = bilateral nominal exchange rate against partner $i$ at time $t$ (expressed so that an increase = appreciation)
- $S_{i0}$ = bilateral rate at base period
- $w_i$ = trade weight for partner $i$ ($\sum w_i = 1$)

**CNB NEER methodology (base 2020):**
- 13 currency areas
- Eurozone: 64% weight
- Poland: 8.5%
- China: 7.5%
- Two weight variants: total foreign trade vs. SITC 5–8 (manufactured goods only)

**Trend:** The CZK has experienced long-run nominal **appreciation** since 1993 (visible in CNB NEER index rising above 100 as of 2020 base). Post-2008 GFC: temporary depreciation; 2013–2021 CNB FX floor (cap at 27 CZK/EUR).

## Real Effective Exchange Rate (REER)

The **REER** adjusts the NEER for relative price levels, measuring **competitiveness**:

$$\boxed{REER_t = 100 \times \prod_{i=1}^{n} \left(\frac{S_{it}}{P_{it}^*}\right)^{w_i}}$$

A rise in REER = real appreciation = loss of competitiveness (domestic goods become relatively more expensive). In practice, REER is computed as:

$$REER_t = NEER_t \times \frac{P_t^*}{P_t}$$

**CPI-based vs. PPI-based REER:**
- **CPI-based REER** includes non-tradables → rises faster in converging countries (captures BS effect)
- **PPI-based REER** is closer to tradables prices → rises more slowly

For CEE countries converging to EU levels, **CPI-REER appreciates faster than PPI-REER**, because non-tradable prices rise more than tradable prices during convergence — the hallmark of the [[Balassa_Samuelson_Effect]].

## Czech REER Vis-à-Vis Germany (Illustrative)

| Period | Trend | Driver |
|---|---|---|
| 1993–2000 | Sharp real appreciation | Productivity catch-up (BS effect) + capital inflows |
| 2000–2008 | Continued appreciation | Continued convergence + CZK nominal appreciation |
| 2009 | Real depreciation | GFC + nominal CZK depreciation |
| 2011–2019 | Gradual appreciation | Recovery + structural productivity gains |

The **divergence** between CPI-REER and PPI-REER in the Czech data is a direct measure of the relative price increase of non-tradables — confirming the Balassa-Samuelson mechanism empirically.
