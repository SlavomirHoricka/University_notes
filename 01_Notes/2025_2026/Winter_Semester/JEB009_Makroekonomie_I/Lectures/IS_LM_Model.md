---
course: "JEB009"
topic: "IS-LM model"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_8.pdf"
tags: [JEB009, makroekonomie, IS-LM, fiskální-politika, monetární-politika, past-likvidity]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_8.pdf]]
Related: [[Keynesianska_Ekonomie_a_Model_Duveru_Vydaje]], [[AD_AS_Model]], [[Poptavka_po_Penezich]], [[Nabidka_Penez_a_Monetarni_Politika]]

# IS-LM model

## Kontext a základní předpoklady

IS-LM model (John Hicks, 1937) rozšiřuje model Důchod–výdaje o **endogenní úrokovou míru**:

**Stejné předpoklady jako v modelu D-V:**
- $Y$ určeno efektivní poptávkou
- $Y$ pod úrovní potenciálu
- Konstantní $P$ (tedy $i = r$, $\pi^e = 0$)
- Krátké období (změny bohatství ze spoření zanedbány)

**Co je nové:**
- Investice závisejí na úrokové míře: $I = I(i)$
- Úroková míra určena na **trhu peněz** — Keynesova teorie preference likvidity

## Teorie preference likvidity

Keynes přidává k transakčnímu motivu dva nové motivy držby peněz:

1. **Opatrnostní motiv** — nechceme propást příležitost nebo platit penalizaci za nelikviditu.
2. **Spekulativní motiv** — peníze jako specifické aktivum s nulovou nominální ztrátou.

Celková poptávka po penězích:
$$L = L_T(Y) + L_O(Y; i) + L_S(Y; i) = L(Y; i)$$

kde $\partial L/\partial Y > 0$ a $\partial L/\partial i < 0$.

### Spekulativní motiv — perpetuita

Reprezentativní obligace — **perpetuita** s kuponem $CU$ a tržní cenou $MV$:
$$MV = \frac{CU}{i} \implies MV \text{ klesá, když } i \text{ roste}$$

Celkový výnos z obligace:
$$\text{výnos} = i - \frac{i^E}{1+i^E} \approx i - i^E$$

Pokud $i < i^E$: Očekávaná kapitálová ztráta převyšuje kupónový výnos → **preferujeme peníze**.

## Křivka LM

**Definice:** Kombinace $(i, Y)$, pro které se nabídka peněz rovná poptávce ($L = M^S/P$).

**Formalizace** (lineární poptávka po penězích $L = kY - hi$):
$$kY - hi = \frac{M}{P} \implies \boxed{i = \frac{k}{h}Y - \frac{1}{h}\frac{M}{P}}$$

**Sklon LM:** $\partial i/\partial Y|_{LM} = k/h > 0$ (rostoucí)

### Posuny LM

Nárůst $M/P$ (reálných peněžních zůstatků):
- Horizontální posun doprava o $\frac{1}{k} \cdot \frac{\Delta M}{P}$
- Vertikální posun dolů o $\frac{1}{h} \cdot \frac{\Delta M}{P}$

### Vliv parametrů na sklon LM

| Parametr | Efekt na sklon LM |
|---|---|
| $k \downarrow$ (nižší citlivost $L$ na $Y$) | LM se zplošťuje |
| $h \uparrow$ (vyšší citlivost $L$ na $i$) | LM se zplošťuje |

### Body mimo křivku LM

- **E3** (vlevo od LM): Přebytečná nabídka peněz (ESM) → $i \downarrow$
- **E4** (vpravo od LM): Přebytečná poptávka po penězích (EDM) → $i \uparrow$

## Křivka IS

**Definice:** Kombinace $(i, Y)$, pro které se ex-ante výdaje rovnají výstupu (rovnováha na trhu zboží).

**Odvození** z modelu D-V (přidáme $I = I_A - b \cdot i$):

$$Y = \mu_t \cdot (A - b \cdot i) \implies \boxed{i = \frac{A}{b} - \frac{1}{\mu_t \cdot b} Y}$$

kde $A = C_A + I_A + G_A + c \cdot TR_A$ a $\mu_t = 1/[1-c(1-t)]$.

**Sklon IS:** $\partial i/\partial Y|_{IS} = -1/(\mu_t \cdot b) < 0$ (klesající)

### Horizontální a vertikální posuny IS

Nárůst autonomních výdajů $\Delta A$ (nebo $\Delta G$):
- Horizontální posun doprava o $\mu_t \cdot \Delta A$
- Vertikální posun nahoru o $\Delta A / b$

### Vliv parametrů na sklon IS

| Parametr | Efekt na sklon IS |
|---|---|
| $\mu_t \uparrow$ (vyšší multiplikátor) | IS se zplošťuje |
| $b \uparrow$ (vyšší citlivost $I$ na $i$) | IS se zplošťuje |

