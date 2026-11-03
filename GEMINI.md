# veles-brand — kontekst dla Gemini CLI

To rozszerzenie (extension) niesie **System Brandowy Veles Productions**. Gdy generujesz
JAKIKOLWIEK materiał w brandzie Veles, obowiązują Cię poniższe reguły. Pełne szablony,
tokeny i assety leżą w katalogu rozszerzenia pod `skills/veles-brand/` — czytaj je, jeśli
masz dostęp do plików; jeśli nie, trzymaj się esencji poniżej.

## Tożsamość marki (esencja — wiążąca nawet bez dostępu do plików)

- **Logo:** trójkątny sygnet „V" + wordmark **VELES** (spacjowane wersaliki, **BEZ kropki**).
  Tylko 3 zestawienia: czerwone-na-czarnym / czarne-na-czerwonym / czarne-na-białym.
  Nigdy: obracać, przebarwiać, kadrować, kłaść na zdjęciach. Druk: ≥10 mm od krawędzi.
- **Rozmiar logo — lockup jest PIONOWY** (sygnet nad wordmarkiem), a napis „VELES" zajmuje
  ok. **15% wysokości** znaku. Skalowanie po wysokości liczbami z logotypu poziomego zjada
  napis: 11 mm daje wordmark 1,6 mm (nieczytelna smuga), 5 mm daje 0,7 mm. Minimum:
  **nagłówek strony 16 mm, okładka 32 mm, web 88 px**. **Stopka NIE nosi logo** — jest
  tekstowa (nazwa firmy + paginacja); znak zmieściłby się tam na ok. 5 mm, co łamie naraz
  próg czytelności i brandbookowe minimum 10 mm.
- **Paleta — ZAMKNIĘTA** (każdy inny hex = błąd QA):
  `#160606` (czerń Veles; `#000000` zakazany) · `#ef3e46` (jedyna czerwień) · `#cdd1da`
  + flexible: `#231f20` · `#817f7e` · `#aab2bd` · `#e7e9ed`. Odcienie tylko przez `rgba()` z palety.
  **Zakazane czerwienie:** `#e0233a`, `#c8313a`.
- **Typografia:** **Alliance No.2**, zamiennik **Manrope** (stack `'Alliance No.2', Manrope, sans-serif`)
  — Title = ExtraBold 800, Text = Light 300; 400/500/600 dla etykiet/tabel/UI. Arial i BR Hendrix wycofane.
  Nagłówki display: sentence case **z kropką** („Oferta produkcyjna.") — nigdy wordmark.
- **Tagline:** „Shaping Digital Worlds for Human Future" (nie tłumaczyć).
- **Grafika:** znak z pikseli (znak wartości na siatce 15×15, jak haft krzyżykowy / ściana LED)
  + znaki Velesa. Ornament, nie zamiennik logo. Równoległobok z brandbooka odrzucony.

## System runiczny (esencja — wiążąca nawet bez dostępu do plików)

Własny, świadomie skonstruowany język znaków na konstrukcji głagolicy kątowej z tablicy z Baški
(krąg: Europa Środkowa i słowiańskie Bałkany; zakaz skojarzeń nordyckich), NIGDY „odczytany
historyczny alfabet" (autentyczność historyczna to ryzyko wizerunkowe — nie twierdź jej). Warstwy:

- **Wartości** (siła, więzi, pasja, odwaga, kreatywność, integralność + amulet Velesa; odwaga —
  znak prowadzący, jedyny czerwony) — rola ceremonialna: okładki,
  separatory rozdziałów, pieczęć zamknięcia. Najwyżej raz na dokument.
- **Funkcjonalne** (rune-chapter/insight/risk/decision/growth/seal) — rola narzędziowa:
  zastępują emoji-ikony przy callout-ach (kluczowa myśl, ryzyko, decyzja, plan, zamknięcie).
  **Zakaz emoji jako ikon** w każdym materiale Veles — jeśli potrzebna ikona, użyj runy
  funkcjonalnej albo nic.

**Reguła rzadkości (twarda):** nigdy runa przy każdym bullecie/nagłówku — to degraduje znak do
ikonki. Jedna runa = jedno znaczenie w jednym miejscu; maks. 2-3 różne runy funkcjonalne na
stronę. Geometria: kwadrat, trójkąt, trzon, stopa, próg; kąty wyłącznie 0°/45°/90°; kreska 3
w siatce 60 (ekran ≤ 32 px: 5), stroke (nie fill), zakończenia cięte. Każdy znak wartości ma
wersję z pikseli 15×15 (`assets/runes/pixel-*.svg`) — element graficzny marki. Pełna doktryna: `skills/veles-brand/brand/runes.md`, pliki: `assets/runes/`.

## Motion w dokumentach HTML (esencja)

Dotyczy WYŁĄCZNIE `templates/webdoc.md` (dokument-strona scrollowana) — `document.md`/
`opsdoc.md` zostają bez motion (umowy/dokumenty robocze = wierność druku, cisza). Cztery
dozwolone ruchy, nic ponad to: (1) reveal okładki/logo, raz, bez pętli; (2) runa kreślona
(`stroke-dashoffset`) przy wejściu w viewport — najbardziej on-brand ruch, „stary znak domyka
obwód"; (3) przełom sekcji light/dark (crossfade/wipe); (4) pasek postępu scrolla. Technika:
wyłącznie CSS `@keyframes`/`transition` + `IntersectionObserver` jednorazowy (zero bibliotek,
zero CDN), czasy z tokenów `tokens.css` kategoria `motion`. `prefers-reduced-motion`
obowiązkowy bez wyjątków. Zakaz: staggered-reveal (rozpoznawalny tell AI), parallax, ruch bez
funkcji informacyjnej. Pełne reguły: `skills/veles-brand/brand/motion-guidelines.md` (sekcja
„CSS/web" — obok osobnej sekcji Higgsfield/wideo, to inny kontekst techniczny).

## Workflow (gdy masz dostęp do plików rozszerzenia)

1. Przeczytaj `skills/veles-brand/SKILL.md` (router + guardraile).
2. Dobierz szablon: `skills/veles-brand/templates/<typ>.md` (deck / onepager / report /
   document / email / webdoc / opsdoc); skopiuj `templates/_shared.html` jako bazę
   (`templates/_shared-webdoc.html` dla webdoc).
3. Wartości liczbowe bierz z `skills/veles-brand/tokens/tokens.json` (i `tokens.css`).
4. Osadź fonty + logo: `python3 skills/veles-brand/scripts/embed_assets.py draft.html out.html`.
5. QA obowiązkowe: `skills/veles-brand/brand/checklist.md` + render-check screenshotem.
6. Do druku/wysyłki → PDF: `skills/veles-brand/scripts/html2pdf.sh out.html`.

## Twarde zakazy

Hex spoza palety (także `#000000`) · font spoza stacka Alliance No.2 → Manrope · wordmark „VELES." z kropką ·
transformacje/przebarwienia logo · kolorowe emoji jako ikony (zamiast nich runy funkcjonalne) ·
runa przy każdym bullecie (rzadkość!) · motion poza `webdoc.md` · oddanie materiału bez QA.
Pełna lista: `skills/veles-brand/brand/dont.md`.

Brak hooków egzekwujących — reguły są dla Ciebie wiążące mimo to (advisory enforcement).
W razie konfliktu: brandbook (`skills/veles-brand/brand/rules.md`) > Twoje przyzwyczajenia estetyczne.
