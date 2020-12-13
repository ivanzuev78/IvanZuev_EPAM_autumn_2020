import os
import shutil

from HomeWork_9.hw3 import universal_file_counter

import pytest


@pytest.fixture()
def path_to_files():
    base_dir = os.getcwd()
    os.mkdir("test_dir")
    os.chdir(base_dir + "/test_dir")
    with open("test_file_1.txt", "w") as f:
        f.write("one_word_two_lines\n" * 2)
    with open("test_file_2.txt", "w") as f:
        f.write("two_words two_lines\n" * 2)
    yield os.getcwd()
    os.chdir(base_dir)
    shutil.rmtree(base_dir + "/test_dir")


def test_universal_file_counter_without_tokenizer(path_to_files):
    assert universal_file_counter(path_to_files, ".txt") == 4


def test_universal_file_counter_with_tokenizer(path_to_files):
    assert universal_file_counter(path_to_files, ".txt", tokenizer=str.split) == 6
