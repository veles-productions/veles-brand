# Veles Productions — Wytyczne Animacji & Higgsfield AI

Dokument określający rygorystyczne reguły tworzenia wideo, animacji (motion) oraz grafik generatywnych w ekosystemie **Veles Productions**. Dwa różne konteksty, dwie sekcje: generacja wideo/obrazu przez Higgsfield CLI (poniżej) oraz animacja CSS w samodzielnych dokumentach HTML (webdoc — dalsza część pliku).

---

## Wideo/obraz — Higgsfield

### 1. Kadrowanie i Format Obrazu (Ratio)
- **Vertical Drama (9:16):** Podstawowy format dla mobilnych form narracyjnych i reklamowych. Zawsze wymuszaj proporcje `9:16` w parametrach generacji wideo.
- **Kąty i Perspektywa:** Preferuj rzuty pod kątem ostrym **45 stopni**, nadające scenom dynamiki i trójwymiarowości (spójnie z kątami 0/45/90 znaków Velesa). Unikaj płaskich rzutów od przodu.

---

### 2. Paleta Kolorów w Generacjach (Color Guardrails)
Podczas generowania obrazów i wideo przez Higgsfield AI, zawsze narzucaj w promptach rygorystyczne ograniczenie kolorów (Color Guardrails):
- **Czerń Veles (`#160606`):** Dominujące tło, głębokie, ciepłe, filmowe cienie (*low-key lighting*).
- **Czerwień Veles (`#ef3e46`):** Stosowana jako światło obrysowe (*rim-light*), neonowe akcenty świetlne lub laserowe refleksy.
- **Biel i szarości:** Neutralne oświetlenie wolumetryczne i szczegóły twarzy/tekstur.
- **Zakazy:** Żadnych ciepłych pastelowych gradientów, tęczowych flar czy miękkich, rozproszonych teł.

---

### 3. Przykładowe Struktury Promptów (Brand Prompts)

Stosuj poniższe formuły jako bazę do promptów w komendach `higgsfield generate create`:

### A. Dla Generacji Wideo (Video Motion):
> `"Veles Productions style cinematic video of [TEMAT], dramatic low-key lighting with signature neon red rim-light #ef3e46, 45-degree sharp geometric camera angle, deep shadows, dark moody atmosphere, volumetric smoke, ultra-high fidelity, 9:16 vertical drama framing, minimal aesthetic, Seedance 2.0 --ar 9:16"`

### B. Dla Zdjęć Produktowych (Product Photoshoot):
> `"Veles Productions product-photoshoot mode of [PRODUKT], levitating in dark room, sharp angular laser reflections in signature red color #ef3e46, cinematic light, dark background, industrial aesthetic, ultra-sharp detail, high-end CGI, no warm gradients"`

---

### 4. Łączenie z Tożsamością Cyfrową (Soul ID)
Zawsze zachowuj spójność twarzy przy użyciu wytrenowanych modeli Soul:
1. Uruchom proces uczenia: `higgsfield soul-id train` (pobierz `reference_id`).
2. Wywołaj generację z flagą: `higgsfield generate create --model soul_cinema_studio --prompt "[PROMPT]" --soul-id <reference_id>`.

---

## CSS/web — animacja w dokumentach HTML

Dotyczy webdoc (`templates/webdoc.md`) i innych self-contained dokumentów HTML — kontekst
całkowicie inny niż generacje Higgsfield powyżej: brak modelu wideo, tylko przeglądarka.
Ruch tu nie jest dekoracją, tylko **narracją "przebudzenia"** systemu runicznego (zobacz
`brand/runes.md`) — starożytność opowiadamy geometrią i sekwencją, nigdy fakturą.

### 1. Dozwolone ruchy (zamknięta lista — cztery, nic ponad to)

1. **Reveal okładki/logo** — jedna sekwencja odpalana przy załadowaniu strony (fade/slide
   znaku "V" lub tytułu). Odtwarzana raz, nigdy w pętli.
