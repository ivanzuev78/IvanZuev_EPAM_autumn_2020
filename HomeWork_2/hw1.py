"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import json
import string
from typing import List


def unicode_char_replacer(char: str) -> str:

    with open("dict_unicode_char_replacer.txt", "r") as f:
        text_dict = json.load(f)

    return text_dict[char]


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
    pass_unicode_extra_letters = 0
    with open(file_path, "r") as file:

        for line in file:
            for index, letter in enumerate(line):

                if pass_unicode_extra_letters:
                    pass_unicode_extra_letters -= 1
                    continue

                elif letter == "\\":
                    letter = unicode_char_replacer(line[index + 2: index + 6])
                    pass_unicode_extra_letters += 5
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
                        parsed_text.append(word)
                        word = []

    if output == "WORDS":
        return parsed_text
    elif output == "SYMBOLS":
        return symbols


def read_words(file_path: str) -> List[List[str]]:
    return reader(file_path, output="WORDS")


def read_letters(file_path: str) -> List[str]:
    return reader(file_path, output="SYMBOLS")


# --------------------- tasks funcs ---------------------------
def get_longest_diverse_words(file_path: str) -> List[str]:

    return [
        "".join(letter for letter in word)
        for word in sorted(
            list(read_words(file_path)),
            key=lambda word: len(set(word)),
            reverse=True,
        )[:10]
    ]


def get_rarest_char(file_path: str) -> str:

    counter = {}

    rarest_char = None

    for i in read_letters(file_path):
        if i not in counter:
            counter[i] = 0
        counter[i] += 1

    for i in counter:
        if rarest_char is None:
            rarest_char = i
        elif counter[i] < counter[rarest_char]:
            rarest_char = i

    return rarest_char


def count_punctuation_chars(file_path: str) -> int:

    return sum(1 for i in read_letters(file_path) if i in string.punctuation)


def count_non_ascii_chars(file_path: str) -> int:

    return sum(1 for i in reader(file_path, output="SYMBOLS") if not i.isascii())


def get_most_common_non_ascii_char(file_path: str) -> str:

    counter = {}
    most_common = None

    for i in reader(file_path, output="SYMBOLS"):

        if not i.isascii():
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
            if most_common is None:
                most_common = i
            elif counter[i] > counter[most_common]:
                most_common = i

    return most_common
