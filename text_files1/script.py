# Имя файла с текстом
filename = 'source.txt'

# Открываем файл для чтения
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()  # читаем все строки в список

# Находим длину самой длинной строки
max_length = max(len(line.rstrip('\n')) for line in lines)

# Выводим результат
print("Длина самой длинной строки:", max_length)