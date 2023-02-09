# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

n = int(input())


def fib(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(n))