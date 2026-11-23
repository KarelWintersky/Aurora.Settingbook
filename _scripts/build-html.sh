#!/usr/bin/env bash
# Сборка готового HTML-документа в PDF (A4) через печать Chromium.
# Здесь pandoc не нужен: листы персонажей — уже сверстанный HTML со своим <style>.
# Использование: ./_scripts/build-html.sh input.html output.pdf
# Пути аргументов считаются от корня репозитория.
set -euo pipefail
cd "$(dirname "$0")/.."

in="${1:?usage: build-html.sh input.html output.pdf}"
out="${2:?usage: build-html.sh input.html output.pdf}"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# Фрагмент оборачиваем в документ; готовый документ с <!DOCTYPE> берём как есть.
if head -c 512 "$in" | grep -qi '<!doctype'; then
  cp "$in" "$tmp/page.html"
else
  {
    printf '%s\n' '<!DOCTYPE html>' '<html lang="ru"><head><meta charset="utf-8">'
    printf '%s\n' "<title>$(basename "$in" .html)</title></head><body>"
    cat "$in"
    printf '%s\n' '</body></html>'
  } > "$tmp/page.html"
fi

chromium --headless --no-sandbox --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=3000 \
  --print-to-pdf="$out" "$tmp/page.html" 2>/dev/null

pdfinfo "$out" | grep -E 'Pages|Page size'
