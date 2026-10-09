---
course: "JEB009"
topic: "Teorie investic"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_6.pdf"
tags: [JEB009, makroekonomie, investice, Tobin-q, akcelerátor, RCC, nemovitosti]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_6.pdf]]
Related: [[Neoklasicky_Model]], [[Keynesianska_Ekonomie_a_Model_Duveru_Vydaje]], [[IS_LM_Model]], [[AS_Modely_Agregátní_Nabídky]]

# Teorie investic

## Základní charakteristika investic

- **Druhá největší** složka HDP (kolem 1/3).
- Jedna z **nejvíce volatilních** složek HDP — klíčová pro vysvětlení hospodářského cyklu (silně procyklické).
- Investice = část AD, ale zároveň ovlivňují budoucí AS (akumulace kapitálu).

### Tři typy investic

1. **Investice do fixního kapitálu (HTFK)** — budovy, stroje, zařízení.
2. **Investice do bydlení** — byty, rodinné a bytové domy.
3. **Změna zásob** — vlastní výrobky, zboží, vstupy, meziprodukt.

> **Pozor:** Finanční investice **nejsou** investicemi ve smyslu složky HDP!

### Klíčové pojmy

- **Stav kapitálu** (stock) $K$ vs. **tok investic** (flow) $I$: $\dot{K} = I$
- **Čisté investice:** $I_{NET} = I_G - \delta K = \dot{K}$
- **Hrubé investice:** $I_G = I_{NET} + \delta K$

---

## Teorie fixních investic

### 1. Model jednoduchého akcelerátoru (raná keynesiánská teorie)

**Předpoklady:** Kapitálová zásoba je proporcionální produktu: $K^* = v \cdot Y$ (kde $v \approx 3$–$4$).

$$I = \Delta K^* = v \cdot (Y_2^* - Y_1)$$

**Klíčová otázka:** Co determinuje důchod? (Keynesiánci: AD; Neoklasika: technologie a $r$.)

**Nedostatek:** Nebere v úvahu náklady kapitálu.

---

### 2. Neoklasický přístup

**Reálné náklady kapitálu (RCC):**

$$RCC = \frac{P_K}{P} \cdot (i - \dot{P}_K/P_K + \delta) = \frac{P_K}{P} \cdot (r + \delta)$$

kde:
- $i \cdot P_K$ — náklady příležitosti
- $-\dot{P}_K$ — pokles ceny = ztráta
- $\delta \cdot P_K$ — fyzické opotřebení a morální zastarávání

Pro $\pi = \dot{P}_K/P_K$ a Fisherovu rovnici $i - \pi = r$, a za předpokladu $P_K = P$:

$$\boxed{RCC = r + \delta}$$

**Optimální kapitálová zásoba** z podmínky $MPK = RCC$:

Pro Cobb-Douglas $F(K;L) = A K^\alpha L^{1-\alpha}$:
$$MPK = A \cdot \alpha \cdot (L/K)^{1-\alpha} = \alpha \cdot Y/K$$

Optimum: $MPK = r + \delta \implies \alpha \cdot Y / K^* = r + \delta$

$$\boxed{K^* = \frac{\alpha \cdot Y}{r + \delta}}$$

**Determinanty $K^*$:**

| Parametr | Efekt na $K^*$ |
|---|---|
| $K \uparrow$ | $MPK \downarrow$ (pohyb po křivce) — $K^*$ dosažen |
| $L \uparrow$ (imigrace) | $MPK \uparrow \to K^* \uparrow$ (posun MPK doprava) |
| $A \uparrow$ (technologie) | $MPK \uparrow \to K^* \uparrow$ (posun MPK doprava) |
| $r \uparrow$ | $RCC \uparrow \to K^* \downarrow$ |

**Daně a investice:**
$$TA \uparrow \implies RCC \uparrow \implies K^* \downarrow \implies I \downarrow$$

- Přímé daně (DPPO): Podhodnocení amortizace → nadhodnocení zisku → vyšší reálné zdanění.
- **Investiční daňový dobropis** — podpora investic; investice jako náklad odepsán ze zisku.

---

### 3. Model flexibilního akcelerátoru

Kapitál se přizpůsobuje postupně (ne ihned):

$$K = K_{-1} + \lambda(K^* - K_{-1})$$

Investice:
$$I = \dot{K} = \lambda(K^* - K_{-1}) = \lambda\left(\frac{\alpha \cdot Y}{r + \delta} - K_{-1}\right)$$

kde $\lambda \in (0, 1)$ je rychlost přizpůsobení.

---

### 4. Tobinova $q$ teorie investic

**Motivace:** K neoklasickým nákladům přidává **instalační náklady** (přerušení výroby, trénování zaměstnanců, čas manažerů).

**Tobinovo $q$:**

$$q = \frac{\text{tržní cena instalovaného kapitálu}}{\text{reprodukční hodnota kapitálu}}$$

**Investiční pravidlo:**
- $q > 1$: Nárůst $K$ zvyšuje tržní hodnotu firmy → $K^* \uparrow$, $I \uparrow$
- $q < 1$: Firma prodá kapitál nebo neinvestuje ($I \leq 0$)

**Implikace:** $\text{ceny akcií} \uparrow \implies q \uparrow \implies I \uparrow \implies \text{AD} \uparrow$

Akciové indexy jako **leading indicator** hospodářského cyklu.

**Likviditní omezení** (*credit rationing / credit crunch*): Investice závisí i na vlastních zdrojích firmy → příčiny: asymetrická informace, *adverse selection*, morální hazard, nízká vymahatelnost kontraktů.

---

## Investice do bydlení

- Prováděny domácnostmi → větší likviditní omezení.
- Dlouhodobé (20–30 let), forma aktiva.
- Dva trhy: **Trh s existujícími domy** & **Trh s novými domy**.

**Determinanty:**
- $W \uparrow \implies D \uparrow \implies P_H \uparrow \implies I_H \uparrow$
- $P \uparrow \implies D \uparrow \implies P_H \uparrow \implies I_H \uparrow$
- $i \uparrow \implies D \downarrow \implies P_H \downarrow \implies I_H \downarrow$
- Čistý reálný výnos z nemovitosti (nájem + kap. zisky − odpisy − úrok) $\uparrow \implies I_H \uparrow$

Makroekonomické dopady splaskávání cenových bublin v nemovitostech jsou závažnější než v jiných aktivech: trvají déle (~4 roky vs. ~1,5 roku u akcií), hrozí finanční stabilitě a ovlivňují spotřebu.

---

## Investice do zásob

1. Zásoby jsou **prvním nárazníkem** změn AD:
   - $AD > AS \implies$ zásoby klesají
   - $AD < AS \implies$ zásoby rostou
2. **Motivy držby zásob:** Zpoždění výroby, množstevní slevy, vyhlazování výroby, zachycení meziproduktů.
3. **Vysoká volatilita:** Změna zásob je nejvolatilnější složka AE (stock vs. flow efekt).
4. Anticipovaná změna zásob: **procyklická**; neočekávaná změna zásob při statických očekáváních: krátkodobě **proticyklická**.
