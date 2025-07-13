fruits = ["Банан", "яблоко", "Вишня", "арбуз"]
# Сортируем список, игнорируя регистр
sorted_fruits = sorted(fruits, key=str.lower)

print(sorted_fruits)