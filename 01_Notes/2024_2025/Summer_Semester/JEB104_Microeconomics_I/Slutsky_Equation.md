---
course: JEB104
topic: Slutsky Decomposition
source: 00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_11_SlutskyDecomposition_Students.pdf
tags: [JEB104, microeconomics, Slutsky, substitution-effect, income-effect, Slutsky-matrix, consumer-theory]
created: 2026-04-19
---

Parent: [[JEB104_Microeconomics_I_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_11_SlutskyDecomposition_Students.pdf]]
Related: [[Income_and_Substitution_Effects]], [[Marshallian_Demand]], [[Expenditure_Minimization_and_Hicksian_Demand]], [[Duality]], [[Indirect_Utility_Function_and_Roys_Identity]]

# The Slutsky Equation

## Overview

The **Slutsky equation** (Slutsky 1915; independently Hicks & Allen 1934) decomposes the total price effect on Marshallian (uncompensated) demand into:

1. **Substitution effect (SE):** movement along the indifference curve — the compensated (Hicksian) price effect.
2. **Income effect (IE):** the change in demand due to the implied change in real purchasing power.

## Derivation

### Setup

Let $x_i^*(p, m)$ be Marshallian demand and $h_i(p, \bar{u})$ be Hicksian demand. The duality identity states:

$$h_i(p, \bar{u}) = x_i^*(p,\ e(p, \bar{u})) \tag{1}$$

where $e(p, \bar{u})$ is the expenditure function and $\bar{u} = v(p, m)$ is the achieved utility level.

### Step 1 — Differentiate (1) w.r.t. $p_j$

$$\frac{\partial h_i}{\partial p_j} = \frac{\partial x_i^*}{\partial p_j}\bigg|_m + \frac{\partial x_i^*}{\partial m} \cdot \frac{\partial e}{\partial p_j} \tag{2}$$

### Step 2 — Apply Shephard's Lemma

By Shephard's Lemma: $\displaystyle\frac{\partial e(p, \bar{u})}{\partial p_j} = h_j(p, \bar{u}) = x_j^*(p, m)$ at the optimum.

### Step 3 — Rearrange

Substituting into (2):

$$\frac{\partial h_i}{\partial p_j} = \frac{\partial x_i^*}{\partial p_j} + x_j^* \frac{\partial x_i^*}{\partial m}$$

Solving for the Marshallian price effect:

$$\boxed{\frac{\partial x_i^*}{\partial p_j} = \underbrace{\frac{\partial h_i}{\partial p_j}}_{\text{SE}} - \underbrace{x_j^* \frac{\partial x_i^*}{\partial m}}_{\text{IE}}}$$

This is the **Slutsky equation**.

## Interpretation

| Term | Name | Sign (own-price, $i = j$) | Interpretation |
|------|------|--------------------------|----------------|
| $\partial x_i^*/\partial p_i$ | Total price effect | Ambiguous (neg. for normal goods) | How Marshallian demand changes with $p_i$ |
| $\partial h_i/\partial p_i$ | Substitution effect | $\leq 0$ always | Pure relative price change; compensated demand moves opposite price |
| $-x_i^* \partial x_i^*/\partial m$ | Income effect | $\leq 0$ for normal goods | Effective income loss when $p_i$ rises |

**Law of demand for normal goods:** Both SE and IE are negative (own-price), so $\partial x_i^*/\partial p_i < 0$.

**Giffen goods:** IE is positive and dominates SE: $\partial x_i^*/\partial p_i > 0$.

## Slutsky Matrix

Define the **Slutsky matrix** $S(p, m)$ with entries:

$$S_{ij}(p, m) = \frac{\partial h_i}{\partial p_j}(p, v(p,m)) = \frac{\partial x_i^*}{\partial p_j} + x_j^* \frac{\partial x_i^*}{\partial m}$$

**Properties of $S$:**

