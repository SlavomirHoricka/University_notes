---
course: JEB010
topic: Očekávání v makroekonomii
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_1.pdf
tags: [JEB010, makroekonomie, očekávání, racionální-očekávání, adaptivní-očekávání]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_1.pdf]]
Related: [[Modely_Agregatni_Nabidky_AS]], [[Model_DAD_DAS]], [[Teorie_Spotreby]]

# Očekávání v makroekonomii

Očekávání jsou klíčovým prvkem moderní makroekonomické teorie, protože ekonomické subjekty přijímají rozhodnutí na základě svých předpovědí o budoucím vývoji proměnných (cen, příjmů, úrokových sazeb). Způsob formování očekávání zásadně ovlivňuje účinnost hospodářské politiky.

## Typy očekávání

### 1. Statická očekávání

Nejjednodušší forma: subjekt očekává, že příští hodnota proměnné bude totožná s hodnotou aktuální.

$$p_t^{e_{t-1}} = p_{t-1}$$

**Implikace:** Model nabídky a poptávky s tržní rovnováhou:

$$x_t^d = a - b \cdot p_t + u_t \qquad (\text{poptávka})$$
$$x_t^s = c + d \cdot p_t^{e_{t-1}} + v_t \qquad (\text{nabídka})$$

Rovnováha při statických očekáváních ($p_t^e = p_{t-1}$) vede k tzv. pavoukovému efektu (*cobweb model*) — cena osciluje kolem rovnováhy. Stabilita závisí na poměru sklonů křivek nabídky a poptávky: $|d/b| < 1$ → konvergence; $|d/b| > 1$ → divergence.

### 2. Adaptivní očekávání

Ekonomické subjekty aktualizují svá očekávání na základě chyby z minulého období:

$$p_t^{e_{t-1}} = p_{t-1} + \Theta \cdot (p_{t-1}^{e_{t-2}} - p_{t-1}), \qquad \Theta \in [0;1]$$

Alternativní zápis:

$$p_t^{e_{t-1}} = \Theta \cdot p_{t-1}^{e_{t-2}} + (1-\Theta) \cdot p_{t-1}$$

**Speciální případy:**
- $\Theta = 0$: statická očekávání ($p_t^e = p_{t-1}$)
- $\Theta = 1$: konstantní očekávání (ignoruje aktuální informace)

**Problém:** Adaptivní očekávání jsou systematicky chybná v obdobích trendového vývoje (inflační spirála): pokud ceny trvale rostou, subjekty chybu systematicky podceňují.

### 3. Racionální očekávání (John Muth, 1961)

Subjekty využívají všechny dostupné informace efektivně — jejich očekávání jsou podmíněný střední hodnota proměnné $X$ při informační množině $I_{t-1}$:

$$X_t^{e_{t-1}} = E(X \mid I_{t-1})$$

Pro diskrétní rozdělení:
$$X_t^{e_{t-1}} = \sum_i p_i \cdot X_i$$

Pro spojité rozdělení:
$$X_t^{e_{t-1}} = \int X \cdot f(X) \, dX$$

#### Vlastnosti racionálních očekávání

1. **Nulová střední chyba:** $E(X_t - X_t^{e_{t-1}}) = 0$ — systematické chyby jsou nemožné
2. **Ortogonalita:** Chyba předpovědi $\varepsilon_t = X_t - X_t^{e_{t-1}}$ je nekorelovaná se všemi informacemi dostupnými v čase $t-1$
3. **Zákon iterovaných očekávání:** $E_{t-2}(E_{t-1}(X_t)) = E_{t-2}(X_t)$

**Politická implikace:** Systémová (předvídatelná) hospodářská politika má na reálné proměnné nulový efekt (*Lucas critique*) — účinek přichází pouze ze šokového, nepředvídaného komponenty politiky.

## Měření očekávání v praxi

| Metoda | Příklad |
|---|---|
| Futures trhy | Termínová cena ropy jako predikce spotové ceny |
| Fisherova rovnice | $\pi^e \approx i_{FIX} - i_{FLOAT}$ (rozdíl fixních a plovoucích výnosů obligací) |
| Průzkumy | Consensus Forecast, průzkumy firem a domácností |
| Ceny aktiv | Akciové trhy jako leading indicator |

### Fisherova rovnice pro měření inflačních očekávání

Z Fisherovy rovnice $i \approx r + \pi^e$:

$$\pi^e \approx i_{FIX} - i_{FLOAT}$$

kde $i_{FIX}$ je výnos nominální (fixní) obligace a $i_{FLOAT}$ výnos indexované (plovoucí) obligace. Tento rozdíl (break-even inflation) přímo odráží tržní inflační očekávání.

## Srovnání typů očekávání

| Vlastnost | Statická | Adaptivní | Racionální |
|---|---|---|---|
| Využití informací | Pouze $p_{t-1}$ | Vážený průměr minulosti | Všechny dostupné informace |
| Systematická chyba | Ano (v trendech) | Ano (v trendech) | Ne |
| Nákladnost | Nulová | Nízká | Vysoká (modelování) |
| Politická efektivita | Vysoká | Střední | Nulová (Lucas) |
