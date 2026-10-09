---
course: "JEB009"
topic: "Keynesiánská ekonomie a model Důchod–výdaje"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_7.pdf"
tags: [JEB009, makroekonomie, keynesiánství, multiplikátor, spotřeba, fiskální-politika]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_7.pdf]]
Related: [[IS_LM_Model]], [[AD_AS_Model]], [[01_Notes/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Teorie_Investic]], [[AS_Modely_Agregátní_Nabídky]]

# Keynesiánská ekonomie a model Důchod–výdaje

## Historické pozadí

**Velká deprese 1929–1933:**
- Propad akciového trhu: říjen 1929 o 37 %; 3. 9. 1929 – 8. 8. 1932 o 90 %
- Bankrot 9 000 bank
- HNP klesl o 30 %, nezaměstnanost z 3 % na 25 %

**Změna teorie a politiky:**
- *New Deal* (Roosevelt, 1933–37)
- J. M. Keynes: *Obecná teorie zaměstnanosti, úroku a peněz* (1936)

## Klíčové předpoklady keynesiánského modelu

1. Ekonomika **pod úrovní potenciálního produktu**.
2. Ceny se **nemění** (nekonečně pružná AS → horizontální).
3. Firmy mohou prodat jakékoli množství výstupu (pokud je po něm poptávka).
4. **Výstup určen efektivní poptávkou** — negace neoklasického Sayova zákona.

## Keynesiánská teorie spotřeby

Spotřeba závisí na disponibilním důchodu (nikoli na $W/P$ jako v neoklasice):

$$C = C_A + c \cdot Y$$

kde $C_A$ je autonomní spotřeba a $c = MPC$ je mezní sklon ke spotřebě ($0 < c < 1$).

**Průměrný sklon ke spotřebě:** $APC = C/Y = c + C_A/Y > c$ (klesá s $Y$)

**Úspory:**
$$S = Y - C = -C_A + (1-c) \cdot Y = -C_A + s \cdot Y$$

kde $s = 1 - c$ je mezní sklon k úsporám.

## Keynesiánská teorie investic

Na rozdíl od neoklasiky: Investice závisí na **očekávaných budoucích cash flows** zachycených čistou současnou hodnotou:

$$NPV = -CF_0 + \frac{CF_1}{1+DF} + \frac{CF_2}{(1+DF)^2} + \frac{CF_3}{(1+DF)^3} + \ldots$$

**Internal Rate of Return (IRR):** Taková diskontní míra $DF$, při níž $NPV(I) = 0$.

Pravidlo: Pokud $IRR > i \implies$ investice provedena $\implies I = I(i)$, přičemž $\partial I/\partial i < 0$.

## Model Důchod–výdaje (základní verze)

**Předpoklady:** $I = I_A$ (exogenní investice — upustíme v IS-LM modelu).

Agregované výdaje:
$$AE = C + I = C_A + c \cdot Y + I_A = A + c \cdot Y$$

kde $A = C_A + I_A$ jsou autonomní výdaje.

**Rovnováha** ($AE = Y$):
$$Y^* = A + c \cdot Y^* \implies \boxed{Y^* = \frac{1}{1-c} \cdot A = \mu \cdot A}$$

kde $\mu = \frac{1}{1-c} = \frac{1}{s}$ je **keynesiánský multiplikátor**.

**Efekt multiplikátoru — alternativní odvození (kola výdajů):**

| Kolo | $\Delta AE$ | Kumulativní $\Delta Y$ |
|---|---|---|
| 1 | $\Delta A$ | $\Delta A$ |
| 2 | $c \cdot \Delta A$ | $(1+c) \cdot \Delta A$ |
| 3 | $c^2 \cdot \Delta A$ | $(1+c+c^2) \cdot \Delta A$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $\infty$ | | $\frac{1}{1-c} \cdot \Delta A$ |

## Přidání veřejného sektoru

Daně: $TA = t \cdot Y$ (proporcionální)  
Transfery: $TR$ (autonomní)  
Vládní výdaje: $G_A$ (autonomní)

Spotřební funkce:
$$C = C_A + c \cdot Y_D = C_A + c \cdot (Y - TA + TR)$$

Agregované výdaje:
$$AE = C_A + c(Y - tY + TR_A) + G_A + I_A = A + c(1-t) \cdot Y$$

**Rovnovážný výstup:**
$$\boxed{Y^* = \frac{1}{1 - c(1-t)} \cdot A = \mu_t \cdot A}$$

kde $\mu_t = \frac{1}{1-c(1-t)}$ je **multiplikátor s daněmi** ($\mu_t < \mu$).

Přebytek státního rozpočtu:
$$BS = TA - G - TR = t \cdot Y - G - TR$$

**Cyklicky očištěný (strukturální) přebytek:**
$$BS^P = t \cdot Y^P - G - TR$$
$$BS = BS^P + t \cdot (Y - Y^P) \quad \text{(strukturální + cyklická složka)}$$

### Reakce přebytku na výdajový šok $\Delta G$

$$\Delta Y = \mu_t \cdot \Delta G = \frac{\Delta G}{1-c(1-t)}$$
$$\Delta BS = t \cdot \Delta Y - \Delta G = \frac{t}{1-c(1-t)} \cdot \Delta G - \Delta G = \left(\frac{t}{1-c(1-t)} - 1\right) \Delta G < 0$$

Přebytek klesá o méně než $\Delta G$ — **automatické stabilizátory** ($t$) tlumí dopad.

## Multiplikátor vyrovnaného rozpočtu (Haavelmův teorém)

Simultánní nárůst $G$ a $TA$ o stejnou částku tak, aby $\Delta BS = 0$:

Podmínka $\Delta BS = 0 \implies \Delta TA = \Delta G$:

$$AE = c(Y - \Delta G) + \Delta G$$
$$Y(1-c) = \Delta G(1-c) \implies \Delta Y = \Delta G$$

$$\boxed{\mu_{balanced} = \frac{\Delta Y}{\Delta G} = 1}$$

Multiplikátor vyrovnaného rozpočtu = **1** bez ohledu na hodnotu $c$ (Haavelmo 1945).

## Přidání zahraničí

Import závisí na důchodu: $M = M_A + m \cdot Y$

$$AE = C + I + G + NX = C + I + G + X_A - (M_A + m \cdot Y)$$

Rovnovážný výstup:
$$Y^* = \frac{1}{1 - c(1-t) + m} \cdot (C_A + I_A + G_A + TR_A \cdot c + X_A - M_A)$$

Multiplikátor v otevřené ekonomice je **menší** než $\mu_t$ (část stimulu „uniká" do dovozu).

## Pravidla rozpočtové odpovědnosti (EU)

| Pravidlo | Podmínka |
|---|---|
| **Dluhové** | Dluh/HDP $< 60\%$; nebo klesá o $\geq 1/20$ ročně |
| **Deficitní** | Deficit sektoru vl. institucí $< 3\%$ HDP |
| **Strukturálního salda** | Strukturální saldo $>$ MTO nebo $\Delta BS_{struct} > 0{,}5\%$ |
| **Výdajové** | Reálný růst upravených výdajů $<$ 10Y průměr $g_{Y^P}$ |
