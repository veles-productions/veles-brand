# Template: webdoc (dokument-strona rolowana)

**Kiedy:** materiał do czytania w przeglądarce/link (propozycja, manifest, długi tekst z
danymi i cytatami) — NIE do druku. Jeśli materiał ma iść na drukarkę, do podpisu lub jako
PDF-pismo, użyj `templates/document.md` (papier A4, bez motion) zamiast tego przepisu.
**Format:** scroll-native, self-contained HTML, `width` i wysokość naturalne (BEZ
`width:297mm`, BEZ `page-break-after`) — dokument rośnie w dół, nie dzieli się na strony.

## Anatomia

1. **Okładka** (`.cover`, ciemna, `.pixel-sign` — mały znak z pikseli jako podpis w rogu, nie w skali okładki) — logo, `.label` + `.h1` tytułu, `.meta`.
   Reveal przy załadowaniu (ruch #1 z motion-guidelines).
2. **Rozdziały light/dark na przemian** (`.section` / `.section.dark`) — każdy otwiera
   `.chapter`: mała `rune-chapter.svg` grzbietu + `.label` + `.h2`, potem `.acc` + `.lede` +
   treść. Naprzemienność rejestru = punktacja rozdziałów, nie ozdoba — nie zagnieżdżaj dwóch
   `.section` tego samego rejestru pod rząd bez treściowego powodu.
3. **Separatory rozdziałów** (`.section-break`, pełnoekranowe, zawsze ciemne) — jedna runa
   FUNKCYJNA jako pieczęć chwili (kreślona przy wejściu w viewport), dobrana do roli treści
   w tym miejscu (patrz „Reguły run" niżej). Używaj oszczędnie — nie po każdym rozdziale.
4. **Pieczęć zamknięcia** (`.section-break.closing`, ostatnia sekcja dokumentu) — `amulet.svg`
   (viewBox `0 0 60 200`), JEDNA na cały webdoc. Sygnalizuje koniec dokumentu, nie kolejny
   separator śróddokumentowy.

## Wyliczenie atomów (brief = ta lista, w kolejności użycia)

| Atom | Rola |
|---|---|
| `.cover` | okładka ciemna, `.pixel-sign`, reveal on-load |
| `.chapter` | otwarcie rozdziału: runa grzbietu + `.label` + `.h2` |
| `.acc` | akcentowa kreska pod tytułem rozdziału |
| `.lede` / `.body` | proza w kolumnie `--measure` (65-75ch) |
| `.pull` | cytat, bleed szerszy niż proza (`--bleed`) |
| `.stat` / `.stats` | kafle liczbowe, bleed |
| `.cols` / `.col` | warianty/karty w kolumnach, bleed |
| `table.t` | zestawienia danych, bleed |
| `.tag` | etykieta inline (`.r`/`.k`/`.g`) — zamiast emoji |
| `.section-break` | separator śróddokumentowy, pieczęć-runa funkcyjna |
| `.section-break.closing` | pieczęć zamknięcia, `amulet.svg`, raz na dokument |
| `.scroll-progress` | pasek postępu scrolla na `--veles-red` |

Wypisz w briefie webdoca te atomy w kolejności, w jakiej mają wystąpić w dokumencie — tak
jak przy `report.md`/`deck.md`, brief = struktura stron/sekcji, nie proza opisowa.

## Reguły run (odsyłacz: `brand/runes.md`)

- **Rzadkość jest twarda.** Runa funkcyjna maks. 1-2 razy na sekcję; nie każdy `.section-break`
  musi mieć inną runę — lepiej mniej separatorów niż runa przy każdym akapicie.
- `rune-seal.svg` / `amulet.svg` wyłącznie na `.section-break.closing` (ostatnia sekcja) —
  nigdy w środku dokumentu.
- Runa wartości (`power`/`connections`/...) maks. raz na cały webdoc, tylko jeśli temat
  sekcji semantycznie pasuje — pełna tabela ról w `brand/runes.md` §5.
- Pełna geometria/dozwolone kąty/zakazy: `brand/runes.md` (sekcje 2, 4, 6).

## Reguły motion (odsyłacz: `brand/motion-guidelines.md` §„CSS/web")

- WYŁĄCZNIE 4 dozwolone ruchy: reveal okładki, runa kreślona, przełom sekcji light/dark,
  pasek postępu — wszystkie już zaimplementowane w `_shared-webdoc.html`, nie dodawaj innych.
- Czasy/easing zawsze przez `--veles-motion-*` z `tokens/tokens.css` — nigdy hardkoduj `ms`.
- `prefers-reduced-motion: reduce` jest obowiązkowy (blok już w `_shared-webdoc.html`) —
  jeśli dopisujesz nową sekcję z motion, sprawdź że jest objęta tym blokiem.
- Zakaz: staggered-reveal na kolejnych elementach, ruch bez funkcji, parallax, pętle w treści.
- Domyślny stan (bez JS, wolny inline-script, `prefers-reduced-motion`) MUSI być w pełni
  widoczny/dokreślony — `.chapter`/`.section-break`/`.rune-draw` chowają się TYLKO pod
  klasą `.js-motion` na `<html>`, dokładaną synchronicznym inline-scriptem na starcie
  `<body>` (już w `_shared-webdoc.html`). Nowa sekcja z motion musi zachować ten wzorzec —
  inaczej no-JS/wolny render pokaże niewidoczną treść (FOUC).

## Workflow

1. Skopiuj `templates/_shared-webdoc.html` jako bazę, duplikuj `.section`/`.section.dark`
   ile trzeba, wypełnij treścią (placeholdery `{{...}}` opisane w pliku).
2. `python3 scripts/embed_assets.py draft.html out.html` → self-contained (fonty + logo
   base64; `{{PIXEL_SIGN}}` dla `.pixel-sign`). Runy funkcyjne/wartości wpisuj jako inline SVG
   bezpośrednio z `assets/runes/*.svg` — `embed_assets.py` nie zna placeholderów SVG.
3. **QA obowiązkowe:** `brand/checklist.md` + render-check (headless Chrome: scroll płynny,
   runy kreślą się przy wejściu w viewport, pasek postępu rośnie, `prefers-reduced-motion`
   sprowadza wszystko do stanu końcowego bez animacji, brak błędów konsoli).
4. Webdoc idzie do przeglądarki/linku, NIE do druku — nie proponuj `html2pdf.sh` domyślnie;
   jeśli ktoś mimo to potrzebuje PDF, zaznacz że sekcje pełnoekranowe (`.section-break`) i
   scroll-native rytm nie są projektowane pod paginację.
