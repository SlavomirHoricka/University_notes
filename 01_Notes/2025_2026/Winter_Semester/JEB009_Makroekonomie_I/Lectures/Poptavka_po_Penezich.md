---
course: "JEB009"
topic: "Poptávka po penězích"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_10_11.pdf"
tags: [JEB009, makroekonomie, poptávka-po-penězích, Baumol-Tobin, Friedman, kvantitativní-teorie]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_10_11.pdf]]
Related: [[IS_LM_Model]], [[Nabidka_Penez_a_Monetarni_Politika]], [[Neoklasicky_Model]]

# Poptávka po penězích

## Co jsou peníze?

### Teoretická definice

Peníze = vše, co je **všeobecně přijímáno** při platbách za zboží a služby a při splácení dluhů.

**Historické formy:** Mušle, sůl, pivo, cigarety, korálky, kovy, dobytek. První mince: Mezopotámie 4–5 000 př. n. l.; papírové peníze: Čína 10. stol., Evropa (Švédsko) 1661.

**Požadavky na peníze:** Dělitelnost, vzácnost, nezaměnitelnost, homogenita, stálost.

### Funkce peněz

1. **Prostředek směny** — snižují transakční náklady.
2. **Účetní jednotka** — zúčtovací jednotka.
3. **Uchovatel hodnoty** — zachování kupní síly v čase.

### Empirická definice — peněžní agregáty

| Agregát | Složky |
|---|---|
| $MB$ | Hotovostní oběživo ($CU$) + rezervy bank ($RE$); „high powered money" |
| $M1$ | $MB: CU$ + vklady na požádání (běžné vklady) |
| $M2$ | $M1$ + termínovaná depozita + vklady s výpovědní lhůtou (spořící účty) |
| $M3$ | $M2$ + Repo operace + Akcie/podílové listy fondů peněžního trhu + Dluhopisy do 2 let |
| $L$ | $M2$ + Pokladniční poukázky MF + PP ČNB (do 2002) |

---

## Motivy držby peněz

1. **Transakční motiv** — zdůrazňován klasickou školou.
2. **Opatrnostní motiv** — nechceme propást příležitost / platit pokutu za nelikviditu.
3. **Spekulativní motiv** — peníze jako specifické aktivum (Keynes).

---

## Kvantitativní teorie peněz

### Fisherova transakční rovnice směny

$$M^D \cdot V_T = P \cdot T$$

kde $V_T$ = transakční rychlost obratu, $T$ = reálné transakce.

**Problém:** Jak měřit transakce? Proto Marshallova/Cambridgská škola:

$$M^D = k \cdot P \cdot Y \implies M \cdot V = P \cdot Y$$

kde $V = V_T \cdot a$ je **důchodová rychlost obratu peněz**, $k = 1/V$.

### Důchodová rychlost obratu $V$

Faktory změn $V$ (resp. $k$):

| Faktor | Efekt na $V$ |
|---|---|
| Horizontální integrace (mergery) | $V \downarrow$ (peněžní transakce s meziproduky → interní) |
| Privatizace | $V \uparrow$ (opačné) |
| Posun průmyslu → služby | $V \uparrow$ |
| Nezahrnutí nástroje plnícího funkce peněz (bitcoin, stravenky…) | $M/P$ podhodnoceno, $V$ zdánlivě $\uparrow$ |
| Snížená frekvence výplat (Baumol-Tobin) | $M/P \uparrow \implies V \downarrow$ |
| $\pi^e \uparrow$ | $i \uparrow \implies M/P \downarrow \implies V \uparrow$ |
| Finanční inovace | $r_c \downarrow \implies M/P \downarrow \implies V \uparrow$ |

---

## Teorie preference likvidity — spekulativní motiv

Domácnosti alokují bohatství mezi **peníze** ($M$) a **obligace** ($B$): $W = M + B$.

Reprezentativní obligace — perpetuita s kuponem $CU$:
$$MV = \frac{CU}{i} \implies \text{očekávaná kapitálová ztráta} = \frac{i^E}{1+i^E}$$

Celkový výnos z obligace: $i - i^E/(1+i^E)$
- Pokud $i < \frac{i^E}{1+i^E}$: Preferujeme peníze.
- Každá domácnost drží **vše v penězích nebo vše v obligacích** (nevýhoda Keynesovy teorie).

---

## Portfoliová teorie poptávky po penězích

### Tobinův model (1958)

