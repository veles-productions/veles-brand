# Veles — znaki Velesa (system runiczny, doktryna)

Brand 3.0 (decyzje Artura z 1–2.11.2026). Pliki SVG: `assets/runes/`. Zapis danych:
`tokens/tokens.json` → `brand.runes`.

## 1. Pozycjonowanie — czym znaki SĄ i czym NIE SĄ

Znaki Velesa to **własny, świadomie skonstruowany język znaków**, zbudowany według zasad
głagolicy kątowej z **tablicy z Baški** (Chorwacja, ok. 1100). Nie udają pisma i nie są
odczytanym alfabetem — to rzemiosło i intencja: nazywamy nimi wartości firmy i funkcje
dokumentu.

- **Krąg kulturowy: Europa Środkowa i słowiańskie Bałkany** (Polska, Słowacja, Czechy,
  Ukraina, Chorwacja, Bułgaria i pokrewne) — „żeby było wiadomo, że zajmujemy się tą częścią”.
  Główna referencja: tablica z Baški; pomocniczo wycinanki z Kurpi Białych. Pozostałe
  referencje z tablicy (Čičmany, belka z Beskidu Śląskiego, kraszanki z Hany, idol ze
  Zbrucza, haft bułgarski) to tło, nie źródło.
- **Zakaz skojarzeń nordyckich** — żadnych kamieni runicznych, futharku ani stylizacji
  wikińskiej, w rysunku, w referencjach i w promptach generacji.
- Materiały Veles NIGDY nie sugerują autentyczności historycznej. Poprawna narracja:
  „zbudowaliśmy własny system znaków na konstrukcji głagolicy, żeby nazwać nasze wartości”.
- Metafora ruchu: znak liniowy **kreśli się** (`stroke-dashoffset`), znak z pikseli
  **zapala się** piksel po pikselu (`motion-guidelines.md`). Starożytność pokazujemy
  geometrią i ruchem, NIGDY fakturą (pergamin, sepia, przetarcia — zakaz z `dont.md`).

## 2. Geometria konstrukcyjna (wspólna dla wszystkich znaków)

- Moduły głagolicy kątowej: **kwadrat, trójkąt, trzon pionowy, stopa (podstawa), próg**.
  Znaki wartości stoją na trzonie ze stopą; znaki funkcyjne są prostsze — wskazują.
- Kąty **wyłącznie 0° / 45° / 90°** — żadnych łuków, żadnych dowolnych kątów.
- Siatka `viewBox="0 0 60 60"`; amulet `viewBox="-8 0 136 322"`.
- **Kreska 3** w siatce 60 (decyzja 2026-11-02 „B · kreska 3”); na ekranie przy rozmiarze
  ≤ 32 px — kreska 5. `stroke-linecap="square"`, `stroke-linejoin="miter"` (cięte
  zakończenia jak w głagolicy), `fill="none"`, `stroke="currentColor"`.
- Zero faktur, zero gradientów, zero zaokrągleń — te same zakazy co reszta systemu.

## 3. Warstwy

### Znaki wartości (6 + amulet)

| Znak | Znaczenie PL | EN | Plik | Z pikseli |
|---|---|---|---|---|
| power | siła | power | `power.svg` | `pixel-power.svg` |
| connections | więzi | connections | `connections.svg` | `pixel-connections.svg` |
| passion | pasja | passion | `passion.svg` | `pixel-passion.svg` |
| courage | **odwaga** | courage | `courage.svg` | `pixel-courage.svg` |
| creativity | kreatywność | creativity | `creativity.svg` | `pixel-creativity.svg` |
| integrity | integralność | integrity | `integrity.svg` | `pixel-integrity.svg` |
| amulet Velesa | trzy piętra po dwa znaki, romby na osi, pieczęć | amulet of Veles | `amulet.svg` | — |

- **Odwaga zastąpiła innowację** (decyzja 2026-11-01): była wartością nr 1 w trzech
  kolejnych listach kultury Veles i wróciła. To **znak prowadzący** — jedyny skierowany
  w górę i jedyny, który wolno barwić na czerwono (`#ef3e46`); pozostałe znaki są w kolorze
  tekstu. Uzasadnień obronnych tej zmiany nie umieszczamy w materiałach.
- **Amulet**: trzy piętra jak na idolu ze Zbrucza — odwaga + siła / więzi + kreatywność /
  pasja + integralność; piętra łączą romby (motyw z Čičman), u góry romb zawieszenia, na
  dole pieczęć. Ścieżki odwagi i pieczęci mają `class="accent"` — na ciemnym tle szablon
  barwi je na czerwono (`.accent{stroke:var(--veles-red)}`).
