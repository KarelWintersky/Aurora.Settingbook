#!/usr/bin/env bash
# Сборка листа персонажа «Аврора»: markdown -> HTML -> PDF (A4).
# Запускать из любой директории: пути считаются от корня репозитория.
set -euo pipefail
cd "$(dirname "$0")/.."

pandoc -f markdown -t html5 erls4/character-sheet.md -o /tmp/aurora-sheet-body.html

{
  printf '%s\n' '<!DOCTYPE html>' '<html lang="ru"><head><meta charset="utf-8">'
  printf '%s\n' '<title>Аврора — лист персонажа</title></head><body>'
  cat /tmp/aurora-sheet-body.html
  printf '%s\n' '</body></html>'
} > /tmp/aurora-sheet.html

chromium --headless --no-sandbox --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=3000 \
  --print-to-pdf=erls4/character-sheet.pdf /tmp/aurora-sheet.html 2>/dev/null

pdfinfo erls4/character-sheet.pdf | grep -E 'Pages|Page size'
