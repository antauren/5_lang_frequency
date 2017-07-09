import sys
import os.path
import re
from collections import Counter


def print_help():
    print(
        'Для того чтоб узнать как работает программа введите: python lang_frequency.py --help или python3 lang_frequency.py --help')


def get_filepath(argv_list):
    if len(argv_list) < 2:
        print('Вас привествует программа подсчета слов в тексте\n')
        print_help()
        return None

    if argv_list[1] == '--help':
        print('\nЧтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <текстовый файл>\n'
              'Наример: python3 lang_frequency.py war_and_peace.txt\n')
        return None

    filepath = argv_list[1]

    if not os.path.exists(filepath):
        print('Ошибка: программа не может найти текстовый файл\n')
        print_help()
        return None
    else:
        return filepath


def load_data(filepath):
    with open(filepath, 'r', encoding='windows-1251') as file:
        return file.read()


def get_most_frequent_words(text):
    pattern = r'[а-я]|[a-z]+'
    words = re.findall(pattern, text.lower())
    return Counter(words)


def word_count(most_frequent_words, quantity=10):
    return most_frequent_words.most_common(quantity)


def output():
    argv_list = sys.argv
    filepath = get_filepath(argv_list)

    if filepath is None:
        return None

    text = load_data(filepath)
    most_frequent_words = get_most_frequent_words(text)
    records = word_count(most_frequent_words)

    print('\nслово и количество его упоминаний:\n')
    for record in records:
        word, count_of_word = record
        print(word, count_of_word)


if __name__ == '__main__':
    output()
