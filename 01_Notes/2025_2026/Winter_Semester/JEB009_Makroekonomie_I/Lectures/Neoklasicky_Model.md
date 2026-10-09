---
course: "JEB009"
topic: "Neoklasický model — firmy, domácnosti, trhy"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_1_3.pdf"
tags: [JEB009, makroekonomie, neoklasika, produkční-funkce, trh-práce, klasická-dichotomie]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_1_3.pdf]]
Related: [[Solow_Model]], [[Mereni_HDP]], [[AS_Modely_Agregátní_Nabídky]], [[Vymezeni_a_Metody_Makroekonomie]]

# Neoklasický model

## Předpoklady neoklasické ekonomie

- Přibližně platný do 50. let (před Keynesem).
- Důraz na **mikroekonomické základy** — reprezentativní firma/domácnost.
- **Trhy se vyčišťují** (*market clearing*): $S = D$ na všech trzích.
- Dokonalá konkurence, nulové transakční náklady, dokonalá informovanost, dokonalá vymahatelnost kontraktů.
- **Finanční systém nahrazen kapitálovým trhem** (implicitní předpoklady).

## Firmy

Existuje mnoho firem (nebo jedna reprezentativní) — nemohou ovlivnit žádnou cenu ($P$, $W$, $i$).

### Produkční funkce

$$Y = F(K; L), \quad F_L > 0, \quad F_{LL} < 0 \quad \text{(kladný klesající MPL)}$$

**Konstantní výnosy z rozsahu (CRS):**
$$F(zL; zK) = z \cdot F(K; L) \implies F(K; L) = \frac{\partial F}{\partial L} \cdot L + \frac{\partial F}{\partial K} \cdot K$$

### Typy produkčních funkcí

| Typ | Funkční forma | Limitní vlastnosti |
|---|---|---|
| **Lineární** | $F(L) = a \cdot L$ | Konstantní MPL |
| **Cobb-Douglas** | $F(K;L) = A \cdot K^\alpha \cdot L^{1-\alpha}$ | Pro $\gamma \to 0$ v CES |
| **Leontief** | $F(K;L) = \min[aK;\, bL]$ | Pro $\gamma \to -\infty$ v CES |
| **CES** | $F(K;L) = A[\theta(a_K K)^\gamma + (1-\theta)(a_L L)^\gamma]^{1/\gamma}$ | Obecná forma |

**Zachycení technologie:**
- Labour-augmenting (Harrod-neutral): $F(K; A \cdot L) = K^\alpha (AL)^{1-\alpha}$
- Capital-augmenting: $F(AK; L) = (AK)^\alpha L^{1-\alpha}$
- Hicks-neutral: $F(K; L) = A \cdot K^\alpha L^{1-\alpha}$

### Maximalizace zisku

$$\max_{K,L} \Pi = P \cdot F(K;L) - W \cdot L - i \cdot K$$

Podmínky prvního řádu (FOC):
$$\frac{\partial \Pi}{\partial L} = 0: \quad P \cdot MPL = W \implies MPL = \frac{W}{P}$$
$$\frac{\partial \Pi}{\partial K} = 0: \quad P \cdot MPK = i \implies MPK = \frac{i}{P} \equiv r$$

**Zisk v optimu** (Eulerova věta pro CRS):
$$\Pi^* = P \cdot [F(K;L) - MPL \cdot L - MPK \cdot K] = 0$$

## Domácnosti

$$\max_{C, L} U(C; L) \quad \text{s.t.} \quad P \cdot C \leq W \cdot L$$

V optimu je míra substituce práce za spotřebu rovna $W/P$ (reálná mzda).

## Trhy v neoklasickém modelu

Systém čtyř trhů v rovnováze:

### 1. Trh práce
Rovnováha: $L^D(W/P) = L^S(W/P) \implies (W/P)^*, L^*$

### 2. Trh zboží
$$Y^S = F(K; L^*), \quad Y^D = C\left(\frac{W}{P}\right) + I(r) + G$$
Rovnováha: $Y^S = Y^D \implies Y^* = Y^P$

### 3. Kapitálový trh (trh zápůjčních fondů)
$$I(r) = S(r) \implies r^*$$

### 4. Trh peněz — Klasická dichotomie

Neoklasika **odděluje** reálnou a peněžní ekonomiku (*klasická dichotomie*):
- Reálné veličiny ($Y$, $r$, $W/P$) určeny reálnými faktory.
- Peněžní trh určuje pouze cenovou hladinu $P$ prostřednictvím **kvantitativní teorie peněz**:

$$M^D = \frac{1}{v} P Y \implies M \cdot v = P \cdot Y$$

kde $v$ je rychlost obratu peněz.

## Komparativní statika neoklasického modelu

### Expanze agregátní poptávky (posun AD)
Výsledek: zvýšení $P$, $Y$ zůstává na $Y^P$ — peníze jsou **neutrální**.

### Efekt imigrace
$L^S$ roste $\to$ $W/P$ klesá $\to$ $L^*$ roste $\to$ $Y^*$ roste, $r$ klesá (více investic).

### Efekt eroze půdy (technologický regres)
$A$ klesá $\to$ $MPL$, $MPK$ klesají $\to$ $LD$ se posouvá doleva $\to$ $Y^*$ klesá, $r$ klesá.
