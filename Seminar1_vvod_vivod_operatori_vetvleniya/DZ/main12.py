# Задача 12: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

num1 = int(input('Задумайте первое число: '))
num2 = int(input('Задумайте второе число: '))

hint_sum = num1 + num2
hint_multy = num1 * num2
print(f'Сумма {hint_sum}, произведение {hint_multy}')
x = 0
y = 1
count = 1
for x in range(hint_sum):
    for y in range(hint_multy):
        if x + y == hint_sum and x * y == hint_multy and count == 1:
            print(f'Задуманные числа {x} и {y}')
            count += 1
