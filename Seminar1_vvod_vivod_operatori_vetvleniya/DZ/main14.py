# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8
n = int(input(f'Введите число: '))
num_degree = 1
while num_degree < n:
    print(num_degree, end=' ')
    num_degree *= 2
