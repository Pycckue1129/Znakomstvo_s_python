# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input())
num1 = 0
num2 = 1
list_1 = [1, 0, 1]
fib = 0
count = 0
while k - 1 > count:
    fib = num1 + num2
    num1 = num2
    num2 = fib
    list_1.append(fib)
    list_1.insert(0, -fib)
    count += 1
print(list_1)