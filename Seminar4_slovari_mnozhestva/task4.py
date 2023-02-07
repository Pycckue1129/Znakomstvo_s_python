my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20, 'g': 9999}

# maxim = 0
# for i in my_dict.values():
#     temp = i
#     if i > maxim:
#         maxim = i
# print(maxim)

maxim = 0
for i in my_dict.items():
    if maxim < i[1]:
        maxim = i[1]

print(maxim)