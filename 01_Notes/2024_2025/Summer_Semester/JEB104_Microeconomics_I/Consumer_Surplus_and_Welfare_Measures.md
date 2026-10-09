---
course: JEB104
topic: Welfare Measurement
source: 00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_12_Measuring_Welfare_Changes_Students.pdf
tags: [JEB104, microeconomics, consumer-surplus, compensating-variation, equivalent-variation, welfare, deadweight-loss]
created: 2026-04-19
---

Parent: [[JEB104_Microeconomics_I_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_12_Measuring_Welfare_Changes_Students.pdf]]
Related: [[Duality]], [[Expenditure_Minimization_and_Hicksian_Demand]], [[Indirect_Utility_Function_and_Roys_Identity]], [[Income_and_Substitution_Effects]], [[Slutsky_Equation]], [[Marshallian_Demand]]

# Consumer Surplus and Welfare Measures

## Motivation

When prices change, the consumer's welfare changes. Three measures quantify this welfare change in **monetary terms**:

1. **Consumer Surplus (CS)** — area under the Marshallian demand curve (approximate).
2. **Compensating Variation (CV)** — area under the Hicksian demand curve at **old** utility.
3. **Equivalent Variation (EV)** — area under the Hicksian demand curve at **new** utility.

## Consumer Surplus

### Definition

**Consumer surplus** is the net benefit consumers receive from purchasing a good at market price $p_1$ — the area between the demand curve and the price:

$$CS(p_1) = \int_{p_1}^{\bar{p}} x_1^*(t, p_2, m)\, dt$$

where $\bar{p}$ is the choke price (price at which demand = 0).

### Change in CS

For a price change from $p_1^0$ to $p_1^1$:

$$\Delta CS = -\int_{p_1^0}^{p_1^1} x_1^*(t, p_2, m)\, dt$$

(Negative integral because demand falls as price rises — $\Delta CS < 0$ when price rises.)

**Limitation:** CS uses **Marshallian demand**, which conflates substitution and income effects. It is an exact welfare measure only when the marginal utility of income is constant (quasi-linear preferences). Otherwise, CV and EV are preferred.

## Compensating Variation (CV)

### Definition

**CV** is the income transfer that leaves the consumer **as well off as before** the price change — the compensation required at the **new** prices to restore original utility $\bar{u}^0$:

$$CV = e(p^1, \bar{u}^0) - e(p^0, \bar{u}^0) = m - e(p^1, \bar{u}^0)$$

since $e(p^0, \bar{u}^0) = m$ (the consumer was on budget at old prices).

- If $p_1$ rises: $e(p^1, \bar{u}^0) > m$, so $CV > 0$ — the consumer needs compensation.
- If $p_1$ falls: $CV < 0$ — the consumer would pay up to $|CV|$ for the price reduction.

### Integral Representation

By Shephard's Lemma, $\partial e / \partial p_1 = h_1(p, \bar{u})$:

$$CV = \int_{p_1^0}^{p_1^1} h_1(t, p_2, \bar{u}^0)\, dt$$

This is the area to the left of the **Hicksian demand curve at old utility $\bar{u}^0$** between the two prices.

## Equivalent Variation (EV)

### Definition

**EV** is the income transfer (at **old** prices) that would make the consumer **as well off as** after the price change — the equivalent of the price change measured in old-price terms:

$$EV = e(p^0, \bar{u}^1) - e(p^0, \bar{u}^0) = e(p^0, \bar{u}^1) - m$$

where $\bar{u}^1 = v(p^1, m)$ is the utility achieved at new prices.

- If $p_1$ rises: $\bar{u}^1 < \bar{u}^0$, so $e(p^0, \bar{u}^1) < m$ and $EV < 0$ — this is the income loss equivalent.
- If $p_1$ falls: $EV > 0$ — the consumer gains.

### Integral Representation

$$EV = \int_{p_1^0}^{p_1^1} h_1(t, p_2, \bar{u}^1)\, dt$$

Area to the left of the **Hicksian demand curve at new utility $\bar{u}^1$**.

## Comparison: CV, EV, and $\Delta CS$

