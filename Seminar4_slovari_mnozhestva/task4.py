# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 999}

# maxim = 0
# for i in my_dict.values():
#     temp = i
#     if i > maxim:
#         maxim = i
# print(maxim)
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 9999}
maxim_value1 = 0
maxim_value2 = 0
maxim_value3 = 0
for i in my_dict.items():
    if maxim_value1 < i[1]:
        maxim_value1 = i[1]
        maxim_key1 = i[0]
for i in my_dict.values():
    if i[1] == maxim_value1:
        del my_dict[i[0]]

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
# del my_dict[20]
print(my_dict)