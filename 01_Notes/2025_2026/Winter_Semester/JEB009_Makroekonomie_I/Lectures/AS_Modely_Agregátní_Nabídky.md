---
course: "JEB009"
topic: "Modely agregátní nabídky (AS)"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_5.pdf"
tags: [JEB009, makroekonomie, agregátní-nabídka, strnulé-mzdy, Phillipsova-křivka, AS]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_5.pdf]]
Related: [[Neoklasicky_Model]], [[AD_AS_Model]], [[IS_LM_Model]], [[Keynesianska_Ekonomie_a_Model_Duveru_Vydaje]]

# Modely agregátní nabídky (AS)

## Motivace

Sklon křivky AS zásadně ovlivňuje výsledek modelu AS-AD:
- **Vertikální AS** (neoklasická): Šok AD se plně přenáší do cen, výstup se nemění.
- **Horizontální AS** (keynesiánská): Šok AD se plně přenáší do výstupu, ceny se nemění.
- **Rostoucí AS** (Phillipsova křivka): Šoky AD mají smíšený efekt.

## Odvození AS z Phillipsovy křivky

Phillipsova křivka (mzdová):
$$g_W = -\beta(u - u^*) \implies W = W_{-1} \cdot [1 - \beta(u - u^*)]$$

Z lineární produkční funkce $Y = aL$ a mark-up oceňování $P = (1+z) \cdot W/a$:

$$P_{-1} = (1+z) \cdot W_{-1}/a$$

Odvozením dostaneme **krátkodobou křivku AS**:
$$P = P_{-1} + \frac{1}{\alpha}(Y - Y^*) \quad \text{nebo ekvivalentně} \quad Y = Y^* + \alpha(P - P_{-1})$$

## Čtyři modely AS se stoupající křivkou

Všechny čtyři modely mají tvar:
$$\boxed{Y = Y^* + \alpha(P - P^e)}$$

Liší se interpretací $P^e$ a mechanismem vzniku.

### 1. Model strnulých mezd (*Sticky Wage Model*)

**Předpoklady:**
- Nominální mzdy nastaveny dopředu na základě kolektivního vyjednávání.
- Vyjednávání závisí na **očekávané** cenové hladině: $W = \mu \cdot P^e$.
- Tedy reálná mzda: $W/P = \mu \cdot P^e / P$.

**Mechanismus:**

| Situace | Efekt na $W/P$ | Efekt na $L^S$, $L^D$ | Efekt na $Y$ |
|---|---|---|---|
| $P > P^e$ | $W/P \downarrow$ | $L^S > L^D$ (nezaměstnanost) | $Y \downarrow$ |
| $P < P^e$ | $W/P \uparrow$ | $L^S < L^D$ (volná místa) | $Y \uparrow$ |

**Alternativní předpoklady:**
- Alt 1: Zpět zahnutá AS (mzdy flexibilní oběma směry)
- Alt 2: Mzdy strnulé **pouze dolů** (asymetrická rigidita — typický keynesiánský výsledek)
- Alt 3: $L^S$ determinována $L^D$ (efektivní poptávka určuje i nabídku práce)

$P^e = E_{t-1}(P_t)$ (očekávání formovaná v předchozím období).

### 2. Model mzdové iluze (*Worker Misperception Model*)

**Autor:** Milton Friedman

**Předpoklady:**
- Trhy se **vyčišťují** — žádná nezaměstnanost ani volná pracovní místa.
- Zaměstnanci nerozeznávají správně skutečnou cenovou hladinu.

**Mechanismus:**
- $\text{AD} \uparrow \implies W \uparrow, P \uparrow$ (tak, že $W/P$ konstantní)
- Zaměstnanci vnímají $W \uparrow$ jako $W/P \uparrow \implies L^S \uparrow \implies L, Y \uparrow$

Formálně:
$$L^D = L^D(W/P), \quad L^S = L^S(W/P^e) = L^S\left(\frac{W}{P} \cdot \frac{P}{P^e}\right)$$

$P \uparrow \implies P/P^e \uparrow \implies L^S$ doprava $\implies L, Y \uparrow$.

**Proč mají firmy lepší informace než zaměstnanci:**
1. Firmy sledují méně cen (vstupy, výstupy, substituty).
2. Zaměstnanci kontrolují ceny méně často.
3. Firmy mají lepší přístup k datům (úspory z rozsahu).

