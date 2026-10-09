---
course: "JEB108"
topic: "Profit Maximization"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/2_profit.pdf"
tags: [JEB108, microeconomics, profit, firm-behaviour]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/2_profit.pdf]]
Related: [[Production_Technology]], [[Returns_to_Scale]], [[Cost_Minimization]], [[Firm_Supply_Curve]], [[Marshallian_Demand|Marshallian Demand (consumer analogue)]]

# Profit Maximization

## Definition

A **profit-maximizing firm** chooses output $y$ and inputs $(x_1, x_2, \ldots, x_n)$ to maximize:

$$\pi = py - \sum_{i=1}^n w_i x_i = py - w_1 x_1 - w_2 x_2$$

where $p$ is the output price and $w_i$ are input prices (factor wages/rental rates).

**Key assumption:** Under **perfect competition**, the firm is a **price-taker** — it takes $p$ and all $w_i$ as given.

---

## Two-Stage Approach

Profit maximization can be decomposed:

1. **Cost minimization** (see [[Cost_Minimization]]): For any output level $y$, minimize costs to find $c(w, y)$.
2. **Output choice**: Choose $y$ to maximize $\pi(y) = py - c(w,y)$.

---

## First-Order Condition (FOC)

For an interior solution $y^* > 0$:

$$\frac{d\pi(y^*)}{dy} = p - \frac{dTC(y^*)}{dy} = 0$$

$$\Rightarrow \boxed{p = MC(y^*)}$$

**Price equals marginal cost** — the fundamental condition for competitive profit maximization.

## Second-Order Condition (SOC)

For $y^*$ to be a **maximum** (not minimum), marginal profit must be decreasing:

$$\frac{d^2\pi(y^*)}{dy^2} = \frac{d^2 TR}{dy^2} - \frac{d^2 TC}{dy^2} = \underbrace{\frac{dp}{dy}}_{=0 \text{ (competitive)}} - \frac{dMC(y^*)}{dy} < 0$$

$$\Rightarrow \frac{dMC(y^*)}{dy} > 0$$

The firm must produce on the **upward-sloping portion** of the MC curve.

---

## Existence and Multiplicity of Optima

### No Maximum

If the production function exhibits **increasing returns to scale**, profit grows without bound under perfect competition → no finite maximum exists.

### Multiple Local Maxima

When the TC curve has non-standard shape (e.g., S-shaped), multiple local maxima can exist. The global maximum is the local maximum with the **highest profit level**.

### Corner Solution ($y^* = 0$)

The firm shuts down if:

$$\frac{d\pi(0)}{dy} = p - MC(0) < 0 \quad \Leftrightarrow \quad p < MC(0)$$

Even if FOC and SOC are satisfied at some $y^* > 0$, the firm shuts down if $\pi(y^*) < 0$. More precisely: shuts down when $p < \min AC$ (short-run: when $p < \min AVC$).

### Summary of Optimality Conditions

| Condition | Formula |
|---|---|
| Interior maximum: FOC | $p = MC(y^*)$ |
| Interior maximum: SOC | $dMC(y^*)/dy > 0$ |
| Corner solution | $y^* = 0$ |

---

## Returns to Scale and Profit

| Returns to Scale | Profit Outcome |
|---|---|
| IRS (increasing) | No finite maximum; shut down or infinite profit |
| CRS (constant) | $\pi = 0$ in equilibrium (any scale equally profitable) |
| DRS (decreasing) | Unique finite maximum with $\pi > 0$ possible |

*See* [[Returns_to_Scale]] *for formal derivations.*

---

## Isoprofit Lines

In $(x_1, y)$-space, an **isoprofit line** is the set of input-output combinations yielding profit level $\bar{\pi}$:

$$y = \frac{\bar{\pi} + w_1 x_1}{p} = \frac{\bar{\pi}}{p} + \frac{w_1}{p} x_1$$

- Slope: $w_1/p$ (the real input price)
- Intercept: $\bar{\pi}/p$
- Higher lines correspond to **higher profits**

The firm maximizes profit by choosing the highest isoprofit line tangent to the production function.

---

## Revealed Profitability (Weak Axiom of Profit Maximization)

**WAPM:** Let $(y^t, x^t)$ and $(y^s, x^s)$ be observed profit-maximizing choices at prices $(p^t, w^t)$ and $(p^s, w^s)$. Then:

$$p^t y^t - w_1^t x_1^t - w_2^t x_2^t \geq p^t y^s - w_1^t x_1^s - w_2^t x_2^s$$
$$p^s y^s - w_1^s x_1^s - w_2^s x_2^s \geq p^s y^t - w_1^s x_1^t - w_2^s x_2^t$$

Combining:
$$\Delta p \cdot \Delta y - \Delta w_1 \cdot \Delta x_1 - \Delta w_2 \cdot \Delta x_2 \geq 0$$

This yields all standard comparative statics results (supply slopes up, factor demands slope down in prices).

**Recovering Technology:** By observing multiple price-quantity pairs satisfying WAPM, we can construct an **inner approximation** of the true technology — plotting isoprofit lines and taking their intersection gives a tighter estimate of the production set.

**Empirical Application — NYC Taxi Drivers** (Camerer et al., 1997, *QJE*): Standard theory predicts labour supply increases with wages. But NYC cab drivers exhibit backward-bending supply: they quit early on high-wage days and work longer on low-wage days. Explanation: daily earnings target + one-day planning horizon (psychological factors). Optimal strategy (constant hours) would yield 5–10% higher earnings.

---

## Exercise

**Setup:** $TC(y) = 2y^3 - 30y^2 + 150y$, perfect competition.

**Q1: Profit-maximizing output at $p = 6$?**

$$MC(y) = \frac{dTC}{dy} = 6y^2 - 60y + 150$$

Set $p = MC$: $6 = 6y^2 - 60y + 150 \Rightarrow y^2 - 10y + 24 = 0 \Rightarrow (y-4)(y-6) = 0$

Local maxima at $y = 4$ and $y = 6$. SOC: $dMC/dy = 12y - 60$:
- At $y = 4$: $12(4) - 60 = -12 < 0$ → **local minimum**
- At $y = 6$: $12(6) - 60 = 12 > 0$ → **local maximum**

Check $y = 0$: $\pi(0) = 0$. $\pi(6) = 6(6) - [2(216) - 30(36) + 150(6)] = 36 - [432 - 1080 + 900] = 36 - 252 = -216 < 0$.

→ Firm **shuts down** at $p = 6$ ($\pi(0) = 0 > -216$).
