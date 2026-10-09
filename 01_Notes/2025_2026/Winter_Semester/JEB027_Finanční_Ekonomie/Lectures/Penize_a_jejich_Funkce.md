---
course: "JEB027"
topic: "Peníze a jejich funkce — definice, měnové agregáty, peněžní multiplikátor"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P01B-2025_ZS_Penize_a_urokova_mira_final.pdf"
tags: [JEB027, penize, menove-agregaty, penezni-multiplikator, CBDc]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P01B-2025_ZS_Penize_a_urokova_mira_final.pdf]]
Related: [[Urokova_Mira_a_Casova_Hodnota_Penez]], [[Centralni_Bankovnictvi]], [[Decentralizovane_Finance]], [[Poptavka_po_Penezich]]

# Peníze a jejich funkce

## Definice peněz

### Teoretická definice

**Peníze** jsou aktivum, jež je všeobecně zúčastněnými subjekty přijímáno a používáno při placení zboží a služeb či při splácení dluhu. Tato definice je spojena se třemi klíčovými funkcemi peněz:

1. **Prostředek směny (medium of exchange):** eliminují potřebu vzájemného souhlasu potřeb (double coincidence of wants) při barteru.
2. **Zúčtovací jednotka (unit of account):** standardní měřítko hodnoty, tzv. *numéraire*.
3. **Uchovatel hodnoty (store of value):** umožňují přesun kupní síly z přítomnosti do budoucnosti.

### Empirická definice

Empirická definice peněz je spjata s potřebou predikce ekonomických veličin ovlivněných množstvím peněz (zejména inflace). Týká se **měnových (peněžních) agregátů**.

> **Poznámka:** Kryptoaktiva (např. Bitcoin) nesplňují definici peněz jako *numéraire*, protože nejsou obecně přijímaným prostředkem směny a vykazují vysokou volatilitu hodnoty. Jedná se tedy o nehmotnou movitou věc, nikoli „kryptoměnu" v pravém slova smyslu.

## Měnové (peněžní) agregáty

Měnové agregáty jsou označeny písmenem **M** a číslicí (0 až 3). S rostoucí číslicí:
- **klesá likvidita** (M0 obsahuje nejlikvidnější prostředky — oběživo),
- **roste stabilita** agregátu.

| Agregát | Obsah | Poznámka |
|---------|-------|----------|
| **M0** (Měnová báze) | Oběživo + rezervy komerčních bank u CB | Nestabilní; tvoří cca 10–12 % M2 |
| **M1** | M0 + jednodenní vklady | Nejužší „funkční" peníze |
| **M2** | M1 + krátkodobé termínované vklady, spořící vklady | Nejčastěji sledovaný agregát |
| **M3** | M2 + repo operace, fondy peněžního trhu, dluhové CP do 2 let | Nejširší agregát ECB |

Podíl oběživa (M0) na M2 je přibližně **10–12 %** (platí pro ČR i globálně).

## Měnová báze a peněžní multiplikátor

### Měnová báze (MB / M0)

$$MB = \text{Oběživo} + \text{Rezervy komerčních bank u CB}$$

Centrální banka přímo kontroluje měnovou bázi prostřednictvím svých operací (repo operace, přímý nákup/prodej aktiv).

### Peněžní multiplikátor

Peněžní multiplikátor vyjadřuje, kolikrát větší je peněžní zásoba $M2$ oproti měnové bázi $MB$:

$$m = \frac{M2}{MB}$$

**Učebnicový (monetaristický) mechanismus:** Centrální banka zvýší MB → komerční banky půjčují přebytečné rezervy → depozita a úvěry v ekonomice rostou, čímž se peněžní zásoba M2 násobí.

### Proč multiplikátor selhal v roce 2008?

Po globální finanční krizi 2007–2009 a v důsledku kvantitativního uvolňování (QE):
- Komerční banky **držely nové peníze v rezervách** u centrální banky (v M0), místo aby je přelily do reálné ekonomiky (M2).
- Důvody selhání multiplikátoru:
  1. Nedostatek poptávky po úvěrech ze strany podniků a domácností.
  2. Opatrnostní motivy bank (deleveraging, fear of credit risk).
  3. Přísnější regulatorní požadavky (Basel III — viz [[Bancni_Regulace_a_Basel]]).

$$\text{Důsledek: } \uparrow MB \;\not\Rightarrow\; \uparrow M2$$

Empiricky: "Kvantitativní uvolňování (QE) nefungovalo tak jako za standardních podmínek" (Zamrazilová, 2014).

## Nové systémy emise peněz

### Tradiční 2-úrovňový systém

1. Centrální banka emituje peníze prostřednictvím **komerčních bank (Tier 1)**.
2. Komerční banky distribuují peníze uživatelům — domácnostem a firmám **(Tier 2)**.

### Digitální peníze centrální banky (CBDC)

**CBDC** (*Central Bank Digital Currency*) jsou digitální formou peněz vydávaných přímo centrální bankou. Oproti kryptoaktivům jsou CBDC:
- Plně regulované a uznávané jako zákonné platidlo.
- Vázané na hodnotu národní měny (stabilní hodnota).
- Součástí měnové politiky.

Srovnání CBDC vs. kryptoaktiva — viz [[Kryptoaktiva]].

**Příklady:** Bahamy — první celostátní CBDC (říjen 2020); Čína, Švédsko — pilotní projekty (2020).

Z dlouhodobého hlediska CBDC pravděpodobně vytlačí soukromá kryptoaktiva jako platební prostředek.

## Vazba na úrokovou míru

Množství peněz v oběhu přímo ovlivňuje úrokové sazby v ekonomice. Poptávka po penězích a nabídka peněz determinují rovnovážnou úrokovou míru (viz [[Urokova_Mira_a_Casova_Hodnota_Penez]], [[Poptavka_po_Penezich]]).

Klíčová literatura: Mejstřík, M. et al. (2014). *Bankovnictví v teorii a praxi*. Praha: Karolinum.
