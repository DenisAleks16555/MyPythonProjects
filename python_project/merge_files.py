try:
    with open('file1.txt', 'r', encoding='utf-8') as f1, \
         open('file2.txt', 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
except FileNotFoundError:
    print("Один из файлов не найден.")
    exit()

# Создаем новый файл для записи
with open('merged.txt', 'w', encoding='utf-8') as outfile:
    # Определяем минимальную длину
    min_len = min(len(lines1), len(lines2))
    # Чередуем строки
    for i in range(min_len):
        outfile.write(lines1[i])
        outfile.write(lines2[i])
    # Если остались строки в первом файле
    for i in range(min_len, len(lines1)):
        outfile.write(lines1[i])
    # Если остались строки во втором файле
    for i in range(min_len, len(lines2)):
        outfile.write(lines2[i])