---
course: JEB104
topic: Labour Supply
source: 00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_14_Labor_Students.pdf
tags: [JEB104, microeconomics, labour-supply, leisure, wage, backward-bending, income-effect, substitution-effect]
created: 2026-04-19
---

Parent: [[JEB104_Microeconomics_I_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_14_Labor_Students.pdf]]
Related: [[Endowment_Economy_and_Buying_Selling]], [[Budget_Constraint]], [[Income_and_Substitution_Effects]], [[Marshallian_Demand]], [[Utility_Function]]

# Labour Supply

## Setup

A consumer allocates the **time endowment** $T$ (e.g., 24 hours per day) between:
- **Leisure:** $l \in [0, T]$ — directly generates utility.
- **Labour:** $L = T - l$ — earns wage income $wL$.

**Goods:**
- Leisure $l$: price = wage $w$ (opportunity cost of leisure is forgone earnings).
- Composite consumption good $c$: price normalised to 1.
- Non-labour income: $m \geq 0$ (dividends, transfers, etc.).

## Budget Constraint

**Expenditure form:**

$$c + w l = wT + m \equiv I$$

where $I$ is **full income** — the income the consumer would earn if working every hour. This is an **endowment budget constraint** (the consumer "owns" leisure worth $wT$).

**Income form (using $L = T - l$):**

$$c = wL + m$$

The budget line:
- Vertical intercept ($L=0$, pure leisure): $c = m$.
- Horizontal intercept ($l=0$, all work): $c = wT + m$.
- Slope in $(l, c)$ space: $-w$ (opportunity cost of one hour of leisure = $w$ units of consumption forgone).

## Utility Maximization

Consumer maximises $u(l, c)$ subject to $c + wl = I$:

**First-order condition:**

$$\frac{MU_l}{MU_c} = w$$

$$MRS_{lc} = \frac{\partial u/\partial l}{\partial u/\partial c} = w$$

At an interior optimum, the marginal rate of substitution between leisure and consumption equals the wage.

## Labour Supply Function

From the optimum conditions, derive:
- **Leisure demand:** $l^*(w, m)$ — Marshallian demand for leisure.
- **Labour supply:** $L^s(w, m) = T - l^*(w, m)$.

**Properties inherited from demand theory:**
- The Slutsky matrix structure applies.
- $\partial l / \partial w = \partial h_l/\partial w + (T - l) \partial l/\partial m$ (endowment Slutsky with $\omega_l = T$).
- So: $\partial L^s/\partial w = -\partial h_l/\partial w - (T - l) \partial l/\partial m = \underbrace{\partial h_L/\partial w}_{\text{SE} \geq 0} - \underbrace{L \partial l/\partial m}_{\text{IE}}$

where $\partial h_L/\partial w > 0$ (compensated labour supply is upward sloping: higher wage makes leisure more expensive → supply more labour) and the IE sign depends on whether leisure is a normal or inferior good.

## Income and Substitution Effects of a Wage Increase

| Effect | Mechanism | Direction |
|--------|-----------|-----------|
| **Substitution effect** | Higher $w$ makes leisure relatively expensive → substitute away from leisure → work more | $\partial L/\partial w|_{SE} > 0$ |
| **Income effect** | Higher $w$ raises real income (worker is richer) → demand more leisure (if normal) → work less | $\partial L/\partial w|_{IE} < 0$ (if leisure is normal) |

**Total effect:** $\partial L^s/\partial w = SE + IE$ — ambiguous sign.

## Backward-Bending Labour Supply

At **low wages**: SE dominates — labour supply increases with wage.

At **high wages**: IE dominates — as the consumer becomes wealthier, they "buy" more leisure and work less.

This produces the iconic **backward-bending labour supply curve**:

$$\frac{dL^s}{dw} \begin{cases} > 0 & \text{at low } w \text{ (forward-bending segment)} \\ = 0 & \text{at wage } w^* \text{ (labour supply peak)} \\ < 0 & \text{at high } w \text{ (backward-bending segment)} \end{cases}$$

**Formal condition for backward bend:** $L \cdot \partial l/\partial m > \partial h_L/\partial w$, i.e., the income effect outweighs the substitution effect.

## Corner Solutions

### Non-participation ($L = 0$)

The consumer does not work if the reservation wage $w^R$ exceeds the market wage $w$:

$$w^R = MRS_{lc}\bigg|_{l=T, c=m} = \frac{MU_l(T, m)}{MU_c(T, m)}$$

If $w < w^R$: stay at home (corner solution, $L^s = 0$).
If $w > w^R$: enter the labour market.

### Maximum Labour ($l = 0$)

Rarely binding in practice; would require $MRS_{lc}(0, I) < w$.

## Comparative Statics

### Effect of Non-Labour Income $m$

$$\frac{\partial l^*}{\partial m} = \frac{\partial x_l}{\partial m}\bigg|_{(\text{via Marshallian demand})}$$

If leisure is a **normal good** ($\partial l^*/\partial m > 0$): higher non-labour income reduces labour supply. A lottery winner works less.

### Effect of Wage Tax

A **proportional wage tax** at rate $\tau$ reduces the net wage to $w(1-\tau)$. Both the SE and IE push in opposing directions:
- SE: lower net wage makes leisure cheaper → work less.
- IE: lower income → work more (if leisure is normal).

The net effect on labour supply is ambiguous — a key result motivating the study of optimal taxation.

## Specific Utility Examples

### Cobb-Douglas: $u = c^\alpha l^\beta$

Budget: $c + wl = I = wT + m$.

Marshallian leisure demand: $l^* = \frac{\beta}{\alpha + \beta} \cdot \frac{I}{w}$

Labour supply: $L^s = T - l^* = T - \frac{\beta I}{(\alpha+\beta)w}$

Since $I = wT + m$: $L^s = T - \frac{\beta(wT + m)}{(\alpha+\beta)w} = \frac{\alpha T}{\alpha+\beta} - \frac{\beta m}{(\alpha+\beta)w}$

$\partial L^s/\partial w = \frac{\beta m}{(\alpha+\beta)w^2} > 0$ when $m > 0$: upward-sloping supply (no backward-bend for C-D since the substitution and income effects cancel away the backward bend for this functional form with zero non-labour income).

## Related Concepts

- [[Endowment_Economy_and_Buying_Selling]] — labour-leisure is an endowment economy with leisure as the endowed good
- [[Budget_Constraint]] — the labour budget constraint mirrors the endowment constraint
- [[Income_and_Substitution_Effects]] — the backward-bending labour curve illustrates a dominant income effect
- [[Intertemporal_Choice]] — both involve time allocation and endowment-based budgets
- [[Marshallian_Demand]] — labour supply is derived from the demand for leisure
