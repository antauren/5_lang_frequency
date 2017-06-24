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

def output(most_frequent_words, quantity=10):
    print('\nслово и количество его упоминаний:\n')
    for record in most_frequent_words.most_common(quantity):
        word, count_of_word = record
        print(word, count_of_word)

def get_filepath(argv_list):
    if len(argv_list) < 2:
        print('Вас привествует программа подсчета слов в тексте\n')
        return None

    if argv_list[1] == '--help':
        print('\nЧтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <текстовый файл>\n'
              'Наример: python3 lang_frequency.py war_and_peace.txt\n')
        return None

    filepath = argv_list[1]

    if not os.path.exists(filepath):
        print('Ошибка: программа не может найти текстовый файл\n')
        return None
    else:
        return filepath


if __name__ == '__main__':
    argv_list = sys.argv
    filepath = get_filepath(argv_list)
    try:
        text = load_data(filepath)
        most_frequent_words = get_most_frequent_words(text)
        output(most_frequent_words)    
    except TypeError:
        print('Для того чтоб узнать как работает программа введите: python lang_frequency.py --help или python3 lang_frequency.py --help')