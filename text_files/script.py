# Название исходного файла
input_filename = 'C:/Users/0/OneDrive/Рабочий стол/text_files/source.txt'
# Название файла, куда запишем результат
output_filename = 'C:/Users/0/OneDrive/Рабочий стол/text_files/result.txt'

# Открываем исходный файл для чтения
with open(input_filename, 'r', encoding='utf-8') as infile:
    # Читаем все строки файла в список
    lines = infile.readlines()

print("Чтение строк из файла:", input_filename)
print("Количество строк перед удалением:", len(lines))

# Удаляем последнюю строку
if lines:
    lines.pop()

print("Количество строк после удаления:", len(lines))

# Записываем оставшиеся строки в новый файл
with open(output_filename, 'w', encoding='utf-8') as outfile:
    outfile.writelines(lines)

