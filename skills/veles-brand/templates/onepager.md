# Template: onepager

**Kiedy:** streszczenie usługi/produktu/projektu na 1 stronę — leave-behind po spotkaniu, załącznik do maila, materiał targowy.
**Format:** A4 **portrait** (`.page.portrait`), JEDNA strona, self-contained HTML. `@page{size:A4 portrait}` — nadpisz w `<style>`.

## Struktura (góra → dół)

1. **Header**: `.ptop` — logo czarne (**16 mm**) + `.cap` z typem dokumentu i datą.
2. **Hero**: `.label` (kategoria) → `.h1` (max 2 linie, z kropką, `.r` na akcencie) → `.acc` → `.lede` (2–3 zdania wartości).
3. **3–4 stat tiles** (`.stats` z `grid-template-columns:repeat(3,1fr)` lub 4): kluczowe liczby.
4. **Dwie kolumny body** (`display:grid;grid-template-columns:1fr 1fr;gap:8mm`): lewa = co robimy (lista `.body`), prawa = jak pracujemy / dla kogo.
5. **CTA bar** na dole: panel `--veles-black`, biały tekst, kontakt + `.tag.r`; albo zwykły `.foot`.

## Reguły specyficzne

- Bez tabel budżetowych — onepager nie sprzedaje ceną.
- Maksymalnie JEDEN element graficzny (znak z pikseli albo znak Velesa) — strona ma oddychać.
- Całość MUSI mieścić się na 1 stronie w PDF — render-check obowiązkowy.

## Workflow

Jak w `deck.md` (skopiuj `_shared.html`, zostaw jedną `.page.portrait`, embed, QA, PDF).
