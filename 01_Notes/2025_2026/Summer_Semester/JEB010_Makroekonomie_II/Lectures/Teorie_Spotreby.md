---
course: JEB010
topic: Teorie spotřeby
source: 00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_9.pdf
tags: [JEB010, spotřeba, permanentní-důchod, životní-cyklus, Friedman, Modigliani]
created: 2026-04-22
---

Parent: [[JEB010_Makroekonomie_II_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB010_Makroekonomie_II/Lectures/Makro_2_Prednaska_9.pdf]]
Related: [[Intertemporalni_a_Intratemporalni_Substituce]], [[Barro_Ricardanska_Ekvivalence]], [[Teorie_Realnych_Hospodarskych_Cyklu]]

# Teorie spotřeby

Spotřeba tvoří kolem 50 % HDP a je jednou z nejstabilnějších složek. Její podíl na HDP je většinou proticyklický.

## 1. Keynesiánská spotřební funkce

$$C = C_A + c \cdot Y \quad \text{nebo} \quad C = C(Y_D)$$

kde $C_A > 0$ je autonomní spotřeba a $c \in (0,1)$ je mezní sklon ke spotřebě.

$$MPC = \frac{dC}{dY} = c \qquad APC = \frac{C}{Y} = c + \frac{C_A}{Y}$$

**Vlastnost:** $APC \geq MPC$ (průměrný sklon je vždy vyšší než mezní sklon).

## 2. Teorie reálných hospodářských cyklů — spotřeba

- Intratemporální substituce: $C = C(W/P)$
- Intertemporální substituce: $C = C(r)$
- Barro-Ricardánská ekvivalence (viz [[Barro_Ricardanska_Ekvivalence]])

## 3. Friedmanův model permanentního důchodu

$$M^D/P = M^D/P(Y_P; E_B; E_M; E_A; \pi^E) \Rightarrow C = C(Y_P; \pi^E)$$

Spotřeba závisí na **permanentním důchodu** $Y_P$ (dlouhodobá aproximace důchodu):

$$C = c \cdot Y_P \Rightarrow APC = \frac{C}{Y} = c \cdot \frac{Y_P}{Y}$$

Aktuální důchod $Y = Y_P + Y_T$ (permanentní + tranzitorní složka).

### Kuznetzova hádanka — vysvětlení

Proč APC klesá v krátkém období, ale je stabilní v dlouhém?

- Krátkodobě: $\uparrow Y$ → spotřebitelé nevědí, zda jde o $\uparrow Y_P$ nebo $\uparrow Y_T$ → zpočátku přisoudí nárůstu $Y_T$ → $Y_P = const$, $\downarrow Y_P/Y$, $\downarrow APC$
- Dlouhodobě: Pokud $\uparrow Y$ potvrzeno → $Y_P$ se zvyšuje proporcionálně → $APC$ stabilní

### Adaptivní očekávání permanentního důchodu

$$Y_t^P = Y_{t-1} + \Theta(Y_t - Y_{t-1}) = \Theta \cdot Y_t + (1-\Theta) \cdot Y_{t-1}$$

Ekvivalentně (Koyckova transformace):
$$Y^P = (1-\lambda) \cdot \sum_i \lambda^i \cdot Y_{t-i} \qquad \text{(dynamický multiplikátor)}$$

Racionální očekávání: $Y \approx N(Y^{P*}; \sigma)$ — permanentní důchod se mění jen s nepředvídanou informací.

## 4. Fisherův model s likviditním omezením

Intertemporální BC:
$$c_t + \frac{c_{t+1}}{1+i} = y_t + \frac{y_{t+1}}{1+i} + \frac{b_{t-1}(1+i)}{P} - \frac{b_{t+1}}{P(1+i)}$$

**Likviditní omezení:** Spotřebitelé nemohou si půjčovat na základě budoucích příjmů.

