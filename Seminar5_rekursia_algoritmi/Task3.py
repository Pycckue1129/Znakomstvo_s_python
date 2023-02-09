# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым


def is_simple(num):
    if num == 2 or num == 1:
        print('Число является простым')
        return True

    for i in range(2, num):
        if num % i == 0:
            print('Число не является простым')
            return False
    if i == num - 1:
        print('Число является простым')
        return True


n = int(input('Введите число: '))
is_simple(n)
