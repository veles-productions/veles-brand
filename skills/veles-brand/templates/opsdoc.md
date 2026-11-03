# Template: opsdoc (dokument roboczy / operacyjny)

**Kiedy:** kalendarz zdjęciowy, plan produkcji, lista kontaktowa, harmonogram dnia zdjęciowego
— dokumenty ROBOCZE tworzone przez zespół (nie-designerów) do wewnętrznego obiegu i wysyłki do
ekipy. **Odpowiedź na antywzorzec** z audytu dokumentów: kalendarz produkcyjny robiony w Wordzie
(Arial, `#dd0000`, zero logo/stopki — ocena 2/10). Cel: ta sama osoba dostaje ścieżkę „wklej
tabelę → dostań brandowany dokument" w mniej niż 5 minut, bez wiedzy o brandzie.

**Format:** A4, self-contained HTML, na bazie `_shared.html` — jak `document.md`, ale odchudzony
do minimum: nagłówek + (opcjonalny) tytuł + tabela + stopka. Orientacja `.page` (landscape,
domyślna) dla szerokich siatek (kalendarz wielodniowy, harmonogram godzinowy); `.page.portrait`
dla list jednokolumnowych (kontakty). Wybierz jedną, nie mieszaj w obrębie dokumentu.

## Struktura

1. **Nagłówek** (`.ptop`): logo czarne **16 mm** po lewej (jak w `document.md`), po prawej `.cap`
   z tytułem dokumentu + datą („PLAN ZDJĘCIOWY · 21.07.2026") — jedyne miejsce na kontekst.
2. **Tytuł** (opcjonalny, gdy tabela sama nie mówi za siebie): `.label` + `.h2`, BEZ `.lede` —
   dokument roboczy nie potrzebuje wstępu.
3. **Tabela** (`table.t` z `_shared.html`) — GŁÓWNY element dokumentu. Wklej dane wprost:
   nagłówki kolumn w `<thead>`, wiersze w `<tbody>`; zebra-stripe i bordery już są w stylu,
   nic nie trzeba dostrajać. Dla podsumowań/kwot użyj wiersza `.price` jak w innych szablonach.
4. **Stopka** (`.foot`): VELES PRODUCTIONS + numer strony/wersji, **bez logo** (tekstowa) — jedyny brandowy
   element poza nagłówkiem i tabelą.

## Reguły specyficzne

- **Zero ozdób** — żadnych znaków wartości, żadnego znaku z pikseli. Jedyny opcjonalny
  element ponad minimum: `rune-seal.svg` jako mała pieczęć obok stopki na dokumentach, które
  opuszczają firmę (np. harmonogram wysyłany do zewnętrznej ekipy) — nigdy obowiązkowa; jeśli
  jej nie ma, dokument jest równie poprawny.
- Zero emoji jako ikon statusu/priorytetu w tabeli — użyj gotowych atomów `.tag.r`/`.tag.k`/
  `.tag.g` z `_shared.html` albo zwykłego pogrubienia.
- Kolor: czerwień tylko jako akcent (border nagłówka tabeli, `.tag.r`) — nigdy jako tło komórek
  ani całych wierszy.
- Font: stack marki przez `_shared.html`; gdy dokument trafia do edycji poza HTML (np. eksport
  do Excela lub Arkuszy Google) → Manrope (jak w innych szablonach), nigdy inny font.
- Wielostronicowe kalendarze: duplikuj `.page` na kolejne tygodnie/dni, każda strona z tym
  samym nagłówkiem i stopką (jak w `deck.md`).

## Workflow (dla nie-designera — najkrótsza ścieżka w systemie)

1. Skopiuj `templates/_shared.html`, usuń sekcję `COVER` (opsdoc nie ma okładki) — zostaw
   wzorzec `CONTENT page`.
2. Wklej tytuł/datę do `.cap`, wklej tabelę (z Excela/Worda — sam markup `<table>`, zachowaj
   `class="t"` na tagu `<table>`) w miejsce `{{CONTENT}}`.
3. `python3 scripts/embed_assets.py draft.html out.html` (fonty + logo base64 — jeden krok,
   nie wymaga wiedzy o brandzie).
4. QA: skrócona wersja `brand/checklist.md` wystarczy — kolory, font, brak emoji;
   render-check jednym screenshotem.
5. PDF do wysyłki ekipie: `scripts/html2pdf.sh out.html`.
