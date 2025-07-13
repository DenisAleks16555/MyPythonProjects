input_expression = input("Введите арифметическое выражение (например, 23+12): ") 

# Использование eval() для вычисления выражения и вывод результата 
try: 
    result = eval(input_expression) 
    print("Результат:", result) 
except Exception as e: 
    print("Ошибка в выражении:", e) 