---
course: JEB010
topic: Modely agregátní nabídky (AS)
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_2.pdf
tags: [JEB010, AS, agregátní-nabídka, sticky-wage, Lucas, nová-keynesiánská-ekonomie]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_2.pdf]]
Related: [[Ocekavani_v_Makroekonomii]], [[Model_DAD_DAS]], [[Nova_Keynesianska_Ekonomie]]

# Modely agregátní nabídky (AS)

Všechny čtyři standardní modely krátkodobé agregátní nabídky dospívají ke stejné výsledné rovnici:

$$\boxed{Y = Y^* + \alpha(P - P^e)}$$

kde $Y^*$ je přirozená úroveň výstupu, $P$ je skutečná cenová hladina a $P^e$ je očekávaná cenová hladina. Rozdíl v mechanismu přenosu se liší.

## Model 1: Strnulé mzdy (Sticky Wage Model)

*Autorem je nespecifikovaný ekonom; zachycuje keynesiánskou rigiditu nominálních mezd.*

### Assumptions

- Nominální mzda $W$ je sjednána předem na základě očekávané cenové hladiny:
$$W = \omega \cdot P^e$$
kde $\omega$ je cílová reálná mzda.
- Trh práce se nevyčišťuje ihned; zaměstnanost určuje firma.

### Mechanismus

Skutečná reálná mzda:
$$\frac{W}{P} = \omega \cdot \frac{P^e}{P}$$

Pokud $P < P^e$: reálná mzda roste → firmy snižují poptávku po práci ($L_D$) → roste nezaměstnanost → klesá $Y$.

Pokud $P > P^e$: reálná mzda klesá → firmy zvyšují $L_D$ → roste $Y$.

**Výsledek:** $Y = Y^* + \alpha(P - P^e)$; $\alpha > 0$

## Model 2: Mzdová iluze (Worker Misperception Model)

*Friedman (1968) — základní model Phillipsovy křivky.*

### Assumptions

- Trhy se vyčišťují (tržní rovnováha v každém období).
- Pracovníci vnímají nominální mzdu $W$ jako signál o reálné mzdě, ale chybně odhadují cenovou hladinu: nabídka práce závisí na $W/P^e$, nikoli $W/P$.

$$L^S = L^S\!\left(\frac{W}{P^e}\right)$$

### Mechanismus

Pokud $P > P^e$: firmy vidí vyšší reálnou cenu jejich produktu → zvyšují poptávku po práci. Pracovníci vidí vyšší $W$, myslí si, že $W/P$ roste (protože neznají $P$) → zvyšují nabídku práce. Rovnováha na trhu práce je vyšší → roste $Y$.

**Výsledek:** $Y = Y^* + \alpha(P - P^e)$

## Model 3: Nedokonalé informace (Imperfect Information Model)

*Lucas (1972) — model „mlhy".*

### Assumptions

- Firmy znají vlastní výstupní cenu, ale neznají celkovou cenovou hladinu.
- Z lokálního cenového signálu nemohou určit, zda jde o relativní nebo absolutní cenový pohyb.

### Mechanismus

Firma vidí $\uparrow P_i$ (cena jejího produktu). Část pohybu přisuzuje zvýšení relativní ceny (poptávkový posun) → zvyšuje výstup. Část přisuzuje inflaci → nereaguje.

Parametr $\alpha$ závisí na:
- Variabilitě poptávky v daném odvětví
- Historické variabilitě inflace v dané zemi (v zemích s vysokou inflací je $\alpha$ nižší — firmy ví, že cenový signál je většinou inflační šum)

**Výsledek:** $Y = Y^* + \alpha(P - P^e)$

## Model 4: Strnulé ceny (Sticky Price Model)

*Nová keynesiánská ekonomie — firmy s tržní silou versus cenoví příjemci.*

### Assumptions

Firmy se dělí na dvě skupiny:
- **Price makers** (podíl $1-s$): nastavují ceny s předstihem na základě očekávání:
$$p^T = P^E + a(Y^E - Y^{*E})$$
- **Price takers** (podíl $s$): reagují okamžitě na aktuální podmínky:
$$p^P = P + a(Y - Y^*)$$

### Derivace

Agregovaná cenová hladina (vážený průměr):

$$P = s \cdot p^P + (1-s) \cdot p^T = s[P + a(Y-Y^*)] + (1-s)[P^E + a(Y^E - Y^{*E})]$$

Po zjednodušení (předpoklad $Y^E = Y^*$ pro price makers):

$$P - P^E = \frac{1-s}{s} \cdot a \cdot (Y - Y^*)$$

Tedy inverzně:
$$Y = Y^* + \frac{s}{(1-s)a}(P - P^E)$$

**Výsledek:** $Y = Y^* + \alpha(P - P^e)$ kde $\alpha = \frac{s}{(1-s)a}$

Vyšší podíl flexibility ($s$ malé) → strmější AS → menší reálný efekt šoku.

## Srovnání modelů

| Model | Klíčová rigidita | Trh práce |
|---|---|---|
| Strnulé mzdy | Nominální mzda | Nevyčišťuje se |
| Mzdová iluze | Informace pracovníků | Vyčišťuje se |
| Nedokonalé informace | Informace firem | Vyčišťuje se |
| Strnulé ceny | Nominální ceny | — |

## Grafické znázornění

- **Krátkodobá AS (SAS):** rostoucí křivka $Y = Y^* + \alpha(P-P^e)$
- **Dlouhodobá AS (LAS):** vertikála $Y = Y^*$ (v dlouhém období $P^e = P$)
- Šok $\uparrow P^e$: SAS se posouvá nahoru → stagflace při neakomodativní politice
