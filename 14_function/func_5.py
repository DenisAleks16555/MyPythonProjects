def product_in_range(lower, upper):
    # Проверяем, какая граница меньше
    if lower > upper:
        lower, upper = upper, lower  # Меняем местами границы

    # Инициализируем переменную для произведения
    product = 1

    # Умножаем все целые числа в диапазоне от lower до upper
    for number in range(lower, upper + 1):
        product *= number  # Умножаем текущее число на product

    return product  # Возвращаем итоговое произведение

# Примеры вызова функции
result1 = product_in_range(3, 5)  # 3 * 4 * 5 = 60
result2 = product_in_range(5, 3)  # 3 * 4 * 5 = 60 (границы перепутаны)
result3 = product_in_range(1, 4)  # 1 * 2 * 3 * 4 = 24

print("Произведение от 3 до 5:", result1)  # Ожидаемый вывод: 60
print("Произведение от 5 до 3:", result2)  # Ожидаемый вывод: 60
print("Произведение от 1 до 4:", result3)  # Ожидаемый вывод: 24