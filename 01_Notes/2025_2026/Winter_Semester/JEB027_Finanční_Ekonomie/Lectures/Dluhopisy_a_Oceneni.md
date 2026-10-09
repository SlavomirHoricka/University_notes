---
course: "JEB027"
topic: "Dluhopisy a jejich oceňování — kupon, YTM, durace, konvexita, kreditní riziko"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P03-2025_Financni_instrumenty_final.pdf"
tags: [JEB027, dluhopisy, YTM, durace, konvexita, kreditni-riziko, rating]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P03-2025_Financni_instrumenty_final.pdf]]
Related: [[Financni_Instrumenty]], [[Urokova_Mira_a_Casova_Hodnota_Penez]], [[Financni_Trhy]], [[Bancni_Regulace_a_Basel]]

# Dluhopisy a jejich oceňování

## Základní charakteristiky dluhopisu

Dluhopis (bond, obligace) je dluhový cenný papír. Emitent (issuer) přijímá prostředky od investorů a zavazuje se:
- Platit pravidelné **kuponové platby** $C$ (obvykle pololetně nebo ročně)
- Splatit **nominální hodnotu (face value / par value)** $F$ při splatnosti $T$

### Klíčové parametry

| Parametr | Označení | Popis |
|----------|----------|-------|
| Nominální hodnota | $F$ | Jmenovitá hodnota, splatná při maturitě (typicky 1 000 CZK či 1 000 USD) |
| Kuponová sazba | $c$ | Fixní procento z $F$; roční kupon $C = c \cdot F$ |
| Splatnost | $T$ (maturity) | Datum splacení jistiny |
| Tržní cena | $P$ | Aktuální cena na sekundárním trhu |
| Výnos do splatnosti | YTM, $r$ | Vnitřní výnosové procento (IRR) při nákupu za $P$ a držení do splatnosti |

## Oceňování dluhopisu

Cena dluhopisu je **součet současných hodnot** všech budoucích cash flows při diskontní sazbě YTM:

$$P = \sum_{t=1}^{n} \frac{C}{(1+r)^t} + \frac{F}{(1+r)^n}$$

Pomocí vzorce pro anuitu:

$$\boxed{P = C \cdot \frac{1 - (1+r)^{-n}}{r} + \frac{F}{(1+r)^n}}$$

**Klíčový vztah (inverzní):** $P \uparrow \Leftrightarrow r \downarrow$ a vice versa.

### Speciální případy

- **Dluhopis na pari (at par):** $P = F \Leftrightarrow c = r$
- **Dluhopis pod pari / s diskontem (below par):** $P < F \Leftrightarrow c < r$
- **Dluhopis nad pari / s prémií (above par):** $P > F \Leftrightarrow c > r$

### Bezkuponový dluhopis (Zero-coupon bond)

Bez průběžných kuponů — veškerý výnos pochází z rozdílu mezi nákupní cenou a nominální hodnotou:

$$P = \frac{F}{(1+r)^n}$$

YTM lze vyjádřit jako:

$$r = \left(\frac{F}{P}\right)^{1/n} - 1$$

## Durace (Duration)

**Macaulayova durace** je váženým průměrem dob do inkasování cash flows, kde váhy jsou podíly PV jednotlivých CF na ceně dluhopisu:

$$D_{Mac} = \frac{\sum_{t=1}^{n} t \cdot \frac{CF_t}{(1+r)^t}}{P}$$

Durace měří **průměrnou dobu splatnosti** nebo citlivost ceny na malé změny YTM.

**Modifikovaná durace** (Modified Duration) přímo vyjadřuje procentní citlivost ceny na absolutní změnu YTM:

$$D_{Mod} = \frac{D_{Mac}}{1+r}$$

$$\frac{\Delta P}{P} \approx -D_{Mod} \cdot \Delta r$$

Příklad: Dluhopis s $D_{Mod} = 5$ ztratí přibližně 5 % hodnoty při vzrůstu YTM o 1 procentní bod (100 bps).

## Konvexita (Convexity)

Modifikovaná durace je lineární aproximace — pro větší změny YTM je nutno zohlednit **konvexitu** (zakřivení vztahu P-r):

$$\frac{\Delta P}{P} \approx -D_{Mod} \cdot \Delta r + \frac{1}{2} \cdot \text{Convexity} \cdot (\Delta r)^2$$

$$\text{Convexity} = \frac{1}{P \cdot (1+r)^2} \sum_{t=1}^{n} t(t+1) \cdot \frac{CF_t}{(1+r)^t}$$

Konvexita je vždy kladná pro standardní dluhopisy (long positions). Vyšší konvexita je výhodná: dluhopis roste více při poklesu sazeb a klesá méně při vzrůstu sazeb.

## Kreditní riziko a ratingové hodnocení

### Kreditní riziko

**Kreditní riziko** je riziko, že emitent **nesplatí** závazky (default). Kompenzací za kreditní riziko je **kreditní spread** — přirážka nad bezrizikovou sazbu:

$$r_{\text{korporátní}} = r_f + \text{spread}$$

kde $r_f$ je výnos bezrizikového dluhopisu (typicky státní dluhopis nejkvalitnějšího emitenta).

### Ratingové agentury

| Agentura | Investment Grade | Spekulativní (High Yield/Junk) |
|----------|-----------------|-------------------------------|
| **Moody's** | Aaa, Aa, A, Baa | Ba, B, Caa, Ca, C |
| **S&P / Fitch** | AAA, AA, A, BBB | BB, B, CCC, CC, C, D |

**Investment grade:** BBB-/Baa3 a výše — přijatelné kreditní riziko, přístup na institucionální trh.
**High yield (junk):** Nižší než BBB-/Baa3 — vyšší spreads, omezený přístup institucionálních investorů.

## Typy dluhopisů

| Typ | Popis |
|-----|-------|
| **Státní dluhopis (sovereign)** | Emitent = stát; v ČR „státní dluhopisy" (SD) emituje MF ČR |
| **Komunální dluhopis** | Emitent = municipality |
| **Korporátní dluhopis** | Emitent = soukromá firma |
| **Hypoteční zástavní list (HZL)** | Zajištěn pohledávkami z hypotečních úvěrů |
| **Podřízený dluh** | V případě úpadku splacen až po senior dluhu, ale před akcionáři |
| **Konvertibilní dluhopis** | Možnost převodu na akcie emitenta za předem stanovených podmínek |
| **Inflačně vázaný dluhopis** | Nominál a/nebo kupony indexovány na inflaci (TIPS v USA, ČR: dluhopisy vázané na CPI) |

## Výpočet aktuálního výnosu (Current Yield)

$$\text{Current Yield} = \frac{C}{P}$$

Jednoduchá aproximace YTM — ignoruje kapitálové zisky/ztráty a složené úročení. Platí: $\text{Current Yield} \approx \text{YTM}$ pouze pokud $P \approx F$.

Viz [[Urokova_Mira_a_Casova_Hodnota_Penez]] pro základy diskontování a [[Financni_Trhy]] pro kontext obchodování s dluhopisy.
