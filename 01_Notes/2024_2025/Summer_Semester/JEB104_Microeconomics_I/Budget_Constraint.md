---
title: "Budget Constraint"
course: JEB104
topic: Consumer Theory
tags: [budget-constraint, budget-set, numeraire, consumer-theory]
date_created: 2026-04-19
---

# Budget Constraint

## Definition

The **budget constraint** describes the set of consumption bundles $(x_1, x_2)$ that a consumer can afford given market prices $(p_1, p_2)$ and income $m$. The **budget set** is:

$$B(p_1, p_2, m) = \{(x_1, x_2) \in \mathbb{R}^2_+ : p_1 x_1 + p_2 x_2 \leq m\}$$

The boundary of the budget set is the **budget line**:

$$p_1 x_1 + p_2 x_2 = m$$

## Slope of the Budget Line

Rewriting the budget line in slope-intercept form:

$$x_2 = \frac{m}{p_2} - \frac{p_1}{p_2} x_1$$

The slope is $-p_1/p_2$, representing the **opportunity cost** of good 1 in terms of good 2 — how many units of good 2 must be given up to obtain one additional unit of good 1.

The intercepts are $m/p_1$ (horizontal) and $m/p_2$ (vertical), representing maximal affordable quantities of each good.

## Shifts and Rotations

| Change | Effect on Budget Line |
|--------|-----------------------|
| Income $m$ increases | Parallel outward shift; slope unchanged |
| $p_1$ increases | Clockwise rotation about vertical intercept; horizontal intercept falls to $m/p_1'$ |
| $p_2$ increases | Counter-clockwise rotation about horizontal intercept; vertical intercept falls |
| Both prices double | Budget line unchanged (equivalent to halving income) |

**Formal:** The budget set is homogeneous of degree zero in $(p_1, p_2, m)$ — multiplying all prices and income by $\lambda > 0$ leaves the budget set unchanged:

$$B(\lambda p_1, \lambda p_2, \lambda m) = B(p_1, p_2, m)$$

## Numeraire

A **numeraire** is a good whose price is normalized to 1. Setting $p_2 = 1$ expresses all prices in units of good 2. The budget constraint becomes:

$$p_1 x_1 + x_2 \leq m$$

where $p_1$ is now the relative price of good 1. This simplification is valid because only relative prices matter for the budget set (homogeneity of degree zero).

## Taxes and Subsidies

**Quantity tax:** A tax of $t$ per unit on good 1 raises its effective price to $p_1 + t$. The budget line rotates inward.

**Ad valorem tax:** A proportional tax at rate $\tau$ raises the effective price to $(1+\tau)p_1$.

**Quantity subsidy:** A subsidy of $s$ per unit reduces the effective price to $p_1 - s$. The budget line rotates outward.

**Lump-sum tax:** Reduces income $m$ directly, causing a parallel inward shift.

**In-kind transfers:** Provide a specific quantity $\bar{x}_1$ of good 1 for free, creating a kinked budget line. If $\bar{x}_1 \leq x_1^*$ (optimal without transfer), the constraint is non-binding and the kink does not affect choice.

**Rationing:** An upper bound $\bar{x}_1$ on consumption truncates the budget set for $x_1 > \bar{x}_1$, creating a vertical segment at $x_1 = \bar{x}_1$.

## Generalisation to $n$ Goods

With $n$ goods at prices $\mathbf{p} = (p_1, \ldots, p_n)$ and income $m$:

$$\sum_{i=1}^n p_i x_i \leq m$$

## Related Concepts

- [[Preferences_and_Indifference_Curves]] — preferences determine which bundle within $B$ is chosen
- [[Utility_Maximization_and_Optimal_Choice]] — the consumer's problem is to maximise utility subject to the budget constraint
- [[Marshallian_Demand]] — Marshallian demand functions are derived from this constrained optimisation
- [[Endowment_Economy_and_Buying_Selling]] — when income derives from an endowment, the budget constraint has a different structure
- [[Labor_Supply]] — the labor-leisure budget constraint is a special case
- [[Intertemporal_Choice]] — the intertemporal budget constraint maps present vs future consumption
