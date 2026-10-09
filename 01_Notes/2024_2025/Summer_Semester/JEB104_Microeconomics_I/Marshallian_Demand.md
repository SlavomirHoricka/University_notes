---
title: "Marshallian Demand"
course: JEB104
topic: Consumer Theory
tags: [Marshallian-demand, Walrasian-demand, Engel-curve, income-effect, price-effect, normal-good, Giffen-good, consumer-theory]
date_created: 2026-04-19
---

# Marshallian Demand

## Definition

The **Marshallian (Walrasian) demand function** $x_i^*(p, m)$ gives the quantity of good $i$ demanded by a utility-maximising consumer at prices $\mathbf{p} = (p_1, p_2)$ and income $m$:

$$x_i^*(p, m) = \underset{x_i \geq 0}{\arg\max} \; u(x_1, x_2) \quad \text{s.t.} \quad p_1 x_1 + p_2 x_2 = m$$

## Properties of Marshallian Demand

### 1. Homogeneity of Degree Zero
$$x_i^*(\lambda p, \lambda m) = x_i^*(p, m) \quad \forall \lambda > 0$$

Multiplying all prices and income by the same factor leaves the budget set unchanged, hence demand is unchanged. This reflects the absence of money illusion.

### 2. Walras's Law
At any $(p, m)$: $\sum_i p_i x_i^*(p, m) = m$.

The consumer spends all income (holds with equality when preferences are monotone).

### 3. Symmetry of Cross-Price Effects (via Slutsky)
The Slutsky matrix is symmetric: $\partial h_i / \partial p_j = \partial h_j / \partial p_i$ (see [[Slutsky_Equation]]).

## Comparative Statics: Income

**Income offer curve (income expansion path):** The locus of optimal bundles as $m$ varies with prices fixed. Connects the optima on indifference curves tangent to parallel budget lines.

**Engel curve:** The graph of $x_i^*(p, m)$ as a function of $m$ (holding $p$ fixed).

### Normal vs Inferior Goods
$$\frac{\partial x_i^*}{\partial m} > 0 \implies \text{good } i \text{ is normal (Engel curve upward-sloping)}$$
$$\frac{\partial x_i^*}{\partial m} < 0 \implies \text{good } i \text{ is inferior (Engel curve downward-sloping)}$$

**Luxury goods:** $\epsilon_{x_i, m} > 1$ (income elasticity exceeds 1; budget share rises with income).
**Necessities:** $0 < \epsilon_{x_i, m} < 1$ (income elasticity between 0 and 1).

By Walras's Law, both goods cannot be inferior simultaneously (expenditure-weighted income elasticities average to 1).

## Comparative Statics: Own Price

**Price offer curve (price expansion path):** The locus of optimal bundles as $p_1$ varies with $p_2$ and $m$ fixed.

### Ordinary vs Giffen Goods
$$\frac{\partial x_i^*}{\partial p_i} < 0 \implies \text{ordinary good (law of demand holds)}$$
$$\frac{\partial x_i^*}{\partial p_i} > 0 \implies \text{Giffen good (demand rises with own price)}$$

**Giffen goods** require: (i) the good is strongly inferior, (ii) a large income effect that outweighs the substitution effect. Giffen behaviour requires $|IE| > |SE|$, with $IE$ negative (income-reducing price increase reduces demand less than the negative income effect amplifies it).

## Cross-Price Effects: Substitutes and Complements

$$\frac{\partial x_i^*}{\partial p_j} > 0 \implies \text{goods } i \text{ and } j \text{ are (gross) substitutes}$$
$$\frac{\partial x_i^*}{\partial p_j} < 0 \implies \text{goods } i \text{ and } j \text{ are (gross) complements}$$

Note: Gross substitutability is not symmetric in general ($\partial x_i^*/\partial p_j \neq \partial x_j^*/\partial p_i$). Net (Hicksian) substitutability is symmetric.

## Elasticities

**Own-price elasticity:** $\epsilon_{ii} = \frac{\partial x_i^*}{\partial p_i} \cdot \frac{p_i}{x_i^*}$

**Cross-price elasticity:** $\epsilon_{ij} = \frac{\partial x_i^*}{\partial p_j} \cdot \frac{p_j}{x_i^*}$

**Income elasticity:** $\eta_i = \frac{\partial x_i^*}{\partial m} \cdot \frac{m}{x_i^*}$

**Cournot aggregation** (from homogeneity): $\sum_j \epsilon_{ij} + \eta_i = 0$

**Engel aggregation** (from Walras's Law): $\sum_i s_i \eta_i = 1$ where $s_i = p_i x_i^*/m$ is the budget share.

## Demand Functions for Standard Utility Functions

### Cobb-Douglas: $u = x_1^\alpha x_2^{1-\alpha}$

$$x_1^* = \frac{\alpha m}{p_1}, \quad x_2^* = \frac{(1-\alpha) m}{p_2}$$

Constant expenditure shares: $p_1 x_1^* / m = \alpha$, $p_2 x_2^* / m = 1 - \alpha$.

### Perfect Substitutes: $u = ax_1 + bx_2$

$$x_1^* = \begin{cases} m/p_1 & \text{if } a/p_1 > b/p_2 \\ [0, m/p_1] & \text{if } a/p_1 = b/p_2 \\ 0 & \text{if } a/p_1 < b/p_2 \end{cases}$$

### Perfect Complements: $u = \min\{x_1, x_2\}$

$$x_1^* = x_2^* = \frac{m}{p_1 + p_2}$$

### Quasilinear: $u = v(x_1) + x_2$, $v'' < 0$

FOC: $v'(x_1^*) = p_1/p_2$. The demand for $x_1$ is determined solely by the price ratio — no income effect on $x_1$ (as long as $m$ is large enough for an interior solution).

## Related Concepts

- [[Utility_Maximization_and_Optimal_Choice]] — the problem whose solution yields Marshallian demand
- [[Income_and_Substitution_Effects]] — decomposes price responses into SE and IE
- [[Slutsky_Equation]] — links Marshallian and Hicksian demand
- [[Expenditure_Minimization_and_Hicksian_Demand]] — the dual demand concept
- [[Indirect_Utility_Function_and_Roys_Identity]] — Roy's identity recovers Marshallian demand from the indirect utility function
- [[Revealed_Preferences]] — Marshallian choices reveal preferences without assuming a utility function