1. **Symmetry:** $S_{ij} = S_{ji}$ — because $S_{ij} = \partial^2 e / \partial p_j \partial p_i$ and mixed partials commute.
2. **Negative semi-definite (NSD):** $v^T S v \leq 0$ for all $v \in \mathbb{R}^n$ — because $e(p, \bar{u})$ is concave in $p$.
3. **$S p = 0$:** Hicksian demand is homogeneous of degree zero in $p$, so by Euler's theorem $\sum_j p_j S_{ij} = 0$.
4. **$S_{ii} \leq 0$:** Own-price compensated demands are non-increasing.

### Matrix Form

$$S = \frac{\partial \mathbf{h}}{\partial \mathbf{p}^T} = \frac{\partial \mathbf{x}^*}{\partial \mathbf{p}^T} + \mathbf{x}^* \left(\frac{\partial \mathbf{x}^*}{\partial m}\right)^T$$

## Slutsky vs Hicks Compensation

Two compensation concepts yield two decompositions:

| Type | Compensation | Effect |
|------|-------------|--------|
| **Slutsky** | Pivoted budget line: $m' = p' \cdot x_0$ (can afford old bundle at new prices) | Keeps purchasing power; overcompensates for normal goods |
| **Hicks (EV-based)** | $m^H = e(p', \bar{u}_0)$ (remain on original indifference curve) | Keeps utility; used in welfare analysis |

The Slutsky equation above uses **Hicksian** compensation (Hicksian SE). Both approaches yield the same mathematical NSD result.

## Cross-Price Slutsky Terms

For goods $i \neq j$:

$$S_{ij} = \frac{\partial h_i}{\partial p_j}$$

- $S_{ij} > 0$: goods $i$ and $j$ are **Hicksian substitutes** (compensated demand for $i$ rises when $p_j$ rises).
- $S_{ij} < 0$: goods $i$ and $j$ are **Hicksian complements**.

**Note:** Hicksian substitutability/complementarity uses the compensated demand, unlike Marshallian gross substitutes/complements which include income effects.

By symmetry, $S_{ij} = S_{ji}$: if $i$ is a Hicksian substitute for $j$, then $j$ is a Hicksian substitute for $i$.

## Cobb-Douglas Example

For $u = x_1^\alpha x_2^{1-\alpha}$ with Marshallian demand $x_1^* = \alpha m/p_1$:

$$\frac{\partial x_1^*}{\partial p_1} = -\frac{\alpha m}{p_1^2}$$

$$\frac{\partial x_1^*}{\partial m} = \frac{\alpha}{p_1}, \quad x_1^* = \frac{\alpha m}{p_1}$$

**Income effect:** $x_1^* \cdot \partial x_1^*/\partial m = \frac{\alpha m}{p_1} \cdot \frac{\alpha}{p_1} = \frac{\alpha^2 m}{p_1^2}$

**Slutsky equation verification:**

$$S_{11} = \frac{\partial x_1^*}{\partial p_1} + x_1^* \frac{\partial x_1^*}{\partial m} = -\frac{\alpha m}{p_1^2} + \frac{\alpha^2 m}{p_1^2} = -\frac{\alpha(1-\alpha)m}{p_1^2} \leq 0 \checkmark$$

**Hicksian demand verification:** $h_1 = \bar{u} \left(\frac{(1-\alpha)p_1}{\alpha p_2}\right)^{-(1-\alpha)}$, and $\partial h_1/\partial p_1 = -\frac{(1-\alpha)\alpha m}{p_1^2}$... confirming the identity.

## Related Concepts

- [[Income_and_Substitution_Effects]] — graphical and economic interpretation of the decomposition
- [[Expenditure_Minimization_and_Hicksian_Demand]] — defines Hicksian demand $h_i$; Shephard's Lemma used in derivation
- [[Duality]] — the Slutsky equation follows directly from the duality identity $h_i = x_i^*(p, e(p,\bar{u}))$
- [[Marshallian_Demand]] — the left-hand side of the Slutsky equation
- [[Revealed_Preferences]] — WARP implies NSD of the Slutsky matrix
- [[Consumer_Surplus_and_Welfare_Measures]] — CV and EV involve Hicksian demands derived via Slutsky structure