| Measure | Demand used | Utility held constant | Direction of compensation |
|---------|-------------|----------------------|-----------------------------|
| $\Delta CS$ | Marshallian $x_1^*$ | Neither | Approximate |
| $CV$ | Hicksian $h_1(p, \bar{u}^0)$ | Old utility $\bar{u}^0$ | At new prices |
| $EV$ | Hicksian $h_1(p, \bar{u}^1)$ | New utility $\bar{u}^1$ | At old prices |

### Ordering for a Price Increase

For a **normal good** ($\partial x_1^*/\partial m > 0$), a price rise implies $\bar{u}^1 < \bar{u}^0$, so $h_1(\cdot, \bar{u}^0) > h_1(\cdot, \bar{u}^1)$ (higher utility → higher Hicksian demand), hence:

$$EV \leq \Delta CS \leq CV \leq 0 \quad \text{(all negative; price rise hurts consumer)}$$

Wait — if a price rise hurts: $CV > 0$ (compensation paid to consumer), $EV < 0$ (consumer pays to avoid). Re-sign convention: if we define all three as **welfare gains**:

$$CV \geq \Delta CS \geq EV \quad \text{for a price fall (welfare gain)}$$

$$CV \leq \Delta CS \leq EV \quad \text{for a price rise (welfare loss)}$$

For **inferior goods**, the ordering reverses.

**When are they equal?** For **quasi-linear preferences** ($u = v(x_1) + x_2$), there is no income effect, so $h_1 = x_1^*$ and $CV = EV = \Delta CS$.

## Deadweight Loss (DWL)

When a price distortion (tax, monopoly markup) raises price from $p^*$ to $p^T$:

- Consumer surplus falls by $\Delta CS$.
- Producer revenue / tax revenue partially offsets this.
- The **deadweight loss** is the portion of the welfare reduction not captured by any party:

$$DWL = \Delta CS - \text{Tax Revenue}$$

In competitive markets with a per-unit tax $t$ on good 1:

$$DWL \approx \frac{1}{2} t^2 \left|\frac{\partial x_1^*}{\partial p_1}\right|$$

(The triangle between supply and demand; second-order in the tax rate.)

## Money Metric Utility

The **money metric indirect utility function** at reference prices $p^0$:

$$\mu(p, m; p^0) = e(p^0, v(p, m))$$

This gives the minimum expenditure at reference prices $p^0$ to achieve the utility attained at $(p, m)$. It is an exact, ordinal welfare measure. Note:
- $EV = \mu(p^0, m; p^0) - \mu(p^1, m; p^0) = m - e(p^0, \bar{u}^1)$... wait, actually $EV = e(p^0, \bar{u}^1) - m$, sign depends on convention.

The key point: $e(p^0, v(p,m))$ preserves the same preference ordering as $v(p,m)$ for fixed $p^0$.

## Application: Tax Reform Analysis

Suppose government considers replacing a per-unit tax (distortionary) with a lump-sum tax (non-distortionary) raising equal revenue. Using EV:

- Per-unit tax: consumer's EV = $e(p^0, \bar{u}^{\text{tax}}) - m < 0$.
- Lump-sum tax: purely shifts budget line, so $\bar{u}^{\text{lump}} > \bar{u}^{\text{tax}}$ at same revenue.
- Therefore the lump-sum tax is **Pareto superior** — same revenue, higher consumer welfare.

## Related Concepts

- [[Expenditure_Minimization_and_Hicksian_Demand]] — CV and EV are expressed in terms of the expenditure function and Hicksian demands
- [[Indirect_Utility_Function_and_Roys_Identity]] — utility levels $\bar{u}^0, \bar{u}^1$ come from the indirect utility function
- [[Duality]] — the CV/EV framework exploits the full duality between $v$ and $e$
- [[Slutsky_Equation]] — the decomposition of price effects underlies the gap between CS, CV, and EV
- [[Income_and_Substitution_Effects]] — the income effect drives the wedge between Marshallian CS and Hicksian CV/EV
- [[Marshallian_Demand]] — CS is computed from uncompensated demand
