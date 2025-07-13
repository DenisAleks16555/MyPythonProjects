# Шаг 1: Ввод данных
input_data = input("Введите целые числа через пробел: ")
# Преобразуем строку в список целых чисел
numbers = list(map(int, input_data.split()))

# Шаг 2: Находим индексы максимального и минимального элементов
max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))

# Шаг 3: Переставляем элементы местами
numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

# Шаг 4: Вывод измененного списка с помощью распаковки
print(*numbers)