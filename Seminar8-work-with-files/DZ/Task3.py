# ДОП ЗАДАЧА.
# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста.
# У нас труб будет больше.
#
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения
# всего бассейна только одной данной работающей трубой (в часах). Затем после пустой
# строки перечислены трубы, которые будут заполнять бассейн. Сколько минут на это потребуется?
#
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
#
# Результат запишите в файл time.txt
#
# Пример
# Ввод
#
# 1
# 2
# 3
# (пустая строка)
# 1 2 3
#
# Вывод
# 32.72727272727273


with open('pipes.txt', 'w', encoding='utf-8') as file:
    amount = int(input('Введите количество насосов: '))
    for i in range(amount):
        file.write(str(i + 1) + '\n')
    file.write('\n')
    for j in range(amount):
        file.write(str(j + 1) + ' ')

with open('pipes.txt', 'r', encoding='utf-8') as file:
    list1 = file.read().split('\n')
list1.remove('')
pumps = list1[-1].split()
with open('time.txt', 'w', encoding='utf-8') as time:
    summ = 0
    for i in pumps:
        summ += 1 / int(i)
    time.write(str(60 / summ))