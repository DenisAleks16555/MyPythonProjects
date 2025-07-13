def remove_number(numbers, target):
    count = 0  # Счётчик удалённых элементов
    while target in numbers:  # Пока число target есть в списке
        numbers.remove(target)  # Удаляем первое вхождение числа target
        count += 1  # Увеличиваем счётчик на 1
    return count  # Возвращаем количество удалённых элементов
my_list = [1, 2, 3, 2, 4, 2, 5]
removed_count = remove_number(my_list, 2)
print("Количество удалённых чисел:", removed_count)  # Выведет: 3
print("Обновлённый список:", my_list)  # Выведет: [1, 3, 4, 5]