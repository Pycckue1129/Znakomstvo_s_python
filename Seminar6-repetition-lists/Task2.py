# 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в
# данном массиве определит количество элементов, у которых два соседних и,
# при этом, оба соседних элемента меньше данного. Сначала вводится число
# N — количество элементов в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.
#
array = [1, 2, 3, 1, 7, 5]
n = 0
for i in range(1, len(array) - 1):
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        n += 1
print(n)

