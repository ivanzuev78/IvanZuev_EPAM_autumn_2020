import os

import pytest

from HomeWork_4.task_1_read_file import read_magic_number


@pytest.fixture
def input_int_1():
    with open("data.txt", "w") as file:
        file.write("1")

    yield

    os.remove("data.txt")


@pytest.fixture
def input_int_3():
    with open("data.txt", "w") as file:
        file.write("3")

    yield

    os.remove("data.txt")


@pytest.fixture
def input_float_2dot718281():
    with open("data.txt", "w") as file:
        file.write("2.718281")

    yield

    os.remove("data.txt")


@pytest.fixture
def input_text():
    with open("data.txt", "w") as file:
        file.write("it is not a number")

    yield

    os.remove("data.txt")


def test_read_magic_number_input_int_numb_1(input_int_1):

    assert read_magic_number("data.txt") is True


def test_read_magic_number_input_int_numb_3(input_int_3):

    assert read_magic_number("data.txt") is False


def test_read_magic_number_input_float_2dot718281(input_float_2dot718281):

    assert read_magic_number("data.txt") is True


def test_read_magic_number_input_text(input_text):

    with pytest.raises(ValueError) as ex:
        read_magic_number("data.txt")
