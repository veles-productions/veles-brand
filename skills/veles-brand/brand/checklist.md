# Veles — QA checklist zgodności z marką

Przejdź PRZED oddaniem każdego materiału. Wszystkie punkty muszą być ✅ (albo świadomie odnotowane odstępstwo zatwierdzone przez człowieka).

## Automatyczne (grep/inspekcja kodu)

- [ ] **Kolory:** w pliku nie występuje żaden hex spoza: `#160606 #ef3e46 #cdd1da #231f20 #817f7e #aab2bd #e7e9ed #ffffff` (+ `rgba()` pochodne palety).
      `grep -oiE '#[0-9a-f]{3,8}' plik.html | sort -u` → porównaj z listą.
- [ ] **Zakazane hexy:** brak `#000000` (i `#000`), `#e0233a`, `#c8313a`, `#bc3138`, `#dd0000`.
- [ ] **Font stack:** `'Alliance No.2', Manrope, sans-serif`; brak innych rodzin, w tym Ariala i BR Hendrix (grep `font-family`).
- [ ] **Wagi:** tylko 300/400/500/600/800 (grep `font-weight`).
- [ ] **Znaki:** kreska 3 (ekran ≤ 32 px: 5), `stroke-linecap="square"`; brak starych ścieżek run z Brand 2.0 (`stroke-width="1.4"`) i pliku `innovation.svg`.
- [ ] **Wordmark:** brak ciągu `VELES.` (kropka po wordmarku). Nagłówki z kropką — OK.
- [ ] **Self-contained:** brak `http(s)://` w `src=`/`url(` poza ewentualnymi jawnymi linkami nawigacyjnymi `<a href>`; fonty i logo jako `data:`.
- [ ] **Tagline** (jeśli użyty): dokładnie „Shaping Digital Worlds for Human Future".
- [ ] **Ikony:** brak kolorowych emoji jako ikon (obcy język graficzny; ikonografię docelowo
      pokrywają runy funkcjonalne — Faza 2.0).

## Wizualne (render-check — screenshot przez headless Chrome / preview)

- [ ] Logo: jedno z 3 dozwolonych zestawień; nieobrócone, proporcje OK, nie leży na zdjęciu/teksturze; safe zone czysta; w druku ≥10 mm i ≥10 mm od krawędzi.
- [ ] **Wordmark „VELES" daje się odczytać w KAŻDYM wystąpieniu logo** — powiększ zrzut i przeczytaj napis, nie poprzestawaj na „sygnet wygląda dobrze". Lockup jest pionowy, więc napis to ok. 15% wysokości znaku: nagłówek ≥16 mm, okładka 32 mm, web ≥88 px. Znak mniejszy niż 16 mm w druku = fail (`rules.md` → minimum czytelności lockupu).
- [ ] Stopka **bez logo** — sama nazwa firmy tekstem + paginacja. Miniaturka znaku w stopce (ok. 5 mm) to fail, nie detal.
- [ ] H1/H2: Alliance No.2 (lub Manrope) ExtraBold 800, sentence case z kropką na końcu (styl display).
- [ ] Okładka: najwyżej jeden znak z pikseli albo amulet — nigdy oba; tło `#160606`, nie czysta czerń.
- [ ] Body: Light, czytelny rozmiar (≥10 pt druk / ≥14 px web).
- [ ] Czerwień jako akcent (label, accent bar, wyróżnienia) — nie jako tło długiej treści.
- [ ] Print: strony A4 nie ucinają treści (sprawdź PDF z `html2pdf.sh`), stopka (nazwa firmy + paginacja) na miejscu.
- [ ] PL: polskie znaki renderują się w osadzonym foncie marki (ąćęłńóśźż w nagłówku testowym) — a nie w systemowym zastępstwie, gdy w `assets/fonts/` brakuje plików.
- [ ] **(opcjonalnie) Impeccable audit:** jeśli w bieżącym środowisku istnieje katalog
      `.claude/skills/impeccable`, uzupełnij
      render-check o `impeccable audit <plik>` (kontrast/a11y/anti-pattern — czego ta lista
      nie sprawdza); jeśli katalogu nie ma, pomiń krok bez błędu.

## Kontekstowe

- [ ] Materiał Veles vs materiał projektu klienta — użyty właściwy brand (patrz `dont.md`).
- [ ] Dane wrażliwe: brak kluczy API, danych osobowych, stawek poufnych — chyba że dokument jest oznaczony CONFIDENTIAL i adresat potwierdzony.
- [ ] Wersja językowa zgodna z odbiorcą (PL/EN), typografia polska w PL.
