# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть выведите
# такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1

first_el = 0
second_el = 1
number = int(input())
next_el = first_el + second_el
i = 3
while next_el < number:
    first_el = second_el
    second_el = next_el
    next_el = first_el + second_el
    i += 1
if next_el == number:
    print(i)
else:
    print(-1)
