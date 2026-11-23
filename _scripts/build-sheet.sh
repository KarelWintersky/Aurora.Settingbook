#!/usr/bin/env bash
# Сборка основного листа персонажа «Аврора» (A4): HTML -> PDF.
# Скрипт-обёртка, вся работа в build-html-to-pdf.sh.
set -euo pipefail
exec "$(dirname "$0")/build-html-to-pdf.sh" erls4/character-sheet.html erls4/character-sheet.pdf
