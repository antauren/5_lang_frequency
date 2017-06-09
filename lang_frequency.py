import sys
import os.path
import re
import operator


def load_data(filepath):
    f = open(filepath, 'r', encoding='windows-1251')
    return f
    f.close()


def get_10_most_frequent_words(text):
    dict_word_frequency = {}
    pattern = r'[а-я]|[a-z]+'

    for line in text:
        words = re.findall(pattern, line, re.IGNORECASE)
        for word in words:
            word = word.lower()
            if word in dict_word_frequency:
                dict_word_frequency[word] += 1
            else:
                dict_word_frequency[word] = 1

    sorted_dict = sorted(dict_word_frequency.items(), key=operator.itemgetter(1), reverse=True)

    counter = 0
    print('\nслово и количество его упоминаний:\n')
    for record in sorted_dict:
        word = record[0]
        count_of_word = record[1]

        print(word, count_of_word)
        counter += 1
        if counter >= 10:
            break


def start_script(argv_list):
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
    get_10_most_frequent_words(text)


if __name__ == '__main__':
    argv_list = sys.argv
    start_script(argv_list)