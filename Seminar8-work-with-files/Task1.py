import time

# with open('les8test.txt', 'r', encoding='utf-8') as file:
#     find_letter = input()
#     count = 0
#     start = time.time()
#     for letter in file.read():
#         if letter == find_letter:
#             count += 1
#     end = time.time()
#     print(count)
#     print(end - start)


with open('les8test.txt', 'r', encoding='utf-8') as file:
    find_letter = input()
    start = time.time()
    print(file.read().count(find_letter))
    end = time.time()
    print(end - start)
