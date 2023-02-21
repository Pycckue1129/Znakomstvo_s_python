# Напишите функцию read_last(lines, file), которая будет открывать
# определенный файл file и выводить на печать построчно последние
# строки в количестве lines (на всякий случай проверим, что задано
# положительное целое число). Протестируем функцию на файле «article.txt»
# со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


with open('article.txt', 'r', encoding='utf-8') as file:
    text = file.read().splitlines()
    print(text)


def read_last(lines, file1):
    if lines < 0:
        return False
    else:
        for word in range(len(file1) - lines, len(file1)):
            print(file1[word])


read_last(4, text)