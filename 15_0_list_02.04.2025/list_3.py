# Шаг 1: Ввод числа n
n = int(input("Введите натуральное число n: "))

# Шаг 2: Создание списка квадратов
squares = [x**2 for x in range(1, n + 1)]

# Шаг 3: Вывод элементов списка
for square in squares:
    print(square)