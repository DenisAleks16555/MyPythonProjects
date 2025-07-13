numbers = [45, 12, 103, 6]
sorted_numbers = sorted(numbers, key=lambda x: x % 10)
print(sorted_numbers)  # Вывод: [12, 103, 45, 6]