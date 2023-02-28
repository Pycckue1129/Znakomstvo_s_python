# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(f'    whoAmI_human  whoAmI_robot')
for i in range(len(data.values)):
    if data.values[i] == 'robot' and i < 10:
        print(f'{i}          0          1')
    elif data.values[i] == 'robot' and i > 10:
        print(f'{i}         0          1')
    elif data.values[i] == 'human' and i < 10:
        print(f'{i}          1          0')
    elif data.values[i] == 'human' and i > 10:
        print(f'{i}         1          0')

