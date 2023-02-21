# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).


with open('article.txt', 'r', encoding='utf-8') as file:
    text = file.read().split()
print(text)


def longest_words(file1):
    text2 = {}
    for el in file1:
        for i in range(len(el) - 1, len(el)):
            text2[el] = i + 1
    maxim = 0
    for i in text2.items():
        if maxim < i[1]:
             maxim = i[1]
    for key, value in text2.items():
        if value == maxim:
            print(key)


longest_words(text)