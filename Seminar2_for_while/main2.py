# 9. По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

n = int(input())
i = n
while i != 1:
    n = n * (i - 1)
    i = i - 1
print(n)