2. **Runa kreślona** (`stroke-dasharray`/`stroke-dashoffset`) — przy wejściu runy w viewport
   obrys "domyka się" jak dopisywany znak. To najbardziej on-brand ruch systemu: stary znak
   odzyskuje kształt = przebudzenie starożytnej technologii. Używaj wyłącznie na runach
   funkcjonalnych/wartości z `assets/runes/`, nigdy na dekoracji bez znaczenia.
3. **Przełom sekcji light/dark** — przy granicy rozdziałów (`.chapter`/`.section-break`)
   subtelny crossfade albo `clip-path` wipe, sygnalizujący zmianę rejestru, nie efekt sam
   w sobie.
4. **Pasek postępu scrolla** — cienki pasek na akcencie `.acc`, szerokość = postęp czytania.
   Funkcjonalny wskaźnik, nie ornament.

Nic poza tą czwórką nie wchodzi do dokumentów HTML bez świadomej decyzji brandowej.

### 2. Technika (twarda)

- Wyłącznie CSS `@keyframes`/`transition` + vanilla `IntersectionObserver`. Zero bibliotek
  animacyjnych, zero CDN (self-contained HTML to zasada nadrzędna skilla — patrz
  `scripts/embed_assets.py`).
- Każda animacja sterowana `IntersectionObserver` odpala się **raz**: po wejściu elementu
  w viewport wykonaj `observer.unobserve(el)` (albo `disconnect()` dla pojedynczego elementu).
  Scroll w górę/dół nie ma retriggerować ruchu.
- Czasy trwania i krzywe easingu **zawsze** przez zmienne z `tokens/tokens.css` (kategoria
  `motion`, np. `--veles-motion-duration-*` / `--veles-motion-ease-*`) — nigdy hardkodowane
  `ms`/`cubic-bezier()` w szablonach. Dokładne nazwy zmiennych: `tokens/tokens.json` →
  `motion`.

### 3. `prefers-reduced-motion` (obowiązkowy, bez wyjątków)

Każdy dokument z motion MUSI zawierać blok `@media (prefers-reduced-motion: reduce)`, który
sprowadza wszystkie animowane elementy do stanu końcowego natychmiast (bez przejścia):
runy w pełni dokreślone, okładka w pełni odsłonięta, sekcje bez wipe'u. Brak tego bloku =
błąd QA (dopisz do `brand/checklist.md` przy wdrażaniu webdoc).

### 4. Twarde zakazy

- **Staggered fade-and-rise** na kolejnych elementach/sekcjach (rozpoznawalny tell generacji
  AI — Impeccable go łapie) — żadnych sekwencyjnych "wjazdów" bulletów/kart.
- Ruch bez funkcji informacyjnej (animacja dla samej animacji).
- Animacje zapętlone w treści dokumentu (loop dozwolony wyłącznie poza treścią, np. w promptach
  wideo Higgsfield powyżej — nie w webdoc).
- Parallax (efekt warstw przy scrollu) w jakiejkolwiek formie.

### 5. Wzorcowe snippety (do kopiowania przez `templates/_shared-webdoc.html`)

**Runa kreślona — CSS:**
```css
.rune-draw path {
  fill: none;
  stroke-dasharray: var(--rune-length, 300);
  stroke-dashoffset: var(--rune-length, 300);
  transition: stroke-dashoffset var(--veles-motion-duration-draw, 1200ms)
    var(--veles-motion-ease-draw, ease-out);
}
.rune-draw.is-visible path {
  stroke-dashoffset: 0;
}
@media (prefers-reduced-motion: reduce) {
  .rune-draw path { transition: none; stroke-dashoffset: 0; }
}
```

**IntersectionObserver — jednorazowe odpalenie, bez bibliotek:**
```js
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.4 });
  document.querySelectorAll('.rune-draw, .chapter, .section-break')
    .forEach((el) => io.observe(el));
} else {
  document.querySelectorAll('.rune-draw, .chapter, .section-break')
    .forEach((el) => el.classList.add('is-visible'));
}
```

