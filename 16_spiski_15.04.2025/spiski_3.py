fruits = ["apple", "banana", "cherry", "avocado", "orange"]

# Функция фильтрации
def starts_with_a(word):
    return word.startswith('a')

# Применение filter и map
filtered_fruits = filter(starts_with_a, fruits)
uppercased_fruits = map(str.upper, filtered_fruits)

# Преобразование в список
result = list(uppercased_fruits)

# Итоговый вывод
print(result)  # ['APPLE', 'AVOCADO']