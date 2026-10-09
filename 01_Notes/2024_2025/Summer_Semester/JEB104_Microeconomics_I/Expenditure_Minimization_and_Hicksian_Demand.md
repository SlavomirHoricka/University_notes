---
title: "Expenditure Minimization and Hicksian Demand"
course: JEB104
topic: Consumer Theory
tags: [expenditure-minimization, Hicksian-demand, compensated-demand, expenditure-function, Shephard-lemma, consumer-theory]
date_created: 2026-04-19
---

# Expenditure Minimization and Hicksian Demand

## The Expenditure Minimization Problem (EMP)

The **dual** to the utility maximization problem (UMP) is:

$$\min_{x_1, x_2 \geq 0} \; p_1 x_1 + p_2 x_2 \quad \text{subject to} \quad u(x_1, x_2) \geq \bar{u}$$

The consumer minimizes expenditure while achieving at least utility level $\bar{u}$. The solution is the **Hicksian (compensated) demand**:

$$h_i(p, \bar{u}) = \underset{x}{\arg\min} \; p \cdot x \quad \text{s.t.} \quad u(x) \geq \bar{u}$$

## Hicksian Demand

The Hicksian demand $h_i(p, \bar{u})$ holds utility constant and varies with prices. It isolates the pure **substitution effect** — how demand changes in response to price changes with utility held fixed.

**Contrast with Marshallian demand:** $x_i^*(p, m)$ holds income constant; $h_i(p, \bar{u})$ holds utility constant. At the optimum:

$$h_i(p, v(p, m)) = x_i^*(p, m) \quad \text{and} \quad x_i^*(p, e(p, \bar{u})) = h_i(p, \bar{u})$$

## The Expenditure Function

The **expenditure function** is the value function of the EMP:

$$e(p, \bar{u}) = \min_{x} \{p \cdot x : u(x) \geq \bar{u}\} = p \cdot h(p, \bar{u})$$

### Properties of $e(p, \bar{u})$

**P1 — Homogeneous of degree 1 in prices:**
$$e(\lambda p, \bar{u}) = \lambda \, e(p, \bar{u}) \quad \forall \lambda > 0$$
Doubling all prices doubles the minimum expenditure required.

**P2 — Non-decreasing in each $p_i$:**
$$\frac{\partial e}{\partial p_i} \geq 0$$
Higher prices cannot reduce the cost of achieving $\bar{u}$.

**P3 — Concave in prices:**
$$e(\lambda p + (1-\lambda)p', \bar{u}) \geq \lambda \, e(p, \bar{u}) + (1-\lambda) \, e(p', \bar{u})$$

**Intuition:** When prices change from $p$ to $p'$, the consumer can re-optimise. At the average price vector $\bar{p} = \lambda p + (1-\lambda)p'$, the consumer re-optimises and does weakly better than just paying the average of the two optimal costs. Concavity follows.

**P4 — Increasing in $\bar{u}$:**
$$\frac{\partial e}{\partial \bar{u}} > 0$$
Achieving a higher utility level costs more.

**P5 — Continuous in $(p, \bar{u})$.

## Shephard's Lemma

The key result linking the expenditure function to Hicksian demand:

$$h_i(p, \bar{u}) = \frac{\partial e(p, \bar{u})}{\partial p_i}$$

### Derivation (Envelope Theorem)

$$e(p, \bar{u}) = p \cdot h(p, \bar{u})$$

Differentiating with respect to $p_i$:

$$\frac{\partial e}{\partial p_i} = h_i + \sum_j p_j \frac{\partial h_j}{\partial p_i}$$

At the optimum, the EMP's first-order conditions require $p_j = \mu \frac{\partial u}{\partial x_j}$ for all $j$, so $\sum_j p_j \frac{\partial h_j}{\partial p_i} = \mu \sum_j \frac{\partial u}{\partial x_j} \frac{\partial h_j}{\partial p_i} = 0$ (since $u(h) = \bar{u}$ implies $\sum_j u_j \partial h_j/\partial p_i = 0$). Therefore:

$$\frac{\partial e}{\partial p_i} = h_i(p, \bar{u})$$

### Implication for Substitution Effects

By symmetry of second-order partial derivatives of $e$:

$$\frac{\partial h_i}{\partial p_j} = \frac{\partial^2 e}{\partial p_j \partial p_i} = \frac{\partial^2 e}{\partial p_i \partial p_j} = \frac{\partial h_j}{\partial p_i}$$

The Slutsky matrix $S_{ij} = \partial h_i / \partial p_j$ is **symmetric**.

Concavity of $e$ implies the matrix of second derivatives $\partial^2 e / \partial p_i \partial p_j$ is negative semi-definite. Hence the **Slutsky matrix is negative semi-definite** (NSD):

$$v^T S v \leq 0 \quad \forall v \in \mathbb{R}^n$$

In particular, $S_{ii} = \partial h_i / \partial p_i \leq 0$ (own Hicksian effects are non-positive).

## Hicksian Demand for Standard Utility Functions

### Cobb-Douglas: $u = x_1^\alpha x_2^{1-\alpha}$

Solve the EMP: $\mathcal{L} = p_1 x_1 + p_2 x_2 - \mu(x_1^\alpha x_2^{1-\alpha} - \bar{u})$

FOCs: $p_1 = \mu \alpha x_1^{\alpha-1} x_2^{1-\alpha}$ and $p_2 = \mu(1-\alpha)x_1^\alpha x_2^{-\alpha}$.

Dividing: $p_1/p_2 = \frac{\alpha x_2}{(1-\alpha)x_1}$, so $x_2 = \frac{(1-\alpha)p_1}{\alpha p_2} x_1$.

Substituting into the constraint:

$$h_1(p, \bar{u}) = \bar{u} \left(\frac{\alpha p_2}{(1-\alpha) p_1}\right)^{1-\alpha}, \quad h_2(p, \bar{u}) = \bar{u} \left(\frac{(1-\alpha) p_1}{\alpha p_2}\right)^{\alpha}$$

Expenditure function:

$$e(p, \bar{u}) = \frac{\bar{u} \, p_1^\alpha \, p_2^{1-\alpha}}{\alpha^\alpha (1-\alpha)^{1-\alpha}}$$

### Perfect Complements: $u = \min\{x_1, x_2\}$

At optimum $x_1 = x_2 = \bar{u}$: $h_1 = h_2 = \bar{u}$, $e = (p_1 + p_2)\bar{u}$.

### Perfect Substitutes: $u = x_1 + x_2$

$$h_i(p, \bar{u}) = \begin{cases} \bar{u} & \text{if } p_i < p_j \\ [0, \bar{u}] & \text{if } p_i = p_j \\ 0 & \text{if } p_i > p_j \end{cases}$$

## Related Concepts

- [[Duality]] — the EMP is the dual of the UMP; $e$ and $v$ are duals of each other
- [[Income_and_Substitution_Effects]] — Hicksian demand defines the substitution effect
- [[Slutsky_Equation]] — derived from differentiating the duality identity $x_i(p, e(p,u)) = h_i(p,u)$
- [[Indirect_Utility_Function_and_Roys_Identity]] — $v(p, e(p,u)) = u$ and $e(p, v(p,m)) = m$
- [[Consumer_Surplus_and_Welfare_Measures]] — CV and EV are areas under Hicksian demand curves
