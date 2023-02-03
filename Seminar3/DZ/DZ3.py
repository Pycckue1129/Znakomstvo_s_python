# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_1 = [1.1, 1.2, 3.1, 5, 10.01]
maxim = 0
for i in list_1:
    if i > maxim:
        maxim = i
minim = maxim
for i in list_1:
    if i < minim:
        minim = i
diff = (maxim % 1) - (minim % 1)
diff = abs(diff)
print(f'Минимум: {minim},Максимум: {maxim}')
print(round(diff, 2))
