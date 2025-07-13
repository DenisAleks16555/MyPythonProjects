mixed = [3, 7, "apple", 2.5, [1, 2]]
numbers = []

for item in mixed:
    if type(item) in (int, float):  # Проверяем, является ли элемент целым или дробным числом
        numbers.append(item)

print(numbers)  # Вывод: [3, 7, 2.5]