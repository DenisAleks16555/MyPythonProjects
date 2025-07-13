numbers = [3, -1, 0, 7, -5, 2, 0, -3, 4, -2]
print(f"Список чисел: {numbers}")

# Инициализируем min и max значениями первого элемента списка
min_value = numbers[0]
max_value = numbers[0]

# Находим минимальный и максимальный элементы
for number in numbers:
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number

# Подсчитываем количество отрицательных, положительных элементов и нулей
negative_count = 0
positive_count = 0
zero_count = 0

for number in numbers:
    if number < 0:
        negative_count += 1
    elif number > 0:
        positive_count += 1
    else:
        zero_count += 1

# Выводим результаты
print(f"Минимальный элемент: {min_value}")
print(f"Максимальный элемент: {max_value}")
print(f"Количество отрицательных элементов: {negative_count}")
print(f"Количество положительных элементов: {positive_count}")
print(f"Количество нулей: {zero_count}")