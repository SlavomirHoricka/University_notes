---
course: JEB010
topic: Hospodářská politika a debata pravidla vs. diskrece
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_11.pdf
tags: [JEB010, stabilizační-politika, Taylorovo-pravidlo, dynamická-nekonzistence, Lucas-kritika]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_11.pdf]]
Related: [[Ocekavani_v_Makroekonomii]], [[Model_DAD_DAS]], [[Nezamestnanost]]

# Hospodářská politika a debata pravidla vs. diskrece

## Stabilizační politika — ano či ne?

### Argumenty ve prospěch

- **Riziková averze:** Volatilita výstupu negativně ovlivňuje utilitu; vyhlazení cyklu je přínosné
- **Hystereze:** Méně stabilní $Y \Rightarrow$ pomalejší $Y_P$ (hystereze v trhu práce, R&D)
- **Definitivní ztráta výstupu:** Recese mohou mít trvalé negativní efekty (zdecimování firem, lidského kapitálu)

### Argumenty proti

**Vnitřní zpoždění:**
- *Datové zpoždění:* Data dostupná se zpožděním (HDP: čtvrtletně s opravami)
- *Rozpoznávací zpoždění:* Identifikace recese trvá 2–4 čtvrtletí
- *Legislativní zpoždění:* Fiskální politika vyžaduje legislativní schválení
- *Transmisní zpoždění:* Měnová politika působí s 6–18 měsíci

**Vnější zpoždění:** Efekt politiky přichází příliš pozdě → politika může destabilizovat místo stabilizovat

**Automatické stabilizátory:** Příjmové daně, podpory v nezaměstnanosti fungují automaticky bez zpoždění

**Lucas kritika:** Standardní metody hodnocení politiky nepočítají s efektem politiky na očekávání — změna pravidel mění chování agentů, takže historické parametry model nejsou platné pro novou politiku

**Trade-off:** Stabilizace výstupu zvyšuje inflaci → vyšší inflace → pomalejší $Y_P$ → trade-off mezi krátkodobou stabilitou a dlouhodobým růstem

## Debata pravidla vs. diskrece

- **Diskrece:** Policy maker reaguje na události podle vlastního uvážení (v mezích cílů, ale volně)
- **Pravidla:** Policy maker omezen pravidly (inflační cílení, monetární cíle, fiskální pravidla)

### Proč mohou pravidla vylepšit politiku?

- Politika závisí na zájmových skupinách, politici nemají dostatečnou znalost ekonomiky
- **Politický hospodářský cyklus (Nordhaus):** Manipulace voleb ekonomickými nástroji (expanze před volbami)
- **Dynamická nekonzistence diskrétních politik:** I policy maker sdílející preference veřejnosti může dosáhnout sociálně sub-optimálního výsledku

## Dynamická nekonzistence (Kydland & Prescott, 1977)

Policy maker minimalizuje ztrátu:

$$\max_\pi L(\pi; Y) = \pi^2 + a \cdot (Y - Y^*)^2$$

za omezení (Phillipsova křivka, AS):

$$Y = Y^{**} + \alpha \cdot (\pi - \pi^E)$$

kde $Y^{**} < Y^*$ je přirozená úroveň výstupu a $Y^*$ je cílová (socially optimal) úroveň.

### Derivace

Substituujeme AS do ztrátové funkce:

$$L(\pi; Y) = \pi^2 + a \cdot [Y^{**} - Y^* + \alpha(\pi - \pi^E)]^2$$

FOC ($\partial L / \partial \pi = 0$):

$$2\pi + a \cdot 2[Y^{**} - Y^* + \alpha(\pi - \pi^E)] \cdot \alpha = 0$$

Řešení:

$$\pi = \frac{a \cdot \alpha \cdot [Y^* - Y^{**} + \alpha \pi^E]}{1 + \alpha^2 \cdot a}$$

V dlouhém období musí platit $\pi = \pi^E$ (racionální očekávání), tedy:

$$\boxed{\pi = a \cdot \alpha \cdot [Y^* - Y^{**}]}$$

**Interpretace (inflační bias):** Pokud policy maker chce $Y^* > Y^{**}$ (chce výstup nad přirozenou úrovní), výsledkem je kladná inflace i přesto, že výstup zůstane na $Y^{**}$. Pravidlo nulové inflace je sociálně lepší.

### Příklady problémů dynamické nekonzistence

- Teroristé a rukojmí (slíbit že nevyjednáváme vs. skutečnost)
- Trade-off inflace–výstup (credibility problem)
- Investiční a FDI pobídky (expropriation after investment)
- R&D a patentový monopol
- Státní vymáhání zákonů

## Typy pravidel pro měnovou politiku

| Pravidlo | Obsah | Nevýhody |
|---|---|---|
| **Monetaristické (Friedman)** | Nízký stabilní růst $M$ (3–5 % ročně) | Nestabilní rychlost oběhu peněz $V$ |
| **Cílování nominálního HDP** | Plánovaný vývoj $P \cdot Y$ | Složité komunikovat veřejnosti |
| **Taylorovo pravidlo** | $i_t = \pi_t + r_t^* + a_\pi(\pi_t - \pi_t^*) + a_y(y_t - \bar{y}_t)$ | Parametrizace, měření $r^*$ |
| **Inflační cílení** | i) cílování současné $\pi$; ii) cílování predikce $\pi$; iii) komplexní pravidla | Ignoruje output gap |

### Taylorovo pravidlo

$$\boxed{i_t = \pi_t + r_t^* + a_\pi(\pi_t - \pi_t^*) + a_y(y_t - \bar{y}_t)}$$

kde $\pi_t^*$ je inflační cíl, $\bar{y}_t$ je potenciální výstup, $r_t^*$ je přirozená reálná úroková míra. Koeficienty $a_\pi > 1$ (Taylor princip) a $a_y > 0$ zajišťují stabilizaci.
