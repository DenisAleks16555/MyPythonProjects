# Шаг 1: Определение кортежей
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (4, 5, 8, 9)

# Шаг 2: Преобразование кортежей в множества
set1 = set(tuple1)
set2 = set(tuple2)
set3 = set(tuple3)

# Шаг 3: Нахождение пересечения
common_elements = set1 & set2 & set3

# Шаг 4: Вывод результата
print(common_elements)