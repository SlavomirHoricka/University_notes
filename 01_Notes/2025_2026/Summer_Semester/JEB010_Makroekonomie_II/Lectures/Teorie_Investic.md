---
course: JEB010
topic: Teorie investic
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_10.pdf
tags: [JEB010, investice, neoklasická-teorie, Tobin-q, akcelerátor, kapitál]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_10.pdf]]
Related: [[Teorie_Spotreby]], [[Solow_Model_Ekonomickeho_Rustu]]

# Teorie investic

Investice tvoří ~1/3 HDP, jsou nejvolatilnější složkou a silně procyklické. Jsou součástí AD, ale zároveň ovlivňují budoucí AS prostřednictvím kapacity ekonomiky.

## Základní typy investic

1. **Investice do fixního kapitálu (HTFK):** Budovy, stroje, zařízení — nejdůležitější kategorie
2. **Investice do bydlení:** Byty, rodinné domy — specifické (dlouhodobé, domácnosti, likviditní omezení)
3. **Změna zásob:** Vlastní výrobky, zboží, vstupy, meziprodukt
4. **Finanční investice nejsou investicemi ve smyslu HDP!**

**Stav kapitálu $K$ vs. tok investic $I$:**
$$I = \Delta K \qquad I_G = I_N + \delta \qquad I_N = \Delta K = I_G - \delta$$

## 1. Model jednoduchého akcelerátoru

**Předpoklad:** Kapitálová zásoba proporcionální k produktu: $K^* = v \cdot Y$

Pokud ekonomika v počátečním equilibriu: $K_1 = K_1^* = v \cdot Y_1$

Optimální kapitál pro příští období: $K_2^* = v \cdot Y_2^E$

$$\boxed{I = K_2^* - K_1 = v \cdot (Y_2^* - Y_1)}$$

V praxi $v \approx 3$–4. **Slabina:** Ignoruje náklady kapitálu.

## 2. Neoklasický přístup

### Náklady kapitálu (cost of capital)

Nominální náklady investice za jednotku $P_K$:

$$NCC = i \cdot P_K - \Delta P_K + \delta \cdot P_K = P_K\left(i - \frac{\Delta P_K}{P_K} + \delta\right)$$

Reálné náklady kapitálu (RCC):

$$RCC = \frac{P_K}{P}\left(i - \pi_K + \delta\right)$$

Pokud cenový vývoj kapitálového zboží odpovídá celkové inflaci ($\pi = \pi_K = \Delta P_K/P$) a z Fisherovy rovnice $i - \pi = r$:

$$\boxed{RCC = \frac{P_K}{P} \cdot (r + \delta)}$$

### Optimální kapitál

Firma maximalizuje zisk: $\text{MPK} = RCC$

Pro **Cobb-Douglasovu produkční funkci** $F(K;L) = A \cdot K^\alpha \cdot L^{1-\alpha}$:

$$MPK = A \cdot \alpha \cdot K^{\alpha-1} \cdot L^{1-\alpha} = \alpha \cdot \frac{Y}{K}$$

Z $MPK = RCC$:

$$\alpha \cdot \frac{Y}{K^*} = \frac{P_K}{P}(r+\delta) \Rightarrow \boxed{K^* = \frac{\alpha \cdot Y}{r + \delta}} \quad \text{(pro } P_K = P\text{)}$$

### Změny $K^*$

| Šok | Efekt |
|---|---|
| $\uparrow K$ | $\downarrow MPK$ → pohyb po křivce |
| $\uparrow L$ (imigrace) | $\uparrow MPK$ → posun křivky doprava |
| $\uparrow A$ (technologie) | $\uparrow MPK$ → posun křivky doprava |
| $\uparrow r$ | $\uparrow RCC$ → $\downarrow K^*$ |

### Daně a investice

$$\uparrow TA \Rightarrow \uparrow RCC \Rightarrow \downarrow K^* \Rightarrow \downarrow I$$

