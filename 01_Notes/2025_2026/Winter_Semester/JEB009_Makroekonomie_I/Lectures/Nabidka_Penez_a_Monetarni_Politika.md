---
course: "JEB009"
topic: "Nabídka peněz a monetární politika"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_10_11.pdf"
tags: [JEB009, makroekonomie, nabídka-peněz, monetární-politika, peněžní-multiplikátor, ČNB, transmisní-mechanismus]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_10_11.pdf]]
Related: [[Poptavka_po_Penezich]], [[IS_LM_Model]], [[AD_AS_Model]]

# Nabídka peněz a monetární politika

## Bilance centrální banky (ČNB)

**Aktiva ČNB:**
- $\check{C}ZA$ — Čistá zahraniční aktiva (devizové rezervy, pohledávky ze zahraničí)
- $DL$ — Diskontní půjčky bankám (věřitel poslední instance; regulace $M$)
- $SCP$ — Státní cenné papíry (MF, FNM)
- $OA$ — Ostatní aktiva (fixní aktiva, pohledávky)

**Pasiva ČNB:**
- $CU$ — Oběživo (bankovky a mince mimo trezory ČNB)
- $RE$ — Rezervy komerčních bank (PMR, platební systém, oběživo v pokladnách bank)
- $BHSR$ — Běžné hospodaření státního rozpočtu
- $JM$ — Vlastní jmění ČNB
- $OP$ — Ostatní závazky

**Peněžní báze** (*High powered money*):
$$MB = CU + RE = \check{C}ZA + DL + SCP + OA - BHSR - JM - OP$$

### Vliv ČNB na peněžní bázi

| Operace | Efekt na MB |
|---|---|
| Nákup obligací od bank (OMO) | $SCP \uparrow \implies MB \uparrow$ |
| Diskontní půjčka bance | $DL \uparrow \implies MB \uparrow$ |
| Úvěr státu | $BHSR \uparrow \implies MB$ nezměněna |
| Devizové intervence (nákup deviz) | $\check{C}ZA \uparrow \implies MB \uparrow$ |

---

## Proces tvorby peněz — peněžní multiplikátor

### Mikroskopický pohled (T-accounts)

Výchozí situace: OMO — ČNB nakoupí CP od banky 1 za 100:

| Banka | $\Delta BD$ | $\Delta RE$ | $\Delta \acute{U}$ |
|---|---|---|---|
| Banka 1 | 0 | 0 | 100 |
| Banka 2 | 100 | 10 | 90 |
| Banka 3 | 90 | 9 | 81 |
| Banka 4 | 81 | 8,1 | 72,9 |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| **Suma** | **1 000** | **100** | **1 000** |

(Při PMR $r_D = 10\%$.)

### Algebra peněžního multiplikátoru

Definice: $cu = CU/D$ (poměr hotovosti k vkladům), $r_D$ (povinné min. rezervy):

$$MB = CU + RE = cu \cdot D + r_D \cdot D = (cu + r_D) \cdot D$$
$$M1 = CU + D = (cu + 1) \cdot D$$

$$\boxed{m_{M1} = \frac{M1}{MB} = \frac{cu + 1}{cu + r_D}}$$

**Faktory multiplikátoru:**

$$m = m(r_D,\; cu,\; i_{DISK},\; i_{CREDIT},\; i_{DEPO},\; i_{OMR},\; \text{BANK},\; \text{SYSTEM},\; W)$$
$$\quad\quad\quad\; (-) \quad (-) \quad\; (-) \qquad\quad (+) \qquad\quad (+) \qquad (-) \qquad\quad (-) \qquad\quad (-) \quad (+)$$

### Stabilita multiplikátoru a exogenita MB

MB je exogenní (kontrolovatelná CB) pokud:
- ČZA fixní (pevný kurz → problém: příliv kapitálu → $MB \uparrow$)
- DL exogenní (částečně endogenní — závisí na poptávce bank)
- BHSR nezávislý na CB (CB nefinancuje schodky)

**Trade-off:** Exogenita MB × stabilita multiplikátoru.

---

## Nástroje centrální banky

### Konvenční nástroje

| Nástroj | Mechanismus |
|---|---|
| **Operace na volném trhu (OMO)** | Nákup/prodej obligací; v ČR REPO operace |
| **Diskontní nástroje** | Diskontní úvěr (O/N depozitní facilita), Lombardní úvěr (O/N zápůjční facilita) |
| **Povinné minimální rezervy (PMR)** | Ovlivnění multiplikátoru; „zdanění bank" |
| **Devizové intervence** | Ovlivnění kurzu + ČZA |
| **Administrativní nástroje** | Úvěrové limity, likviditní pravidla, kapitálová přiměřenost |

