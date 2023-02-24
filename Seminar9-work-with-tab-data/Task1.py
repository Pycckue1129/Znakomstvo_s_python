#  https://colab.research.google.com/drive/11udiVDM85HFjqLqDqfz0ef9NLBgHUWn-?usp=share_link

#  http://kodesource.top/python-exercises/pandas/practice-set1/index.php


import pandas as pd

df = pd.read_csv('california_housing_train.csv')
df.head(11)  # Посмотреть первые 11 строк
df.tail()  # Посмотреть последние 5 строк
df.shape  # Возвращает размеры таблицы: кортеж из 2 значений, 1 кол-во строк, 2 - кол-во столбцов
df.isnull().sum()  # Посмотреть есть ли у нас пустые значения
df.dtypes  # Проверить тип данных в столбцах
df.columns  # Посмотреть все столбцы


# Выбор данных
df['latitude']  # Выбор 1 столбца - [широты]
df[['latitude', 'population']]  # Выбор нескольких столбцов [широта, кол-во жителей]
df[df['housing_median_age'] < 5]  # Выбор определенного кол-ва рядов
df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]  # Для отбора можно использовать несколько условий одновременно
df[(df['housing_median_age'] > 20) | (df['total_rooms'] > 2000)]
df.loc[df['population'] < 100, ['total_bedrooms', 'total_rooms']]  # Выбор определенного кол-ва рядов и столбцов

print(df['population'].max())  # Максимальное значение
print(df['population'].min())  # Минимальное значение
print(df['population'].mean())  # Среднее значение
print(df['population'].sum())  # Сумма

df[['population', 'total_rooms']].median()  # Медианное значение
df.describe()



