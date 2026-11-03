#!/usr/bin/env bash
# Veles: self-contained HTML -> PDF przez headless Chrome (print CSS @page).
# Użycie: scripts/html2pdf.sh plik.html [plik.pdf]
set -euo pipefail

IN="${1:?Użycie: html2pdf.sh plik.html [plik.pdf]}"
OUT="${2:-${IN%.html}.pdf}"

find_chrome() {
  # Ścieżki uniksowe pierwsze (macOS, Linux), Windows/Git Bash na końcu.
  local localapp=""
  if [ -n "${LOCALAPPDATA:-}" ] && command -v cygpath >/dev/null 2>&1; then
    localapp="$(cygpath -u "$LOCALAPPDATA")"
  fi
  for c in \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "/Applications/Chromium.app/Contents/MacOS/Chromium" \
    "$(command -v google-chrome || true)" \
    "$(command -v chromium || true)" \
    "/c/Program Files/Google/Chrome/Application/chrome.exe" \
    "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe" \
    "${localapp:+$localapp/Google/Chrome/Application/chrome.exe}"; do
    [ -x "$c" ] && { echo "$c"; return; }
  done
  echo "Brak Chrome/Chromium" >&2; exit 1
}

# Chrome na Windows nie rozumie ścieżek MSYS (/c/...) — obie strony muszą być natywne.
to_native() {
  if command -v cygpath >/dev/null 2>&1; then cygpath -m "$1"; else printf '%s' "$1"; fi
}
to_url() {
  if command -v cygpath >/dev/null 2>&1; then printf 'file:///%s' "$(cygpath -m "$1")"
  else printf 'file://%s' "$1"; fi
}

IN_ABS="$(cd "$(dirname "$IN")" && pwd)/$(basename "$IN")"
OUT_ABS="$(cd "$(dirname "$OUT")" && pwd)/$(basename "$OUT")"

CHROME="$(find_chrome)"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$(to_native "$OUT_ABS")" "$(to_url "$IN_ABS")" 2>/dev/null
echo "OK $OUT"