- **DPPO (daň ze zisku firem):** závisí na metodě odpisování (lineární vs. zrychlené); $\uparrow\pi$ → podhodnocení amortizace → nadhodnocení zisku → vyšší reálná daňová zátěž
- **Investiční daňový dobropis:** Investice jako náklad odpočteny ze zisku (de facto 100% odpisy); dočasný dobropis má větší dopad než permanentní (pokud ohlášen předem)

## 3. Rychlost přizpůsobení a model flexibilního akcelerátoru

**Striktní neoklasika:** $K = K^*$ okamžitě (racionální očekávání) — nekonečné investice v krátkém čase (nerealistické).

**Neokeynesiánské teorie (mainstream):** Postupné přizpůsobení kvůli časovému zpoždění a instalačním nákladům (rychlé investice dražší než pomalé).

**Model flexibilního akcelerátoru:**
$$K = K_{-1} + \lambda \cdot (K^* - K_{-1})$$

$$\boxed{I = K - K_{-1} = \lambda \cdot (K^* - K_{-1}) = \lambda \cdot \left(\frac{\alpha \cdot Y}{r+\delta} - K_{-1}\right)}$$

kde $\lambda \in (0,1)$ je rychlost přizpůsobení.

## 4. Tobinova $q$ teorie investic

Nad rámec neoklasického přístupu uvažuje **instalační náklady** (přerušení výroby, trénování zaměstnanců, čas managerů).

$$\boxed{q = \frac{\text{tržní cena instalovaného kapitálu}}{\text{reprodukční hodnota kapitálu}}}$$

**Interpretace:**
- $q > 1$: Nárůst $K$ zvyšuje tržní hodnotu firmy → $\uparrow K^*$, $\uparrow I$
- $q < 1$: Firma prodá kapitál nebo neinvestuje → $\downarrow K$, $\downarrow I_N$

**Makroekonomická implikace:** $\downarrow$ cen akcií $\Rightarrow \downarrow q \Rightarrow \downarrow I \Rightarrow \downarrow AD$

Akciové indexy jsou proto **leading indicators** hospodářského cyklu.

### Likviditní omezení a finanční akcelerátor

Investice závisí i na vlastních zdrojích firmy (interní financování), protože:
- Asymetrická informace (věřitel nezná kvalitu projektu)
- Morální hazard (dlužník může zvolnout rizikovější projekt)
- Nepříznivý výběr (adverse selection)
- Nízká vynutitelnost kontraktů

**Finanční akcelerátor:** Pokles $q$ → pokles hodnoty kolaterálu → zpřísnění úvěrových podmínek → další pokles investic (procyklický multiplikátor).

## 5. Investice do bydlení

Specifické vlastnosti: stojí na hranici investice a spotřeby; prováděny domácnostmi; větší likviditní omezení; dlouhodobé (20–30 let); forma aktiva.

**Dvoutrhový model:**
- **Trh s existujícími domy** ($H_N$ fixní krátkodobě): $P_H$ určena rovnováhou $Y_D = Y_S$
- **Trh s novými domy:** Nová výstavba spuštěna, když $P_H > P_{MAX}$ (náklady výstavby)

| Šok | Efekt |
|---|---|
| $\uparrow W$ | $\uparrow D$, $\uparrow P_H$, $\uparrow I_H$ |
| $\uparrow P$ (obecná inflace) | $\uparrow D$, $\uparrow P_H$, $\uparrow I_H$ |
| $\uparrow i$ | $\downarrow D$, $\downarrow P_H$, $\downarrow I_H$ |
| $\uparrow$ čistý reálný výnos (nájem − úrok − odpisy + kapitálové zisky) | $\uparrow D$, $\uparrow P_H$, $\uparrow I_H$ |

## 6. Investice do zásob

Zásoby jsou nejvolatilnější část AD (stock vs. flow!):

**Motivy držby zásob:**
- Prodleva výroby — zásoby jako nárazník
- Množstevní slevy na vstupy
- Vyhlazování výroby
- Zásoby v rámci produkčního procesu (meziprodukt)

**Cyklicita:**
- Anticipované změny zásob: většinou procyklické
- Neočekávané změny: závisí na očekáváních; jediná výjimka — statická očekávání → po neočekávaném šoku zásoby přechodně proticyklické
