# replace_word.py
def main():
    # Путь к файлу с текстом
    file_path = 'input.txt'

    # Спросим у пользователя, что искать и на что заменять
    word_to_find = input("Введите слово, которое нужно заменить: ")
    word_to_replace = input("Введите слово, на которое заменить: ")

    # Читаем содержимое файла
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Заменяем все вхождения слова
    new_text = text.replace(word_to_find, word_to_replace)

    # Записываем изменённый текст обратно в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_text)

    print("Замена выполнена успешно!")

if __name__ == '__main__':
    main()

