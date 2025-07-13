# Название исходного файла
input_filename = 'source.txt'
# Название файла для записи статистики
output_filename = 'statistics.txt'

# Определяем гласные буквы
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'

# Инициализация счетчиков
char_count = 0
line_count = 0
vowel_count = 0
consonant_count = 0
digit_count = 0

# Открываем исходный файл для чтения
with open(input_filename, 'r', encoding='utf-8') as infile:
    # Читаем все строки
    lines = infile.readlines()
    line_count = len(lines)
    for line in lines:
        # Обновляем счетчик символов
        char_count += len(line)
        for ch in line:
            if ch.isdigit():
                digit_count += 1
            elif ch.isalpha():
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

# Записываем статистику в выходной файл
with open(output_filename, 'w', encoding='utf-8') as outfile:
    outfile.write(f'Количество строк: {line_count}\n')
    outfile.write(f'Количество символов: {char_count}\n')
    outfile.write(f'Количество гласных: {vowel_count}\n')
    outfile.write(f'Количество согласных: {consonant_count}\n')
    outfile.write(f'Количество цифр: {digit_count}\n')

print("Статистика успешно записана в файл statistics.txt")
