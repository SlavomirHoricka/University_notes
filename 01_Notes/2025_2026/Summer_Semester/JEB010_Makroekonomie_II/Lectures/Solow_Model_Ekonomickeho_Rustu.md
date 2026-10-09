---
course: JEB010
topic: Solowův model ekonomického růstu
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_11.pdf
tags: [JEB010, Solow, ekonomický-růst, stálý-stav, zlaté-pravidlo, konvergence]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_11.pdf]]
Related: [[01_Notes/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Teorie_Investic]], [[Hospodarska_Politika_a_Debata_Pravidel]]

# Solowův model ekonomického růstu

Solowův model (1956) vysvětluje dlouhodobý ekonomický růst prostřednictvím akumulace kapitálu a exogenního technologického pokroku. Je základem všech moderních modelů růstu.

## Základní model (bez populačního a technologického růstu)

### Assumptions

- Produkční funkce s konstantními výnosy z rozsahu: $Y = F(K;L)$
- $F(z \cdot K; z \cdot L) = z \cdot Y$ pro $z = 1/L$:

$$y = f(k) \qquad \text{kde } y = Y/L,\ k = K/L$$

- Poptávka: $y = c + i$; spotřební funkce: $c = (1-s) \cdot y$
- Z toho: $i = s \cdot y = s \cdot f(k)$

### Dynamika kapitálu

Absolutní změna kapitálu: $\Delta K = s \cdot F(K;L) - \delta \cdot K$

Přepis na pracovníka:
$$\boxed{\Delta k = s \cdot f(k) - \delta \cdot k}$$

### Stálý stav

Stálý stav definován podmínkou $\Delta k = 0$:

$$\boxed{s \cdot f(k^*) = \delta \cdot k^*}$$

**Konvergence:** Pro $k < k^*$: $s \cdot f(k) > \delta \cdot k \Rightarrow \Delta k > 0$ (ekonomika roste)  
Pro $k > k^*$: $s \cdot f(k) < \delta \cdot k \Rightarrow \Delta k < 0$ (ekonomika klesá)

### Determinanty $k^*$

- $\uparrow s$ → proporcionální posun křivky $s \cdot f(k)$ nahoru → $\uparrow k^*$; pozor: $c = (1-s) \cdot y$ nejprve klesá, pak roste
- $\downarrow \delta$ → plošší linie $\delta \cdot k$ → $\uparrow k^*$
- $\uparrow$ produkční funkce → $\uparrow k^*$

## Zlaté pravidlo stálého stavu

Hledáme míru úspor $s^{**}$ maximalizující spotřebu ve stálém stavu:

Ve stálém stavu: $i^* = s \cdot f(k^*) = \delta \cdot k^*$

$$c^* = y^* - i^* = f(k^*) - \delta \cdot k^*$$

**Maximalizační problém:**
$$\max_{k^*} \, c^* = f(k^*) - \delta \cdot k^*$$

**FOC:**
$$(c^*)' = f'(k^*) - \delta = 0 \Rightarrow \boxed{MPK = f'(k^{**}) = \delta}$$

*Zlaté pravidlo:* Optimální kapitálová zásoba je tam, kde mezní produkt kapitálu se rovná míře odpisování.

**Přechod na $k^{**}$:** Pokud $k^* < k^{**}$: nutno zvýšit $s$ → počáteční pokles spotřeby → poté vyšší trvalá spotřeba. Otázka: Je NPV(C) kladná? Závisí na diskontní sazbě.

## Přidání růstu populace

Pracovní síla roste konstantní mírou $n$: $\frac{dL/dt}{L} = n$

Dynamika kapitálu na pracovníka:

$$\frac{dk}{dt} = s \cdot f(k) - k \cdot (n + \delta)$$

**Stálý stav:**
$$\boxed{s \cdot f(k^*) = (n + \delta) \cdot k^*}$$

**Zlaté pravidlo:**
$$MPK = f'(k^{**}) = n + \delta$$

**Interpretace:** Populační růst podobný efektu jako depreciace — každý nový zaměstnanec musí být vybaven kapitálem → $\uparrow n \Rightarrow \downarrow k^* \Rightarrow \downarrow y^*$. Země s vysokým $n$ jsou chudé.

Ve stálém stavu: $K/L$ a $Y/L$ jsou konstantní → $K$ a $Y$ rostou tempem $n$.

## Přidání technologického růstu

Produkční funkce s **efektivní prací** $A \cdot L$ (kde $A$ = produktivita technologie):

$$Y = F(K; A \cdot L) \qquad \frac{dA/dt}{A} = g \text{ (exogenní)}$$

Redefinice na efektivního pracovníka: $y = Y/(A \cdot L)$, $k = K/(A \cdot L)$

$$\frac{dk}{dt} = s \cdot f(k) - k \cdot (n + \delta + g)$$

**Stálý stav:**
$$\boxed{s \cdot f(k^*) = (n + g + \delta) \cdot k^*}$$

**Zlaté pravidlo:**
$$MPK = f'(k^{**}) = n + g + \delta$$

**Interpretace:** Technologický růst má podobný efekt na $k^*$ jako $n$ nebo $\delta$ — paradoxně! (Každá nová jednotka technologie musí být vybavena kapitálem — ale $k$ je definován jinak!)

Ve stálém stavu: $k$ a $y$ konstantní → $K/L$ a $Y/L$ rostou tempem $g$ → $K$ a $Y$ rostou tempem $(n+g)$.

## Souhrn Solowova modelu

| | $\Delta k$ | $\Delta y$ | $\Delta(K/L)$ | $\Delta(Y/L)$ | $\Delta K$ | $\Delta Y$ |
|---|---|---|---|---|---|---|
| $n=0$, $g=0$ | 0 | 0 | 0 | 0 | 0 | 0 |
| $n=n$, $g=0$ | 0 | 0 | 0 | 0 | $n$ | $n$ |
| $n=n$, $g=g$ | 0 | 0 | $g$ | $g$ | $n+g$ | $n+g$ |

## Solowův reziduál (Total Factor Productivity)

Pro $Y = K^\alpha L^{1-\alpha}$: $\Delta Y = MPK \cdot \Delta K + MPL \cdot \Delta L$

$$\frac{\Delta Y}{Y} = \alpha \cdot \frac{\Delta K}{K} + (1-\alpha) \cdot \frac{\Delta L}{L}$$

**TFP (Solow residual):**
$$\boxed{\frac{\Delta A}{A} = \frac{\Delta Y}{Y} - \alpha \cdot \frac{\Delta K}{K} - (1-\alpha) \cdot \frac{\Delta L}{L}}$$

TFP zachycuje technologický pokrok, kvalitu pracovní síly, institucionální faktory atd.

## Modifikace Solowova modelu

1. **Endogenizace úspor:** Optimalizující agenti (Ramsey model)
2. **Endogenizace technologie:** AK model, Romer model (R&D)
3. **Lidský kapitál:** Rozšířený Solow (Mankiw-Romer-Weil) — lidský kapitál jako třetí výrobní faktor

## Empirické implikace — konvergence

**Bezpodmínečná konvergence:** Chudší ekonomiky rostou rychleji (podobné $s$, $n$, technologie) — platí v rámci homogenních skupin (OECD, EU regiony)

**Podmínečná konvergence:** Ekonomiky konvergují ke svým vlastním $k^*$ (různé charakteristiky) — potvrzena empiricky

Historická evidence: Japonsko 8,2 %, Německo 5,7 %, USA 2,2 % (1948–1972); Asijští tygři, BRICS vs. PIIGS
