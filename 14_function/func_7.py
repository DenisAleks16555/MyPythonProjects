def is_palindrome(number):
    # Преобразуем число в строку
    number_str = str(number)
    
    # Сравниваем строку с её обратной версией
    if number_str == number_str[::-1]:
        return True  # Это палиндром
    else:
        return False  # Это не палиндром

# Примеры вызова функции
result1 = is_palindrome(12321)   # Ожидаемый вывод: True
result2 = is_palindrome(546645)   # Ожидаемый вывод: True
result3 = is_palindrome(421987)   # Ожидаемый вывод: False

print("12321 является палиндромом:", result1)
print("546645 является палиндромом:", result2)
print("421987 не является палиндромом:", result3)