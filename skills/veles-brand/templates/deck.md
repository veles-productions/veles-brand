# Template: deck (prezentacja / oferta / pitch)

**Kiedy:** prezentacja sprzedażowa, oferta handlowa z budżetem, pitch deck, prezentacja inwestorska.
**Format:** A4 **landscape** (297×210 mm), self-contained HTML, multi-page `.page`.

## Struktura stron

1. **Cover — Kadr** (`.page.kadr`: `<img class="bg">` z prawdziwym zdjęciem z planu Veles + `.shade` + mały `.pixel-sign` jako podpis w rogu; brand/rules.md §4): logo czerwone (32 mm), `.label` (typ dokumentu), `.h1` 44pt biały z `.r` na słowie kluczowym, `.meta` (klient · data · CONFIDENTIAL jeśli trzeba). Tytuł z kropką.
2. **Agenda / kontekst** (`.page` light): `.label` + `.h1` + `.acc` + `.lede`.
3. **Strony treści**: stat tiles (`.stats`/`.stat`) dla liczb, `.cols`/`.col` dla wariantów (v1 czarny / v2 grey-blue / v3 czerwony border), `table.t` dla budżetów (wiersz `.price` na podsumowanie, `.hl` na rekomendowany wariant).
4. **Separator sekcji** (opcjonalnie `.page.red` lub `.page.dark`): wielki `.h1`, numer sekcji.
5. **Zamknięcie**: CTA + kontakt + tagline „Shaping Digital Worlds for Human Future".

## Reguły specyficzne

- Każda strona content: `.ptop` (logo czarne **16 mm** + caption) i `.foot` (VELES PRODUCTIONS · paginacja — **stopka jest tekstowa, bez logo**; dlaczego: `brand/rules.md` → minimalne wysokości znaku).
- Max ~5 bloków na stronę; landscape nie znosi ścisku — lepiej dodać stronę.
- Budżety: kwoty wyrównane do prawej, separator tysięcy spacją, waluta po kwocie (`120 000 PLN`).
- Wariant rekomendowany oznacz `.tag.r` „REKOMENDACJA" + `.hl` w tabeli.

## Workflow

1. Skopiuj `templates/_shared.html` → wypełnij placeholdery i treść (duplikuj `.page` ile trzeba).
2. `python3 scripts/embed_assets.py draft.html out.html` (fonty+logo base64).
3. QA: `brand/checklist.md` + render-check (screenshot pierwszej i ostatniej strony).
4. PDF: `scripts/html2pdf.sh out.html` (landscape jest w `@page`).
