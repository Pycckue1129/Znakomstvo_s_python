# 39. Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором
# массиве. Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором
# массиве. Затем элементы второго массива

# array1 = []
# array2 = []
# array3 = []
# n1 = int(input())
# n2 = int(input())
# for i in range(n1):
#     array1.append(int(input()))
# print(array1)
# for j in range(n2):
#     array2.append(int(input()))
# print(array2)

#
# for i in array1:
#     if array2.count(i) < 1:
#         array3.append(i)
# print(array3)

# --------------------------------------------
first_list = [int(input()) for _ in range(int(input('Введите ко-во чисел: ')))]
second_list = [int(input()) for _ in range(int(input('Введите ко-во чисел: ')))]

# --------------------------------------------
# for el in first_list:
#     if el not in second_list:
#         print(el)


# ----------------------------------------------

second_set = set(second_list)
for el in first_list:
    if el not in second_set:
        print(el)