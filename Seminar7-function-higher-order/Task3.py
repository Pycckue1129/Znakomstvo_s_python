# Дан массив с числами, и целевое значение. Нужно проверить найдутся ли в массиве два числа,
#  чья сумма равна целевому значению
import time
import random

summa = 102
some_list = [random.randint(1, 100000) for _ in range(10 ** 6)]

start = time.perf_counter()
some_set = set(some_list)
for el in some_set:
    if summa - el in some_set:
        print(el, summa - el)
        break
else:
    print('no')
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
for el in some_list:
    if summa - el in some_list:
        print(el, summa - el)
        break
else:
    print('no')
end = time.perf_counter()
print(end - start)
