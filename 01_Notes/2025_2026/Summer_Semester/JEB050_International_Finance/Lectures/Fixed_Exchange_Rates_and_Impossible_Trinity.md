---
course: JEB050
topic: Fixed Exchange Rates, Monetary Policy Impotence, Devaluation, and the Impossible Trinity
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_8/IF_2026_lecture_9_large_slides.pdf
tags: [JEB050, fixed-exchange-rate, impossible-trinity, sterilization, devaluation, monetary-policy]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_8/IF_2026_lecture_9_large_slides.pdf]]
Related: [[DD_AA_Model]], [[Policy_in_DD_AA]], [[UIP_and_CIP]]

# Fixed Exchange Rates, Monetary Policy Impotence, Devaluation, and the Impossible Trinity

## Fixed Exchange Rate Mechanics

Under a **fixed (pegged) exchange rate**, the central bank commits to maintain $E = \bar{E}$ by intervening in the foreign exchange market:

- **Depreciation pressure** ($E$ tends to rise): CB sells foreign currency (FC) and buys domestic currency → domestic money supply contracts
- **Appreciation pressure** ($E$ tends to fall): CB buys FC and sells domestic currency → domestic money supply expands

In the [[DD_AA_Model]] framework, the fixed ER is represented by a **horizontal line** at $E = \bar{E}$. Equilibrium output is determined by the intersection of the DD curve and this horizontal line (the AA curve must also pass through the intersection, which is ensured by the CB's money supply adjustments).

## Monetary Policy Impotence Under Fixed ER

**Attempt:** CB tries to increase $M^s$ (expansionary monetary policy).

**Sequence of events:**
1. $M^s \uparrow$ → excess money supply → $R \downarrow$
2. $R \downarrow$ → capital outflow → domestic currency faces **depreciation pressure** ($E$ tends to rise above $\bar{E}$)
3. CB intervenes: **sells FC, buys domestic currency** (unsterilized intervention)
4. Buying domestic currency → $M^s \downarrow$ — the initial expansion is reversed
5. The AA curve returns to its original position

**Conclusion:** Under a fixed exchange rate with perfect capital mobility, **monetary policy is completely impotent**. Any attempt to change the money supply is automatically reversed by the intervention required to defend the peg.

**Diagram:** AA attempts to shift to AA' (right) but is immediately pulled back to AA by CB intervention; the horizontal $\bar{E}$ line and DD curve intersection is unchanged.

### Sterilized vs. Unsterilized Intervention

| | Sterilized | Unsterilized |
|---|---|---|
| **Definition** | CB offsets the effect of FX intervention on domestic money supply by open market operations (e.g., sell domestic bonds to absorb the new domestic money) | No offsetting operation; money supply changes with intervention |
| **Effect on $M^s$** | Unchanged | Changes with intervention |
| **Effect on exchange rate** | **Not sustainable** if capital is perfectly mobile (sterilization is temporary) | Immediately restores equilibrium |
| **Mechanism** | Signals CB intent; may work via portfolio balance channel | Standard mechanism |

## Fiscal Policy Effectiveness Under Fixed ER

**Fiscal expansion** ($G \uparrow$): 
1. $Y \uparrow$ → money demand $L\uparrow$ → $R\uparrow$ 
2. Higher $R$ → capital inflow → appreciation pressure ($E$ tends to fall below $\bar{E}$)
3. CB intervenes: **buys FC, sells domestic currency** → $M^s \uparrow$
4. Money supply increases until $R$ returns to $R^*$ (equal to foreign rate)
5. AA shifts up; new equilibrium at higher $Y$ and same $\bar{E}$

**Conclusion:** Under fixed ER, fiscal policy is **highly effective** — the CB's accommodating money supply expansion amplifies the fiscal stimulus. There is **no exchange rate crowding out** (because the exchange rate is pegged), and no interest rate crowding out (CB supplies the money needed).

## Devaluation

A **devaluation** is a deliberate change in the pegged rate from $\bar{E}_0$ to $\bar{E}_1 > \bar{E}_0$ (domestic currency weakened by CB decision):

**Effects:**
1. Nominal $E$ rises → $EP^*/P$ rises → $CA \uparrow$ → $D \uparrow$ → $Y \uparrow$ (move along DD)
2. The new equilibrium at $\bar{E}_1$ has **higher output** ($Y_2 > Y_0$)
3. Higher $Y$ raises money demand → excess money demand → $R$ would rise above $R^*$
4. CB intervenes: **buys FC** → $M^s \uparrow$ → AA shifts up to the new $\bar{E}_1$ level
5. Final equilibrium: $Y_2 > Y_0$, $E = \bar{E}_1$

In the DD-AA diagram: the fixed ER line shifts from $\bar{E}_0$ to $\bar{E}_1$; the new intersection with DD is at higher $Y$; AA accommodates by shifting up.

**Note:** If the Marshall-Lerner condition $\eta_x + \eta_m > 1$ holds (see [[Marshall_Lerner_Condition_and_Swan_Diagram]]), the devaluation does improve the CA in the long run. Short-run: J-curve effect may mean CA worsens first.

## The Impossible Trinity (Policy Trilemma)

The **Impossible Trinity** (also: policy trilemma or Mundell trilemma) states that a country **cannot simultaneously maintain all three of**:

1. **Fixed exchange rate**
2. **Free capital mobility** (full convertibility)
3. **Monetary policy autonomy** (independent interest rate setting)

**Proof sketch:** 
- With free capital mobility, $R$ must equal $R^*$ (UIP, risk-neutral) — if $R \neq R^*$, capital flows instantaneously drive $E$ away from the peg.
- With a fixed $E$, the CB cannot change $R$ (since changing $M^s$ would break the peg, as shown above).
- Therefore, with both fixed $E$ and free capital mobility, monetary autonomy is lost.

### Real-World Responses — Choosing Two of Three

| Country/regime | Fixed ER | Capital mobility | Monetary autonomy |
|---|---|---|---|
| **Eurozone members** | ✓ (sharing euro) | ✓ | ✗ (ECB sets policy) |
| **China (historically)** | ✓ (managed peg) | ✗ (capital controls) | ✓ |
| **USA, UK, Czech Rep.** | ✗ (floating) | ✓ | ✓ |
| **Bretton Woods 1944–71** | ✓ | ✗ (limited) | ✓ (limited) |

### Intermediate Solutions

The trilemma describes extreme corners. In practice:
- **Managed float**: partial exchange rate stability + partial capital controls + partial monetary autonomy
- **Currency board** (e.g. Bulgaria, pre-euro Estonia): fixed + full mobility, zero monetary autonomy (CB passively backs every unit of domestic money with FC reserves)
- **ERM II** (Czech Republic's path to euro): semi-fixed within ±15% bands

**Czech Republic context:** The Czech Republic currently floats (monetary autonomy + capital mobility). To adopt the euro, it would need to sacrifice monetary autonomy in exchange for full fixed ER. The CNB's FX commitment of 2013–2017 (floor at 27 CZK/EUR) was an example of temporarily choosing fixed ER + capital mobility, sacrificing short-term monetary autonomy.
