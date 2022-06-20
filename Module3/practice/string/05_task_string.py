# Вам дана строка, состоящая из строчных латинских букв и пробелов.
# Ваша задача — определить, является ли эта строка «перевертышем», если удалить из нее все пробелы и знаки пуктуации.
# Строка называется «перевертышем», если читается одинаково слева направо и справа налево.

# Пример строки перевертыша: "И темен город. Мороз узором дорог не мети."

text = input('Введите строку: ')
spaces_and_punctuation_free_text = text.replace(' ', '').replace(',', '').replace('.', '').lower()
j = -1
counter = 0
for i in range(len(spaces_and_punctuation_free_text)):
    if spaces_and_punctuation_free_text[i] == spaces_and_punctuation_free_text[j]:
        counter += 1
    j -= 1
if counter == len(spaces_and_punctuation_free_text):
    print('перевертыш')
else:
    print('не перевертыш')