- **Krátkodobě:** Likviditní omezení aktivní → $\Delta C < \Delta Y$ → $MPC = \Delta C / \Delta Y < 1$
- **Dlouhodobě:** Likviditní omezení neaktivní → $\Delta C = \Delta Y$ → $MPC = 1$

Toto vysvětluje Kuznetzovu hádanku: krátkodobá PK je plošší (MPC<1), dlouhodobá strmější (MPC=1).

## 5. Duesenberyho socio-psychologická hypotéza spotřeby

**Předpoklady:**
- Dlouhodobá proporcionalita mezi $C$ a $Y$
- Spotřebitelé udržují spotřebu krátkodobě stabilní (rituály, sociální status, Veblenova okázalá spotřeba)
- Rigidita spotřeby směrem dolů

Funkce úspor jako podíl na historicky maximálním příjmu $Y_{MAX}$:

$$\frac{S}{Y} = a \cdot \frac{Y}{Y_{MAX}} + b$$

Odvozená spotřební funkce:

$$C = (1-b) \cdot Y - a \cdot \frac{Y^2}{Y_{MAX}}$$

Vysvětluje proticyklický APC: v recesi spotřebitelé šetří méně (ochrání spotřebu), v expanzi více.

## 6. Modiglianino hypotéza životního cyklu (HŽC)

Ekonomické subjekty plánují spotřebu a úspory přes celý život (vyhlazování spotřeby):

**Předpoklady:**
- Pracuje od $t=0$, odchází do důchodu ve věku $R$, umírá ve věku $T$
- Během práce: příjem $Y$; v důchodu: nulový příjem
- Vyhlazování spotřeby: $c_1 = c_2 = ... = c_T$ (nulové úroky implicitně)
- Žádné počáteční bohatství, žádná nejistota

**Rovnováha:**
$$C \cdot T = R \cdot Y \Rightarrow C = \frac{R}{T} \cdot Y$$
$$MPC = APC = \frac{R}{T}$$

**Úspory a bohatství:**
$$S = Y - C = \frac{T-R}{T} \cdot Y$$
$$W_{MAX} = R \cdot S = C \cdot (T-R) \qquad W_t = t \cdot S = t \cdot \frac{T-R}{T} \cdot Y$$

### S počátečním bohatstvím $W$:

V čase $t$ (zbývá $T-t$ let, $R-t$ let do důchodu):
$$C = \frac{W}{T-t} + \frac{R-t}{T-t} \cdot Y$$

### Vysvětlení Kuznetzovy hádanky:

$$APC = \frac{C}{Y} = \frac{1}{T-t} \cdot \frac{W}{Y} + \frac{R-t}{T-t}$$

- **Krátkodobě:** $\uparrow Y$ nemění $W$ → $\downarrow W/Y$ → $\downarrow APC$
- **Dlouhodobě:** $\uparrow Y$ vyvolá $\uparrow W$ → $APC$ se nemění

### Implikace HŽC

- Úspory se mění v různých životních fázích (mladí více spoří než důchodci — ale empiricky důchodci nerozdávají úspory dle HŽC)
- Agregované úspory závisí na **demografické struktuře** populace
- Penzijní pojištění: nárůst daní + penzí → pokles soukromých úspor
- Možná rozšíření: nejistota (opatrnostní úspory), dědictví (altruismus), úrokové sazby

## Srovnání teorií spotřeby

| Teorie | Determinant $C$ | $MPC_{SR}$ | $MPC_{LR}$ |
|---|---|---|---|
| Keynesiánská | $Y$ nebo $Y_D$ | $c < 1$ | $c < 1$ |
| RBC | $W/P$, $r$ | závisí | závisí |
| Permanentní důchod (Friedman) | $Y_P$ | blízko 0 | $c$ |
| Životní cyklus (Modigliani) | $W$, $Y$, $R/T$ | $R/T$ (krát.) | $R/T$ |
| Fisher s likvid. omez. | $y_t$ (krátkodobě) | $< 1$ | $= 1$ |
| Duesenbery | $Y$, $Y_{MAX}$ | $<$ APC | $=$ APC |