Jakmile zaměstnanci rozpoznají skutečnou cenovou hladinu, $L^S$ se vrátí a $Y$ se vrátí na $Y^*$.

$P^e = E_t(P_t)$ — v tomto modelu mají zaměstnanci **soudobou** nepřesnou informaci.

### 3. Model nedokonalé informace (*Imperfect Information Model*)

**Autor:** Robert Lucas

**Předpoklady:**
- „Model cenové iluze" — stejná informační bariéra pro firmy i zaměstnance.
- Každý výrobce zná perfektně cenu svého **výstupu**, ale ceny vstupů kontroluje méně.
- Rozhodování o výrobě závisí na **relativních cenách** $P_{OUTPUT}/P_{INPUT}$.

**Mechanismus:**
- Nárůst celkové cenové hladiny — každá firma zaznamená vyšší cenu výstupu → mylně interpretuje jako relativní cenový signál → $Y \uparrow$.
- Závisí na volatilitě inflace: v zemích s historicky nízkou inflací je $\alpha$ vysoké (firmy snáze rozlišují); v zemích s vysokou a volatilní inflací je $\alpha$ nízké.

$P^e = E_t(P_t)$ — soudobá nepřesná informace (jako M.M.I.).

### 4. Model strnulých cen (*Sticky Price Model*)

**Předpoklady:**
- Část firem (podíl $s$) jsou **cenoví tvůrci** — mají dlouhodobé smlouvy a nemění ceny okamžitě.
- Část firem (podíl $1-s$) jsou **cenoví příjemci** — ceny nastavují okamžitě.

**Cenová tvorba:**
- Cenoví tvůrci: $p_T = P^E + a(Y^E - Y^{*E})$ nebo $p_T = P^E$ (pro $Y^E = Y^{*E}$)
- Cenoví příjemci: $p_P = P + a(Y - Y^*)$

Celková cenová hladina:
$$P = s \cdot P^E + (1-s)[P + a(Y - Y^*)]$$
$$\boxed{P = P^E + \frac{(1-s) \cdot a}{s}(Y - Y^*)} \implies \alpha = \frac{s}{(1-s) \cdot a}$$

$P^e = E_{t-1}(P_t)$ — jako M.S.M.

## Rekapitulace modelů AS

| Model | Vyčišťují se trhy? | Nedokonalost na | $P^e$ |
|---|---|---|---|
| Strnulých mezd (M.S.M.) | Ne | Práce | $E_{t-1}(P_t)$ |
| Mzdové iluze (M.M.I.) | Ano | Práce | $E_t(P_t)$ |
| Nedokonalé informace (M.N.I.) | Ano | Zboží | $E_t(P_t)$ |
| Strnulých cen (M.S.C.) | Ne | Zboží | $E_{t-1}(P_t)$ |

**Implikace pro délku hospodářského cyklu:**
- M.M.I. & M.N.I.: Cyklus trvá jen po dobu „zmatení" (1–2 měsíce).
- M.S.M. & M.S.C.: Cyklus trvá po celou dobu platnosti smluv.

## Cyklické chování reálných mezd $W/P$

| Model | Cyklické chování $W/P$ | Mechanismus |
|---|---|---|
| **M.S.M.** | Proticyklické | $P \uparrow \implies W/P \downarrow$ |
| **M.M.I.** | Proticyklické | $P \uparrow \implies P/P^e \uparrow \implies W/P \downarrow$ |
| **M.N.I.** | Procyklické | $P_{OUT} \uparrow \implies L, W/P \uparrow$ |
| **M.S.C.** | Procyklické | $\text{AD} \uparrow \implies Y \uparrow \implies L^D \uparrow \implies W/P \uparrow$ |
| **Realita** | Procyklické | Navíc závisí na úrovni konkurence a cykličnosti marží (mark-up) |

## Dlouhodobá křivka AS

V dlouhém období jsou ceny plně flexibilní, $P = P^e$, takže:
$$Y = Y^* + \alpha(P - P^*) \implies Y = Y^*$$

**Dlouhodobá AS je vertikální** na úrovní potenciálního produktu $Y^*$ — platí pro všechny keynesiánské modely.
