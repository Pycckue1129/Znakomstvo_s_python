# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


num1 = int(input('Введите первый элемент: '))
diff = int(input('Введите разность: '))
num2 = int(input('Введите кол-во повторений: '))
for i in range(num2):
    print(num1 + i * diff)