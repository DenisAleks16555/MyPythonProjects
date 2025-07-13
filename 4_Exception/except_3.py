my_list = [10, 20, 30, 40, 50]
try:
    index = int(input("Введите индекс элемента (от 0 до 4): "))
    print(f"Элемент списка: {my_list[index]}")
except IndexError:
    print("Ошибка: индекс выходит за границы списка.")
except ValueError:
    print("Ошибка: введено не число.")