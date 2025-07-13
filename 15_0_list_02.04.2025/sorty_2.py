# Шаг 1: Получение ввода от пользователя
user_input = input("Введите целые числа, разделенные пробелами: ")

# Шаг 2: Преобразование ввода в список целых чисел
numbers = list(map(int, user_input.split()))

# Шаг 3: Сортировка списка по возрастанию
sorted_ascending = sorted(numbers)

# Сортировка списка по убыванию
sorted_descending = sorted(numbers, reverse=True)

# Шаг 4: Вывод результата
print("Список по возрастанию:", sorted_ascending)
print("Список по убыванию:", sorted_descending)