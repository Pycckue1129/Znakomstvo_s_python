# Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

# 1 способ
# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 9999}
# maxim_value1 = 0
# maxim_value2 = 0
# maxim_value3 = 0
# for i in my_dict.items():
#     if maxim_value1 < i[1]:
#         maxim_value1 = i[1]
#         maxim_key1 = i[0]
# del my_dict[maxim_key1]
#
# for i in my_dict.items():
#     if maxim_value2 < i[1]:
#         maxim_value2 = i[1]
#         maxim_key2 = i[0]
# del my_dict[maxim_key2]
#
# for i in my_dict.items():
#     if maxim_value3 < i[1]:
#         maxim_value3 = i[1]
#         maxim_key3 = i[0]
# del my_dict[maxim_key3]
#
# print(maxim_value1, maxim_value2, maxim_value3)
#
# print(my_dict)

# Второй способ
# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 9999}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# for i in my_dict.items():
#     if i[0] == result[0] or i[0] == result[1] or i[0] == result[2]:
#         print(i[1], end=' ')

# Третий способ
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 9999}
from heapq import nlargest
result = nlargest(3, my_dict, key=my_dict.get)
for i in my_dict.items():
    if i[0] == result[0] or i[0] == result[1] or i[0] == result[2]:
        print(i[1], end=' ')
