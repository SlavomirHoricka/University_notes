---
course: "JEB108"
topic: "Seminar Applications — Monopoly"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_7_Solutions.pdf"
tags: [JEB108, microeconomics, seminars, monopoly, MR, deadweight-loss]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_7_Solutions.pdf]]
Related: [[Monopoly]], [[Price_Discrimination]], [[Industry_Equilibrium]], [[Consumer_Surplus_and_Welfare_Measures]]

# Seminar Applications — Monopoly (Seminar 7)

Worked exercises on monopolist optimization ($MR = MC$), welfare analysis, and the deadweight loss triangle.

---

## Setting Up the Monopolist's Problem

For a monopolist facing **inverse demand** $p(y) = a - by$:

$$TR(y) = p(y) \cdot y = ay - by^2$$

$$MR(y) = \frac{dTR}{dy} = a - 2by$$

**Key property:** The MR curve has twice the slope of the demand curve (for linear demand). They share the same price-axis intercept $a$.

---

## Optimal Monopoly Output

**FOC:** $MR = MC$

With constant $MC = c$:

$$a - 2by^* = c \Rightarrow y^M = \frac{a - c}{2b}$$

$$p^M = a - b \cdot y^M = a - \frac{a-c}{2} = \frac{a + c}{2}$$

$$\pi^M = (p^M - c) y^M = \frac{(a-c)^2}{4b}$$

## Welfare Analysis

**Consumer surplus:** Area of triangle above $p^M$ below demand:

$$CS = \frac{1}{2}(a - p^M) y^M = \frac{1}{2} \cdot \frac{a-c}{2} \cdot \frac{a-c}{2b} = \frac{(a-c)^2}{8b}$$

**Deadweight loss:**

Under perfect competition: $p^{PC} = c$, $y^{PC} = (a-c)/b$.

$$DWL = \frac{1}{2}(p^M - c)(y^{PC} - y^M) = \frac{1}{2} \cdot \frac{a-c}{2} \cdot \frac{a-c}{2b} = \frac{(a-c)^2}{8b}$$

Note: $DWL = CS^M$ — under linear demand and constant MC, the DWL triangle equals the consumer surplus under monopoly.

**Welfare table (linear demand, constant MC):**

| Measure | Perfect Competition | Monopoly |
|---|---|---|
| Output | $(a-c)/b$ | $(a-c)/2b$ |
| Price | $c$ | $(a+c)/2$ |
| Consumer Surplus | $(a-c)^2/2b$ | $(a-c)^2/8b$ |
| Producer Surplus | $0$ | $(a-c)^2/4b$ |
| Total Surplus | $(a-c)^2/2b$ | $3(a-c)^2/8b$ |
| DWL | $0$ | $(a-c)^2/8b$ |

---

## Worked Exercise

**Setup:** Demand $D(p) = 20 - p$, so inverse demand $p = 20 - y$. $TC(y) = y^2 + 4$.

$$MR = 20 - 2y, \quad MC = 2y$$

**Optimum:** $20 - 2y = 2y \Rightarrow y^M = 5$, $p^M = 15$

$$\pi = (15)(5) - (25 + 4) = 75 - 29 = 46$$

$$CS = \frac{1}{2}(20 - 15)(5) = 12.5$$

$$DWL = \frac{1}{2}(15 - 10)(10 - 5) = 12.5 \quad \text{(at competitive output } y^{PC} = 10\text{, } p^{PC} = MC(10) = 20\text{)}$$

Wait — competitive output: $p = MC \Rightarrow 20 - y = 2y \Rightarrow y^{PC} = 20/3 \approx 6.67$, $p^{PC} = 40/3$.

$$DWL = \frac{1}{2}(p^M - p^{PC})(y^{PC} - y^M) = \frac{1}{2}\left(15 - \frac{40}{3}\right)\left(\frac{20}{3} - 5\right) = \frac{1}{2} \cdot \frac{5}{3} \cdot \frac{5}{3} = \frac{25}{18} \approx 1.39$$

---

## Natural Monopoly — Regulation Approaches

**Natural monopoly:** $LRATC$ decreases throughout the relevant demand range (IRS technology). One firm serves the market more cheaply than several.

**Regulatory options (see also [[Monopoly]]):**

| Policy | Price Rule | Efficiency | Profitability |
|---|---|---|---|
| Marginal-cost pricing | $p = MC$ | Efficient (no DWL) | Loss ($p < ATC$) — needs subsidy |
| Average-cost pricing | $p = ATC$ | Second-best | Zero profit |
| Two-part tariff | $p = MC$ + fixed fee $A$ | Efficient | Profit from fee |
| Rate-of-return cap | $\pi/K \leq \bar{r}$ | Distorted input mix | Zero excess profit |

---

## Lerner Index — Empirical Application

$$L = \frac{p - MC}{p} = \frac{1}{|\varepsilon_D|}$$

In practice, MC is unobservable; economists estimate $L$ using price-cost margins from accounting data (adjusted for opportunity costs) or instrument demand elasticities.

Higher Lerner index → greater market power → more welfare loss from monopoly → stronger antitrust case.
