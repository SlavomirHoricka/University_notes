---
course: JEB010
topic: Dynamický model AD-AS (DAD-DAS)
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_5.pdf
tags: [JEB010, DAD, DAS, dynamický-AD-AS, inflace, výstupní-mezera]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_5.pdf]]
Related: [[Modely_Agregatni_Nabidky_AS]], [[Ocekavani_v_Makroekonomii]], [[Inflace_a_Hyperinflace]]

# Dynamický model AD-AS (DAD-DAS)

Dynamický model agregátní poptávky a nabídky (DAD-DAS) pracuje s mírou inflace $\pi$ a výstupem $Y$ namísto cenové hladiny $P$ a $Y$ jako v statickém modelu.

## Derivace DAS (Dynamická agregátní nabídka)

DAS vychází ze standardní AS křivky:

$$Y = Y^* + \alpha(P - P^e)$$

Přepišme jako změny cenové hladiny. Výstupní mezera $\hat{Y} = Y - Y^*$:

$$P - P^e = \frac{1}{\alpha}(Y - Y^*)$$

Přeformulováno v mírách inflace ($\pi = \Delta P/P$, $\pi^e$ = očekávaná inflace):

$$\boxed{\pi = \pi^e + \frac{1}{\alpha}(Y - Y^*)}$$

Se záporným nabídkovým šokem $\varepsilon > 0$ (zdražení vstupů):

$$\pi = \pi^e + \frac{1}{\alpha}(Y - Y^*) + \varepsilon$$

### Interpretace DAS

- **Pozitivní sklon** v prostoru $(Y, \pi)$: při daných inflačních očekáváních vyšší output = vyšší inflace
- **Posuny DAS:** Změna $\pi^e$ nebo nabídkový šok $\varepsilon$ posouvá křivku vertikálně
- **Dlouhodobá DAS (LAS):** Vertikála $Y = Y^*$ (v dlouhém období $\pi = \pi^e$)

## Derivace DAD (Dynamická agregátní poptávka)

### Krok 1: IS křivka

$$Y = \alpha[A - b \cdot r]$$

kde $\alpha = 1/(1-c)$ je multiplikátor, $A$ je autonomní poptávka, $b$ je citlivost investic na úrokovou míru.

### Krok 2: LM křivka

$$i = -\frac{M}{P} \cdot \frac{1}{h} + \frac{k}{h} \cdot Y$$

kde $h$ je citlivost poptávky po penězích na $i$ a $k$ na $Y$.

### Krok 3: Fisherova rovnice

$$i = r + \pi^e \Rightarrow r = i - \pi^e$$

### Krok 4: Derivace AD

Substituujeme LM do IS (přes Fisherovu rovnici):

$$Y = \gamma A + \gamma \frac{b}{h} \frac{M}{P} + \gamma b \pi^e$$

kde $\gamma = \frac{\alpha h}{h + \alpha b k}$ je fiskální multiplikátor.

### Krok 5: Přechod na DAD

Logaritmická diferenciace AD (v mírách změn $m = \Delta M/M$, $\pi = \Delta P/P$):

$$\boxed{\pi = m + \frac{h}{b}\Delta A + h\Delta\pi^e + \frac{h}{\gamma b}Y_{t-1} - \frac{h}{\gamma b}Y_t}$$

**Interpretace:** Inflace je tím vyšší, čím vyšší je:
- Růst peněžní zásoby $m$
- Fiskální expanze $\Delta A$
- Nárůst inflačních očekávání $\Delta\pi^e$
- Nižší aktuální výstup $Y_t$ při daném $Y_{t-1}$ (pokles Y → uvolnění tlaků → vyšší inflace? ne — DAD je klesající v $Y$)

## Aplikace DAD-DAS modelu

### 1. Monetární restrikce ($\downarrow m$)

- DAD se posune doleva (nižší inflace při každém $Y$)
- Dopad: $\downarrow Y$, $\downarrow \pi$
- **Adaptivní očekávání:** DAS se postupně posouvá dolů (jak $\pi^e$ klesá) → postupná dezinflace
- **Racionální očekávání:** DAS skočí okamžitě dolů na $[Y^*, m_1]$ — bez ztráty výstupu (pokud věrohodná politika)

### 2. Sacrifice ratio (poměr obětování)

Kumulativní ztráta %HDP na 1 procentní bod snížení inflace. Pro USA (Volckerova dezinflace 1979–87): ~4,3 %.

**Faktory snižující sacrifice ratio:**
- Předběžné oznámení politiky
- Důvěryhodnost centrální banky
- Racionální očekávání
- Pomalejší dezinflace (*cold turkey* vs. *gradualism*)
- Méně nominálních rigidit

### 3. Fiskální expanze ($\uparrow A$)

- DAD se posune doprava → $\uparrow Y$, $\uparrow \pi$
- **Adaptivní očekávání:** DAS se posouvá nahoru v následujícím období → inflační spirála
- **Racionální očekávání:** Okamžitý skok DAS

### 4. Nabídkový šok ($\uparrow \varepsilon$)

DAS se posune nahoru (stagflace). Tři možné politické reakce:

| Varianta | Politika | Efekt |
|---|---|---|
| A — neutrální | $m$ nezměněno | $Y$ se vrátí k $Y^*$ časem (dočasný šok), $\pi$ přechodně ↑ |
| B — akomodativní | $\uparrow m$ (posun DAD doprava) | $Y$ stabilní, ale trvale $\uparrow\pi$ |
| C — restriktivní | $\downarrow m$ (posun DAD doleva) | $\pi$ stabilní, ale $\downarrow Y$ |

### 5. Permanentní vs. dočasný nabídkový šok

- **Dočasný:** $Y^*$ se nezmění; DAS se vrátí dolů sama bez politiky
- **Permanentní:** $Y^*$ se posune trvale → DAS se posune trvale; vhodná je restriktivní/neutrální politika

### 6. Pozitivní nabídkový šok (technologie)

DAS se posune dolů:
- Při neměnné DAD: $\uparrow Y$, $\downarrow\pi$ (ideální kombinace)
- Politický trade-off: CB může využít prostor ke snížení $\pi$ (restriktivní DAD) nebo umožnit ještě vyšší $Y$ (expanzivní DAD)
