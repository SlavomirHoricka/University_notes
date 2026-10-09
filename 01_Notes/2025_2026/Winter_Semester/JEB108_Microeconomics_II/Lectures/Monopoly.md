---
course: "JEB108"
topic: "Monopoly"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/7_monopoly.pdf"
tags: [JEB108, microeconomics, monopoly, market-power, deadweight-loss]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/7_monopoly.pdf]]
Related: [[Industry_Equilibrium]], [[Price_Discrimination]], [[Oligopoly_Models]], [[Consumer_Surplus_and_Welfare_Measures]], [[Firm_Supply_Curve]]

# Monopoly

## Definition

A **monopoly** is a market structure with a **single seller** that faces the entire market demand curve. Unlike a competitive firm (which takes price as given), a monopolist is a **price-maker** — it chooses either price or quantity, and the market demand determines the other.

**Barriers to entry:** Technological (IRS / natural monopoly), legal (patents, licences), strategic (predatory pricing), resource ownership.

---

## Profit Maximization

The monopolist maximizes profit:

$$\pi(y) = p(y) \cdot y - c(y)$$

where $p(y)$ is the **inverse demand function** (demand seen by the firm).

**FOC:**

$$\frac{d\pi}{dy} = p(y) + y \cdot p'(y) - MC(y) = MR(y) - MC(y) = 0$$

$$\boxed{MR(y^*) = MC(y^*)}$$

**Marginal Revenue:**

$$MR(y) = p(y) + y \cdot p'(y) = p\left(1 + \frac{y}{p} \cdot p'(y)\right) = p\left(1 - \frac{1}{|\varepsilon_D|}\right)$$

where $\varepsilon_D = -\frac{dD}{dp} \cdot \frac{p}{D}$ is the price elasticity of demand.

Since $p'(y) < 0$ (downward-sloping demand): $MR < p$ — the monopolist must lower price on all units to sell an additional unit.

---

## Monopoly Markup — Lerner Condition

From $MR = MC$:

$$p\left(1 - \frac{1}{|\varepsilon_D|}\right) = MC$$

$$\boxed{\frac{p - MC}{p} = \frac{1}{|\varepsilon_D|}}$$

The **Lerner index** (price-cost margin) equals the inverse of the elasticity of demand.

**Implications:**
- $|\varepsilon_D| = 1$ (unit elastic): $MC = 0$
- $|\varepsilon_D| > 1$ (elastic demand): $p > MC > 0$
- $|\varepsilon_D| < 1$ (inelastic demand): $MC < 0$ → impossible → monopolist always produces on **elastic portion** of demand.

---

## Inverse Elasticity Rule

For a monopolist facing linear inverse demand $p = a - by$:

$$MR = a - 2by$$

Optimal output: $MR = MC \Rightarrow a - 2by^* = MC$

$$y^* = \frac{a - MC}{2b}, \quad p^* = \frac{a + MC}{2} = \frac{a + c}{2}$$

(Assuming constant $MC = c$.)

Under perfect competition: $p^{PC} = MC = c$, $y^{PC} = (a-c)/b$.

**Comparison:**

| Outcome | Monopoly | Perfect Competition |
|---|---|---|
| Output | $(a-c)/2b$ | $(a-c)/b$ |
| Price | $(a+c)/2$ | $c$ |
| Profit | $(a-c)^2/4b$ | $0$ |

---

## Deadweight Loss of Monopoly

Monopoly restricts output below the competitive level and raises price above MC, creating a **deadweight loss (DWL)**:

$$DWL = \frac{1}{2}(p^M - MC)(y^{PC} - y^M)$$

This is the triangular area between the demand curve and MC curve, between $y^M$ and $y^{PC}$.

**Welfare decomposition:**
- Consumer surplus: falls by the DWL triangle + the rectangle transferred to producer.
- Producer surplus (profit): rises by the transferred rectangle, minus the DWL.
- Net social welfare: falls by the DWL.

---

## Natural Monopoly

A **natural monopoly** arises when the production technology exhibits **increasing returns to scale** (decreasing LRATC) over the relevant range of demand:

$$LRATC(y) \text{ decreasing} \Rightarrow \text{one firm can serve market more cheaply than two}$$

**Regulation of natural monopoly:**

| Regulation | Rule | Issue |
|---|---|---|
| Marginal-cost pricing | $p = MC$ | Firm makes losses (requires subsidy) |
| Average-cost pricing | $p = ATC$ | Zero profit; less DWL than monopoly |
| Rate-of-return regulation | Cap on profit rate | May distort input mix (Averch-Johnson effect) |
| Two-part tariff | Fixed fee + per-unit price at MC | Efficiency + allows cost recovery |

---

## Multiplant Monopoly

If a monopolist operates $k$ plants with cost functions $c_i(y_i)$, efficiency requires:

$$MC_1(y_1) = MC_2(y_2) = \cdots = MC_k(y_k) = MC_T(Y)$$

where $Y = \sum y_i$ is total output. The multiplant MC curve is derived by **horizontally summing** individual MC curves.

---

## Monopoly Power: Sources and Measurement

**Sources:**
- Control over a unique resource
- Economies of scale (natural monopoly)
- Government regulation / intellectual property

**Measurement — Lerner Index:**
$$L = \frac{p - MC}{p} = \frac{1}{|\varepsilon_D|} \in [0, 1]$$

$L = 0$: perfect competition; $L = 1$: extreme monopoly power ($MC = 0$).

**Herfindahl-Hirschman Index (HHI):**
$$HHI = \sum_{i=1}^n s_i^2$$
where $s_i$ is firm $i$'s market share. Used in antitrust analysis (EU, US). $HHI > 2500$ indicates high concentration.
