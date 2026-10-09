---
course: JEB104
topic: Endowment Economy and Trade
source: 00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_13_Buying_and_selling_Students.pdf
tags: [JEB104, microeconomics, endowment, net-demand, buying, selling, offer-curve, consumer-theory]
created: 2026-04-19
---

Parent: [[JEB104_Microeconomics_I_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_13_Buying_and_selling_Students.pdf]]
Related: [[Budget_Constraint]], [[Marshallian_Demand]], [[Slutsky_Equation]], [[Income_and_Substitution_Effects]], [[Labor_Supply]], [[Intertemporal_Choice]]

# Endowment Economy and Buying/Selling

## Setup: Endowment Budget Constraint

In many economic environments, income is not exogenously given but **derived from selling an endowment**. A consumer holds an initial endowment $(\omega_1, \omega_2)$ and faces prices $(p_1, p_2)$.

**Budget constraint:** The consumer can buy or sell goods, so the budget line passes through the endowment:

$$p_1 x_1 + p_2 x_2 = p_1 \omega_1 + p_2 \omega_2 = m$$

where $m = p_1 \omega_1 + p_2 \omega_2$ is **endowment income** (value of the endowment at market prices).

**Key property:** The budget line always passes through $(\omega_1, \omega_2)$, regardless of prices — the endowment is always affordable.

## Net Demand

- **Gross demand:** $x_i$ — total consumption of good $i$.
- **Net demand (net trade):** $z_i = x_i - \omega_i$ — quantity bought ($z_i > 0$) or sold ($z_i < 0$).

The budget constraint in terms of net demands:

$$p_1 z_1 + p_2 z_2 = 0$$

i.e., the value of net purchases equals the value of net sales — budget balance.

## Slutsky Equation with Endowments

When income is endogenous ($m = p \cdot \omega$), a change in $p_1$ affects **both** the budget line slope **and** endowment income. The total effect on demand decomposes as:

$$\frac{dx_1}{dp_1} = \underbrace{\frac{\partial h_1}{\partial p_1}}_{\text{SE} \leq 0} + \underbrace{(\omega_1 - x_1) \frac{\partial x_1^*}{\partial m}}_{\text{Endowment IE}}$$

**Derivation:** Differentiate $x_1^*(p_1, p_2, p_1 \omega_1 + p_2 \omega_2)$ w.r.t. $p_1$:

$$\frac{dx_1}{dp_1} = \frac{\partial x_1^*}{\partial p_1}\bigg|_m + \frac{\partial x_1^*}{\partial m} \cdot \omega_1$$

Using the standard Slutsky equation $\partial x_1^*/\partial p_1|_m = \partial h_1/\partial p_1 - x_1 \partial x_1^*/\partial m$:

$$\frac{dx_1}{dp_1} = \frac{\partial h_1}{\partial p_1} - x_1 \frac{\partial x_1^*}{\partial m} + \omega_1 \frac{\partial x_1^*}{\partial m} = \frac{\partial h_1}{\partial p_1} + (\omega_1 - x_1)\frac{\partial x_1^*}{\partial m}$$

**Interpretation:**
- If the consumer is a **net seller** ($\omega_1 > x_1$, so $z_1 < 0$): a rise in $p_1$ is a **terms-of-trade improvement** — endowment income rises. The endowment income effect is positive, potentially making the own-price response positive (consumer supplies more when their good becomes more valuable — like labour supply).
- If the consumer is a **net buyer** ($\omega_1 < x_1$): the endowment income effect is negative, standard outcome.

## Offer Curve

The **offer curve** (or trading curve) traces out the consumer's net demand $(z_1, z_2)$ as prices vary. It shows how much the consumer offers to trade across different relative prices.

- Starts at the endowment $(\omega_1, \omega_2)$ when prices equal the MRS.
- Traces through net buyer / net seller regions as $p_1/p_2$ changes.

The offer curve is fundamental in **general equilibrium** analysis — market clearing requires aggregate net demands to sum to zero.

## Price Changes and Regime Switching

A consumer may change from **net seller to net buyer** (or vice versa) as prices change. At the endowment:
- If $p_1/p_2 < |MRS|$ at $\omega$: the consumer wants to buy good 1 (net buyer).
- If $p_1/p_2 > |MRS|$ at $\omega$: the consumer wants to sell good 1 (net seller).

**Critical price:** $p_1^* / p_2 = |MRS(\omega_1, \omega_2)|$ — the consumer is just willing to consume the endowment without trade.

## Gains from Trade

The consumer is always **weakly better off** at any price $p \neq p^*$ (where $p^*$ is the endowment-optimal price):

$$v(p, p \cdot \omega) \geq v(p^*, p^* \cdot \omega)$$

**Proof:** At prices $p$, the consumer can always choose $x = \omega$ (costless by construction). If they choose a different bundle, revealed preference implies they prefer it. Hence opening markets (allowing trade) weakly improves welfare. $\blacksquare$

## Labour Supply as a Special Case

The **labour-leisure** model is an endowment economy with:
- Good 1: leisure $l$, endowment $T$ (time), price = wage $w$.
- Good 2: consumption $c$, price = 1.
- Earned income: $wL = w(T - l)$ where $L$ is hours worked.

Budget constraint: $c = w(T - l) + m_0$ where $m_0$ is non-labour income.

See [[Labor_Supply]] for full analysis.

## Intertemporal Budget Constraint

The intertemporal choice problem (periods 0 and 1, endowments $m_0, m_1$) is an endowment economy with:
- Good 1: present consumption $c_0$, price = 1.
- Good 2: future consumption $c_1$, price = $1/(1+r)$.

$$c_0 + \frac{c_1}{1+r} = m_0 + \frac{m_1}{1+r}$$

See [[Intertemporal_Choice]] for full analysis.

## Related Concepts

- [[Budget_Constraint]] — the standard budget constraint with exogenous income is a special case
- [[Marshallian_Demand]] — gross demand $x_i$ derived from the endowment-income UMP
- [[Slutsky_Equation]] — the modified Slutsky equation includes the endowment income effect
- [[Income_and_Substitution_Effects]] — the endowment IE replaces the standard IE when income is endogenous
- [[Labor_Supply]] — the labour-leisure model is the canonical endowment economy application
- [[Intertemporal_Choice]] — saving/borrowing as an endowment economy across time periods
