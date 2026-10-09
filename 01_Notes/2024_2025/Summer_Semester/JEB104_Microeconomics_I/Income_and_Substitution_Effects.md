---
title: "Income and Substitution Effects"
course: JEB104
topic: Consumer Theory
tags: [income-effect, substitution-effect, Hicksian-decomposition, normal-good, inferior-good, Giffen-good, consumer-theory]
date_created: 2026-04-19
---

# Income and Substitution Effects

## Motivation

When the price of a good changes, two distinct forces alter demand:

1. **Substitution effect (SE):** The good becomes relatively cheaper or more expensive, inducing substitution toward or away from it, holding real purchasing power (utility) constant.
2. **Income effect (IE):** The price change alters real purchasing power (the budget set shifts), inducing a change in demand similar to an income change.

The **Hicksian decomposition** disentangles these two effects.

## Hicksian Decomposition

Suppose $p_1$ falls from $p_1$ to $p_1'$. The total change in demand for good 1 is:

$$\Delta x_1^* = x_1^*(p_1', p_2, m) - x_1^*(p_1, p_2, m)$$

### Step 1 — Substitution Effect

**Pivot the budget line:** Adjust income so that the consumer can just afford the original bundle at new prices. The pivoted income is $m' = p_1' x_1^* + p_2 x_2^*$ (Slutsky compensation).

Alternatively, adjust income so the consumer remains on the **original indifference curve** (Hicksian/compensated adjustment): $m^H = e(p_1', p_2, u_0)$.

The SE measures the move from the original optimum to the new optimum on the compensated budget line:

$$SE = h_1(p_1', p_2, u_0) - h_1(p_1, p_2, u_0)$$

where $h_1$ is Hicksian demand. **The SE is always non-positive for own-price changes** (substitution effect law): $\partial h_i / \partial p_i \leq 0$.

### Step 2 — Income Effect

**Shift the pivoted budget line:** Return income from $m'$ (or $m^H$) to $m$ at the new prices $p_1'$.

The IE measures the demand change due to this income adjustment:

$$IE = x_1^*(p_1', p_2, m) - x_1^*(p_1', p_2, m')$$

For a **normal good** ($\partial x_1^*/\partial m > 0$): a fall in $p_1$ raises real income, so the IE increases demand. Both SE and IE work in the same direction — demand definitely rises.

For an **inferior good** ($\partial x_1^*/\partial m < 0$): the IE counteracts the SE. If $|IE| < |SE|$: demand still rises (ordinary inferior good). If $|IE| > |SE|$: demand falls — this is a **Giffen good**.

## Graphical Decomposition

1. **Start:** optimum $A$ at $(p_1, m)$ on indifference curve $u_0$.
2. **Price fall** $p_1 \to p_1'$: budget line rotates outward.
3. **SE:** pivot the budget line to be tangent to $u_0$ at new slope $-p_1'/p_2$. New optimum $B$ — this is the pure substitution effect.
4. **IE:** shift the pivoted line outward to original income. New optimum $C$ — this is the income effect.

The total change $A \to C$ = SE ($A \to B$) + IE ($B \to C$).

## Classification of Goods

| Type | $\partial x_1^*/\partial m$ | $\partial x_1^*/\partial p_1$ | Example |
|------|-----------------------------|-------------------------------|---------|
| Normal | $> 0$ | $< 0$ | Most goods |
| Inferior | $< 0$ | $< 0$ | Some staples at high income |
| Giffen | $< 0$ | $> 0$ | Potato in Irish famine (debated) |

**Necessary condition for Giffen:** The good must be inferior **and** account for a large share of expenditure (so the IE is large).

## The Slutsky Equation

The mathematical relationship between SE and IE is given by the **Slutsky equation** (see [[Slutsky_Equation]] for full derivation):

$$\frac{\partial x_i^*}{\partial p_j} = \frac{\partial h_i}{\partial p_j} - x_j^* \frac{\partial x_i^*}{\partial m}$$

For own-price effects ($i = j$):

$$\underbrace{\frac{\partial x_i^*}{\partial p_i}}_{\text{total effect}} = \underbrace{\frac{\partial h_i}{\partial p_i}}_{\text{SE} \leq 0} - \underbrace{x_i^* \frac{\partial x_i^*}{\partial m}}_{\text{IE}}$$

## Normal Goods and Law of Demand

For a normal good, both SE and IE reinforce each other in the same direction:
- Own-price increase: SE reduces demand, IE reduces demand (real income falls, demand falls further for normal good)
- Result: $\partial x_i^*/\partial p_i < 0$ — law of demand holds

For an inferior good, SE and IE oppose:
- Own-price increase: SE reduces demand, but IE increases demand (real income falls, but inferior good demand rises)
- If $|SE| > |IE|$: demand still falls (ordinary inferior)
- If $|SE| < |IE|$: demand rises — Giffen behaviour

## Related Concepts

- [[Expenditure_Minimization_and_Hicksian_Demand]] — defines the SE in terms of compensated demand
- [[Slutsky_Equation]] — the formal decomposition linking Marshallian and Hicksian demand
- [[Marshallian_Demand]] — total demand response including both SE and IE
- [[Duality]] — the Hicksian decomposition is grounded in the duality between UMP and EMP
- [[Consumer_Surplus_and_Welfare_Measures]] — CV and EV use this decomposition to measure welfare changes
