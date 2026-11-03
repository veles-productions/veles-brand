# velesproductions.com → Brand 3.2 — brief for Sam

**Goal:** the whole site — home and every subpage — speaks Brand 3.2.
**Keep:** the structure and the dynamics of the current site (full-screen image, very big type,
motion on scroll, card rails, the LED pixel grid feeling). Artur likes how the site *moves*.
**Change:** colour, font, graphic element, a few details below.

Rules: `../BRAND-BOOK.md` · tokens: `../skills/veles-brand/tokens/tokens.css` · snippets: `../embeds/`.

## 1. Global changes (Webflow → Site settings / Style guide)

| What | Now | Brand 3.2 |
|---|---|---|
| Body background | `#000000` | `#160606` (Veles black) |
| Text on dark | `#e7e9ed` | stays `#e7e9ed` |
| Accent | various reds | only `#ef3e46` |
| Font | BR Hendrix | **Manrope** (add in Site settings → Fonts → Google Fonts; weights 300, 400, 500, 600, 800). Font stack `'Alliance No.2', Manrope, sans-serif` |
| Headlines | BR Hendrix 900 | Manrope **800**, sentence case, ending with a full stop |
| Body text | — | Manrope **300**, line-height 1.5–1.6 |
| Labels / eyebrow | BR Hendrix 500, tracked | Manrope 600, uppercase, letter-spacing .12em, small red square before the label |
| Buttons | — | sharp corners (max 4 px), text + arrow →, red fill or 1 px outline |
| Cards | — | sharp corners, no coloured shadows, no glow |

Search the Webflow CSS for any other hex and map it to the palette. Leftover classes with
old colours: delete or remap.

## 2. Hero (home)

- Full-bleed video or set photo stays. Black gradient from bottom-left for legibility.
- Very big headline (e.g. *Stories + Systems.*), red label with a square above it, buttons with arrows.
- **Pixel sign** in the hero, at most ~200 px: paste `embeds/pixel-sign-hero.html`
  into a Webflow **Code Embed** (instructions inside the file). One live grid per screen, no more.

## 3. Every subpage

- Same palette, font, buttons, labels. Page titles with a full stop.
- Section breaks: full Veles black or full red; no patterns behind content.
- One functional or value sign per section at most (`skills/veles-brand/assets/runes/*.svg`) — e.g. a drawn sign
  next to a section title with `embeds/sign-draw.html`. Not at every heading.
- Long pages: optional red progress bar (`embeds/reveal-and-progress.html`).
- Reveal on scroll for blocks (same snippet). `prefers-reduced-motion` must be respected.

## 4. Logo

- Red logo on Veles black (or black on red). Minimum **88 px** height on screen.
  If it does not fit somewhere, write *Veles Productions* in text instead of shrinking it.
- Never on top of a photo or video; never stretched (in flex containers: `align-self:flex-start`).

## 5. Images

- Real Veles set photos and video (Media Lab). No stock "tech" images, no AI glow, no neon.
- Faces: confirmed by Artur before going live.

## 6. Veles Systems pages

If the site links to Veles Systems, use only a **hint** of the green system: a small green
label or accent `#2f9e44` on that link/section, black logo. The full Systems brand is not
finished — do not restyle whole pages green. See `../systems/README.md`.

## 7. Done when

- [ ] no `#000000`, no BR Hendrix, no other reds anywhere in the published CSS
- [ ] all headlines Manrope 800 with a full stop; body Manrope 300
- [ ] hero has the pixel sign; it stops with `prefers-reduced-motion`
- [ ] logo ≥ 88 px, never on photos
- [ ] all subpages checked on desktop and mobile (991 / 767 / 479 px)
- [ ] staging link sent to Artur **before** publishing to the live domain
