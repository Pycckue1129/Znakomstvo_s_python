with open('les8test.txt', 'r', encoding='utf-8') as file:  # Чтение
    # text = file.read().splitlines()
    # print(text)

    while True:
        line = file.readline()
        if not line:
            break
        # print(line)
        print(line.strip())


with open('filetest.txt', 'w', encoding='utf-8') as file:   # Запись
    some_list = ['Привет', 'Пока']
    for word in some_list:
        file.write(word + '\n')

