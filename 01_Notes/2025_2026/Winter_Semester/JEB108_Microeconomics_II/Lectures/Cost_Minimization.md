---
course: "JEB108"
topic: "Cost Minimization"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/3_cost_minimization.pdf"
tags: [JEB108, microeconomics, cost, cost-minimization, duality]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/3_cost_minimization.pdf]]
Related: [[Profit_Maximization_Firm]], [[Production_Technology]], [[Production_Technology|Isoquant and TRS]], [[Cost_Curves]], [[Expenditure_Minimization_and_Hicksian_Demand|Expenditure Minimization (consumer analogue)]]

# Cost Minimization

## Problem Statement

A profit-maximizing firm's cost-side problem is to **minimize the cost** of producing any given output level $y$:

$$\min_{x_1, x_2}\; w_1 x_1 + w_2 x_2 \quad \text{subject to} \quad f(x_1, x_2) = y$$

The solution is the **cost function** $c(w_1, w_2, y)$ — minimized costs as a function of input prices and required output.

**Scope:** All costs must be included — including **opportunity costs** (the value of the best foregone alternative).

---

## Solution Methods

### Method 1 — Lagrange Multipliers

Set up the Lagrangian:

$$\mathcal{L} = w_1 x_1 + w_2 x_2 - \lambda[f(x_1, x_2) - y]$$

**First-order conditions:**

$$\frac{\partial \mathcal{L}}{\partial x_1} = w_1 - \lambda \frac{\partial f}{\partial x_1} = 0 \quad \Rightarrow \quad w_1 = \lambda \cdot MP_1$$

$$\frac{\partial \mathcal{L}}{\partial x_2} = w_2 - \lambda \frac{\partial f}{\partial x_2} = 0 \quad \Rightarrow \quad w_2 = \lambda \cdot MP_2$$

Dividing:

$$\frac{w_1}{w_2} = \frac{MP_1}{MP_2} \quad \Leftrightarrow \quad TRS = -\frac{w_1}{w_2}$$

**The technical rate of substitution equals the factor price ratio** — the producer optimality condition, analogous to MRS = price ratio in consumer theory.

### Method 2 — Tangency Condition

Isocost line: $x_2 = \frac{C}{w_2} - \frac{w_1}{w_2} x_1$ has slope $-w_1/w_2$.

At the cost minimum, the isocost line is **tangent** to the isoquant, so their slopes are equal: $TRS = -w_1/w_2$.

---

## Corner Solutions

When the tangency condition cannot be satisfied (e.g., one input is too expensive), the firm uses **zero of one input** ($x_j^* = 0$). The optimality conditions become **complementary slackness** conditions (KKT):

$$\frac{\partial \mathcal{L}}{\partial x_j}\bigg|_{x^*} \geq 0, \quad x_j^* \geq 0, \quad \frac{\partial \mathcal{L}}{\partial x_j}\bigg|_{x^*} \cdot x_j^* = 0$$

In terms of economic condition: $\frac{w_i}{MP_i} \leq \frac{w_j}{MP_j}$ for all $j$, with equality whenever $x_j^* > 0$.

---

## Conditional Factor Demands and Cost Function

**Conditional factor demands** (derived factor demands):

$$x_i^*(w_1, w_2, y): \text{ cost-minimizing input of } x_i \text{ given prices and output target}$$

**Cost function:**

$$c(w_1, w_2, y) = \sum_i w_i x_i^*(w_1, w_2, y)$$

### Example — Cobb-Douglas

$f(x_1, x_2) = x_1^a x_2^b$. From the TRS condition:

$$\frac{w_1}{w_2} = \frac{a x_2}{b x_1} \Rightarrow x_2 = \frac{b w_1}{a w_2} x_1$$

Substituting into the constraint $f = y$:

$$x_1^* = \left(\frac{a w_2}{b w_1}\right)^{b/(a+b)} \cdot y^{1/(a+b)} \cdot \text{const}$$

Cost function: $c(w_1, w_2, y) = K \cdot w_1^{a/(a+b)} w_2^{b/(a+b)} \cdot y^{1/(a+b)}$

---

## Properties of the Cost Function

