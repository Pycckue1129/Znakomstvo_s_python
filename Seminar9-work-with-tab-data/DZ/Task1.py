import pandas as pd

df = pd.read_csv('california_housing_train.csv')

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

print(df.loc[(df['population'] >= 0) & (df['population'] <= 500), ['median_house_value']].mean())


# Задача 42: Узнать какая максимальная households в зоне минимального значения population

print(df.loc[df['population'] == df['population'].min(), ['households']].max())
