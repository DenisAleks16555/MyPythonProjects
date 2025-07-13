def count_digits(number):
    # Преобразуем число в строку
    number_str = str(number)
    
    # Убираем знак минус, если он есть (для отрицательных чисел)
    if number_str[0] == '-':
        number_str = number_str[1:]

    # Подсчитываем количество цифр
    digit_count = len(number_str)
    
    return digit_count  # Возвращаем количество цифр

# Примеры вызова функции
result1 = count_digits(3456)    # Ожидаемый вывод: 4
result2 = count_digits(-12345)   # Ожидаемый вывод: 5
result3 = count_digits(0)        # Ожидаемый вывод: 1

print("Количество цифр в 3456:", result1)
print("Количество цифр в -12345:", result2)
print("Количество цифр в 0:", result3)