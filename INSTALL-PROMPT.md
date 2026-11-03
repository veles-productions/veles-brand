# Install the new Veles brand in your AI agent

No GitHub account needed. The kit is public:
- Brand book (web): https://veles-productions.github.io/veles-brand/
- Download everything (ZIP): https://github.com/veles-productions/veles-brand/archive/refs/heads/main.zip

**How:** open your agent (Claude Code, Gemini CLI or Cursor), paste the prompt below, press
Enter. The agent downloads the kit, plugs it into its instructions and removes the old Veles
brand rules. It takes about a minute. Then ask it: *"What are the Veles brand colours?"* — it
should answer `#160606` and `#ef3e46`.

---

## The prompt (same for every agent)

```text
Install the new Veles Productions brand (Brand 3.2) for me and replace the old one.

1. Download https://github.com/veles-productions/veles-brand/archive/refs/heads/main.zip
   and unpack it. The ZIP contains a folder named veles-brand-main; rename it so that the
   folder is:
   - Windows: %USERPROFILE%\veles-brand
   - macOS / Linux: ~/veles-brand
   If the folder exists, replace it with the fresh download. Check that AGENTS.md and
   BRAND-BOOK.md are directly inside it. If there is an older ~/veles-brand-kit folder,
   delete it.

2. Connect it to your permanent instructions, depending on which agent you are:
   - Claude Code: add the line  @~/veles-brand/AGENTS.md  to ~/.claude/CLAUDE.md
     (create the file if missing).
   - Gemini CLI: add the line  @~/veles-brand/AGENTS.md  to ~/.gemini/GEMINI.md
     (create the file if missing).
   - Cursor: copy ~/veles-brand/cursor/veles-brand.mdc into .cursor/rules/ of the
     project I have open, and tell me to also paste the contents of AGENTS.md into
     Cursor Settings > Rules > User Rules so it works in every project.

3. Replace the old brand. Search those instruction files (and any rules, skills, memories or
   style files you use) for older Veles brand rules: BR Hendrix, Arial, #000000 as the Veles
   black, the reds #c8313a #e0233a #dd0000 #bc3138, the 45° parallelogram, "Pole LED",
   and any pointer to veles-brand-kit (the old location of this kit).
   Show me what you found, then remove or replace it with a pointer to
   ~/veles-brand/AGENTS.md. Do not touch anything that is not about the Veles brand.

4. Confirm in three lines: where the kit is, which instruction file now points to it, and
   what old rules you removed. Then tell me the two main brand colours and the font.
```

---

## Updating later

Paste the same prompt again — step 1 replaces the folder with the newest version.

## Without an agent

Download the ZIP, unpack it, open `index.html` in a browser. Fonts are in `skills/veles-brand/assets/fonts/`
(install Manrope), logos in `skills/veles-brand/assets/logo/`, colours in `skills/veles-brand/tokens/tokens.css`.

## Making decks and documents (Claude Code / Gemini CLI plugin)

The same repository is also a plugin that builds branded decks, one-pagers, reports and
documents. Setup: `INSTALL.md`. If you cloned this repository before 3 November 2026, delete
that clone and clone it again — its history was rebuilt when it became public.
