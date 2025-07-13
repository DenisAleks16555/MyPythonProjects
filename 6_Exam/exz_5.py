def last_word(sentence):
    words = sentence.split()  # Разделяем строку на слова
    return words[-1] if words else''
input_string = "Python is fun!"
output = last_word(input_string)
print(output)