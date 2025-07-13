fruits = ["apple", "banana", "cherry"]

# Преобразуем список в список длин слов
lengths = list(map(lambda x: len(x), fruits))

# Выводим результат
print(lengths)  # Вывод: [5, 6, 6]