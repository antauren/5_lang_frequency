import sys
import os.path
import re
from collections import Counter


def handling_args(argv_list):
    if len(argv_list) < 2:
        print('Вас привествует программа подсчета слов в тексте\n'
              'Для того чтоб узнать как работает программа введите: '
              'python lang_frequency.py --help или python3 lang_frequency.py --help')
        return None

    arg = argv_list[1]

    if arg == '--help':
        return print_help()

    if not os.path.exists(arg):
        print('Ошибка: программа не может найти текстовый файл\n')
        return None
    filepath = arg

    data = load_data(filepath)
    most_frequent_words = get_most_frequent_words(data)
    records = word_count(most_frequent_words, quantity=10)
    output_most_frequent_words(records)


def print_help():
    print(
        '\nЧтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <текстовый файл>\n'
        'Наример: python3 lang_frequency.py war_and_peace.txt\n')


def load_data(filepath):
    with open(filepath, 'r', encoding='windows-1251') as file:
        return file.read()


def get_most_frequent_words(data):
    pattern = r'[а-я]|[a-z]+'
    words = re.findall(pattern, data.lower())
    return Counter(words)


def word_count(most_frequent_words, quantity=10):
    return most_frequent_words.most_common(quantity)


def output_most_frequent_words(records):
    print('\nслово и количество его упоминаний:\n')
    for record in records:
        word, count_of_word = record
        print(word, count_of_word)


if __name__ == '__main__':
    argv_list = sys.argv
    handling_args(argv_list)