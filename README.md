# Aurora.Settingbook

Материалы по сеттингу «Аврора» и его адаптации под систему **E.R.L.S.4d**:
рабочий документ по адаптации, листы персонажей, вступительная сцена.

Репозиторий: <https://github.com/KarelWintersky/Aurora.Settingbook>

## Структура

```
erls4/                     исходники сеттингбука + собранные PDF рядом
  aurora-erls4d-adaptation.md    адаптация E.R.L.S.4d под сеттинг «Аврора» (Markdown)
  scenario-01-crocodile.md       вступительная сцена «Крокодил не несётся» (Markdown)
  character-sheet.html           пустой бланк (2 стр.) + шпаргалка игрока
  character-sheet-ingvar.html    заполненный лист: Ингвар — HTML
  character-sheet-marta.html     заполненный лист: Марта — HTML
_scripts/                  сборочные скрипты
  build-md-to-pdf.sh             markdown -> HTML -> PDF (A4), универсальный
  print.css                      печатные стили для него: поля A4, рамки таблиц
  build-html-to-pdf.sh           готовый HTML -> PDF (A4), без pandoc
  build-sheet.sh                 обёртка: основной лист персонажа -> PDF
  _fix_rounds.py                 разовая правка раундов в листе Марты
_preview/                  растровые превью (не версионируется)
```

Листы персонажей — не Markdown, а сверстанный HTML: у каждого свой `<style>` с `@page`,
классами и таблицами. Поэтому они собираются `build-html-to-pdf.sh` (Chromium печатает файл как есть),
а не через pandoc: pandoc-HTML-reader выбрасывает `<style>`, и вёрстка теряется.
Markdown-источники (адаптация, сцена) идут через `build-md-to-pdf.sh`.

Исходный текст сеттинга (`_full.md` в корне) — служебный материал, лежит только локально
и в репозиторий не попадает.

## Сборка PDF

Требования: `pandoc` (проверено на 3.11), `chromium`, `pdfinfo` (poppler-utils).
TeX не нужен: цепочка идёт через HTML/HTML5 → печать Chromium.

```bash
# Markdown-источники
./_scripts/build-md-to-pdf.sh erls4/scenario-01-crocodile.md erls4/scenario-01-crocodile.pdf
./_scripts/build-md-to-pdf.sh erls4/aurora-erls4d-adaptation.md erls4/aurora-erls4d-adaptation.pdf

# HTML-листы персонажей (pandoc не нужен)
./_scripts/build-sheet.sh                      # -> erls4/character-sheet.pdf
./_scripts/build-html-to-pdf.sh erls4/character-sheet-marta.html erls4/character-sheet-marta.pdf
```

Скрипты сами переходят в корень репозитория, поэтому пути аргументов считаются
от корня.

## Статус

- [x] Адаптация системы под сеттинг
- [x] Листы персонажей и сцена-проба
- [ ] Сеттингбук (добавляется отдельно)

## Заметки по вёрстке

`build-md-to-pdf.sh` вставляет в `<head>` файл `_scripts/print.css`. Раньше CSS не было вовсе:
pandoc отдаёт «голый» `<table>`, а браузерный дефолт рамок не рисует — таблицы в PDF
сливались в текст. Правки оформления делаются в `print.css`:

```css
@page { size: A4; margin: 15mm 15mm 16mm; }
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; }
th, td { border: 1px solid #999; padding: 3px 6px; vertical-align: top; }
thead th { background: #f0f0f0; }
tr { break-inside: avoid; }
```

`@page` тут важен ещё и потому, что без него Chromium печатает в Letter, а не в A4.
У листов персонажей (`.html`) стили свои, встроенные — `print.css` к ним не применяется.
