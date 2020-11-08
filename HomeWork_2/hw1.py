"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter
from typing import List


def reader(file_path: str, output: str) -> List:
    """
    output: ['WORDS', 'SYMBOLS']
    :param file_path:
    :param output:
    :return:
    """
    word = []
    parsed_text = []
    symbols = []
    skip_unicode_letter = 0
    with open(file_path, "r") as file:

        for line in file:
            for index, letter in enumerate(line):

                if skip_unicode_letter:
                    skip_unicode_letter -= 1
                    continue

                elif letter == "\\":
                    letter = line[index : index + 6]
                    skip_unicode_letter += 5
                    word.append(letter)
                    symbols.append(letter)

                elif letter.isalpha():
                    word.append(letter)
                    symbols.append(letter)

                else:
                    symbols.append(letter)
                    if letter == "-" and line[index + 1] == "\n":
                        break

                    elif word:
                        parsed_text.append(tuple(word))
                        word = []
    print(symbols)
    if output == "WORDS":
        return parsed_text
    elif output == "SYMBOLS":
        return symbols


def read_words(file_path: str) -> List[List[str]]:
    return reader(file_path, output="WORDS")


def read_letters(file_path: str) -> List[str]:
    return reader(file_path, output="SYMBOLS")


def is_ascii(letter: str) -> bool:
    return False if len(letter) > 1 or not letter.isascii() else True


# --------------------- tasks funcs ---------------------------
def get_longest_diverse_words(file_path: str) -> List[str]:
    text = list(set(read_words(file_path)))

    text.sort(key=lambda word: len(set(word)), reverse=True)

    list_to_return = []

    for word in text[:10]:
        word_to_add = ""
        for letter in word:
            word_to_add += letter
        list_to_return.append(word_to_add)

    return list_to_return


def get_rarest_char(file_path: str) -> str:

    symbols = read_letters(file_path)

    counter = Counter()

    for i in symbols:
        counter[i] += 1

    return counter.most_common()[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    symbols = read_letters(file_path)

    counter = 0

    for i in symbols:
        if i in string.punctuation:
            counter += 1

    return counter


def count_non_ascii_chars(file_path: str) -> int:
    symbols = reader(file_path, output="SYMBOLS")

    counter = 0

    for i in symbols:
        if not is_ascii(i):
            counter += 1

    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    symbols = reader(file_path, output="SYMBOLS")

    counter = Counter()

    for i in symbols:
        if not is_ascii(i):
            counter[i] += 1

    return counter.most_common()[0][0]
