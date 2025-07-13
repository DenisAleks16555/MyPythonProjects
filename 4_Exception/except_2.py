try:
    num = int(input("Введите целое число: "))
    print(f"Квадрат числа: {num ** 2}")
except ValueError:
    print("Ошибка: введено не целое число.")