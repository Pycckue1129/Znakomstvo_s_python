# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#
# *Пример:*
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

num = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = []
#
# my_dict = {}
#
# for n in num:
#     my_dict[n] = my_dict.get(n, 0) + 1
# for i in my_dict:
#     if my_dict.get(i) == 1:
#         new_list.append(i)

print([i for i in num if num.count(i) == 1])
