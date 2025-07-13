numbers = [1000, 5, 23, 456]
sorted_numbers = sorted(numbers, key=lambda x: len(str(x)))
print(sorted_numbers)  # Вывод: [5, 23, 456, 1000]