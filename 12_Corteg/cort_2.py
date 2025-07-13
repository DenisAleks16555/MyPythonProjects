# Шаг 1: Определение кортежей
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (4, 5, 8, 9)

# Шаг 2: Преобразование кортежей в множества
set1 = set(tuple1)
set2 = set(tuple2)
set3 = set(tuple3)

# Шаг 3: Нахождение уникальных элементов
unique_to_tuple1 = set1 - set2 - set3
unique_to_tuple2 = set2 - set1 - set3
unique_to_tuple3 = set3 - set1 - set2

# Шаг 4: Вывод результата
print("Уникальные элементы для tuple1:", unique_to_tuple1)
print("Уникальные элементы для tuple2:", unique_to_tuple2)
print("Уникальные элементы для tuple3:", unique_to_tuple3)