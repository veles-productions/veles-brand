# Template: email (stopka / wizytówka / newsletter)

**Kiedy:** stopka e-mail pracownika, wizytówka e-mailowa, newsletter HTML.
**Format:** email-safe HTML — to JEDYNY szablon, gdzie **NIE** osadzamy fontu marki.

## Twarde reguły email-safe

- Font: stack marki `font-family:'Alliance No.2',Manrope,sans-serif` — klient poczty bez web fontów
  spadnie do systemowego sans-serif (świadomie, decyzja 2026-11-01; Arial wycofany).
- Layout na `<table>` (klienty Outlook), style INLINE (`style="..."`), zero `<style>` poza fallbackiem.
- Logo: `Logo_small_red_web.png` hostowane (Media Lab public link lub CDN www) — w mailach data-URI bywa blokowane przez Gmaila; szerokość stała `width="96"`.
- Szerokość newslettera: 600 px. Kolory z palety jako inline hex.

## Stopka pracownika (wzór)

```html
<table cellpadding="0" cellspacing="0" border="0" style="font-family:'Alliance No.2',Manrope,sans-serif">
 <tr>
  <td style="padding-right:14px;border-right:2px solid #ef3e46;vertical-align:top">
    <img src="{URL_LOGO_SMALL_RED}" width="72" alt="VELES">
  </td>
  <td style="padding-left:14px">
    <div style="font-size:13px;font-weight:700;color:#160606">Imię Nazwisko</div>
    <div style="font-size:11px;color:#817f7e;text-transform:uppercase;letter-spacing:.08em">Stanowisko · Veles Productions</div>
    <div style="font-size:11px;color:#231f20;padding-top:6px">
      +48 ··· ··· ··· · <a href="mailto:imie@velesproductions.com" style="color:#ef3e46;text-decoration:none">imie@velesproductions.com</a><br>
      <a href="https://www.velesproductions.com" style="color:#231f20;text-decoration:none">velesproductions.com</a>
    </div>
    <div style="font-size:10px;color:#aab2bd;padding-top:6px">Shaping Digital Worlds for Human Future</div>
  </td>
 </tr>
</table>
```

## Newsletter

- Header: pasek czarny, logo czerwone wycentrowane (red-on-black — dozwolone zestawienie).
- Sekcje: tytuł 20px waga 800 `#160606` (z kropką), body 14px `#231f20`, CTA button: tło `#ef3e46`, tekst biały, bez zaokrągleń >4px.
- Stopka: `#e7e9ed` tło, dane rejestrowe + unsubscribe.

## Workflow

1. Zbuduj na wzorach wyżej (inline styles!).
2. QA: `brand/checklist.md` (sekcja kolorów + wordmark) — pomiń punkty o osadzonym foncie/self-contained.
3. Test renderu: wyślij do siebie draft przez Superhuman i obejrzyj w Gmail/Outlook.
