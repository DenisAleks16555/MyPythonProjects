num = ["8-912-123-45-67", "+79162345678", "abc", "4951234567", "  +7 999 123-45-67 "]

filtered_numbers = []

for number in num:
    # Удаляем все нецифровые символы
    cleaned_number = ''.join(filter(str.isdigit, number))
    
    # Проверяем, есть ли ровно 11 цифр
    if len(cleaned_number) == 11:
        filtered_numbers.append(cleaned_number)

formatted_numbers = []

for number in filtered_numbers:
    # Преобразуем номер в нужный формат
    formatted_number = f"+7 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:11]}"
    formatted_numbers.append(formatted_number)

print(formatted_numbers)