**Hierarchie sazeb ČNB:**
$$i_{DISK} < i_{REPO} < i_{LOMBARD}$$

### Nekonvenční nástroje (post-2008)

| Nástroj | Popis |
|---|---|
| **Kvantitativní uvolňování (QE)** | Nárůst objemu rozvahy CB (nákup státních dluhopisů, MBS) |
| **Kvalitativní uvolňování** | Změna skladby rozvahy (rozšíření protistran, kolaterálu, splatností) |
| **Úvěrové uvolňování** | Kombinace QE + QualE |
| **Forward guidance** | Explicitní závazek udržet sazby na ZLB po delší dobu (ČNB: od 1. 11. 2012) |
| **Kurzový závazek** | Explicitní závazek o kurzu (ČNB: 7. 11. 2013 – 6. 4. 2017, EUR/CZK ≥ 27) |
| **Helicopter drop** | Připsání peněz ve prospěch ekonomických subjektů |
| **Negativní sazby** | „Penalizace držení peněz u CB" |

---

## Transmisní mechanismy měnové politiky

$$\text{Nástroje} \to \text{Operační kritéria} \to \text{Zprostředkující cíle} \to \text{Základní cíle}$$

| Transmisní mechanismus | Kanál | Cíl |
|---|---|---|
| **Peněžní** | $MB \to M2 \to$ inflace, prosperita | Cenová stabilita |
| **Úrokový** | $i_{SR} \to i_{LR} \to$ investice → důchod | Nezaměstnanost, růst |
| **Úvěrový** | $i \to$ objem úvěrů → důchod | Růst |
| **Devizový** | $i \to k \to$ ceny dovozu → inflace | Cenová stabilita (malá otevřená ekonomika) |
| **Inflační cílování** | Cílování predikce inflace | Cenová stabilita |

---

## Cíle centrální banky

**Cíle ČNB** (dle zákona): Primárně cenová stabilita; sekundárně podpora HP vlády vedoucí k udržitelnému rozvoji.

**Tinbergenovo pravidlo:** CB musí mít alespoň stejný počet nezávislých nástrojů, jako má cílů.

**Trade-off cílů:**
- Hospodářský růst × inflace (Phillipsova křivka)
- Stabilita úrokových sazeb × stabilita $M$

### Trade-off mezi cílením $i$ a $M$

**A) Nestabilní trh zboží** ($IS$ se posouvá): Cílování $i$ stabilizuje $Y$ lépe (LM vodorovná).

**B) Nestabilní trh peněz** ($LM$ se posouvá): Cílování $M$ stabilizuje $Y$ lépe (pevný $M \implies$ pevné $LM$).

---

## Debata: Pravidla versus diskrece

### Dynamická nekonzistence diskrétní politiky (Kydland–Prescott, Nobel 1977)

**Problém:** I když CB sdílí veřejné preference, výsledek diskrétní politiky může být **společensky suboptimální**.

Příklad — trade-off inflace–output: CB maximalizuje:
$$\max_\pi L(\pi, Y) = -(Y - Y^*)^2 - a(\pi)^2 \quad \text{s.p.} \quad Y = \bar{Y} + b(\pi - \pi^E)$$

FOC: $\frac{\partial L}{\partial \pi} = 0 \implies \pi^* = \pi^E + \frac{a(Y^* - \bar{Y})}{1} = \pi^E + a \cdot (Y^* - \bar{Y})$

V dlouhém období $\pi = \pi^E \implies \pi^* = a \cdot (Y^* - \bar{Y}) > 0$ — **inflační zkreslení**.

**Příklady dynamické nekonzistence:**
- Teroristé a rukojmí
- Řešení trade-off inflace–výstup
- Investiční/FDI pobídky
- Pobídky pro R&D (dočasný monopol z patentu)

### Typy pravidel pro měnovou politiku

| Pravidlo | Popis |
|---|---|
| **Monetaristické** (Friedman) | Nízký stabilní růst $M$ |
| **Cílování nom. HDP** | Plánovaný vývoj HDP; reaguje na změny $V$ |
| **Taylorovo pravidlo** | $i_t = r^* + \pi_t + \phi_\pi(\pi_t - \pi^*) + \phi_y(Y_t - Y^P_t)$ |
| **Inflační cílování** | Cílování současné $\pi$ nebo predikce $\pi$ |

---

## IS-MP-IA model (alternativa IS-LM)

- Nahrazuje LM křivku **MP** (Monetary Policy) křivkou — přímo zachycuje chování CB s Taylorovým pravidlem.
- Čisté inflační cílení: MP horizontální.
- **IA (Inflation Adjustment):** Inflace je v každém bodě daná; roste pokud $Y > Y^P$, stabilní pokud $Y = Y^P$.
