# Хакер Василий получил доступ к классному журналу и хочет заменить
# все свои минимальные оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
import random
import time

magazine = [random.randint(2, 10) for _ in range(100)]
# list comprehension
start = time.perf_counter()
maxx = max(magazine)
minn = min(magazine)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
minn = magazine[0]
maxx = magazine[0]
for el in magazine:
    if el < minn:
        minn = el
    elif el > maxx:
        maxx = el
end = time.perf_counter()
print(end - start)
for ind in range(0, len(magazine)):
    if magazine[ind] == maxx:
        magazine[ind] = minn
print(magazine)



# print(list1)

