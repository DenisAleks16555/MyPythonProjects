# count_words.py

def load_text(file_path):
    """Читает текст из файла и возвращает строку."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def clean_and_split(text):
    """Удаляет знаки препинания, переводит в нижний регистр и разбивает на слова."""
    punctuation = ".,!?-—:;\"'()[]{}"
    for symbol in punctuation:
        text = text.replace(symbol, '')
    text = text.lower()
    words = text.split()
    return words

def count_words(words):
    """Подсчитывает количество каждого слова в списке."""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def main():
    file_path = 'data/input.txt'  # путь к файлу с текстом
    text = load_text(file_path)
    words = clean_and_split(text)
    counts = count_words(words)

    # Выводим результат
    for word, count in sorted(counts.items()):
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()

