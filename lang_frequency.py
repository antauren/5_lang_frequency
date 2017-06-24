import sys
import os.path
import re
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r', encoding='windows-1251') as file:
        return file.read()


def get_most_frequent_words(text):
    pattern = r'[а-я]|[a-z]+'
    words = re.findall(pattern, text.lower())

    return Counter(words)


def start_script(argv_list, quantity=10):
    if len(argv_list) < 2:
        print('Вас привествует программа подсчета слов в тексте\n'
              'Для того чтоб узнать как работает программа введите: python lang_frequency.py --help или python3 lang_frequency.py --help')
        return None

    if argv_list[1] == '--help':
        print('\nЧтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <текстовый файл>\n'
              'Наример: python3 lang_frequency.py war_and_peace.txt\n')
        return None

    filepath = argv_list[1]

    if not os.path.exists(filepath):
        print('Ошибка: программа не может найти текстовый файл\n'
              'Воспользуйтесь помощью (--help)')
        return None

    text = load_data(filepath)
    most_frequent_words = get_most_frequent_words(text)

    print('\nслово и количество его упоминаний:\n')
    for record in most_frequent_words.most_common(quantity):
        word = record[0]
        count_of_word = record[1]

        print(word, count_of_word)


if __name__ == '__main__':
    argv_list = sys.argv
    start_script(argv_list)
