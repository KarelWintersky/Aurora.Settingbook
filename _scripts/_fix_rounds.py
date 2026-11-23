import re, io, os

# Файлы лежат в erls4/, скрипт — в _scripts/: работаем относительно корня репозитория.
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "erls4"))

p = "character-sheet-marta.html"
s = io.open(p, encoding="utf-8").read()

def repl(start_marker, new_block):
    global s
    i = s.index(start_marker)
    # find the end of this round div: the closing </div> after the <p class="small"...> line
    j = s.index("</div>", s.index('</table>', i)) + len("</div>")
    s = s[:i] + new_block + s[j:]

r2 = '''<div class="round"><div class="rh">Раунд 2 · сближение · инициатива: Марта 8, Ржавый 5</div>
<table><tr><th style="width:14%">Кто</th><th style="width:24%">Действие</th><th style="width:8%">ЕД</th><th style="width:27%">Бросок</th><th>Результат</th></tr>
<tr><td>Марта</td><td>Шаг к сараю</td><td class="c">2</td><td>—</td><td>Дистанция 12 м</td></tr>
<tr><td>Марта</td><td>Прицел + выстрел</td><td class="c">3</td><td>к6+1+1 → <b>2+2=4</b> против 4+2=6</td><td><b>Промах:</b> укрытие съело пулю; на перезарядку осталось 2 ЕД</td></tr>
<tr><td>Ржавый</td><td>Бросает револьвер, выходит из укрытия</td><td class="c">1</td><td>—</td><td>Понимает: на дистанции не выиграть</td></tr>
<tr><td>Ржавый</td><td>Сближение + удар ножом</td><td class="c">4</td><td>к6+3−2 → <b>4+1=5</b> против к6+0 → 2</td><td><b>Попадание.</b> Урон 1d6+1 = <b>4</b>. Марта 13→9: среднее (−1, 40 хитов ранений)</td></tr></table>
<p class="small" style="padding:1.2mm 2mm 1.6mm">Итог: Марта 9 ХП и −1, Ржавый 7 ХП и −2. <b>Урок:</b> пустой дробовик в ближнем бою — просто палка. Нож у неё — навыка нет, попадание к6−5.</p>
</div>'''

r3 = '''<div class="round"><div class="rh">Раунд 3 · вплотную · инициатива: Ржавый 9, Марта 7</div>
<table><tr><th style="width:14%">Кто</th><th style="width:24%">Действие</th><th style="width:8%">ЕД</th><th style="width:27%">Бросок</th><th>Результат</th></tr>
<tr><td>Ржавый</td><td>Удар ножом</td><td class="c">2</td><td>к6+3−2 → <b>5+1=6</b> против к6+0 → 1</td><td><b>Попадание.</b> Урон 1d6+1 = <b>3</b>. Марта 9→6: среднее, суммарный штраф −2, 70 хитов</td></tr>
<tr><td>Ржавый</td><td>Шаг в сторону</td><td class="c">1</td><td>—</td><td>Осталось 3 ЕД</td></tr>
<tr><td>Марта</td><td>Разрыв дистанции</td><td class="c">2</td><td>—</td><td>Отходит на 10 м</td></tr>
<tr><td>Марта</td><td>Перезарядка</td><td class="c">3</td><td>—</td><td>Дробовик заряжен, осталось 2 ЕД</td></tr></table>
<p class="small" style="padding:1.2mm 2mm 1.6mm">Итог: Марта 6 ХП и −2, Ржавый 7 ХП и −2. <b>Урок:</b> ранения складываются. Два средних — это уже −2 на всё, включая стрельбу.</p>
</div>'''

r4 = '''<div class="round"><div class="rh">Раунд 4 · развязка · инициатива: Марта 10, Ржавый 4</div>
<table><tr><th style="width:14%">Кто</th><th style="width:24%">Действие</th><th style="width:8%">ЕД</th><th style="width:27%">Бросок</th><th>Результат</th></tr>
<tr><td>Марта</td><td>Прицел + выстрел</td><td class="c">3</td><td>к6+1+1−2 → <b>5+0=5</b> против 4</td><td><b>Попадание.</b> Урон 2d6+2 = <b>10</b>. Ржавый 7→−3: тяжёлое, суммарно 20 &gt; 17</td></tr>
<tr><td>Ржавый</td><td>Укидка на сознание</td><td class="c">—</td><td>к12 ≤ 9−4 = 5 → выпало 8</td><td><b>Без сознания</b></td></tr>
<tr><td>Марта</td><td>Первая помощь</td><td class="c">3</td><td>к6+0 против сложности 4</td><td>Спасёт — заговорит</td></tr></table>
<p class="small" style="padding:1.2mm 2mm 1.6mm">Итог: Марта 6 ХП, два средних ранения, 5 патронов. Ржавый жив или мёртв — зависит от того, станет ли она его спасать. <b>Урок:</b> бой решается не силой, а дистанцией, укрытием и перезарядкой.</p>
</div>'''

repl('<div class="round"><div class="rh">Раунд 2', r2)
repl('<div class="round"><div class="rh">Раунд 3', r3)
repl('<div class="round"><div class="rh">Раунд 4', r4)

io.open(p, "w", encoding="utf-8").write(s)
print("ok")
