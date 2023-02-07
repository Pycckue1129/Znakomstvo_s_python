# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# d g h t r g r h t j h b v f d s d f
#
# d g h t r g_2 r_2 h_2 t_2 j h_3 b v f d_2 s d_3 f_2

string = 'd g h d r g r h t j h b v f d s d f'
my_list = string.split()
my_dict = {}
new_list = []

for letter in my_list:
    my_dict[letter] = my_dict.get(letter, 0) + 1
    if my_dict.get(letter) > 1:
        new_list.append(letter + '_' + str(my_dict.get(letter)))
    else:
        new_list.append(letter)
print(' '.join(new_list))

