#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wypełnia placeholdery brandu Veles w pliku HTML → self-contained output.

Użycie: python3 scripts/embed_assets.py draft.html out.html

Placeholdery:
  {{FONT_FACES}}      @font-face dla fontu marki (base64): Alliance No.2, a gdy jej pliku
                      nie ma w assets/fonts/ — Manrope (zamiennik, Brand 3.0)
  {{LOGO_RED_B64}}    Logo_big_red.png   (base64, przycięte do bbox jeśli PIL)
  {{LOGO_BLACK_B64}}  Logo_big_black.png
  {{LOGO_WHITE_B64}}  Logo_big_white.png
  {{PIXEL_SIGN}}      data-URI SVG: znak odwagi z pikseli 15x15 (element graficzny okładki)

Inne placeholdery ({{TITLE}} itd.) zostawia nietknięte — wypełnia je agent treścią.
"""
import base64, io, sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
LOGOS = ROOT / "assets" / "logo"
RUNES = ROOT / "assets" / "runes"

# Kolejność = priorytet. Rodzina trafia do @font-face pod własną nazwą, a stack w tokenach
# ('Alliance No.2', Manrope, sans-serif) sam wybierze pierwszą dostępną.
FAMILIES = [
    ("Alliance No.2", "AllianceNo2-*"),
    ("Manrope", "Manrope-*"),
]
WEIGHT_NAMES = {"light": 300, "regular": 400, "medium": 500, "semibold": 600, "extrabold": 800}
FORMATS = {".woff2": ("font/woff2", "woff2"), ".ttf": ("font/ttf", "truetype"), ".otf": ("font/otf", "opentype")}

def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()

def b64_logo(path: Path) -> str:
    try:
        from PIL import Image
        im = Image.open(path).convert("RGBA")
        bbox = im.getbbox()
        if bbox:
            im = im.crop(bbox)
        buf = io.BytesIO()
        im.save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode()
    except ImportError:
        return b64(path)

def font_faces() -> str:
    for family, pattern in FAMILIES:
        faces = []
        for p in sorted(FONTS.glob(pattern)):
            weight = WEIGHT_NAMES.get(p.stem.split("-")[-1].lower())
            if p.suffix.lower() not in FORMATS or weight is None:
                continue
            mime, fmt = FORMATS[p.suffix.lower()]
            faces.append(f"@font-face{{font-family:'{family}';src:url(data:{mime};base64,{b64(p)}) "
                         f"format('{fmt}');font-weight:{weight};font-style:normal;font-display:swap}}")
        if faces:
            return "".join(faces)
    print("UWAGA: brak plików fontu marki w assets/fonts/ (Alliance No.2 ani Manrope) — "
          "tekst spadnie do systemowego sans-serif.", file=sys.stderr)
    return ""

def pixel_sign(name: str = "courage", color: str = "#ef3e46") -> str:
    svg = (RUNES / f"pixel-{name}.svg").read_text(encoding="utf-8")
    svg = svg.replace('fill="currentColor"', f'fill="{color}"')
    return "data:image/svg+xml;utf8," + quote(" ".join(svg.split()), safe=" /:='<>.")  # " → %22: URI siedzi w url("...")

def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    html = src.read_text(encoding="utf-8")
    html = html.replace("{{FONT_FACES}}", font_faces())
    html = html.replace("{{LOGO_RED_B64}}", b64_logo(LOGOS / "Logo_big_red.png"))
    html = html.replace("{{LOGO_BLACK_B64}}", b64_logo(LOGOS / "Logo_big_black.png"))
    html = html.replace("{{LOGO_WHITE_B64}}", b64_logo(LOGOS / "Logo_big_white.png"))
    html = html.replace("{{PIXEL_SIGN}}", pixel_sign())
    dst.write_text(html, encoding="utf-8")
    print(f"OK {dst} ({dst.stat().st_size//1024} kB)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
