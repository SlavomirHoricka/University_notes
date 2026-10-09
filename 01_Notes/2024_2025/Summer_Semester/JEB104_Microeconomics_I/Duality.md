---
title: "Duality in Consumer Theory"
course: JEB104
topic: Consumer Theory
tags: [duality, UMP, EMP, expenditure-function, indirect-utility, Hicksian-demand, Marshallian-demand, consumer-theory]
date_created: 2026-04-19
---

# Duality in Consumer Theory

## Overview

**Duality** refers to the intimate mathematical relationship between two equivalent formulations of the consumer's optimisation:

1. **Utility Maximization Problem (UMP):** Maximise $u(x)$ subject to $p \cdot x \leq m$.
2. **Expenditure Minimization Problem (EMP):** Minimise $p \cdot x$ subject to $u(x) \geq \bar{u}$.

The two problems are duals in the following sense: solving one automatically provides the solution to the other at the appropriate parameter values.

## Fundamental Duality Identities

Let $v(p, m)$ be the indirect utility function and $e(p, \bar{u})$ be the expenditure function. The duality relationships are:

$$v(p, e(p, \bar{u})) = \bar{u} \tag{D1}$$

$$e(p, v(p, m)) = m \tag{D2}$$

**Interpretation of (D1):** The maximum utility achievable when income is just enough to reach $\bar{u}$ is exactly $\bar{u}$.

**Interpretation of (D2):** The minimum expenditure needed to reach the maximum utility achievable with income $m$ is exactly $m$.

## Demand Correspondences

The duality between $v$ and $e$ induces a duality between the two demand functions:

$$x_i^*(p, e(p, \bar{u})) = h_i(p, \bar{u}) \tag{D3}$$

$$h_i(p, v(p, m)) = x_i^*(p, m) \tag{D4}$$

**Interpretation:** Marshallian demand evaluated at compensated income equals Hicksian demand; Hicksian demand evaluated at the achieved utility level equals Marshallian demand.

## Derivation of the Slutsky Equation from Duality

Differentiate identity (D3) with respect to $p_j$:

$$\frac{\partial x_i^*}{\partial p_j}\bigg|_m + \frac{\partial x_i^*}{\partial m} \cdot \frac{\partial e}{\partial p_j} = \frac{\partial h_i}{\partial p_j}$$

By Shephard's Lemma, $\partial e / \partial p_j = h_j(p, \bar{u}) = x_j^*(p, m)$ at the optimum.

Rearranging:

$$\frac{\partial h_i}{\partial p_j} = \frac{\partial x_i^*}{\partial p_j} + x_j^* \frac{\partial x_i^*}{\partial m}$$

Or equivalently, the **Slutsky equation**:

$$\frac{\partial x_i^*}{\partial p_j} = \frac{\partial h_i}{\partial p_j} - x_j^* \frac{\partial x_i^*}{\partial m}$$

See [[Slutsky_Equation]] for complete treatment.

## Roy's Identity from Duality

Differentiate (D2) with respect to $p_i$:

$$\frac{\partial e}{\partial p_i} + \frac{\partial e}{\partial \bar{u}} \cdot \frac{\partial v}{\partial p_i} = 0$$

Since $\partial e / \partial p_i = h_i = x_i^*$ (by Shephard's Lemma and D4), and $\partial e / \partial \bar{u} = 1/(\partial v/\partial m)$ (from D2 differentiated w.r.t. $m$):

$$x_i^* = -\frac{\partial v/\partial p_i}{\partial v/\partial m}$$

This is **Roy's Identity**, also derived in [[Indirect_Utility_Function_and_Roys_Identity]].

## Structure of Duality: A Roadmap

$$\boxed{\text{UMP}} \xrightarrow{\text{solve}} x^*(p,m) \xrightarrow{v = u(x^*)} v(p,m)$$

$$\boxed{\text{EMP}} \xrightarrow{\text{solve}} h(p,\bar{u}) \xrightarrow{e = p \cdot h} e(p,\bar{u})$$

**Connections:**
- $v(p, m) \leftrightarrow e(p, \bar{u})$: related by $v(p, e(p,\bar{u})) = \bar{u}$
- $x^*(p, m) \leftrightarrow h(p, \bar{u})$: related by (D3) and (D4)
- $\partial v/\partial p_i \leftrightarrow h_i$: Roy's Identity
- $\partial e/\partial p_i = h_i$: Shephard's Lemma
- $\partial v/\partial m = \lambda$: marginal utility of income
- $\partial e/\partial \bar{u} = \mu$: marginal cost of utility

## Cobb-Douglas Illustration

For $u = x_1^\alpha x_2^{1-\alpha}$ (as in Nechyba, Chapter 10B):

**Marshallian demand:**
$$x_1^* = \frac{\alpha m}{p_1}, \quad x_2^* = \frac{(1-\alpha)m}{p_2}$$

**Indirect utility:**
$$v(p, m) = \frac{m \cdot \alpha^\alpha (1-\alpha)^{1-\alpha}}{p_1^\alpha p_2^{1-\alpha}}$$

**Expenditure function:**
$$e(p, \bar{u}) = \frac{\bar{u} \cdot p_1^\alpha p_2^{1-\alpha}}{\alpha^\alpha (1-\alpha)^{1-\alpha}}$$

**Hicksian demand:**
$$h_1(p, \bar{u}) = \bar{u} \left(\frac{\alpha p_2}{(1-\alpha)p_1}\right)^{1-\alpha}, \quad h_2(p, \bar{u}) = \bar{u}\left(\frac{(1-\alpha)p_1}{\alpha p_2}\right)^\alpha$$

**Verify (D3):** $x_1^*(p, e(p,\bar{u})) = \alpha e(p,\bar{u})/p_1 = h_1(p,\bar{u})$ ✓

**Verify Shephard:** $\partial e/\partial p_1 = \alpha e/p_1 = h_1$ ✓

## Slutsky Matrix Properties from Duality

Since $S_{ij} = \partial h_i/\partial p_j = \partial^2 e/\partial p_j \partial p_i$:

- **Symmetry:** $S_{ij} = S_{ji}$ (symmetry of mixed partials)
- **NSD:** $\mathbf{v}^T S \mathbf{v} \leq 0$ for all $\mathbf{v}$ (concavity of $e$ in $p$)
- **$S_{ii} \leq 0$:** own-price Hicksian effects are non-positive
- **$Sp = 0$:** by homogeneity of degree zero of Hicksian demand in prices

## Hicksian vs Marshallian Slopes

For **normal goods** ($\partial x_i^*/\partial m > 0$):

$$\left|\frac{\partial x_i^*}{\partial p_i}\right| > \left|\frac{\partial h_i}{\partial p_i}\right|$$

The Marshallian demand is more price-elastic than the Hicksian demand (income effect reinforces substitution effect).

For **inferior goods** ($\partial x_i^*/\partial m < 0$):

$$\left|\frac{\partial x_i^*}{\partial p_i}\right| < \left|\frac{\partial h_i}{\partial p_i}\right|$$

The Marshallian demand is less price-elastic than Hicksian demand.

## Related Concepts

- [[Expenditure_Minimization_and_Hicksian_Demand]] — the EMP and its value function $e(p,\bar{u})$
- [[Indirect_Utility_Function_and_Roys_Identity]] — the UMP value function $v(p,m)$ and Roy's Identity
- [[Slutsky_Equation]] — derived from the duality identity (D3)
- [[Income_and_Substitution_Effects]] — the economic content of the duality
- [[Consumer_Surplus_and_Welfare_Measures]] — CV and EV use the duality between $v$ and $e$
