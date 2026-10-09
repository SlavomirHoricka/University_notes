---
course: "JEB009"
topic: "Makroekonomické indexy a měřicí problémy"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_1_3.pdf"
tags: [JEB009, makroekonomie, indexy, inflace, nezaměstnanost]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_1_3.pdf]]
Related: [[Mereni_HDP]], [[Vymezeni_a_Metody_Makroekonomie]], [[Neoklasicky_Model]]

# Makroekonomické indexy a měřicí problémy

## Stavové vs. tokové indexy

| Stavové indexy $S(t)$ | Tokové indexy $f(t)$ |
|---|---|
| Cenová hladina | Inflace |
| Nezaměstnanost | Produkt (HDP) |
| Peníze (MB, M1, M2, L) | Peněžní růst |
| Bohatství | Úspory |
| Veřejný dluh | Veřejný deficit |
| Kapitál | Investice |
| Úrokové míry | — |
| Devizový kurz | — |

**Vztah stavového a tokového indexu:**
$$S(t_2) - S(t_1) = \int_{t_1}^{t_2}\left[f_{IN}(t) - f_{OUT}(t)\right]dt$$

## Cenové indexy

### Bazický index

$$i^{BASE}_{0/t} = \frac{P_t}{P_0} - 1$$

### Meziměsíční (MoM) index

$$i^{MM}_{t} = \frac{P_t}{P_{t-1}} - 1$$

### Meziroční (YoY) index

$$i^{YY}_{t} = \frac{P_t}{P_{t-12}} - 1 = \prod_{j=0}^{11}(1 + i^{MM}_{t-j}) - 1$$

### Průměrná inflace

$$i^{average}_{t} = \frac{1}{12}\sum_{j=0}^{11} i^{YY}_{t-j}$$

## Laspeyresův vs. Paascheho index

**CPI (Laspeyresův)** — váhy základního období (košík zůstává fixní):
$$\text{CPI} = \frac{\sum_i P^1_i Q^0_i}{\sum_i P^0_i Q^0_i} \leq \text{deflátor}$$

**Deflátor HDP (Paascheho)** — váhy běžného období:
$$\text{deflátor} = \frac{\sum_i P^1_i Q^1_i}{\sum_i P^0_i Q^1_i}$$

### Proč CPI nadhodnocuje skutečnou inflaci

| Zkreslení | Příčina |
|---|---|
| **Substitution bias** | CPI neodráží substituce za levnější alternativy (Laspeyres vs. Paasche) |
| **Quality bias** | Nezachycuje nárůst kvality zboží |
| **New product bias** | Nové produkty nejsou v indexu, dramatický pokles jejich cen není reflektován |
| **Outlet bias** | Přesun spotřebitelů do outletů, nákupy online nejsou dobře zastoupeny |

### Varianty cenových indexů

- **HICP** — Harmonizovaný index spotřebitelských cen (srovnatelnost v EU)
- **Index životních nákladů důchodců** — váhová struktura odpovídá spotřebnímu koši seniorů
- **Jádrová inflace** — CPI bez potravin a energií (méně volatilní)
- **Čistá inflace** — bez regulovaných cen a nepřímých daní
- **Měnověpolitická inflace** — definice specifická pro ČNB

## Ukazatele trhu práce

**Struktura populace:**
- **Zaměstnaní** $E$ — má práci
- **Nezaměstnaní** $U$ — nemá práci, je schopen pracovat, práci hledá a je připraven do ní nastoupit
- **Mimo pracovní sílu** $O$

**Odvozené ukazatele:**
$$L = U + E \quad \text{(Pracovní síla)}$$
$$u = \frac{U}{U + E} \quad \text{(Míra nezaměstnanosti)}$$
$$a = \frac{U + E}{U + E + O} \quad \text{(Míra participace)}$$
$$p = \frac{U}{U + E + O} = u \cdot a \quad \text{(Podíl nezaměstnaných osob)}$$

## Ukazatele ekonomické aktivity

### HDP — definice

**Hrubý domácí produkt (HDP):** Suma všeho finálního zboží a služeb vyprodukovaných na území dané země za dané období (v tržních cenách včetně nepřímých daní).

**Poznámky:**
- Nezahrnuje mezispot­řebu, šedou ekonomiku, externality, transfery.
- Zásoby vstupují jako *Změna stavu zásob* (ZSZ).
- HDP $\neq$ HNP (HNP zahrnuje výnosy rezidentů ze zahraničí).

### Nominální vs. reálný HDP

$$\text{HDP}^N = \sum_i P^1_i Q^1_i$$
$$\text{HDP}^R_1 = \sum_i P^0_i Q^1_i \quad \text{(stálé ceny základního roku)}$$
$$\text{HDP}^R_2 = \sum_i P^1_i Q^1_i / \text{deflátor} \quad \text{(chain-linking)}$$

Zpravidla $\text{HDP}^N > \text{HDP}^R_1 > \text{HDP}^R_2$.

### HDP v USD (PPP)

$$y_{USD} = y_{Kč} + \text{defl} - k_{Kč/USD}$$

### Tři metody výpočtu HDP

| Metoda | Vzorec |
|---|---|
| **Výdajová** | $Y = C + I + G + NX$ |
| **Důchodová** | $Y = w + \pi + \text{odpisy}$ |
| **Produkční** | $Y = \sum_i VA_i = \sum_i (X_i - \sum_j X_{ij}) = \sum_i (w_i + \pi_i + \text{depr}_i)$ |

Výsledky všech tří metod jsou ex-post totožné (národní účetní identita).