| Property | Statement |
|---|---|
| **Increasing in $y$** | $\partial c / \partial y = MC = w_i / MP_i > 0$ |
| **Non-decreasing in $w$** | $\partial c / \partial w_i \geq 0$ |
| **Linearly homogeneous in $w$** | $c(kw, y) = k \cdot c(w, y)$ for all $k > 0$ |
| **Continuous** | $c$ is continuous in $w$ and $y$ |
| **Concave in $w$** | $c(w, y)$ is concave in input prices (can't lose from input price increase by more than proportional) |

### Shephard's Lemma

$$\frac{\partial c(w, y)}{\partial w_i} = x_i^*(w, y)$$

The derivative of the cost function with respect to input price $w_i$ equals the **conditional demand** for input $i$. Analogous to Roy's identity / Shephard's lemma for expenditure (see [[Expenditure_Minimization_and_Hicksian_Demand]]).

**Application:** $x_i$ can be recovered from $c$ without solving the optimization again. Also used to estimate how costs change with a small change in input prices.

---

## Cost Functions for Specific Technologies

| Technology | $f(x_1, x_2)$ | $c(w_1, w_2, y)$ |
|---|---|---|
| Perfect complements | $\min\{x_1, x_2\}$ | $y(w_1 + w_2)$ |
| Perfect substitutes | $x_1 + x_2$ | $y \cdot \min\{w_1, w_2\}$ |
| Cobb-Douglas $x_1^{1/3} x_2^{2/3}$ | (see above) | $K w_1^{1/3} w_2^{2/3} y$ |

---

## Expansion Path

The **expansion path** traces the cost-minimizing input combinations as output $y$ increases (input prices held constant).

- **Normal input:** conditional factor demand increases in $y$ (expansion path has positive slope).
- **Inferior input:** conditional factor demand decreases in $y$ (expansion path has negative slope).

**Key result:** At any given output level, at least one input must be normal; no input can be inferior at all output levels.

---

## Short-Run vs. Long-Run Costs

**Short-run costs** (some input, say $x_2 = \bar{x}_2$, is fixed):

$$c^s(y, \bar{x}_2) = \min_{x_1} (w_1 x_1 + w_2 \bar{x}_2) \quad \text{s.t.} \quad f(x_1, \bar{x}_2) = y$$

**Long-run costs** (all inputs adjust):

$$c^{LR}(y) = \min_{x_1, x_2} (w_1 x_1 + w_2 x_2) \quad \text{s.t.} \quad f(x_1, x_2) = y$$

**Key relationships:**
- $c^{LR}(y) \leq c^s(y, \bar{x}_2)$ for all $y$ — long-run costs are always weakly lower
- The curves are tangent at the output level where $\bar{x}_2 = x_2^{LR*}$

### Fixed Costs, Quasi-Fixed Costs, Sunk Costs

| Type | Definition |
|---|---|
| **Fixed costs (FC)** | Independent of output; not present in the long run |
| **Quasi-fixed costs** | Independent of output, but paid **only if** the firm produces ($y > 0$); can exist in long run |
| **Sunk costs** | Already committed; cannot be recovered regardless of future decisions |

### Sunk Cost Fallacy — Behavioural Application

**Cohen & Dupas (2010):** Randomized experiment pricing malaria bed nets in Kenya.
- Free distribution → higher take-up but lower use
- Positive price → sunk cost effect induces greater actual use
- Policy debate: free vs. cost-sharing depends on relative magnitudes of selection effects and sunk cost effects.

---

## Revealed Cost Minimization (WACM)

**Weak Axiom of Cost Minimization:** Observe choices at two price vectors $w^t, w^s$ with the **same output** $y_0$:

$$w_1^t x_1^t + w_2^t x_2^t \leq w_1^t x_1^s + w_2^t x_2^s$$
$$w_1^s x_1^s + w_2^s x_2^s \leq w_1^s x_1^t + w_2^s x_2^t$$

Adding and rearranging:

$$\Delta w_1 \cdot \Delta x_1 + \Delta w_2 \cdot \Delta x_2 \leq 0$$

This implies conditional factor demands are **non-increasing in own price** — a general comparative statics result requiring only revealed preference, not functional form assumptions.