Výběr mezi **rizikem** a **očekávaným výnosem**; dvě aktiva:
- Peníze: $E_M = 0$, $\sigma_M = 0$
- Obligace: $E_B > 0$, $\sigma_B > 0$

Portfolio s podílem $x_B$ v obligacích:
$$E_P = x_B \cdot E_B, \quad \sigma_P = x_B \cdot \sigma_B$$

V optimu (z podmínky tangenty indiferenční křivky a přímky příležitostí):
$$x_B^* = \frac{\sigma_P^*}{\sigma_B} \implies M^d = (1 - x_B^*) \cdot W = \left(1 - \frac{\sigma_P^*}{\sigma_B}\right) \cdot W$$

**Efekt nárůstu $E_B$:**
- Substituční efekt: $E_B \uparrow \implies x_B^* \uparrow \implies M^d \downarrow$
- Důchodový efekt: $E_B \uparrow \implies W \uparrow \implies x_B^* \downarrow \implies M^d \uparrow$
- Celkový efekt nejistý; obecně předpokládáme $E_B \uparrow \implies M^d \downarrow$ (normální aktiva).

### Friedmanův model (1956)

$$\frac{M^d}{P} = f\left(Y^P;\; E_B - E_M;\; E_S - E_M;\; \pi^e - E_M\right)$$

kde $Y^P$ = **permanentní důchod** (celkové celoživotní bohatství).

**Klíčové vlastnosti:**
- $Y^P$ je **stabilní** (nezávislý na přechodných šocích $\to$ $M^d/P$ stabilní).
- $E_B - E_M$: Zisky bank → depozitní sazby $\uparrow \implies E_M \uparrow \implies M^d/P$ se nemění.
- $\pi^e \uparrow \implies i = r + \pi^e \uparrow \implies E_B \uparrow \implies M^d/P \downarrow$ — ALE $E_M$ (depozitní sazba) roste stejně → efekt nulový.

**Závěr:** $M^d/P$ **nezávisí na úrokových sazbách** (pouze na $Y^P$) → $V$ stabilní.

---

## Baumol–Tobinův model (1952/1956)

Modifikace transakční $M^d$ (kombinace s opatrnostním/spekulačním motivem). Domácnosti dostávají důchod $Y_N$ vždy na začátku období a rovnoměrně ho spotřebovávají.

**Náklady držby peněz:**
1. Náklady příležitosti — úroková míra $i$
2. Transakční náklady — makléřské poplatky $t_c$ + „shoe-leather costs"

Pro $n$ transakcí: Průměrná hotovost $= Y_N / (2n)$

**Celkové náklady:**
$$TC = i \cdot \frac{Y_N}{2n} + n \cdot t_c$$

**Minimalizace** (FOC: $dTC/dn = 0$):
$$-i \cdot \frac{Y_N}{2n^2} + t_c = 0 \implies n^* = \sqrt{\frac{i \cdot Y_N}{2t_c}}$$

**Optimální reálná hotovost:**
$$\frac{M^*}{P} = \frac{Y_N}{2n^*} \cdot \frac{1}{P} = \frac{1}{2}\sqrt{\frac{2t_c Y_N}{i}}$$

nebo v reálném vyjádření ($r_c = t_c/P$):

$$\boxed{\frac{M^*}{P} = \frac{1}{2}\sqrt{\frac{2 r_c Y_N/P}{i}}}$$

### Elasticity Baumol-Tobinova modelu

| Elasticita | Teorie | Empirika |
|---|---|---|
| $\varepsilon_{M,i}$ | $-1/2$ | $(-1/2, 0)$ |
| $\varepsilon_{M,Y}$ | $1/2$ | $(1/2, 1)$ |
| $\varepsilon_{M,r_c}$ | $1/2$ | — |

**Důchodová elasticita = 1/2** (ne 1 jako v jednoduchém kvant. modelu) → **úspory z rozsahu** v transakčních nákladech → $V$ roste s $Y$.

---

## Celková funkce poptávky po penězích

$$\frac{M^d}{P} = f(Y;\; i;\; r_c), \quad \frac{\partial(M^d/P)}{\partial Y} > 0,\; \frac{\partial(M^d/P)}{\partial i} < 0,\; \frac{\partial(M^d/P)}{\partial r_c} > 0$$

Důchodová rychlost obratu:
$$V = \frac{Y}{M^d/P} = f(Y;\; i;\; r_c)$$
