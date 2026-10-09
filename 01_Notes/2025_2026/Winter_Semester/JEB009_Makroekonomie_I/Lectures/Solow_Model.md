---
course: "JEB009"
topic: "Solow model ekonomického růstu"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_4.pdf"
tags: [JEB009, makroekonomie, Solow, hospodářský-růst, stálý-stav, zlaté-pravidlo]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_4.pdf]]
Related: [[Neoklasicky_Model]], [[AS_Modely_Agregátní_Nabídky]]

# Solow model ekonomického růstu

## Motivace a stylizovaná fakta

- Většina ekonomik vykazuje dlouhodobou tendenci k hospodářskému růstu.
- Obrovské mezinárodní rozdíly v životní úrovni: USA GDP/capita ≈ 85 809 USD (2024), Burundi ≈ 154 USD (0,18 %).
- **Konvergence:** Bohatší země rostou pomaleji (Japonsko 8,2 %, Německo 5,7 %, USA 2,2 % v 1948–1972).
- Základní model: **Solow (1956)** — exogenní technologický pokrok.

## Solow model bez populačního a technologického růstu

### Předpoklady

- Produkční funkce s CRS: $Y = F(K; L)$.
- Odvozujeme v *per-capita* tvaru: $y = Y/L$, $k = K/L$, $y = f(k)$.
- Spotřební funkce: $c = (1-s) \cdot y$ (pevná míra úspor $s$).
- Kapitál se opotřebovává mírou $\delta$.

### Pohybová rovnice kapitálu

Hrubé investice $= s \cdot y = s \cdot f(k)$, efektivní opotřebení $= \delta \cdot k$:

$$\dot{k} = s \cdot f(k) - \delta \cdot k$$

### Stálý stav (*Steady State*)

Definován jako $\dot{k} = 0$:

$$s \cdot f(k^*) = \delta \cdot k^*$$

- Pro $k < k^*$: $s \cdot f(k) > \delta \cdot k \implies \dot{k} > 0$ (économika roste k $k^*$)
- Pro $k > k^*$: $s \cdot f(k) < \delta \cdot k \implies \dot{k} < 0$ (ekonomika klesá k $k^*$)

Stálý stav je **stabilní**.

### Determinanty $k^*$

| Změna parametru | Efekt na $k^*$ | Mechanismus |
|---|---|---|
| $s \uparrow$ | $k^* \uparrow$ | Proporcionální posun $s \cdot f(k)$ nahoru |
| $\delta \uparrow$ | $k^* \downarrow$ | Strmější přímka opotřebení |
| $A \uparrow$ (technologie) | $k^* \uparrow$ | Posun produkční funkce |

**Pozor:** Nárůst $s$ zvyšuje $y^*$, ale spotřeba $c = (1-s) \cdot y$ může zpočátku **klesat**!

## Zlaté pravidlo stálého stavu

Hledáme míru úspor $s^{**}$, která maximalizuje spotřebu ve stálém stavu $c^* = f(k^*) - \delta \cdot k^*$.

$$\max_{k^*} c^* = f(k^*) - \delta \cdot k^*$$

FOC:
$$\frac{\partial c^*}{\partial k^*} = f'(k^{**}) - \delta = 0 \implies \boxed{MPK = f'(k^{**}) = \delta}$$

Problém zlatého pravidla — jak se k $s^{**}$ dostat: přechod vyžaduje počáteční pokles spotřeby, jehož NPV musí být kladná, aby byl přechod vhodný.

## Přidání růstu populace

Pracovní síla roste konstantní mírou $n$: $\dot{L}/L = n$.

Pohybová rovnice per-capita kapitálu:

$$\dot{k} = s \cdot f(k) - (n + \delta) \cdot k$$

Stálý stav:
$$s \cdot f(k^*) = (n + \delta) \cdot k^*$$

Zlaté pravidlo:
$$MPK = f'(k^{**}) = n + \delta$$

**Implikace:** Země s rychlejším populačním růstem $n$ jsou bohatší v méně — nová pracovní síla musí být vybavena kapitálem.

## Přidání technologického pokroku

Produkční funkce s *labour-augmenting* technologií:

$$Y = F(K; A \cdot L), \quad \dot{A}/A = g$$

Per-capita v jednotkách efektivní práce: $\tilde{y} = Y/(AL)$, $\tilde{k} = K/(AL)$, $\tilde{y} = f(\tilde{k})$.

Pohybová rovnice:
$$\dot{\tilde{k}} = s \cdot f(\tilde{k}) - (n + g + \delta) \cdot \tilde{k}$$

Stálý stav:
$$s \cdot f(\tilde{k}^*) = (n + g + \delta) \cdot \tilde{k}^*$$

Zlaté pravidlo:
$$MPK = f'(\tilde{k}^{**}) = n + g + \delta$$

**Implikace ve stálém stavu:**

| Veličina | Růstová míra ve SS |
|---|---|
| $\tilde{k} = K/(AL)$ | 0 |
| $K/L$ (per-capita kapitál) | $g$ |
| $K$ (celkový kapitál) | $n + g$ |
| $Y/L$ (per-capita HDP) | $g$ |
| $Y$ (celkové HDP) | $n + g$ |

## Solow reziduál — Growth accounting

Produkční funkce Cobb-Douglas: $Y = A \cdot K^\alpha \cdot L^{1-\alpha}$

Logaritmická diferenciace:
$$\frac{\dot{Y}}{Y} = \frac{\dot{A}}{A} + \alpha \frac{\dot{K}}{K} + (1-\alpha) \frac{\dot{L}}{L}$$

**Solow reziduál (TFP growth):**
$$\frac{\dot{A}}{A} = \frac{\dot{Y}}{Y} - \alpha \frac{\dot{K}}{K} - (1-\alpha) \frac{\dot{L}}{L}$$

Zachycuje veškerý růst nevysvětlený akumulací výrobních faktorů.

## Modifikace a rozšíření Solowova modelu

1. **Ramsey–Cass–Koopmans (RCK) model** — endogenizace míry úspor $s$ (optimalizace domácností v čase).
2. **Endogenní technologie** — R&D modely (Romer, Aghion–Howitt).
3. **Zahrnutí lidského kapitálu** — Mankiw–Romer–Weil (1992).
