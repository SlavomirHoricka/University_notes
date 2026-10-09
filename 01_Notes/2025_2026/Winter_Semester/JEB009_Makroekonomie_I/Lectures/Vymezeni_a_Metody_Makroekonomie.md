---
course: "JEB009"
topic: "Vymezení a metody makroekonomie"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_1_3.pdf"
tags: [JEB009, makroekonomie, metodologie, hospodářský-cyklus]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_1_3.pdf]]
Related: [[Neoklasicky_Model]], [[Keynesianska_Ekonomie_a_Model_Duveru_Vydaje]], [[Mereni_HDP]], [[Solow_Model]]

# Vymezení a metody makroekonomie

## Definice

**Makroekonomie** je ta část ekonomické teorie, která se věnuje analýze ekonomiky jako celku, případně jejích hlavních částí (sektorů). Popisuje vývoj na různých trzích (zboží a služeb, práce, peněžní trhy, devizové trhy…) a pro tento popis využívá různé makroekonomické agregáty (HDP, ceny, nezaměstnanost, bilance zahraničního obchodu…) a zkoumá vztahy mezi nimi.

## Proč studovat makroekonomii?

Makroekonomie má přímý vztah ke dvěma klíčovým oblastem:

1. **Hospodářské politiky** – fiskální a monetární politika. Makroekonomie poskytuje teoretické zázemí pro opatření hospodářské politiky, prognózy dopadů a zdroj dat.
2. **Finanční trhy** – makroekonomické veličiny (úrokové míry, devizový kurz, HDP) jsou klíčové pro vývoj na trzích akcií, obligací a deviz. Téma finanční stability (Financial Stability Reports centrálních bank) trvale nabývá na důležitosti.

## Nástroje a metodologie

### Deduktivní vs. induktivní přístup
- **Deduktivní (mikroekonomický):** Odvozování makrochování z optimalizace jednotlivých agentů (reprezentativní domácnost/firma). Problém agregace.
- **Induktivní (empirický/ekonometrický):** Formulace „zákonů" z pozorovaných dat (Okunův zákon, Phillipsova křivka), časové řady, průřezová analýza, panelová data.

### Architektura makroekonomických modelů

Obecný tvar:

$$\text{Exogenní proměnné} \xrightarrow{\text{MODEL (s předpoklady)}} \text{Endogenní proměnné}$$

Klíčové vlastnosti modelů:
1. **Předpoklady** závisejí na přístupu (neoklasika vs. keynesiánství).
2. Předpoklad *ceteris paribus*.
3. Modely hledají **ekvilibrium** — stav, kdy jsou endogenní veličiny konstantní nebo stabilně rostoucí, resp. kdy se trhy vyčistí ($S = D$).
4. **Stabilitaequilibria** — nutno ověřit, zda je ustálený stav stabilní.
5. **Násobná ekvilibria** — výsledek závisí na počátečních podmínkách.

### Čas v ekonomických modelech

| Typ analýzy | Popis |
|---|---|
| **Statická analýza** | Porovnání jednoho rovnovážného stavu |
| **Komparativní statika** | Porovnání dvou rovnovážných stavů ($E_1$ vs. $E_2$) |
| **Plná dynamická analýza** | Sledování přechodu mezi stavy v čase |
| **Krátké vs. dlouhé období** | Odlišení pružnosti cen; krátké: strnulé ceny, dlouhé: flexibilní |

### Analýza ex post a ex ante
- **Ex post:** Realizované hodnoty (účetní identita).
- **Ex ante:** Plánované/očekávané hodnoty; ex-ante nerovnováha vede k přizpůsobení trhu.

## Historie makroekonomické teorie

| Škola | Hlavní představitelé | Klíčové přínosy |
|---|---|---|
| Klasická / neoklasická | Smith, Ricardo, Malthus; Walras, Jevons, Menger | Trhy se vyčišťují, Sayův zákon |
| Monetarismus | Milton Friedman (od 50. let) | Kvantitativní teorie peněz, monetaristické pravidlo |
| Nová klasická makro (RBC) | Lucas, Barro (od 70. let) | Racionální očekávání, reálné hospodářské cykly |
| Původní keynesiánství | Keynes (1936) | Efektivní poptávka, IS-LM |
| Neokeynesiánská syntéza | Dornbush, Tobin (50.–80. léta) | Strnulé ceny/mzdy, křivka AS |
| Nová keynesiánská ekonomie | Mankiw (od 80. let) | Mikroekonomické základy keynesiánství |
| Marxismus | Marx | Třídní analýza kapitalismu |

## Hospodářský cyklus

**Potenciální výstup** $Y^P$ je definován jako:
1. Úroveň HDP bez inflačních tlaků, nebo
2. Úroveň HDP při vyčišťujících se trzích.

**Mezera výstupu** (*output gap*):
$$Y_G = \frac{Y - Y^P}{Y^P}, \quad \frac{dY_G}{dt} = \frac{(y - y^P) \cdot Y}{Y^P}$$

**Recese** – pokles HDP ve dvou po sobě jdoucích čtvrtletích, nebo nárůst míry nezaměstnanosti o 1,5 p. b. za 12 měsíců.

**Metody měření potenciálního výstupu:**
- Jednoduché trendy: $Y^P = a + bt$, minimalizace $\sum (Y - a - bt)^2$
- Hodrick–Prescottův filtr: $$\min_{Y^P_t} \sum_{t=1}^{T}(Y_t - Y^P_t)^2 + \lambda \sum_{t=2}^{T-1}\left[(Y^P_{t+1} - Y^P_t) - (Y^P_t - Y^P_{t-1})\right]^2$$
- Kalmanův filtr
- Metoda produkční funkce: $Y^P = F(K; L)$

### Okunův zákon

Empirický vztah mezi mezerou výstupu a nezaměstnaností:

$$\text{USA: } u = -0{,}5 \cdot (y - 2{,}25\%)$$
$$\text{ČR: } u = -0{,}27 \cdot (y - 2{,}31\%)$$

### Phillipsova křivka

Krátkodobá (SR) Phillipsova křivka zachycuje záporný vztah mezi inflací (nebo růstem mezd) a nezaměstnaností. Dlouhodobá (LR) Phillipsova křivka je **vertikální** na úrovni přirozené míry nezaměstnanosti $u^*$ — srov. [[AS_Modely_Agregátní_Nabídky]].
