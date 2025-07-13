# Исходный список
numbers = [2, 4, 6, 8, 10]

# Используем map и лямбда-функцию для получения списка квадратов
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Выводим результат
print(squared_numbers)