### Body mimo křivku IS

- **E3** (vpravo od IS): Přebytečná nabídka zboží (ESG) → $Y \downarrow$
- **E4** (vlevo od IS): Přebytečná poptávka po zboží (EDG) → $Y \uparrow$

## Celkový IS-LM model — rovnováha

Substituujeme $i$ z LM do IS:

$$Y = \mu_t\left(A - b\left(\frac{k}{h}Y - \frac{M/P}{h}\right)\right)$$

**Redukovaný tvar:**

$$\boxed{Y^* = \frac{h}{h + \mu_t bk} \cdot \mu_t \cdot A + \frac{\mu_t b}{h + \mu_t bk} \cdot \frac{M}{P}}$$

Nebo kompaktně: $Y^* = \alpha_G \cdot A + \alpha_M \cdot (M/P)$, kde:

### Multiplikátory fiskální a monetární politiky

$$\alpha_G = \frac{\partial Y}{\partial A} = \frac{\mu_t h}{h + \mu_t bk} = \frac{h\mu_t}{h + bk\mu_t}$$

$$\alpha_M = \frac{\partial Y}{\partial (M/P)} = \frac{\mu_t b}{h + \mu_t bk}$$

Porovnání: $\alpha_G < \mu_t$ v důsledku **vytlačování investic** (*crowding out*):

$$\Delta i = \frac{k \cdot \mu_t}{h + k\mu_t b} \cdot \Delta A > 0 \implies \Delta I = -b \cdot \Delta i < 0$$

### Citlivostní analýza (znaménka parciálních derivací)

| $\partial \alpha_G / \partial$ | Efekt |
|---|---|
| $\mu_t \uparrow$ | $\alpha_G \uparrow$ (větší base multiplikátor) |
| $b \uparrow$ | $\alpha_G \downarrow$ (větší vytlačování) |
| $h \uparrow$ | $\alpha_G \uparrow$ (méně reaktivní $i$) |
| $k \downarrow$ | $\alpha_G \uparrow$ (menší nárůst $i$) |

## Speciální případy

### Past likvidity ($h \to \infty$)

Křivka LM **horizontální**; $i$ se nemění při jakékoli $\Delta M$.

$$\alpha_G \to \mu_t \quad \text{(fiskální política maximálně účinná)}$$
$$\alpha_M \to 0 \quad \text{(monetární politika neúčinná)}$$

### Past investic ($b \to 0$)

Křivka IS **vertikální**; investice nereagují na $i$.

$$\alpha_G \to 0 \quad \text{(fiskální politika neúčinná)}$$
$$\alpha_M \to 0 \quad \text{(monetární politika neúčinná)}$$

### Klasický případ ($h \to 0$)

Křivka LM **vertikální**; peníze drží pouze z transakčního motivu.

$$\alpha_G \to 0 \quad \text{(fiskální politika neúčinná — plné vytlačování)}$$
$$\alpha_M \to 1/k \quad \text{(monetární politika maximálně účinná)}$$

## Dynamika IS-LM modelu

**Předpoklad rychlého trhu peněz:**
- Trh peněz se vyčišťuje okamžitě ($i$ se okamžitě přizpůsobí).
- Trh zboží se přizpůsobuje postupně.

Body mimo rovnováhu:
- ESG (přebytečná nabídka zboží): $Y \downarrow$
- EDG (přebytečná poptávka po zboží): $Y \uparrow$
- ESM (přebytečná nabídka peněz): $i \downarrow$
- EDM (přebytečná poptávka po penězích): $i \uparrow$

## Koordinace fiskální a monetární politiky

**„Boj fiskální a měnové politiky":**
- Fiskální expanze ($G \uparrow \implies IS$ doprava) + monetární restrikce ($M \downarrow \implies LM$ doleva) → $Y$ se může vrátit na původní úroveň při vyšším $i$.
- Fiskální expanze + monetární expanze: Oba nástroje směřují $Y \uparrow$, ale kompromis v $i$.

Podmínka pro udržení $Y^*$ nezměněné při $\Delta G$:
$$\Delta M/P = -\frac{k\mu_t}{1} \cdot \Delta G \cdot h = -\frac{k \cdot \mu_t \cdot \Delta G}{1} \cdot h$$

## Kritika modelu IS-LM

### Ze strany neoklasické ekonomie
- Chybějící mikroekonomické základy.
- Chybějící očekávání ekonomických agentů.
- Přílišné zjednodušení reality.
- Nerealistické předpoklady o měnové politice.
- Neodlišování nominální a reálné úrokové míry.

### Ze strany post-keynesiánství
- IS-LM je „kočkopes" míchající Keynese s neklasicismem.
- Oddělení trhu peněz a trhu zboží (proti Keynesově Obecné teorii).
- Kritika rovnovážného přístupu (modely nerovnováhy).
