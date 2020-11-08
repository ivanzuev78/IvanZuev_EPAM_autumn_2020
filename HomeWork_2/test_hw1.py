import os
from HomeWork_2.hw1 import *


def create_txt_file(text: List[str], filename):

    with open(filename, "w") as file:
        for i in text:
            file.write(i + "\n")


def test_get_longest_diverse_words():

    text_nununique_symbols = ["x" * i for i in range(1, 11)]

    # Генерирую такой большой массив, потому что надо минимум 10 слов с уникальными символами
    text_unique_symbols = ["".join(chr(97 + i) for i in range(k)) for k in range(2, 12)]

    create_txt_file(text_nununique_symbols + text_unique_symbols, "test_text.txt")

    assert set(get_longest_diverse_words("test_text.txt")) == set(text_unique_symbols)


def test_get_rarest_char():

    text = ["asd asd qwe-\nr qwe r p \n"]

    create_txt_file(text, "test_text.txt")

    assert get_rarest_char("test_text.txt") == "p"

    os.remove("test_text.txt")


def test_count_punctuation_chars():

    text = ["I. believe: i, can fly!!!"]

    create_txt_file(text, "test_text.txt")

    assert count_punctuation_chars("test_text.txt") == 6

    os.remove("test_text.txt")


def test_count_non_ascii_chars():
    text = ["\\u00bbJetzt und фыва hier\\u00ab \\u00bb"]

    create_txt_file(text, "test_text.txt")

    assert count_non_ascii_chars("test_text.txt") == 7

    os.remove("test_text.txt")


def test_get_most_common_non_ascii_char():

    text = ["\\u00bbJetzt und ввввв \\u00ab \\u00bb"]
    text_2 = ["\\u00bbJetzt und  \\u00ab \\u00bb"]

    create_txt_file(text, "test_text.txt")
    create_txt_file(text_2, "test_text_2.txt")

    assert get_most_common_non_ascii_char("test_text.txt") == "в"
    assert get_most_common_non_ascii_char("test_text_2.txt") == "\\u00bb"

    os.remove("test_text.txt")
    os.remove("test_text_2.txt")
