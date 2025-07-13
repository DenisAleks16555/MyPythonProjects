filename = input("Введите имя файла: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Содержимое файла:\n", content)
except FileNotFoundError:
    print("Ошибка: файл не найден. Проверьте правильность именни файла.")