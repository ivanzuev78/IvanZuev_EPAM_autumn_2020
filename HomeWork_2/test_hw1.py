import os

import pytest

from HomeWork_2.hw1 import *


def create_txt_file(text: List[str], filename):

    with open(filename, "w") as file:
        for i in text:
            file.write(i + "\n")


@pytest.fixture
def fixture_create_txt_file_for_test_get_longest_diverse_words():
    text_nununique_symbols = ["x" * i for i in range(1, 11)]
    text_unique_symbols_in_10_words = [
        "".join(chr(97 + i) for i in range(k)) for k in range(2, 12)
    ]
    create_txt_file(
        text_nununique_symbols + text_unique_symbols_in_10_words, "test_text.txt"
    )
    yield None
    os.remove("test_text.txt")


def test_get_longest_diverse_words(
    fixture_create_txt_file_for_test_get_longest_diverse_words,
):
    text_unique_symbols_in_10_words = [
        "".join(chr(97 + i) for i in range(k)) for k in range(2, 12)
    ]

    assert set(get_longest_diverse_words("test_text.txt")) == set(
        text_unique_symbols_in_10_words
    )


@pytest.fixture
def fixture_create_txt_file_for_test_get_rarest_char():
    text = ["asd asd qwe\nr qwe r p \n"]
    create_txt_file(text, "test_text.txt")
    yield None
    os.remove("test_text.txt")


def test_get_rarest_char(fixture_create_txt_file_for_test_get_rarest_char):
    assert get_rarest_char("test_text.txt") == "p"


@pytest.fixture
def fixture_create_txt_file_for_test_count_punctuation_chars():
    text = ["I. believe: i, can fly!!!"]
    create_txt_file(text, "test_text.txt")
    yield None
    os.remove("test_text.txt")


def test_count_punctuation_chars(
    fixture_create_txt_file_for_test_count_punctuation_chars,
):
    assert count_punctuation_chars("test_text.txt") == 6


@pytest.fixture
def fixture_create_txt_file_for_test_count_non_ascii_chars():
    text = ["\\u00bbJetzt und фыва hier\\u00ab \\u00bb"]
    create_txt_file(text, "test_text.txt")
    yield None
    os.remove("test_text.txt")


def test_count_non_ascii_chars(fixture_create_txt_file_for_test_count_non_ascii_chars):
    assert count_non_ascii_chars("test_text.txt") == 7


@pytest.fixture
def fixture_create_txt_file_for_test_get_most_common_non_ascii_char():

    text = ["\\u00bbJetzt und ввввв \\u00ab \\u00bb"]
    text_2 = ["\\u00bbJetzt und  \\u00ab \\u00bb"]

    create_txt_file(text, "test_text.txt")
    create_txt_file(text_2, "test_text_2.txt")

    yield None

    os.remove("test_text.txt")
    os.remove("test_text_2.txt")


def test_get_most_common_non_ascii_char(
    fixture_create_txt_file_for_test_get_most_common_non_ascii_char,
):

    assert get_most_common_non_ascii_char("test_text.txt") == "в"
    assert get_most_common_non_ascii_char("test_text_2.txt") == "\\u00bb"


@pytest.fixture
def fixture_create_txt_file_for_test_word_wrapping():
    text = ["first, second, third"]
    text_2 = ["first, seco-nd, thir-d"]
    text_3 = ["first, seco-\n" "nd, thir-\n" "d"]

    create_txt_file(text, "test_text.txt")
    create_txt_file(text_2, "test_text_2.txt")
    create_txt_file(text_3, "test_text_3.txt")

    yield None

    os.remove("test_text.txt")
    os.remove("test_text_2.txt")
    os.remove("test_text_3.txt")


def test_word_wrapping(fixture_create_txt_file_for_test_word_wrapping):

    assert len(read_words("test_text.txt")) == 3
    assert len(read_words("test_text_2.txt")) == 5
    assert len(read_words("test_text_3.txt")) == 3
