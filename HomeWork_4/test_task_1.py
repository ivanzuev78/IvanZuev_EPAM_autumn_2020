import os

import pytest

from HomeWork_4.task_1_read_file import read_magic_number


@pytest.fixture
def input_int_1_true():
    with open("data.txt", "w") as file:
        file.write("1")

    yield

    os.remove("data.txt")


@pytest.fixture
def input_int_3_false():
    with open("data.txt", "w") as file:
        file.write("3")

    yield

    os.remove("data.txt")


@pytest.fixture
def input_float_2dot718281_true():
    with open("data.txt", "w") as file:
        file.write("2.718281")

    yield

    os.remove("data.txt")


@pytest.fixture
def input_text_exception():
    with open("data.txt", "w") as file:
        file.write("it is not a number")

    yield

    os.remove("data.txt")


@pytest.fixture
def input_int_out_of_range():
    with open("data.txt", "w") as file:
        file.write("42")

    yield

    os.remove("data.txt")


def test_read_magic_number_input_int_numb_1(input_int_1_true):

    assert read_magic_number("data.txt") is True


def test_read_magic_number_input_int_numb_3(input_int_3_false):

    assert read_magic_number("data.txt") is False


def test_read_magic_number_input_float_2dot718281(input_float_2dot718281_true):

    assert read_magic_number("data.txt") is True


def test_read_magic_number_input_out_of_range(input_int_out_of_range):

    assert read_magic_number("data.txt") is False


def test_read_magic_number_input_text(input_text_exception):

    with pytest.raises(ValueError):
        read_magic_number("data.txt")
