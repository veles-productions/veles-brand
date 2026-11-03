---
description: Wygeneruj materiał w brandzie Veles (deck / onepager / raport / dokument / stopka maila) jako self-contained HTML.
argument-hint: "<typ> <opis treści> — np. onepager o usłudze ICVFX"
---

Pracujesz w systemie brandowym **Veles Productions** (plugin `veles-brand`).

Zanim cokolwiek wygenerujesz, wykonaj DOKŁADNIE:

1. Przeczytaj `${CLAUDE_PLUGIN_ROOT}/skills/veles-brand/SKILL.md` — tożsamość marki, router, guardraile.
2. Dobierz szablon po typie i przeczytaj go z `${CLAUDE_PLUGIN_ROOT}/skills/veles-brand/templates/<typ>.md`
   (deck / onepager / report / document / email). Skopiuj `templates/_shared.html` jako bazę.
3. Wartości liczbowe (kolory, wagi, mm/pt) bierz WYŁĄCZNIE z
   `${CLAUDE_PLUGIN_ROOT}/skills/veles-brand/tokens/tokens.json` — paleta jest ZAMKNIĘTA.
4. Osadź fonty + logo: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/veles-brand/scripts/embed_assets.py draft.html out.html`.
5. QA OBOWIĄZKOWE: przejdź `${CLAUDE_PLUGIN_ROOT}/skills/veles-brand/brand/checklist.md`
   (grep kolorów/fontów + render-check screenshotem). Nie oddawaj materiału bez tego.
6. Materiał do druku/wysyłki → PDF: `${CLAUDE_PLUGIN_ROOT}/skills/veles-brand/scripts/html2pdf.sh out.html`.

Twarde zakazy: hex spoza palety, `#000000` (czerń Veles to `#160606`), font spoza stacka `'Alliance No.2', Manrope, sans-serif`, wordmark „VELES." z kropką,
transformacje/przebarwienia logo. Pełna lista: `brand/dont.md`.

Zadanie użytkownika: $ARGUMENTS
