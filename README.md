# Veles Brand — Brand 3.2

**This is the Veles Productions brand.** One repository for the team and for our AI agents:
the brand book, a one-page guide, logos, signs, colours, fonts, ready-to-paste animated
elements for the website, a banner generator — and the plugin that builds branded decks and
documents in Claude Code and Gemini CLI.

- **Brand book (web, with motion):** https://veles-productions.github.io/veles-brand/
- **Download everything (ZIP, no account needed):** https://github.com/veles-productions/veles-brand/archive/refs/heads/main.zip

## Start here

| If you want to… | Open |
|---|---|
| understand the brand | [`BRAND-BOOK.md`](BRAND-BOOK.md) or the web version |
| know the essentials in one page | [`QUICK-GUIDE.md`](QUICK-GUIDE.md) |
| put the brand into Claude Code, Gemini CLI or Cursor | [`INSTALL-PROMPT.md`](INSTALL-PROMPT.md) |
| update the website | [`website/WEBSITE-BRIEF.md`](website/WEBSITE-BRIEF.md) |
| make a banner | [`banners/banner.html`](banners/banner.html) (open in a browser) |
| add motion to a web page | [`embeds/`](embeds/) |
| build decks and documents with the plugin | [`INSTALL.md`](INSTALL.md), then `/veles-brand` |

## What is inside

```
AGENTS.md              brand rules your AI agent loads (compact) + how to build materials
BRAND-BOOK.md          the full brand book
QUICK-GUIDE.md         one page, plus what each person should do
INSTALL-PROMPT.md      the prompt that installs the brand in your agent
index.html             the brand book as a web page
cursor/                rule file for Cursor (copy of AGENTS.md)
embeds/                pixel-sign hero, sign draw, reveal + progress, UI components
banners/               banner generator: Kadr and Red, four social sizes
website/               brief for the website update
systems/               Veles Systems preview (green, not final)
skills/veles-brand/    the design system and plugin (Polish):
  tokens/              tokens.css, tokens.json — colours, type, motion
  brand/               rules, don'ts, checklist, gaps, signs, motion
  templates/           deck, one-pager, report, document, e-mail, webdoc, opsdoc
  assets/              logo PNGs, Veles signs (SVG), pixel-sign grids, Manrope
  scripts/             embed_assets.py, html2pdf.sh
.claude-plugin/, gemini-extension.json, GEMINI.md, commands/   plugin manifests
```

## Embedding animated elements (Webflow and others)

Each file in `embeds/` opens as a demo in a browser. Copy everything between
`VELES EMBED START` and `VELES EMBED END` into a Webflow **Code Embed** (or any HTML block).
No libraries, no iframes. Motion stops automatically for visitors with reduced motion.

## For maintainers

- Change of brand (tokens/rules) → commit describing the decision; keep `tokens.json` and
  `tokens.css` in sync; `cursor/veles-brand.mdc` is a copy of `AGENTS.md` with a header.
- Versioning: bump `version` together in `plugin.json`, `marketplace.json`, `gemini-extension.json`.
- The repository is **public**: no secrets, no client data, no fonts without a distribution
  licence (Alliance No.2 stays out until its licence allows it — `brand/gaps.md` G12).

## Rights

Logo and Veles signs © Veles Productions — for Veles team and partners working on Veles
materials only. Manrope: SIL Open Font License (`skills/veles-brand/assets/fonts/Manrope-OFL.txt`).

Questions: Artur Paprocki.
