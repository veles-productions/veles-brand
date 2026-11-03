# veles-brand — setup nowej maszyny

> Skrót instalacji per runtime jest w `README.md`. Tu szczegóły i tło.

## 1. Klon (stała ścieżka)

```bash
mkdir -p ~/Projects && cd ~/Projects
gh repo clone veles-productions/veles-brand   # albo: git clone https://github.com/veles-productions/veles-brand
```

Windows (PowerShell): `mkdir D:\Projects; cd D:\Projects; gh repo clone veles-productions/veles-brand`

## 2. Claude Code

**Plugin (zalecane):**

```bash
# w sesji Claude Code:
/plugin marketplace add ~/Projects/veles-brand
/plugin install veles-brand@veles
```

**Luźny skill (alternatywa):** skille user-level NIE synchronizują się przez Google Drive,
dlatego symlink do klonu — celuj w podkatalog `skills/veles-brand`:

```bash
ln -sfn ~/Projects/veles-brand/skills/veles-brand ~/.claude/skills/veles-brand
```

Windows: `New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\veles-brand" -Target "D:\Projects\veles-brand\skills\veles-brand"`

Weryfikacja: nowa sesja → skill `veles-brand` widoczny; prompt „zrób onepager Veles o usłudze X" triggeruje.

## 3. Gemini CLI

```bash
gemini extensions link ~/Projects/veles-brand
# lub z GitHuba:
gemini extensions install https://github.com/veles-productions/veles-brand
# fallback ręczny:
ln -sfn ~/Projects/veles-brand ~/.gemini/extensions/veles-brand
```

Gemini wczytuje `GEMINI.md` jako kontekst + komendę `/veles-brand`.

## 4. Codex / inne

`AGENTS.md` w root prowadzi do `skills/veles-brand/`. Pliki są agent-agnostyczne — każdy agent czyta je wprost.

## 5. Zależności

- `python3` (embed_assets.py; PIL opcjonalny — przycina logo do bbox).
- Google Chrome lub Chromium (html2pdf.sh).
- ŻADNYCH env vars ani sekretów do generowania. Aktualizacja assetów z Media Lab →
  `VELES_MEDIALAB_API_KEY` (skill `veles-medialab`).

## 6. Zasady repo

- Repo **prywatne** — fonty marki leżą tu tylko w zakresie ich licencji; licencja Alliance No.2 do ustalenia (gaps G12).
- Sekrety nigdy w repo (`.gitignore`: `.env`). Repo jest publiczne — żadnych danych klientów w plikach.
- Zmiany brandu (tokens/rules) → commit z opisem decyzji + sync `tokens.json` ↔ `tokens.css`.
- Wersja: bump jednocześnie w `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `gemini-extension.json`.