- Rola: **ceremonialna** — okładki, separatory rozdziałów, zamknięcie dokumentu. Amulet
  w jednym miejscu na dokument (okładka lub ostatnia strona), nigdy obok pojedynczych
  znaków wartości ani obok znaku z pikseli.

### Znaki funkcyjne (role strukturalne dokumentu)

| Znak | Rola | Rysunek | Plik |
|---|---|---|---|
| rune-chapter | rozdział | romb nad progiem — romb z amuletu otwiera nową część, próg zaznacza wejście (od 2026-11-02; dawny trzon z chorągwią wycofany, czytał się jak szubienica) | `rune-chapter.svg` |
| rune-insight | kluczowa myśl | ziarno (kwadrat) ujęte w nawias | `rune-insight.svg` |
| rune-risk | ryzyko | trzon przerwany w trzech miejscach, na stopie | `rune-risk.svg` |
| rune-decision | decyzja | rozwidlenie — dwie drogi z jednego miejsca | `rune-decision.svg` |
| rune-growth | plan | schodki — kolejne kroki w górę | `rune-growth.svg` |
| rune-seal | pieczęć | romb w rombie z krzyżem (z Čičman) | `rune-seal.svg` |

Rola: **narzędziowa** — zastępują emoji-ikony (zakaz z `dont.md`/`checklist.md`) przy
calloutach, TL;DR, ryzykach, decyzjach. Jeden znak = jedna konkretna rola, nie ozdoba.

### Znak z pikseli (element graficzny marki)

Każdy znak wartości ma wersję na siatce 15×15 (`pixel-*.svg`; dane `pixel-grids.json`,
`#` = piksel zapalony). Piksel 6, skok 7 w `viewBox="0 0 104 104"`; zgaszone piksele to
siatka LED z kryciem 0,07. Kiedy i jak używać: `rules.md` §4; ruch: `motion-guidelines.md`.
Siatki rysujemy ręcznie z linii znaku — nie rasteryzujemy ścieżek automatycznie.

## 4. Reguła rzadkości (twarda)

- **NIGDY** znak przy każdym bullecie ani nagłówku — to degraduje znak do ikonki.
- **Jeden znak = jedno znaczenie w jednym miejscu.** Najwyżej dwa–trzy znaki funkcyjne na
  stronę; ten sam znak funkcyjny najwyżej raz na sekcję.
- Znak wartości (siła, więzi…) najwyżej raz na dokument — przy temacie, do którego
  semantycznie pasuje. Amulet i pieczęć — raz na dokument.
- Znak z pikseli na okładce — jeden, statyczny; nigdy jako tapeta ani powtarzany wzór.

## 5. Gdzie używać

| Miejsce | Znak | Uwaga |
|---|---|---|
| Okładka (ciemna) | znak z pikseli (`{{PIXEL_SIGN}}`) albo `amulet.svg` | jedno albo drugie, nie oba naraz |
| Hero strony / ekran startowy dashboardu | znak z pikseli, żywy | `motion-guidelines.md` → „Znak z pikseli” |
| Separator rozdziału / `.chapter` | `rune-chapter.svg` | grzbiet sekcji, mały, przy tytule |
| Najważniejsze zdanie strony / `.pull` | `rune-insight.svg` | zamiast emoji 💡 |
| Callout ryzyka, zastrzeżenie | `rune-risk.svg` | zamiast emoji ⚠️ |
| Callout decyzji / opcji | `rune-decision.svg` | zamiast emoji 🔀 |
| Harmonogram / plan / roadmapa | `rune-growth.svg` | zamiast emoji 📈 |
| Ostatnia strona / zamknięcie | `rune-seal.svg` | jedna na dokument, na końcu |
| Znak wartości przy temacie sekcji | `power.svg` itd. | maks. raz na dokument, świadomie |

## 6. Zakazy (dopełnienie `dont.md`)

- ❌ Znak jako zamiennik logo lub obok logo w tym samym polu kompozycji.
- ❌ Fill zamiast stroke, gradient, cień kolorowy, zaokrąglone naroża w glifach.
- ❌ Kreska inna niż 3 (druk) / 5 (ekran ≤ 32 px); kąty spoza 0°/45°/90°.
- ❌ Czerwień na znaku innym niż odwaga (wyjątek: pieczęć w amulecie i znaki funkcyjne
  w calloutach, które barwi kontekst `.rune`).
- ❌ Faktura postarzenia (pergamin/sepia/przetarcia) na znakach lub wokół nich.
- ❌ Referencje i stylizacja nordycka (kamienie runiczne, futhark).
- ❌ Ozdobne pasma i wzory z wycinanek na całą szerokość strony — odrzucone jako „za dużo”
  (plansza 12).
- ❌ Opisywanie znaków jako „odczytanego” lub „historycznego” alfabetu w tekście dokumentu.
