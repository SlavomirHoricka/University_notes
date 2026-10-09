---
course: JEB050
topic: Balassa-Samuelson Effect and EU Nominal/Real Convergence
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_6/slides.pdf
tags: [JEB050, Balassa-Samuelson, real-convergence, non-tradables, REER, EU-enlargement]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_6/slides.pdf]]
Related: [[PPP_and_Big_Mac_Index]], [[International_Fisher_Effect_and_REER]], [[Marshall_Lerner_Condition_and_Swan_Diagram]]

# Balassa-Samuelson Effect and EU Nominal/Real Convergence

## Historical Attribution

The **Balassa-Samuelson (BS) effect** was independently formalised by Béla Balassa (1964, *Journal of Political Economy*) and Paul Samuelson (1964, *Review of Economics and Statistics*). It is also known as the Harrod-Balassa-Samuelson or Ricardo-Viner-Harrod-Balassa-Samuelson-Penn-Bhagwati (RVHBSPB) effect, reflecting multiple independent discoveries.

**Observation:** Richer countries have systematically higher price levels (measured in a common currency). PPP substantially **underestimates** the living standards of poor countries and overestimates those of rich countries.

## The Two-Sector Model

### Assumptions

- Two sectors: **tradables (T)** and **non-tradables (N)**
- PPP holds for tradables: $P_d^T = E \cdot P_f^T$
- Wages are equalised across sectors within each country: $w_d^T = w_d^N$
- Wages are determined by productivity: $w_d^T = a_d^T \cdot P_d^T$ (competitive labour market)

### Static Version — Price Level Differences

With these assumptions:

$$w_d^T = a_d^T \cdot E \cdot P_f^T$$

Since wages equalise: $w_d^N = w_d^T$. Non-tradable prices:

$$P_d^N = \frac{w_d^N}{a_d^N} = \frac{w_d^T}{a_d^N} = \frac{a_d^T \cdot E \cdot P_f^T}{a_d^N}$$

Compare with the foreign country (where $a_f^T > a_d^T$, i.e., more productive in tradables):

$$P_f^N = \frac{a_f^T \cdot P_f^T}{a_f^N}$$

Since $a_d^T < a_f^T$ (less productive), domestic wages are lower → domestic non-tradable prices are lower → overall domestic price level $P_d < P_f$ (in common currency).

**Conclusion:** Poorer countries (with lower productivity in tradables) have lower overall price levels because their non-tradable prices are lower, even though tradable prices are equalised by arbitrage.

### Dynamic Version — Convergence and Inflation

Now consider a **catching-up** scenario where $a_d^T$ rises toward $a_f^T$ (productivity convergence in tradables), while the nominal exchange rate $E$ is held constant (e.g., in ERM II or euro area):

1. $a_d^T \uparrow$ → $w_d^T \uparrow$ (wages in tradables rise)
2. Wage equalisation: $w_d^N \uparrow$
3. $P_d^N = w_d^N / a_d^N \uparrow$ (non-tradable prices rise, since $a_d^N$ is assumed constant or grows slower)
4. Overall price level $P_d \uparrow$ → **inflation**
5. REER appreciates (domestic goods more expensive in common currency)

**Under a floating exchange rate:** The nominal rate can appreciate, partly offsetting the non-tradable inflation. In practice: combination of nominal appreciation and non-tradable inflation.

## Bhagwati-Kravis-Lipsey Variant

An alternative mechanism based on **capital-labour ratios** (Bhagwati 1984):

- Poor countries have lower $K/L$ → lower $MPL$ → lower wages
- Non-tradables (services) are **labour-intensive**
- → Cheaper services → lower overall price level in poor countries

This produces the same empirical prediction as BS but via a different mechanism.

## Empirical Evidence

### Czechia vs. Austria — ICP 2021 Price Level Indices (Austria = 100)

| Category | Czech Index |
|---|---|
| Alcoholic beverages | ~120 |
| Clothing & footwear | ~90 |
| Restaurants & hotels | **~55** |
| Education | **~43** |
| Health | **~33** |

Tradables (alcoholic beverages, clothing) approach Austrian prices; non-tradables (restaurants, education, health) are dramatically cheaper — confirming the BS pattern.

### CEE Country Regression (EU price levels vs. GDP per capita, 2024)

Eurostat data: $\text{Price level} = 16.5 + 0.83 \times \text{GDP per capita (PPS)}$, $R^2 = 0.69$.

Czech Republic in 2024: GDP per capita ~92% of EU27; price level ~88% of EU average — broadly on the regression line.

### Magnitude Estimates

| Study | Country | BS inflation differential (pp/year) |
|---|---|---|
| Egert (2002) | Czech Republic, Slovakia | ~0 |
| Egert (2002) | Hungary, Poland | ≤ 3.5 pp |
| Sinn & Reutter (2001) | Czech Republic | 2.88 pp |
| Sinn & Reutter (2001) | Hungary | 6.86 pp |

## Policy Implications — Maastricht Criteria Tension

The **inflation convergence criterion** for euro adoption: a candidate country's HICP inflation must not exceed 1.5 percentage points above the average of the three best-performing EU member states.

**Problem:** If a CEE country has a BS-induced structural inflation of, say, 2–3 pp above the eurozone average, it cannot satisfy the inflation criterion without:
- Nominal appreciation of its currency (which may conflict with the exchange rate criterion), or
- Deliberate economic slowdown (which is costly)

**Key nuance:** BS-induced inflation does **not** indicate a loss of competitiveness — productivity in tradables is growing faster than prices in tradables. The standard inflation criterion may thus be **inappropriate** for rapidly converging economies.

**Historical case — Ireland post-euro entry:** BS effect contributed to high inflation in Ireland after 1999; this reduced real interest rates and contributed to the credit boom.

## References

- Balassa, B. (1964). The purchasing-power parity doctrine: A reappraisal. *Journal of Political Economy*, 72(6), 584–596.
- Samuelson, P. A. (1964). Theoretical notes on trade problems. *Review of Economics and Statistics*, 46(2), 145–154.
- Rogoff, K. (1996). The purchasing power parity puzzle. *Journal of Economic Literature*, 34(2), 647–668.
- Bordo, M. D. et al. (2017). Real exchange rates and fundamentals: A cross-country perspective. *Journal of International Money and Finance*, 75, 69–92.
- Egert, B. (2002). Estimating the impact of the Balassa-Samuelson effect on inflation and the real exchange rate. *Economic Systems*, 26(1), 1–16.