**Pasek postępu scrolla:**
```js
const bar = document.querySelector('.scroll-progress');
window.addEventListener('scroll', () => {
  const h = document.documentElement;
  const pct = h.scrollTop / (h.scrollHeight - h.clientHeight);
  bar.style.width = (pct * 100) + '%';
}, { passive: true });
```
```css
.scroll-progress {
  position: fixed; top: 0; left: 0; height: 3px; width: 0;
  background: var(--veles-red);
  transition: width var(--veles-motion-duration-fast, 200ms) linear;
  z-index: 100;
}
```

---

## Znak z pikseli — hero strony i ekran startowy dashboardu

Brand 3.0 (decyzja 2026-11-02). Element graficzny marki w ruchu: znaki wartości na siatce
15×15 zapalają się jak piksele ściany LED. To **piąty ruch**, ale **poza dokumentami** —
webdoc i dokumenty zostają przy czterech ruchach wyżej i pokazują znak z pikseli statycznie.
Wzorzec: płótno Brand 3.0, plansza 13 (`Piksel.dc.html`).

### 1. Gdzie wolno

- Hero strony velesproductions.com (pełny kadr, wielki tytuł, etykieta z kwadratem,
  przyciski ze strzałką — struktura nowej strony zostaje).
- Ekran startowy dashboardu lub interfejsu zespołu.
- Nigdzie indziej: nie w treści, nie w kartach, nie jako loader.

### 2. Ruch

- Siatka: `pixel-grids.json` (15 wierszy po 15 znaków, `#` = piksel zapalony).
- Piksel zapalony `#ef3e46` (odwaga) lub `#e7e9ed` (pozostałe); zgaszony
  `rgba(231,233,237,.07)`.
- **Przejście = obrót płytek** (decyzja 2026-11-02, plansza 15, kierunek C). Każdy piksel to
  płytka z dwiema stronami (`transform-style: preserve-3d`, dwie twarze z
  `backface-visibility: hidden`, tył obrócony o 180°; kontener `perspective: 900px`). Przy
  zmianie znaku na stronę niewidoczną wchodzi nowy znak, a płytka obraca się o kolejne 180°
  (`rotateY(krok*180deg)`), więc obrót zawsze idzie w tę samą stronę.
- Fala kołem od środka: opóźnienie płytki `round(√((w−7)²+(k−7)²) * 140ms)`; obrót
  `transform 1100ms cubic-bezier(.7,-.25,.25,1.3)` — lekki zamach w tył, dobicie z odbiciem.
  Cała zmiana trwa ok. 2,1 s, więc cykl nie krótszy niż 3,6 s.
- Odrzucone na planszy 15: puls od środka (A) i wymiana klocków (B).
- Cykl: kolejny znak co 3,6 s. Szyna sześciu miniatur pod
  tytułem pozwala wybrać znak; kliknięcie **zatrzymuje cykl** na stałe.
- Jedna siatka na ekranie. Zero bibliotek — CSS `transition` + `setInterval`.

### 3. `prefers-reduced-motion`

Obowiązkowy: przy `reduce` bez przejść (`transition: none`) i **bez cyklu** — widać jeden
znak (odwagę), szyna dalej działa jako wybór.

```css
.px-wall{perspective:900px}
.px{transform-style:preserve-3d;
  transition:transform 1100ms cubic-bezier(.7,-.25,.25,1.3)}   /* delay z JS: odległość od środka × 140ms */
.px>i{position:absolute;inset:0;backface-visibility:hidden}
.px>i+i{transform:rotateY(180deg)}
@media (prefers-reduced-motion: reduce){.px{transition:none}}
```

### 4. Zakazy

- Migotanie, losowe zapalanie pikseli, efekt „glitch”.
- Więcej niż jedna żywa siatka na ekranie; znak z pikseli obok amuletu.
- Siatki wygenerowane automatycznym rastrem ze ścieżek — tylko ręcznie rysowane siatki z repo.