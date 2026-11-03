# Veles — anty-wzorce (DO NOT)

Lista twardych zakazów. Część z brandbooka (strona „Logo Usage"), część z realnych wpadek w materiałach Veles. Przy QA porównuj materiał z TĄ listą.

## Logo (brandbook „Logo Usage")

- ❌ NIE kadruj logo ani nie używaj jego fragmentów.
- ❌ NIE zmieniaj koloru logo (np. czerwony sygnet z czerwonym wordmarkiem na białym — niedozwolone; tylko 3 zestawienia z `rules.md`).
- ❌ NIE kładź logo na zdjęciach.
- ❌ NIE zmieniaj proporcji (rozciąganie/ściskanie).
- ❌ NIE kładź logo na niespokojnych teksturach/wzorach.
- ❌ NIE obracaj logo ani nie przestawiaj jego elementów.

## Realne wpadki (już wystąpiły — sprawdzaj w pierwszej kolejności)

- ❌ **„VELES." z kropką** — dokument Nexa `_veles-storyverse.html` używał wordmarku z kropką. Kropka to styl NAGŁÓWKÓW („Our Brand."), nigdy wordmarku.
- ❌ **`#e0233a` zamiast `#ef3e46`** — ta sama wpadka Nexa. Jedyna czerwień Veles to `#ef3e46`.
- ❌ **`#c8313a` („red-dim")** — legacy z wczesnego generatora decków. Zakazany od 2026-06-12; przygaszenia przez `rgba(239,62,70,α)`.
- ❌ **Dokument „w brandzie klienta projektu" wydany jako materiał Veles** — HTML-e jednego z projektów klienta (indigo, Georgia, kremowy papier) NIE są wzorcem brandu Veles. Materiał firmowy Veles = paleta i typografia Veles; brand klienta tylko w materiałach wewnętrznych danego projektu i świadomie.
- ❌ **Poziome rozciąganie logo w kontenerach Flexbox** — umieszczając logo w kolumnowym flexboxie (np. `.cover`), zawsze dodawaj `align-self: flex-start` (lub ustaw `align-items: flex-start` na rodzicu). Brak tego atrybutu powoduje, że domyślne zachowanie Flexbox (`stretch`) rozciąga obraz logotypu w poziomie, brutalnie zniekształcając jego proporcje.

## Typografia i kolor

- ❌ NIE używaj fontów spoza stacka `'Alliance No.2', Manrope, sans-serif` — żadnych innych Google Fonts (Manrope jest jedynym wyjątkiem), system serif itd.
- ❌ **NIE używaj Ariala ani BR Hendrix** — oba wycofane w Brand 3.0 (Arial: „nie ma gorszego”; BR Hendrix: font obecnej strony do przebrandowania).
- ❌ NIE używaj wag spoza zestawu 300/400/500/600/800.
- ❌ **NIE używaj `#000000`** — czerń Veles to `#160606`. Także „czarne” tła okładek, sekcji i ekranów.
- ❌ NIE wprowadzaj nowych hexów — także „prawie dobrych" szarości (`#ccc`, `#888`, `#eee`); zamiast nich `--veles-grey`, `--veles-grey-mid`, `--veles-near-white`.
- ❌ NIE używaj czystej bieli tekstu na czerwieni dla długich akapitów (czerwień = akcent, nie tło treści).
- ❌ NIE stosuj gradientów, cieni kolorowych, glow — dozwolony tylko neutralny cień `rgba(22,6,6,α)` przy podglądzie ekranowym stron (wyjątek: przyciemnienie zdjęcia pod tytułem w hero, gradient z czerni Veles do przezroczystości).

## Layout

- ❌ NIE zaokrąglaj mocno rogów (max 4px w UI/tagach; karty i strony — kąty proste).
- ❌ NIE łam kątów 0°/45°/90° w znakach Velesa i znaku z pikseli.
- ❌ NIE wracaj do odrzuconych elementów: równoległobok 45° z brandbooka, element liniowy z run, pasmo kurpiowskie na całą szerokość.
- ❌ NIE używaj referencji ani stylizacji nordyckiej (kamienie runiczne, futhark) — krąg kulturowy to Europa Środkowa i słowiańskie Bałkany (`runes.md` §1).
- ❌ NIE umieszczaj logo bliżej niż 10 mm od krawędzi strony w materiałach do druku.
- ❌ NIE skaluj logo poniżej **16 mm** wysokości w druku ani **88 px** w webie — nasz lockup jest pionowy i poniżej tego progu wordmark „VELES" przestaje być czytelny (`rules.md`, sekcja 1).
- ❌ NIE wstawiaj logo do stopki strony. Stopka jest tekstowa: nazwa firmy + paginacja.
