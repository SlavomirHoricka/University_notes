---
course: "JEB108"
topic: "Production Technology"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/1_technology-1.pdf"
tags: [JEB108, microeconomics, production, technology]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/1_technology-1.pdf]]
Related: [[Profit_Maximization_Firm]], [[Cost_Minimization]], [[Production_Technology|Isoquant and TRS]], [[Returns_to_Scale]], [[Utility_Function|Utility Function (consumer analogue)]]

# Production Technology

## Overview

Production technology describes how a firm transforms **inputs** (factors of production) into **outputs**. It defines the technological frontier — the maximum output achievable from any combination of inputs — and serves as the foundational constraint for all producer theory in JEB108.

**Factors of production:** land, labour, raw materials, physical capital. Modelled as flow units — quantities per unit time.

### Standard Assumptions

| Assumption | Formal Content |
|---|---|
| Free disposal | Costless not to use all inputs |
| Perfect divisibility | Inputs and outputs are perfectly divisible |
| Perfect information | Firms know their production function exactly |
| No externalities | Output depends only on own inputs |
| Homogeneity | Inputs and outputs are homogeneous within each category |

---

## Definitions

### Production Set

The **production set** is the set of all feasible (input, output) combinations:

$$Y = \{(y, x_1, \ldots, x_n) \mid 0 \leq y \leq f(x_1, \ldots, x_n),\; x_i \geq 0\; \forall i\}$$

### Production Function

The **production function** $f : \mathbb{R}^n_+ \to \mathbb{R}_+$ assigns to each input bundle the **maximum** producible output:

$$y \leq f(x_1, \ldots, x_n)$$

It is the upper boundary of the production set.

### Isoquant of Production

The **isoquant** at output level $y_0$ is the set of all input combinations that yield exactly $y_0$ units of output:

$$Q(y_0) = \{(x_1, \ldots, x_n) \in \mathbb{R}^n_+ \mid f(x_1, \ldots, x_n) = y_0\}$$

Isoquants are the producer analogue of indifference curves in [[Preferences_and_Indifference_Curves|consumer theory]].

---

## Examples of Technologies

### Leontief (Fixed-Proportions) Technology

$$f(x_1, x_2) = \min\{ax_1,\ bx_2\}$$

- Inputs are perfect complements; no substitution possible.
- To produce one unit: requires $\alpha = 1/a$ units of $x_1$ and $\beta = 1/b$ units of $x_2$.
- Isoquants are **L-shaped**; slope of the line through kink points equals $a/b$.

### Perfect Substitutes Technology

$$f(x_1, x_2) = ax_1 + bx_2$$

- Inputs are perfect substitutes.
- To produce one unit: $1/a$ units of $x_1$ **or** $1/b$ units of $x_2$.
- Isoquants are **straight lines** with slope $-a/b$.

### Cobb-Douglas Technology

$$f(x_1, x_2) = A x_1^a x_2^b, \quad A > 0,\; a, b > 0$$

- Intermediate case between perfect complements and perfect substitutes.
- $A$ scales overall productivity.
- $a$ and $b$ measure output elasticities with respect to each input.
- Isoquants are **smooth and convex**.

---

## Properties of the Production Function

Standard assumptions on $f$:

1. **Non-negativity:** $f(x) \geq 0$; inputs $x_i \geq 0$.
2. **Essentiality:** $f(0, \ldots, 0) = 0$ (no free lunch).
   - **Strong essentiality:** $\exists i : x_i = 0 \Rightarrow f(x) = 0$.
3. **Inefficiency is possible:** $0 \leq y \leq f(x)$ (free disposal).
4. **Monotonicity:** $\forall x\; \exists i : \partial f / \partial x_i > 0$ (more inputs, weakly more output).
5. **Convexity of isoquants:** For any $y_0$, the set $\{x \mid f(x) \geq y_0\}$ is convex:
$$f(\lambda x + (1-\lambda)z) \geq f(x) = f(z) = y_0, \quad \lambda \in [0,1]$$

