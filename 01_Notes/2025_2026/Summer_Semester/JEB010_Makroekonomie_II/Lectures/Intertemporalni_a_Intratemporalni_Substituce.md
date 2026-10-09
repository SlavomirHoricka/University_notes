---
course: JEB010
topic: Intertemporální a intratemporální substituce
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_3_&_4.pdf
tags: [JEB010, intertemporální-substituce, Fisher-model, spotřeba, úspory]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_3_&_4.pdf]]
Related: [[Teorie_Realnych_Hospodarskych_Cyklu]], [[Barro_Ricardanska_Ekvivalence]], [[Teorie_Spotreby]]

# Intertemporální a intratemporální substituce

## Fisherův model intertemporální substituce

Spotřebitel si vybírá spotřebu $c_1$ a $c_2$ přes dvě období. Bez počátečního ani konečného dluhu:

$$c_1 + \frac{c_2}{1+r} = y_1 + \frac{y_2}{1+r} + W$$

kde $r$ je reálná úroková míra a $W$ je počáteční bohatství. Sklon rozpočtové přímky je $-(1+r)$.

### Optimum

$$\frac{MU_{c_1}}{MU_{c_2}} = 1 + r$$

Pokud $r$ roste: substituční efekt ($c_1$ relativně dražší → $\downarrow c_1$, $\uparrow c_2$) a důchodový efekt (závisí na tom, zda agent je věřitel nebo dlužník).

### Likviditní omezení

Bez finančního trhu agent nemůže půjčit si na základě budoucích příjmů. Rozpočtové omezení se zpřísnuje:

$$c_t \leq y_t$$

Efekt v krátkém období: $\Delta C < \Delta Y \Rightarrow MPC < 1$ (vysvětlení Kuznetzovy hádanky — viz [[Teorie_Spotreby]]).

V dlouhém období likviditní omezení neaktivní: $\Delta C = \Delta Y \Rightarrow MPC = 1$.

Rozšířené BC (s obligacemi):

$$c_t + \frac{c_{t+1}}{1+i} = y_t + \frac{y_{t+1}}{1+i} + \frac{b_{t-1}(1+i)}{P} - \frac{b_{t+1}}{P(1+i)}$$

## Vládní intertemporální rozpočtové omezení

Vláda čelí analogickému omezení:

$$G_1 + \frac{G_2}{1+r} + D_g(1+r) = TA_1 + \frac{TA_2}{1+r}$$

kde $D_g$ je počáteční veřejný dluh, $G$ jsou výdaje a $TA$ daňové příjmy.

### Podmínka fiskální udržitelnosti

Z podmínky $\Delta D_g / dt = G - TA + D_g \cdot r$:

**Bez seignorage:**
$$TA - G = (r - g) \cdot D_g$$

kde $g$ je růst reálného HDP. Pokud $r > g$ a primární saldo $(TA-G) < (r-g)D_g$, dluh exploduje.

**S možností monetizace dluhu:**
$$TA - G = D_g(r - g - [\pi - \pi^e]) - \frac{\Delta MB}{P}$$

Maastrichtské kritérium: $D_g/Y \leq 60\%$ odpovídá situaci, kdy při $r - g = 3\%$ je deficit $\leq 3\%$ HDP udržitelný.

## Barro-Ricardánská ekvivalence

Viz [[Barro_Ricardanska_Ekvivalence]].

## Intratemporální substituce

Substituce mezi spotřebou $c$ a volným časem $L = 1 - l$ (kde $l$ = práce). Podmínka optimality:

$$\frac{MU_{c}}{MU_{L}} = \frac{1}{MPL} = \frac{W}{P}$$

Agent je lhostejný mezi pracovní a leisurovou alokací na hranici indiferenční křivky s produkční funkcí.

**Posun produkční funkce:**

| Typ posunu | Efekt na $c$ | Efekt na $l$ |
|---|---|---|
| Paralelní ↑ (důchodový efekt) | ↑ | ↓ (volný čas normální statek) |
| Proporcionální ↑ — čistý substituční efekt | ↑ | ↑ (vyšší MPL za každé $l$) |
| Proporcionální ↑ — celkový efekt | ↑ | ? (substituční vs. důchodový) |

**Důchodový efekt:** ↑$c$, ↓$l$ (volný čas normální)  
**Substituční efekt:** ↑$c$, ↑$l$ (dražší volný čas → více práce)  
**Celkový efekt proporcionálního posunu:** ↑$c$, ?$l$
