import pandas as pd

data = {
    'Фамилия': ['Иванов', 'Петров', 'Сидоров', 'Федоров', 'Смирнов', 'Кузнецов', 'Волков', 'Соколов', 'Андреев', 'Дмитриев'],
    'Оценка': [4, 5, 5, 3, 4, 5, 5, 4, 5, 5],
    'Предмет': ['Математика', 'Математика', 'Математика', 'Физика', 'Физика', 'Физика', 'Химия', 'Химия', 'Литература', 'Биология']
}

df = pd.DataFrame(data)
print(df.head())

math_mean = df[df['Предмет'] == 'Математика']['Оценка'].mean()
print(f'Средняя оценка по математике: {math_mean}')

physics_mean = df[df['Предмет'] == 'Физика']['Оценка'].mean()
print(f'Средняя оценка по физике: {physics_mean}')

chemistry_mean = df[df['Предмет'] == 'Химия']['Оценка'].mean()
print(f'Средняя оценка по химии: {chemistry_mean}')

biology_mean = df[df['Предмет'] == 'Биология']['Оценка'].mean()
print(f'Средняя оценка по биологии: {biology_mean}')

literature_mean = df[df['Предмет'] == 'Литература']['Оценка'].mean()
print(f'Средняя оценка по литературе: {literature_mean}')

math_median = df[df['Предмет'] == 'Математика']['Оценка'].median()
print(f'Медианная оценка по математике: {math_median}')

physics_median = df[df['Предмет'] == 'Физика']['Оценка'].median()
print(f'Медианная оценка по физике: {physics_median}')

chemistry_median = df[df['Предмет'] == 'Химия']['Оценка'].median()
print(f'Медианная оценка по химии: {chemistry_median}')

biology_median = df[df['Предмет'] == 'Биология']['Оценка'].median()
print(f'Медианная оценка по биологии: {biology_median}')

literature_median = df[df['Предмет'] == 'Литература']['Оценка'].median()
print(f'Медианная оценка по литературе: {literature_median}')

q1_math = df[df['Предмет'] == 'Математика']['Оценка'].quantile(0.25)
print(q1_math)

q3_math = df[df['Предмет'] == 'Математика']['Оценка'].quantile(0.75)
print(q3_math)

IQR_math = q3_math - q1_math
print(f'IQR для математики: {IQR_math}')

std_math = df[df['Предмет'] == 'Математика']['Оценка'].std()
print(f'Стандартное отклонение для математики: {std_math}')

std_physics = df[df['Предмет'] == 'Физика']['Оценка'].std()
print(f'Стандартное отклонение для физики: {std_physics}')

std_chemistry = df[df['Предмет'] == 'Химия']['Оценка'].std()
print(f'Стандартное отклонение для химии: {std_chemistry}')

std_biology = df[df['Предмет'] == 'Биология']['Оценка'].std()
print(f'Стандартное отклонение для биологии: {std_biology}')

std_literature = df[df['Предмет'] == 'Литература']['Оценка'].std()
print(f'Стандартное отклонение для литературы: {std_literature}')
