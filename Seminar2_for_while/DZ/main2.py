# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


summa = int(input('Введите общее количество журавликов:'))
katya = (summa // 3) * 2
petya = katya // 4
sergey = petya
print(f'Петя сделал {petya} журавликов, Катя {katya} журавликов и Сережа {sergey} журавликов')
