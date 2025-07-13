# Шаг 1: Определение функции
def display_even_numbers(start, end):
    # Шаг 2: Определение диапазона
    if start > end:
        start, end = end, start  # Обмен значениями, если start больше end

    # Шаг 3: Поиск четных чисел
    for number in range(start, end + 1):  # Включаем end в диапазон
        if number % 2 == 0:  # Проверка на четность
            # Шаг 4: Вывод четных чисел
            print(number)

# Шаг 5: Вызов функции
display_even_numbers(3, 10)