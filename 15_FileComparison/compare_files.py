# Открываем оба файла
with open('file1.txt', 'r', encoding='utf-8') as f1, open('file2.txt', 'r', encoding='utf-8') as f2:
    # Читаем строки из каждого файла
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# Находим минимальную длину
min_length = min(len(lines1), len(lines2))

# Перебираем строки и сравниваем
for i in range(min_length):
    if lines1[i] != lines2[i]:
        print(f"Несовпадающая строка из файла 1: {lines1[i].strip()}")
        print(f"Несовпадающая строка из файла 2: {lines2[i].strip()}")
        break
else:
    # Если все строки совпадают до минимальной длины
    if len(lines1) != len(lines2):
        # Выводим оставшиеся строки, если есть
        if len(lines1) > len(lines2):
            print(f"Дополнительная строка в файле 1: {lines1[min_length].strip()}")
        else:
            print(f"Дополнительная строка в файле 2: {lines2[min_length].strip()}")