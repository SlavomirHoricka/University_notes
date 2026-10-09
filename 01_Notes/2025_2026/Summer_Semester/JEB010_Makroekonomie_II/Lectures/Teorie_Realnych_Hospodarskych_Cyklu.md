---
course: JEB010
topic: Teorie reálných hospodářských cyklů (RBC)
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_3_&_4.pdf
tags: [JEB010, RBC, reálné-hospodářské-cykly, intertemporální-substituce, produkční-funkce]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_3_&_4.pdf]]
Related: [[Intertemporalni_a_Intratemporalni_Substituce]], [[Barro_Ricardanska_Ekvivalence]], [[Nova_Keynesianska_Ekonomie]]

# Teorie reálných hospodářských cyklů (RBC)

RBC teorie (Kydland, Prescott, 1982) vysvětluje hospodářské cykly jako **optimální reakce racionálních agentů na reálné (technologické) šoky**, bez potřeby nominálních rigidit nebo peněžní nestability. Je přímou kritikou IS-LM modelu.

## Základní optimalizační problém

Ekonomika sestává z reprezentativního agenta (Robinson Crusoe), který maximalizuje intertemporální užitek:

$$\max \, u(c_1, c_2, L_1, L_2)$$

za intertemporální rozpočtové omezení:

$$c_1 + \frac{c_2}{1+r} \leq f_1(l_1) + \frac{f_2(l_2)}{1+r} + W$$

kde $L_t = 1 - l_t$ je volný čas, $l_t$ je práce, $f_t(l_t)$ je produkční funkce a $W$ je počáteční bohatství.

### Lagrangián a podmínky prvního řádu

$$\Lambda = u(c_1, c_2, L_1, L_2) - \lambda \cdot \left(c_1 + \frac{c_2}{1+r} - f_1(l_1) - \frac{f_2(l_2)}{1+r} - W\right)$$

FOC a jejich podíly:

| Poměr FOC | Ekonomický obsah |
|---|---|
| $\dfrac{MU_{C1}}{MU_{C2}} = 1+r$ | Intertemporální substituce spotřeby |
| $\dfrac{MU_{C1}}{MU_{L1}} = \dfrac{1}{MPL_1}$ | Intratemporální substituce (c vs. volný čas, obd. 1) |
| $\dfrac{MU_{C2}}{MU_{L2}} = \dfrac{1}{MPL_2}$ | Intratemporální substituce (obd. 2) |
| $\dfrac{MU_{L1}}{MU_{L2}} = MPL_1 \cdot (1+r)$ | Intertemporální substituce volného času |

## Intratemporální substituce

Substituce mezi spotřebou $c$ a volným časem $L$ (kde $L = 1 - l$, $l$ = práce):

**Paralelní posun produkční funkce (důchodový efekt):**
- $MPL$ je $\forall l$ stejný → $\uparrow c$, $\downarrow l$ (práce klesá — volný čas je normální statek)

**Proporcionální posun produkční funkce:**
- Čistý substituční efekt ($\uparrow MPL \Rightarrow \uparrow l \Rightarrow \uparrow c$, $\uparrow l$)
- Celkový efekt: důchodový ($\uparrow c$, $\downarrow l$) + substituční ($\uparrow c$, $\uparrow l$) = $\uparrow c$, ?$l$

## Změny v produkční funkci — 4 scénáře

### A) Permanentní paralelní posun nahoru
- $MPL$ se v obou obdobích nemění
- $\uparrow y_1, \uparrow y_2 \Rightarrow \uparrow W \Rightarrow \uparrow c_1, \uparrow c_2, \downarrow l_1, \downarrow l_2$
- $mpc \to 1$, $mps \to 0$

### B) Dočasný paralelní posun (1. období)
- Domácnosti rozdělí příjem mezi obě období; $MPL$ se nemění v žádném období
- $\uparrow c_1, \uparrow c_2, \downarrow l_1, \downarrow l_2$; $\uparrow y_1$ ($\downarrow l_1$ nepřeváží $\uparrow y_1$), $\downarrow y_2$ (díky $\downarrow l_2$)
- $mpc \to 1/2$, $mps \to 1/2$

### C) Permanentní proporcionální posun (pouze substituční efekt)
- $\uparrow MPL$ v obou obdobích $\Rightarrow \uparrow l_1, \uparrow l_2 \Rightarrow \uparrow y_1, \uparrow y_2$
- Intertemporální efekt omezený (stejný nárůst $MPL$ v obou obdobích)

### D) Dočasný proporcionální posun (1. období — čistý substituční efekt)
- $\uparrow MPL_1 \Rightarrow \uparrow l_1 \Rightarrow \uparrow y_1, \uparrow c_1$, ale $\uparrow y_1 > \uparrow c_1$ (intertemporální substituce spotřeby)
- Volný čas v 1. období relativně dražší → intertemporální substituce volného času: $\downarrow l_2 \Rightarrow \downarrow y_2, \uparrow c_2$

## Trh zboží a trh peněz

### Trh zboží (vyčišťující veličina: úroková míra $i$)

Podmínky rovnováhy: $C = Y$ nebo $Y_D(i,...) = Y_S(i,...)$

1. $\uparrow i \Rightarrow$ intertemporální substituce: $\downarrow c$, $\uparrow l \Rightarrow \uparrow y$ (pohyb po $Y_S$)
2. $\uparrow W$ (důchodový efekt) $\Rightarrow \uparrow c$ (tedy $\uparrow Y_D$), $\uparrow l$ omezí původní $\uparrow Y_S$
3. Substituční efekt ze změn $MPL$: $\uparrow l \Rightarrow \uparrow y, \uparrow Y_S$; $\uparrow c \Rightarrow \uparrow Y_D$ ale $\uparrow Y_S > \uparrow Y_D$

### Trh peněz

$$M_S = P \cdot \frac{M_D}{P}(Y, i, tc)$$

Znaky vlivu proměnných: $Y(+)$, $i(-)$, $tc(+)$.

Peněžní trh pasivně „vyčišťuje" přes $P$ — důchod a úroková míra jsou určeny na trhu zboží.

## Walrasův zákon trhů

Pro každou domácnost $i$:

$$y_1^i + \frac{b_0^i(1+i)}{P} + \frac{m_0^i}{P} = c_1^i + \frac{b_1^i}{P} + \frac{m_1^i}{P}$$

Po agregaci a přeskupení (s $B_0 = 0$):

$$\underbrace{(C_1 - Y_1)}_{\text{trh zboží}} + \underbrace{\left(\frac{M_1}{P} - \frac{M_0}{P}\right)}_{\text{trh peněz}} + \underbrace{\frac{B_1}{P}}_{\text{trh obligací}} = 0$$

**Walrasův zákon:** Pokud 2 ze 3 podmínek agregátní konzistence platí (i) $C=Y$, ii) $B=0$, iii) $M_S=M_D$), platí automaticky i třetí.

## Kritika RBC a empirická výzva

Hlavní problém RBC teorie: predikuje **procyklický pohyb práce** (za recese by lidé měli více pracovat, protože je $MPL$ dočasně nízké — zlevňuje volný čas). Empiricky však práce klesá v recesích (proticyklická).

Možné řešení: dočasný $\downarrow MPL \Rightarrow \downarrow l$ (větší posun $Y_S$) — vysvětlení přes dočasné snížení produktivity.
