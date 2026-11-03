# Veles Productions — zasady brandu

Źródło prawdy: **Brand 3.2** (decyzje Artura z 1–2.11.2026; opis dla zespołu: `BRAND-BOOK.md` w katalogu głównym repo).
Brand 3.0 zastępuje w kolorze, foncie i elemencie graficznym **VELES-Brandbook_v0.pdf**
(Media Lab DAM, folder `01_Brand_Identity` 1882128, plik 5477654); logo i reszta zasad
brandbooka obowiązują dalej. Marka obejmuje **Veles Productions** i **Veles Systems**.
Wartości liczbowe → `tokens/tokens.json` / `tokens/tokens.css`. Tu są zasady użycia.

## 1. Logo

- Sygnet: trójkątne „V" (zarejestrowany znak towarowy). Wordmark: **VELES** — spacjowane wersaliki, **bez kropki na końcu**.
- Warianty plikowe: `assets/logo/` (big/small × black/grey/red/white).
- **Dozwolone zestawienia kolorystyczne — TYLKO trzy** (brandbook „Logo with Brand Colours", czerń wg Brand 3.0):
  1. czerwone logo na czerni Veles `#160606` (zestawienie sprawdzone na płótnie Brand 3.0),
  2. czarne logo na czerwonym tle,
  3. czarne logo na białym tle.
  Białe logo (`Logo_big_white.png`) stosuj wyłącznie tam, gdzie brandbook nie wystarcza (np. stopka na panelu `--veles-panel`) i tylko po ludzkiej akceptacji.
- **Safe zone:** wokół logo strefa ochronna — żaden tekst ani grafika nie wchodzi w nią. W druku logo min. **10 mm** wysokości i min. **10 mm** od krawędzi strony.
- **Minimum czytelności naszego lockupu to 16 mm, nie 10 mm.** Brandbookowe 10 mm jest bezwzględną podłogą dla znaku jako takiego. Nasz jedyny asset (`Logo_big_*.png`) to lockup **pionowy**: sygnet nad wordmarkiem, gdzie napis „VELES" zajmuje ok. **15% wysokości** całości. Skalowanie po wysokości liczbami wziętymi z logotypu poziomego zjada napis — przy 11 mm wordmark ma 1,6 mm i czyta się jak smuga, przy 5 mm (miniaturka w stopce) 0,7 mm i jest nierozpoznawalny. Wartości operacyjne: **nagłówek strony 16 mm** (wordmark 2,4 mm), **okładka 32 mm**, **web 88 px**. Niżej nie schodzimy, dopóki nie powstanie poziomy wariant lockupu (`gaps.md` → G13).
- **Stopka nie nosi logo.** W pasku stopki znak zmieściłby się na jakieś 5 mm, co łamie naraz regułę 10 mm i próg czytelności powyżej. Markę w stopce niesie nazwa firmy zapisana tekstem.
- Logo zawsze w standardowej formie: bez modyfikacji, w proporcjach, bez obrotu (podstawa równolegle do dolnej krawędzi strony). „Bez obrotu" nie znaczy „lockup poziomy" — nasz lockup jest pionowy, patrz punkt o minimum czytelności wyżej.

## 2. Kolor

- Paleta jest **zamknięta**: 3 foundational (`#160606`, `#ef3e46`, `#cdd1da`) + 4 flexible (`#231f20`, `#817f7e`, `#aab2bd`, `#e7e9ed`). Każdy inny hex = błąd QA.
- **Czerń Veles to `#160606`** — ciepła, czerwonawa czerń (decyzja 2026-11-01). `#000000` wypadł z palety: nie używaj go na tłach okładek, sekcji, ekranów ani w tekście. Biel `#ffffff` zostaje jako papier i tekst na czerni.
- Odcienie i przygaszenia wyłącznie przez `rgba()` wartości z palety (decyzja 2026-06-12; legacy `#c8313a` zakazany). Cień: `rgba(22,6,6,α)`.
- Zastosowanie kanałów (nota z brandbooka): **RGB** dla digital, **HEX** dla web, **CMYK** dla druku. Przepis CMYK dla `#160606` nie jest jeszcze ustalony — przed pierwszym drukiem próba u drukarza (`gaps.md` → G14).
- Czerwień `#ef3e46` to akcent sygnaturowy — używaj oszczędnie (label, accent bar, wyróżnienie w H1, CTA, znak odwagi), nie jako tło dużych bloków treści (wyjątek: okładki i sekcje brandowe wg brandbooka).

## 3. Typografia

- Font marki: **Alliance No.2** (decyzja 2026-11-01). Plików fontu nie ma jeszcze w `assets/fonts/`, a zakres licencji (druk, aplikacje, osadzanie w PDF i HTML) jest otwarty (`gaps.md` → G12) — do czasu wyjaśnienia szablony osadzają zamiennik.
- **Oficjalny zamiennik: Manrope** (Google Fonts, licencja OFL) — tam, gdzie Alliance No.2 nie wejdzie: Google Docs, prezentacje, poczta, szybkie interfejsy zespołu. Zawsze stack: `'Alliance No.2', Manrope, sans-serif`. Arial i BR Hendrix są wycofane (BR Hendrix to font obecnej strony do przebrandowania, nie marki).
- Wagi: **Title = ExtraBold (800)** — najwyższa waga wspólna obu krojów; **Text = Light (300)**; dalej Regular 400 (tabele), Medium 500 (caption/nav), SemiBold 600 (etykiety, nagłówki tabel, strong inline).
- Styl nagłówków display: sentence case **zakończony kropką** („Our Brand.", „Oferta produkcyjna.") — dotyczy nagłówków, NIGDY wordmarku VELES.
- Skala operacyjna (h1 30pt … footer 7.5pt) → `tokens.css`. Brandbook nie definiuje rozmiarów (luka G1).

## 4. Grafika

- **Element graficzny: znak z pikseli** (decyzja 2026-11-02). Znaki wartości rozpisane na siatkę 15×15 jak wzór haftu krzyżykowego i wyświetlone jak na ścianie LED — ludowe źródło i technologia Veles w jednym elemencie. Pliki: `assets/runes/pixel-*.svg`, siatki w `assets/runes/pixel-grids.json`.
  - **Ekran** (hero strony, ekran startowy dashboardu): znak obraca się płytkami falą od środka i co 3,6 s przechodzi w następny; szyna z sześcioma miniaturami pozwala wybrać znak i zatrzymuje cykl. Siatka w hero najwyżej ok. 200 px — znak ma być akcentem, nie ścianą. Reguły ruchu: `motion-guidelines.md` → „Znak z pikseli”.
  - **Druk i okładki**: znak z pikseli tylko jako **mały podpis** (`{{PIXEL_SIGN}}`, ok. 11 mm w rogu okładki Kadr, 5 mm na rewersie wizytówki). Nigdy w skali strony ani jako wzór na całą płaszczyznę.
  - **Dokument tekstowy**: znak liniowy, nie pikselowy.
  - Piksel zapalony: `#ef3e46` dla odwagi, `#e7e9ed` dla pozostałych; piksel zgaszony: ten sam kolor z kryciem 0,07.
- **Oprawa okładek: Kadr i Gazeta, zależnie od kontekstu** (decyzja 2026-11-02, plansza 16; zastępuje warstwę Pole LED). Duże płaszczyzny niesie fotografia albo typografia, nie wzór:
  - **Kadr** (`.page.kadr`) — decki, oferty, materiały sprzedażowe, ekran startowy aplikacji: okładkę niesie prawdziwe zdjęcie z planu Veles (`<img class="bg">`, Media Lab; twarze potwierdza człowiek), pod tytułem gradient z czerni Veles, logo czerwone, znak z pikseli tylko jako mały podpis. Strona środkowa: biała albo pół kadru, pół tekstu.
  - **Gazeta** (`.page.gazeta`) — raporty, pisma, dokumenty oficjalne: jasny papier `#e7e9ed`, czarne logo, linia nagłówka z metryką (`.masthead`), czerwona kreska nad tytułem. Jedyna dekoracja to znak odwagi rysowany włosową kreską (`#cdd1da`) w skali strony, ucięty krawędzią i ledwo widoczny. Strony środkowe: kolumny, cienkie linie, czerwień tylko w znaku rozdziału i jednej liczbie na stronę.
  - Strony środkowe i separatory bez dekoracji tła: separator to pełna czerwień albo czerń Veles, bez siatki.
  - **Kanwa** (płótno do haftu, znak wyszyty krzyżykami — plansza 14, kierunek B) zarezerwowana dla oprawy **Veles Systems**; nie używać w materiałach Veles Productions.
  - **Światło** (plansza 16, A) — ciemna okładka w butelkowej czerwieni (czerwień Veles przez krycie na czerni), światło z lewego górnego rogu, ciemny prawy dolny róg, bez znaku: kierunek w próbie, nie domyślny.
- Odrzucone i nieużywane: równoległobok 45° z brandbooka, element liniowy z run (plansza 08), pasmo kurpiowskie (plansza 12), rozsypka i zdjęcie w rastrze jako warstwa stała (plansza 14, C i D), warstwa Pole LED — siatka pikseli na całą płaszczyznę (plansza 14 A, wycofana 2026-11-02: „ordynarne i ciężkie”).
- **Runy — znaki Velesa** (nazwa „runy” do rozważenia, bo ciągnie skojarzenie nordyckie — `gaps.md` → G3): sześć znaków wartości — siła, więzi, pasja, **odwaga**, kreatywność, integralność — plus amulet i sześć znaków funkcyjnych. Konstrukcja głagolicy kątowej z tablicy z Baški, kreska 3 w siatce 60, styl liniowy. Ornament i nawigacja, nigdy zamiennik logo. Doktryna: `runes.md`.
- Estetyka materiałów: czerń Veles + biel + jedna czerwień; duża typografia; pełny kadr; ostre kąty (0°/45°/90°), zero zaokrągleń poza drobnymi promieniami UI (≤4px) i tagami.

## 5. Ton głosu

- Tagline: **„Shaping Digital Worlds for Human Future"** (nie tłumaczyć).
- EN: professional/aspirational. PL: konkretnie, krótkie zdania, bez korpomowy; liczby zamiast przymiotników.
- Materiały klienckie PL — typografia polska: „cudzysłowy drukarskie", półpauzy z odstępami.

## 6. Formaty

- Default: **self-contained HTML** (fonty + logo base64, zero zewnętrznych zależności, print CSS `@page`). Strony A4: deck = landscape 297×210 mm, dokumenty = portrait 210×297 mm.
- PDF: `scripts/html2pdf.sh` (headless Chrome).
- PPTX/DOCX/Google: routing do dedykowanych skilli (patrz SKILL.md) — z Manrope jako fontem.
