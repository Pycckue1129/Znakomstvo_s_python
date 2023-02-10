# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exp(num1, exp_num):
    if exp_num == 1:
        return num1
    else:
        return num1 * exp(num1, exp_num - 1)


print(exp(3, 5))