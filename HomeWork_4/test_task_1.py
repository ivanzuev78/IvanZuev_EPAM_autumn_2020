import os

import pytest

from HomeWork_4.task_1_read_file import read_magic_number


@pytest.fixture
def input_int_1_true():
    name_of_file = "data.txt"
    with open(name_of_file, "w") as file:
        file.write("1")
    yield name_of_file
    os.remove(name_of_file)


@pytest.fixture
def input_int_3_false():
    name_of_file = "data.txt"
    with open(name_of_file, "w") as file:
        file.write("3")
    yield name_of_file
    os.remove(name_of_file)


@pytest.fixture
def input_float_2dot718281_true():
    name_of_file = "data.txt"
    with open(name_of_file, "w") as file:
        file.write("2.718281")
    yield name_of_file
    os.remove(name_of_file)


@pytest.fixture
def input_text_exception():
    name_of_file = "data.txt"
    with open(name_of_file, "w") as file:
        file.write("it is not a number")
    yield name_of_file
    os.remove(name_of_file)


@pytest.fixture
def input_int_out_of_range():
    name_of_file = "data.txt"
    with open(name_of_file, "w") as file:
        file.write("42")
    yield name_of_file
    os.remove(name_of_file)


@pytest.fixture
def content_creator():
    name_of_file = "data_from_content_creator.txt"

    def wrapper(text):
        with open(name_of_file, "w") as file:
            file.write(text)
        return name_of_file

    yield wrapper
    os.remove(name_of_file)


def test_read_magic_number_input_int_numb_1(input_int_1_true):
    assert read_magic_number(input_int_1_true) is True


def test_read_magic_number_input_int_numb_3(input_int_3_false):
    assert read_magic_number(input_int_3_false) is False


def test_read_magic_number_input_float_2dot718281(input_float_2dot718281_true):
    with pytest.raises(ValueError, match="First line must be integer!"):
        read_magic_number(input_float_2dot718281_true)


def test_read_magic_number_input_out_of_range(input_int_out_of_range):
    assert read_magic_number(input_int_out_of_range) is False


def test_read_magic_number_input_text(input_text_exception):
    with pytest.raises(ValueError, match="First line must be integer!"):
        read_magic_number(input_text_exception)


def test_read_magic_number_file_doesnt_exists():
    with pytest.raises(
        ValueError, match='File "non-existing_file.txt" doesn\'t exists.'
    ):
        read_magic_number("non-existing_file.txt")


def test_read_magic_number_with_content_creator_good_input(content_creator):
    file_name = content_creator("1\nhello")
    assert read_magic_number(file_name) is True


def test_read_magic_number_with_content_creator_bad_input(content_creator):
    file_name = content_creator("World\nhello")
    with pytest.raises(ValueError, match="First line must be integer!"):
        read_magic_number(file_name)
