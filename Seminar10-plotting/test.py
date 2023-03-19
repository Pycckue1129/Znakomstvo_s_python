def search_number_in_array(arr, num):
    """
    Функция для поиска числа в массиве

    :param arr: Массив, в котором производится поиск
    :param num: Число, которое нужно найти
    :return: Индекс числа в массиве, если оно найдено. -1, если число не найдено.
    """
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1


# Пример использования функции
arr = [3, 5, 1, 7, 2, -1]
num = -1
result = search_number_in_array(arr, num)
if result != -1:
    print("Число", num, "найдено в массиве, индекс =", result)
else:
    print("Число", num, "не найдено в массиве")
