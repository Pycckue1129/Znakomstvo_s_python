# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
n = int(input('Введите количество элементов 1-ого множества: '))
m = int(input('Введите количество элементов 2-ого множества: '))

n1 = set()
m1 = set()
for i in range(n):
    n1.add(int(input('Введите числа 1-ого множества: ')))
for j in range(m):
    m1.add(int(input('Введите числа 2-ого множества: ')))

diff = list(n1.intersection(m1))
diff = sorted(diff)
string = ''
for k in range(len(diff)):
    string = f'{string}{diff[k]} '
print(string)