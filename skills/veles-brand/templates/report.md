# Template: report (raport / case study)

**Kiedy:** raport z projektu/kampanii, case study, analiza, podsumowanie kwartału dla klienta.
**Format:** A4 **portrait**, wielostronicowy, self-contained HTML. `@page{size:A4 portrait}`.

## Struktura stron

1. **Cover — Gazeta** (`.page.portrait.gazeta`, wzór w `_shared.html`): jasny papier, czarne logo, `.masthead` z rodzajem i datą wydania, `.acc` nad tytułem, `.h1` + `.lede`, `.meta`; jedyna dekoracja to znak odwagi włosową kreską (brand/rules.md §4). Bez znaku z pikseli.
2. **Executive summary** (1 strona): `.lede` + 3–4 stat tiles z najważniejszymi wynikami.
3. **Rozdziały**: każdy zaczyna się `.label` (numer: „01 · KONTEKST") + `.h2`; body w jednej kolumnie (max ~75 znaków/wiersz — `max-width:160mm`).
4. **Dane**: `table.t` dla zestawień; proste wykresy słupkowe jako divy (`background:var(--veles-red)/var(--veles-grey-blue)/var(--veles-panel)`, wysokość proporcjonalna) — NIE zewnętrzne biblioteki chart.
5. **Wnioski / next steps**: lista numerowana, każdy punkt z właścicielem i terminem.

## Case study — wariant

Sekcje: Wyzwanie → Rozwiązanie → Proces (timeline pionowy: border-left `--veles-grey`, punkty `--veles-red`) → Rezultaty (stat tiles) → Cytat klienta (blockquote: border-left 2.5pt `--veles-red`, Light italic).

## Reguły specyficzne

- Numeracja stron w `.foot` obowiązkowa (raporty się cytuje).
- Wykresy: max 3 kolory serii (red/grey-blue/panel); legenda tekstowa, nie ikonowa.
- Dane wrażliwe → oznaczenie CONFIDENTIAL w `.cap` każdej strony.

## Workflow

Jak w `deck.md`.
