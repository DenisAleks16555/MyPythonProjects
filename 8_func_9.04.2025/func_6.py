def power_list(numbers, exponent):
    result = []  # Создаем пустой список для хранения результатов
    for number in numbers:  # Проходим по каждому числу в списке
        powered_value = number ** exponent  # Возводим число в степень
        result.append(powered_value)  # Добавляем результат в новый список
    return result  # Возвращаем новый список с результатами

my_numbers = [1, 2, 3, 4]  # Список целых чисел
exponent_value = 2  # Значение степени

powered_numbers = power_list(my_numbers, exponent_value)  # Вызываем функцию и сохраняем результат
print(powered_numbers)  # Выводим новый список