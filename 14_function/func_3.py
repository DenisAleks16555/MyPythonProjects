def draw_square(side_length, symbol, filled):
    if side_length <= 0:
        print("Длина стороны должна быть положительным числом.")
        return
    
    for i in range(side_length):
        if filled:
            print(symbol * side_length)
        else:
            if i == 0 or i == side_length - 1:
                print(symbol * side_length)
            else:
                print(symbol + ' ' * (side_length - 2) + symbol)

# Примеры вызова функции
draw_square(5, '*', True)  # Заполненный квадрат
print()  # Пустая строка для разделения
draw_square(5, '*', False)  # Пустой квадрат