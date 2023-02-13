# 43. Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные друг
# другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# array = [1, 2, 3, 4, 1, 2, 4, 6, 6, 6,]
# array1 = []
# count = 0
# for i in array:
#     if array.count(i) > 1 and i not in array1:
#         count += 1
#         array1.append(i)

# for i in range(len(array)):
#     for j in range(len(array)):
#         if array[i] == array[j] and:

# print(array1)
# print(count)

# ----------------------------------------

some_list = []
while True:
    numbers = int(input())
    if numbers == 0:
        break
    some_list.append(numbers)

count_dict = {}

for el in some_list:
    if count_dict.get(el):
        count_dict[el] += 1
    else:
        count_dict[el] = 1
print(count_dict)

count = 0
for value in count_dict.values():
    count += value // 2
print(count)