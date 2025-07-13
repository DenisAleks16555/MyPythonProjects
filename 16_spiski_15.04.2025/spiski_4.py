numbers = [-5, 10, -3, 20, 0, 7]

# Отфильтровываем положительные числа
positive_numbers = filter(lambda x: x > 0, numbers)

# Умножаем на 2
doubled_positive_numbers = map(lambda x: x * 2, positive_numbers)

# Преобразуем в список и выводим результат
result_list = list(doubled_positive_numbers)
print(result_list)  # Ожидаемый вывод: [20, 40, 14]