---

## Marginal Product

The **marginal product** of input $i$ measures additional output from an infinitesimal increase in $x_i$, holding all other inputs fixed:

$$MP_i(x) = \frac{\partial f}{\partial x_i}(x)$$

**Discrete approximation:**

$$MP_1 \approx \frac{f(x_1 + \Delta x_1, x_2) - f(x_1, x_2)}{\Delta x_1}$$

### Law of Diminishing Marginal Product

$$\frac{\partial MP_1(x_1, x_2)}{\partial x_1} = \frac{\partial^2 f}{\partial x_1^2} \leq 0$$

Each additional unit of an input yields weakly less additional output when other inputs are held constant.

**Application — Microcredit:** The assumption of high marginal returns to capital for poor entrepreneurs underpins the microcredit model (Grameen Bank). De Mel, McKenzie, and Woodruff (2008) confirm this empirically: randomized grants of \$100–200 to Sri Lankan microenterprises yielded returns to capital of approximately **5% per month**.

---

## Technical Rate of Substitution (TRS)

The **TRS** is the slope of the isoquant — it measures the rate at which one input can be substituted for another while holding output constant.

**Derivation:** Along an isoquant, $dy = 0$:

$$dy = \frac{\partial f}{\partial x_1} dx_1 + \frac{\partial f}{\partial x_2} dx_2 = 0$$

$$\Rightarrow \quad TRS(x_1, x_2) = \frac{dx_2}{dx_1}\bigg|_{y = \text{const}} = -\frac{MP_1(x_1, x_2)}{MP_2(x_1, x_2)}$$

**Assumption — Diminishing TRS:** As $x_1$ increases (and $x_2$ decreases along the isoquant), $|TRS|$ falls, reflecting the convex shape of isoquants.

**Exercise:** For $f(x_1, x_2) = \sqrt{x_1+1} + \sqrt{x_2+1} - 2$, find TRS at $(x_1, x_2) = (15, 8)$:

$$MP_1 = \frac{1}{2\sqrt{x_1+1}}\bigg|_{x_1=15} = \frac{1}{8}, \quad MP_2 = \frac{1}{2\sqrt{x_2+1}}\bigg|_{x_2=8} = \frac{1}{6}$$

$$TRS = -\frac{1/8}{1/6} = -\frac{6}{8} = -\frac{3}{4}$$

---

## Technological Efficiency

**Technological efficiency:** A production plan is technologically efficient if it is impossible to produce the same output with strictly less of at least one input (all others unchanged). This corresponds to choosing a point on the **isoquant**, not below it.

**Output efficiency:** $y = f(x)$ — actually achieving the production frontier.

A cost-minimizing firm always operates in the **economic region** where the isoquant has a **negative slope** (both $MP_1 > 0$ and $MP_2 > 0$).

---

## Elasticity of Substitution

The **elasticity of substitution** $\sigma$ measures the curvature of the isoquant — how readily the firm substitutes between inputs in response to a change in the TRS:

$$\sigma = \frac{\% \Delta (x_2/x_1)}{\% \Delta |TRS|} = \frac{d(x_2/x_1)}{d|TRS|} \cdot \frac{|TRS|}{x_2/x_1}$$

- **High $\sigma$:** inputs are good substitutes (flat isoquant).
- **Low $\sigma$:** inputs are poor substitutes / complements (curved isoquant).

### CES (Constant Elasticity of Substitution)

$$f(x_1, x_2) = A(a_1 x_1^\rho + a_2 x_2^\rho)^{1/\rho}, \quad A > 0,\; a_1 + a_2 = 1$$

where $\sigma = 1/(1-\rho)$. Special cases:
- $\rho \to 1$: perfect substitutes ($\sigma \to \infty$)
- $\rho \to -\infty$: Leontief ($\sigma \to 0$)
- $\rho \to 0$: Cobb-Douglas ($\sigma = 1$)

See also: [[Returns_to_Scale]] for how technology scales with all inputs.
