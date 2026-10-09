---
course: JEB104
topic: Intertemporal Choice
source: 00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_15_Intertemporal_choice_Students.pdf
tags: [JEB104, microeconomics, intertemporal-choice, Fisher, present-value, saving, borrowing, interest-rate]
created: 2026-04-19
---

Parent: [[JEB104_Microeconomics_I_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_15_Intertemporal_choice_Students.pdf]]
Related: [[Endowment_Economy_and_Buying_Selling]], [[Budget_Constraint]], [[Income_and_Substitution_Effects]], [[Utility_Function]], [[Labor_Supply]]

# Intertemporal Choice

## Setup: Fisher's Two-Period Model

Consider a consumer living over two periods: **period 0** (present) and **period 1** (future). The consumer receives income $m_0$ in period 0 and $m_1$ in period 1. Let $r$ be the **real interest rate**.

**Decision variables:** Present consumption $c_0$ and future consumption $c_1$.

## Intertemporal Budget Constraint

**Future value form:** Compound all flows to period 1:

$$(1+r)c_0 + c_1 = (1+r)m_0 + m_1$$

**Present value form:** Discount all flows to period 0:

$$\boxed{c_0 + \frac{c_1}{1+r} = m_0 + \frac{m_1}{1+r}}$$

The right-hand side is the **present value of lifetime income** (wealth):

$$W = m_0 + \frac{m_1}{1+r}$$

**Structure:** This is an **endowment budget constraint** — the budget line always passes through the endowment $(m_0, m_1)$.

**Slope:** $-(1+r)$ in the $(c_0, c_1)$ plane — giving up $1$ unit of present consumption enables $(1+r)$ units of future consumption.

## Saving and Borrowing

- **Saver / Lender:** $c_0 < m_0$ — saves $s = m_0 - c_0 > 0$ in period 0, earning $(1+r)s$ in period 1. Net buyer of period 1 goods.
- **Borrower:** $c_0 > m_0$ — borrows $b = c_0 - m_0 > 0$, repays $(1+r)b$ in period 1. Net seller of period 1 goods.

## Utility Maximization

Consumer maximises inter-temporal utility $u(c_0, c_1)$, often with **discounting**:

$$U(c_0, c_1) = u(c_0) + \delta u(c_1), \quad \delta = \frac{1}{1+\rho} \in (0,1)$$

where $\rho > 0$ is the **subjective discount rate** (rate of time preference).

**Optimality condition (Fisher condition):**

$$\frac{u'(c_0)}{\delta u'(c_1)} = 1 + r \quad \Longleftrightarrow \quad \frac{MU_{c_0}}{MU_{c_1}} = 1 + r$$

The **marginal rate of intertemporal substitution (MRIS)** equals the gross interest rate:

$$MRIS = \frac{u'(c_0)}{\delta u'(c_1)} = 1 + r$$

## Comparative Statics: Change in Interest Rate

A rise in $r$ has **both SE and IE**, via the endowment Slutsky equation:

$$\frac{dc_0}{dr} = \underbrace{\frac{\partial h_{c_0}}{\partial r}}_{\text{SE} \leq 0} + \underbrace{(m_0 - c_0)\frac{\partial c_0}{\partial W}}_{\text{Endowment IE}}$$

| Status | Endowment IE | Total Effect |
|--------|-------------|--------------|
| **Saver** ($c_0 < m_0$): | $m_0 - c_0 > 0$, so if $c_0$ is normal: IE $> 0$ | SE and IE work in opposite directions — ambiguous |
| **Borrower** ($c_0 > m_0$): | $m_0 - c_0 < 0$, so IE $< 0$ | Both SE and IE reduce $c_0$ — borrower unambiguously hurts |

**Saver:** A higher $r$ raises the price of present consumption (SE → consume less now), but also raises wealth (IE → consume more now). Net effect on $c_0$ is ambiguous. $c_1$ likely rises.

**Borrower:** Both effects reduce $c_0$ (SE: borrowing is now more expensive; IE: wealth falls). Net effect: $c_0$ falls unambiguously.

## Present Value and Capital Markets

**Fisher Separation Theorem (with capital markets):** When capital markets are perfect (can borrow/lend freely at rate $r$), a multi-period production/investment decision separates into:

1. **Wealth-maximisation:** Choose investment to maximise present value of income.
2. **Utility maximisation:** Choose consumption profile given wealth.

The optimal investment is independent of preferences — only the interest rate matters for the investment decision.

## Specific Example: Log Utility

For $U = \ln c_0 + \delta \ln c_1$ subject to $c_0 + c_1/(1+r) = W$:

**Setting up Lagrangian:**

$$\mathcal{L} = \ln c_0 + \delta \ln c_1 - \lambda\left(c_0 + \frac{c_1}{1+r} - W\right)$$

**FOCs:**

$$\frac{1}{c_0} = \lambda, \qquad \frac{\delta}{c_1} = \frac{\lambda}{1+r}$$

**Dividing:** $c_1 = \delta(1+r) c_0$

**Substituting into budget:**

$$c_0 + \frac{\delta(1+r)c_0}{1+r} = W \implies c_0(1 + \delta) = W$$

$$\boxed{c_0^* = \frac{W}{1+\delta}, \qquad c_1^* = \frac{\delta(1+r)W}{1+\delta}}$$

**Savings rate:** $s = m_0 - c_0^* = m_0 - W/(1+\delta)$. For this utility function, the savings rate depends on $W$, $r$, and $\delta$.

## Borrowing Constraints

If the consumer **cannot borrow** ($c_0 \leq m_0$), the budget set is truncated. A would-be borrower is constrained at $c_0 = m_0$ — they consume only current income.

**Liquidity constraint:** $c_0 \leq m_0$ is binding when the optimal unconstrained $c_0^* > m_0$.

At the constrained optimum, the shadow price of the constraint ($\mu > 0$) augments the first-order conditions:

$$u'(c_0) = \lambda + \mu, \qquad \delta u'(c_1) = \frac{\lambda}{1+r}$$

Implying $u'(c_0) > \lambda$ and $\text{MRIS} > 1+r$ — the consumer would benefit from borrowing at rate $r$ but cannot.

## Multi-Period Extension

With $T+1$ periods, income streams $\{m_t\}$ and gross interest factors $\{R_t = 1+r_t\}$:

**Present value budget:**

$$\sum_{t=0}^{T} \frac{c_t}{\prod_{s=0}^{t-1} R_s} = \sum_{t=0}^{T} \frac{m_t}{\prod_{s=0}^{t-1} R_s}$$

The consumer maximises $\sum_{t=0}^T \delta^t u(c_t)$.

**Euler equation (optimality across adjacent periods):**

$$u'(c_t) = \delta R_{t+1} u'(c_{t+1})$$

This is the **Euler equation for consumption** — the foundation of modern consumption theory (Hall 1978).

## Related Concepts

- [[Endowment_Economy_and_Buying_Selling]] — intertemporal choice is an endowment economy across periods
- [[Budget_Constraint]] — the present-value budget constraint is a special endowment budget constraint
- [[Income_and_Substitution_Effects]] — both effects arise from a change in the interest rate
- [[Labor_Supply]] — both are endowment economies with time/income being the endowed resource
- [[Utility_Function]] — intertemporal utility commonly uses additive time-separable form with discounting
