---
course: "JEB009"
topic: "Model AD-AS"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_9.pdf"
tags: [JEB009, makroekonomie, AD-AS, agregátní-poptávka, agregátní-nabídka, fiskální-politika]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_9.pdf]]
Related: [[IS_LM_Model]], [[AS_Modely_Agregátní_Nabídky]], [[Neoklasicky_Model]]

# Model AD-AS

## Motivace — uvolnění předpokladu fixní cenové hladiny

IS-LM model předpokládá $P = \text{const.}$ (tedy $i = r$, $\pi^e = 0$). Model AD-AS toto uvolňuje:
- Umožňuje analyzovat dopady fiskální a monetární politiky na **cenovou hladinu** i výstup.
- Metodologicky problematický bod: IS-LM je formálně founded na $P = \text{const.}$.

## Křivka AD — odvození z IS-LM

**Křivka AD:** Kombinace $(P, Y)$, pro které jsou trh zboží i trh peněz v rovnováze (IS-LM v rovnováze) při daném $P$.

**Mechanismus:** $P \downarrow \implies M/P \uparrow \implies$ totéž jako monetární expanze $\implies Y \uparrow$

Z redukovaného tvaru IS-LM:
$$Y^* = \alpha_G \cdot A + \alpha_M \cdot \frac{M}{P} = \alpha_G \cdot A + \frac{\mu_t b}{h + \mu_t bk} \cdot \frac{M}{P}$$

Invertujeme:
$$P = \frac{\alpha_M \cdot M}{Y - \alpha_G \cdot A}$$

Křivka AD je tedy **klesající** v prostoru $(Y, P)$.

### Vysvětlení klesajícího sklonu AD

1. **Cambridgský efekt (neoklasický):** $P \uparrow \implies M/P \downarrow \implies$ klesá poptávka.
2. **Keynesův efekt:** $P \uparrow \implies M/P \downarrow \implies$ prodej obligací $\implies P_B \downarrow, i \uparrow \implies I \downarrow \implies$ AD $\downarrow$

> **Pozor:** AD křivka se liší od mikroekonomické nabídkové/poptávkové křivky! Mikroekonomicky $P \uparrow$ mění relativní ceny a vede k substituci; v makroekonomii $P$ je **absolutní cenová hladina**.

## Reakce AD na hospodářskopolitické šoky

### Fiskální expanze ($\Delta G > 0$)

Pro každé $P$: $IS$ se posune doprava o $\mu_t \cdot \Delta G$.

$$\Delta Y|_{\text{každé }P} = \alpha_G \cdot \Delta G$$

Výsledek: **Paralelní posun AD doprava** o $\alpha_G \cdot \Delta G$.

### Monetární expanze ($\Delta M > 0$)

Pro každé $P$: $LM$ se posune doprava o $\frac{\Delta M/P}{k}$.

$$\Delta Y|_{\text{každé }P} = \alpha_M \cdot \frac{\Delta M}{P}$$

Výsledek: Posun AD doprava — **nová křivka je plošší** (efekt $\Delta M$ na $Y$ je větší při nižším $P$).

## Sklon křivky AD

$$\frac{dP}{dY} = -\frac{\alpha_M \cdot M}{(Y - \alpha_G A)^2} < 0$$

| Parametr | Efekt na sklon AD |
|---|---|
| $\mu_t \uparrow$ | AD plošší |
| $b \uparrow$ | AD plošší |
| $k \downarrow$ | AD plošší |
| $h \uparrow$ | AD strmější |

## Křivka AS v modelu AD-AS

Jak bylo odvozeno v [[AS_Modely_Agregátní_Nabídky]]:

**Krátkodobá křivka AS (SRAS):**
$$Y = Y^* + \alpha(P - P^e)$$

**Dlouhodobá křivka AS (LRAS):** Vertikální na $Y = Y^P$.

**Typy podle tvaru:**
- $AS_{NEOCL}$: Vertikální (klasická ekonomika)
- $AS_{KEYNES}$: Horizontální (raná keynesiánská ekonomika)
- $AS_{PHILIPS}$: Kladný sklon (Phillipsova křivka)

## Rovnováha a hospodářský cyklus

### Krátkodobá a dlouhodobá rovnováha

**Krátkodobá (SR) rovnováha:** Průsečík AD a SRAS (obecně $Y \neq Y^P$).

**Dlouhodobá (LR) rovnováha:** Průsečík AD a LRAS ($Y = Y^P$) — $P^e$ se adaptuje.

### Dynamika fiskální expanze

1. **Počáteční stav:** $E_0 = (Y^P, P_0)$ — LRAS, SRAS₀, AD₁ v průsečíku.
2. **Krátkodobý efekt** (SR): AD₁ → AD₂ posunem $\Delta G$; SRAS₀ fixní → $E_1 = (Y_1 > Y^P, P_1 > P_0)$.
3. **Dlouhodobý efekt** (LR): $Y_1 > Y^P \implies$ inflační tlak $\implies P^e \uparrow \implies$ SRAS₀ → SRAS₁ (posun nahoru) → $E_2 = (Y^P, P_2 > P_1)$.

**Závěr long-run:** Fiskální expanze zvyšuje P, ale ne $Y$ v dlouhém období — plné vytlačování a inflační spiral.

## Speciální případy (pasti)

### Past likvidity ($h \to \infty$)

LM křivka horizontální: $LM(P_1) = LM(P_2) \implies$ AD nerespektuje pokles $P$ → AD **vertikální**.

$$\text{AD vertikální: Monetární expanze nemá efekt}$$

### Past investic ($b \to 0$)

IS křivka vertikální: Pokles $P$ neovlivní investice → AD méně reaktivní na $P$.

## Sklon AD v souhrnném přehledu

| IS | LM | AD |
|---|---|---|
| $\mu_t \uparrow$ (plošší IS) | — | plošší |
| $b \uparrow$ (plošší IS) | — | plošší |
| — | $k \uparrow$ (strmější LM) | strmější |
| — | $h \uparrow$ (plošší LM) | strmější |

## Kritika modelu IS-LM (a zprostředkovaně AS-AD)

**Ze strany neoklasické školy:**
- Chybějící mikroekonomické základy.
- Chybějící racionální očekávání.
- Neodlišování $i$ a $r$ ($\pi^e = 0$).

**Ze strany post-keynesiánské školy:**
- IS-LM smíchává Keynese s neoklasika.
- Oddělení trhu peněz a zboží je v rozporu s Keynesovou Obecnou teorií.
- Kritika rovnovážného přístupu; modely nerovnováhy.
