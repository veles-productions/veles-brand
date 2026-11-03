# Template: document (papier firmowy A4)

**Kiedy:** oferta tekstowa, umowa, NDA, SOP, brief kreatywny, notatka formalna, pismo.
**Format:** A4 **portrait**, tekstocentryczny, self-contained HTML. `@page{size:A4 portrait}`.

## Struktura

1. **Nagłówek firmowy** (każda strona): logo czarne **16 mm** w lewym górnym (≥10 mm od krawędzi — reguła brandbooka; 16 mm to minimum czytelności naszego pionowego lockupu, patrz `brand/rules.md`), po prawej `.cap`: typ dokumentu · data · nr ref.
2. **Blok adresowy** (pisma/oferty): nadawca (Veles Productions sp. z o.o. + adres) i adresat w dwóch kolumnach Light 9.5pt.
3. **Tytuł**: `.h2` (15pt Black) — w dokumentach formalnych BEZ kropki na końcu (kropka tylko w display headlines).
4. **Treść**: Light 10.5pt, line-height 1.5, `max-width:160mm`; nagłówki sekcji SemiBold 11pt numerowane (`1. Przedmiot umowy`); listy z wcięciem 6 mm.
5. **Podpisy** (umowy/NDA): dwie kolumny z linią `border-top:1px solid var(--veles-black)`, pod nią imię + funkcja Light 9pt.
6. **Stopka**: `.foot` — dane rejestrowe (NIP/KRS/kapitał) Light 7pt zamiast paginacji ozdobnej; numer strony „2/5".

## Reguły specyficzne

- Zero elementów dekoracyjnych (znaków wartości, znaku z pikseli) — dokument formalny ma być cichy; brand niesie nagłówek + typografia + ewentualnie `.acc` pod tytułem.
- SOP: krok = SemiBold, opis = Light; numeracja `01.` stylem `.label` czarnym.
- Umowy/NDA: paragrafy `§ 1.`, wyrównanie do lewej (nie justuj — Light źle justuje).

## Workflow

Jak w `deck.md`; dla DOCX → routing `anthropic-skills:docx` (Manrope, struktura nagłówków zachowana).
