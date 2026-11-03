---
name: veles-brand
description: Veles Productions Brand & Design System — materiały w brandzie (deck, onepager, raport, dokument, email, webdoc, opsdoc), system run i motion CSS, jako self-contained HTML. Use for ANY Veles-branded material or Veles brand questions.
---

# Veles Brand & Design System

Centralny system materiałów Veles Productions. **Brand jako dane** — wszystko, co
liczbowe, żyje w `tokens/`; zasady w `brand/`; przepisy per typ w `templates/`.

## Tożsamość w pigułce

- **Logo:** trójkątny sygnet „V" + wordmark VELES (spacjowane wersaliki, **BEZ kropki**).
  Tylko 3 zestawienia: czerwone-na-czarnym / czarne-na-czerwonym / czarne-na-białym.
  Nigdy: obracać, przebarwiać, kadrować, kłaść na zdjęciach. Druk: ≥10 mm od krawędzi.
  **Lockup jest PIONOWY — wordmark to ok. 15% wysokości znaku, więc minimum czytelności
  to 16 mm w druku (nagłówek), 32 mm okładka, 88 px web. Stopka bez logo, tekstowa.**
- **Brand 3.0** (decyzje Artura 1–2.11.2026) — marka Veles Productions + Veles Systems.
- **Kolory — paleta ZAMKNIĘTA** (inny hex = błąd QA): czerń Veles **`#160606`** `#ef3e46` `#cdd1da`
  + flexible `#231f20` `#817f7e` `#aab2bd` `#e7e9ed`. Odcienie tylko `rgba()` z palety.
  Zakazane: `#000000`, `#e0233a`, `#c8313a`.
- **Typografia:** **Alliance No.2**, zamiennik **Manrope** — stack `'Alliance No.2', Manrope,
  sans-serif`. Title=**ExtraBold 800**, Text=**Light 300**; 400/500/600 dla etykiet/tabel/UI.
  Arial i BR Hendrix wycofane. Dopóki nie ma plików i licencji Alliance (gaps G12),
  szablony osadzają Manrope. Nagłówki display: sentence case **z kropką** — nigdy wordmark.
- **Tagline:** „Shaping Digital Worlds for Human Future" (nie tłumaczyć).
- **Grafika:** element graficzny = **znak z pikseli** (znak wartości na siatce 15×15 jak
  haft krzyżykowy / ściana LED; żywy w hero i dashboardzie, statyczny na okładkach) +
  **znaki Velesa** z konstrukcji głagolicy z Baški, kreska 3: 6 znaków wartości (siła,
  więzi, pasja, **odwaga**, kreatywność, integralność), amulet, 6 znaków funkcyjnych
  zamiast emoji-ikon (`brand/runes.md`). Ornament, nie zamiennik logo; reguła rzadkości.
  Równoległobok z brandbooka odrzucony.

## Router — co czytać dalej

| Zadanie | Czytaj |
|---|---|
| Prezentacja / oferta / pitch (A4 landscape) | `templates/deck.md` |
| One-pager (1×A4 portrait) | `templates/onepager.md` |
| Raport / case study | `templates/report.md` |
| Umowa / NDA / SOP / brief / pismo | `templates/document.md` |
| Stopka mail / newsletter | `templates/email.md` |
| Dokument-strona rolowana (web, długa forma) | `templates/webdoc.md` |
| Kalendarz / plan produkcji / dokument roboczy | `templates/opsdoc.md` |
| Znaki Velesa / ikonografia (zamiast emoji) / znak z pikseli | `brand/runes.md`, `assets/runes/` |
| Pełne zasady / wątpliwość brandowa | `brand/rules.md`, `brand/dont.md` |
| Wartości liczbowe (hex, pt, mm) | `tokens/tokens.json`, `tokens/tokens.css` |
| Opis marki dla zespołu | `BRAND-BOOK.md` (katalog główny repo) |

## Workflow generowania

1. Przeczytaj template dla typu materiału + skopiuj `templates/_shared.html` jako bazę.
2. Wypełnij treścią (placeholdery `{{...}}` opisane w `_shared.html`).
3. `python3 scripts/embed_assets.py draft.html out.html` → self-contained HTML
   (fonty + logo base64; wymaga uruchomienia z katalogu repo lub pełnych ścieżek).
4. **QA obowiązkowe:** przejdź `brand/checklist.md` (grep kolorów/fontów + render-check
   screenshotem przez headless Chrome lub preview).
5. Jeśli materiał idzie do druku/wysyłki — od razu zaproponuj PDF:
   `scripts/html2pdf.sh out.html`. W innych przypadkach zapytaj raz.

## Routing innych formatów (NIE reimplementuj)

- PPTX / DOCX → skille `anthropic-skills:pptx` / `anthropic-skills:docx` (font: Manrope).
- Google Slides / Docs → skille `gws-slides` / `gws-docs`.
- Wideo / motion / grafika rastrowa → Higgsfield CLI wg `brand/motion-guidelines.md`
  (dozwolone ruchy, technika, brandowe snippety promptów). Ta sama doktryna zawiera też
  sekcję „CSS/web" dla animacji w dokumentach HTML (webdoc) — inny kontekst, ten sam plik.
- Webflow (strona www) → skill `veles-website`. Żywa strona stoi jeszcze na BR Hendrix
  i `#000000` — do przebrandowania na Brand 3.0 przy zachowaniu jej dynamiki i struktury
  (`brand/gaps.md` G4); NIE przenoś jej fontu ani czerni do materiałów.

## Guardraile (twarde)

1. Żadnego hexa spoza palety (także `#000000`). 2. Żadnego fontu spoza stacka Alliance No.2→Manrope.
3. Wordmark bez kropki. 4. Logo tylko w 3 zestawieniach, bez transformacji.
5. Nie oddawaj materiału bez przejścia `brand/checklist.md` i render-checku.
6. Sekrety/dane poufne: nigdy w commitowanych przykładach; CONFIDENTIAL w `.cap` gdy trzeba.

## Faza 2 — sloty

**Zbudowane:** `brand/motion-guidelines.md` (motion CSS/web + prompty Higgsfield);
system run — ikonografia i ornament (`brand/runes.md` + `assets/runes/`, zamyka G7 w gaps.md);
`templates/webdoc.md` + `templates/_shared-webdoc.html` (dokument-strona); `templates/opsdoc.md`.

**Niezbudowane (nie udawaj, że istnieją):** `templates/social.md`, `templates/landing.md`,
`templates/dashboard.md`, infografiki/wykresy danych.

## Struktura repo

`tokens/` (JSON+CSS) · `brand/` (rules/dont/checklist/gaps/runes/motion) · `templates/`
(7 typów + _shared.html + _shared-webdoc.html)
· `scripts/` (embed_assets.py, html2pdf.sh)
· `assets/` (logo PNG, znaki SVG + znaki z pikseli, fonty marki — Alliance No.2 / Manrope, gaps G12)
· przykłady do przegenerowania w Brand 3.2 (gaps G15). Setup nowej maszyny: `INSTALL.md`.
