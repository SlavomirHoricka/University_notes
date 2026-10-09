---
course: JEB010
topic: Nezaměstnanost
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_8.pdf
tags: [JEB010, nezaměstnanost, přirozená-míra, hystereze, Phillipsova-křivka]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_8.pdf]]
Related: [[Model_DAD_DAS]], [[Hospodarska_Politika_a_Debata_Pravidel]]

# Nezaměstnanost

## Definice a populační statistika

Populace ($P$ nebo $P_{15+}$) se dělí na tři skupiny:

1. **Nezaměstnaní (U):** Schopni pracovat, ochotni pracovat, aktivně hledají zaměstnání, mohou nastoupit do práce okamžitě (do 14 dnů), nemají zaměstnání
2. **Zaměstnaní (E):** Zaměstnanci se smlouvou (pracující i nepracující) + sebezaměstnaní
3. **Ekonomicky neaktivní (O):** Z objektivních důvodů (věk, zdraví) nebo subjektivních (rentiéři, bezdomovci)

**Základní identity:**
$$P = U + E + O$$

**Klíčové ukazatele:**

| Ukazatel | Vzorec |
|---|---|
| Pracovní síla | $PS = U + E$ |
| Míra nezaměstnanosti | $u = \dfrac{U}{U+E}$ |
| Míra participace | $a = \dfrac{U+E}{P}$ |
| Míra zaměstnanosti | $z_{15+} = \dfrac{E}{P_{15+}} = (1-u) \cdot a_{15+}$ |

## Vztahy mezi ukazateli

### Penzijní systém a zatížení pracujících

Podmínka stability penzijního systému:
$$E \cdot W \cdot tax = (U+O) \cdot W \cdot k$$

$$tax = \frac{U+O}{E} \cdot k = \left[\frac{1}{a} \cdot \frac{1}{1-u} - 1\right] \cdot k$$

### Výstup per capita

$$Y_{PC} = \frac{Y}{P} = lp \cdot \frac{E}{P} = lp \cdot (1-u) \cdot a$$

kde $lp = Y/E$ je produktivita práce.

## Typy nezaměstnanosti

| Typ | Popis | Remedy |
|---|---|---|
| **Frikční** | Přechod mezi zaměstnáními | Lepší matching (job search platforms) |
| **Cyklická** | Okunův zákon, recese (↓Y → ↑U) | Stabilizační politika |
| **Strukturální/technologická** | Nesoulad kvalifikace (Beveridgeova křivka) | On-the-job training, rekvalifikace |
| **Sezónní** | Zemědělství, stavebnictví, turistika | Automatické stabilizátory |

## Dynamický přístup k nezaměstnanosti

Toky mezi stavy E, U, O:
- $s$ = frekvence propouštění (E → U)
- $f$ = frekvence nalezení práce (U → E)
- $o$ = odchod z pracovní síly (E nebo U → O)
- $d$ = přísun do pracovní síly (O → U nebo E)

Dynamika nezaměstnanosti:
$$\Delta U = sE + oO - fU - dU$$

Přirozená míra nezaměstnanosti ($\Delta U = 0$):

**Jednoduchý model** (O=0):
$$\boxed{u^* = \frac{s}{s+f}}$$

**Rozšířený model** (s osobami mimo pracovní sílu):
$$u^* = \frac{s + o \cdot (1/a - 1)}{s + f + d}$$

## Statická interpretace — determinanty přirozené míry

1. **Minimální mzda:** Pokud $W_{MIN}$ > rovnovážná mzda → přebytek práce → strukturální nezaměstnanost
2. **Podpora v nezaměstnanosti:** Zvyšuje rezervační mzdu → delší trvání nezaměstnanosti ($1/f \uparrow$)
3. **Sociální dávky:** Past chudoby — čistý nahrazovací poměr příliš blízko 1
4. **Odbory:** Preference vyšší mzdy nad zaměstnaností → Wage Offer Curve
5. **Migrace:** Interní i mezinárodní mobilita práce ovlivňuje regionální trhy

## Strukturalistická hypotéza vs. Hypotéza hystereze

Po ropných šocích 70. let: u v USA poklesla z 10% na 6%, v Evropě zůstala na 8–9%.

**I. Strukturalistická hypotéza:** Příčiny na straně nabídky — silnější odbory, lepší sociální pojištění, vyšší zdanění

**II. Hypotéza hystereze:** Pokud $u > u^*$, pak $u^*$ roste (přirozená míra závisí na skutečné):
- Agentura práce nemohou obsloužit všechny nezaměstnané → zhoršuje se matching
- Ztráta pracovních návyků a dovedností → klesá $f$

**Phillipsova křivka:**
$$\pi = \pi^e - \alpha \cdot (u - u^*)$$

Politická odpověď na nabídkový šok: akomodativní (gradualistická) vs. vyhlazující strategie (π smoothing).

## Statistika nezaměstnanosti v ČR

- **MPSV:** „Registrovaná nezaměstnanost" — registr podpory; od 2013 podíl nezaměstnaných osob (PNO) na populaci 15–64
- **ČSÚ:** VŠPS (výběrové šetření pracovních sil) — srovnatelná s EU, čtvrtletně; zaměstnaní = pracovali alespoň 1 hodinu za mzdu
- Obě čísla se liší o skrytou a nepravou nezaměstnanost

**Regionální struktura (prosinec 2012):** Bruntál 18,0%, Jeseník 16,4%, Most 16,0% vs. Praha 3,6–4,5%, Mladá Boleslav 5,1%
