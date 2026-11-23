# Aurora.Settingbook

Материалы по сеттингу «Аврора» и его адаптации под систему **E.R.L.S.4d**:
рабочий документ по адаптации, листы персонажей, вступительная сцена.

Репозиторий: <https://github.com/KarelWintersky/Aurora.Settingbook>

## Структура

```
erls4/                     исходники сеттингбука (Markdown) + собранные PDF рядом
  aurora-erls4d-adaptation.md    адаптация E.R.L.S.4d под сеттинг «Аврора»
  character-sheet.md             лист персонажа (базовый)
  character-sheet-ingvar.md      заполненный лист: Ингвар
  character-sheet-marta.md       заполненный лист: Марта
  scenario-01-crocodile.md       вступительная сцена «Крокодил не несётся»
_scripts/                  сборочные скрипты
  build-pdf.sh                   markdown -> HTML -> PDF (A4), универсальный
  build-sheet.sh                 сборка листа персонажа (A4, плотная вёрстка)
  _fix_rounds.py                 разовая правка раундов в листе Марты
_preview/                  растровые превью (не версионируется)
```

Исходный текст сеттинга (`erls4/_full.md`) — служебный материал, лежит только локально
и в репозиторий не попадает.

## Сборка PDF

Требования: `pandoc` (проверено на 3.11), `chromium`, `pdfinfo` (poppler-utils).
TeX не нужен: цепочка идёт через HTML5 → печать Chromium.

```bash
./_scripts/build-pdf.sh erls4/scenario-01-crocodile.md erls4/scenario-01-crocodile.pdf
./_scripts/build-sheet.sh          # -> erls4/character-sheet.pdf
```

Скрипты сами переходят в корень репозитория, поэтому пути аргументов считаются
от корня.

## Статус

- [x] Адаптация системы под сеттинг
- [x] Листы персонажей и сцена-проба
- [ ] Сеттингбук (добавляется отдельно)

## Заметки по вёрстке

Пайплайн печатает HTML без CSS, поэтому у таблиц в PDF нет рамок и сетки:
pandoc отдаёт «голый» `<table>`, а браузерный дефолт рамок не рисует. При необходимости
рамки добавляются CSS-блоком в `_scripts/build-pdf.sh`:

```css
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #888; padding: 4px 6px; vertical-align: top; }
thead th { background: #eee; }
tr { break-inside: avoid; }
@page { size: A4; margin: 15mm; }
```
