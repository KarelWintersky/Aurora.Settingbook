#!/usr/bin/env bash
# Универсальная сборка: markdown -> HTML -> PDF (A4), без шаблона pandoc.
# Использование: ./_scripts/build-pdf.sh input.md output.pdf
# Пути аргументов считаются от корня репозитория.
set -euo pipefail
cd "$(dirname "$0")/.."

in="${1:?usage: build-pdf.sh input.md output.pdf}"
out="${2:?usage: build-pdf.sh input.md output.pdf}"
tmp="$(mktemp -d)"

pandoc -f markdown -t html5 "$in" -o "$tmp/body.html"

{
  printf '%s\n' '<!DOCTYPE html>' '<html lang="ru"><head><meta charset="utf-8">'
  printf '%s\n' "<title>$(basename "$in" .md)</title></head><body>"
  cat "$tmp/body.html"
  printf '%s\n' '</body></html>'
} > "$tmp/page.html"

chromium --headless --no-sandbox --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=3000 \
  --print-to-pdf="$out" "$tmp/page.html" 2>/dev/null

rm -rf "$tmp"
pdfinfo "$out" | grep -E 'Pages|Page size'
