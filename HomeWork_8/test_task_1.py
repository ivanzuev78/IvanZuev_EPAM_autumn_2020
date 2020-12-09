import os

from HomeWork_8.task1 import KeyValueStorage

import pytest


@pytest.fixture()
def filename():
    filename = "test_task_1.txt"
    with open(filename, "w"):
        pass
    yield filename
    os.remove(filename)


def fill_the_file(dict_to_write, filename):
    with open(filename, "a") as file:
        for key, value in dict_to_write.items():
            file.write(f"{key}={value}\n")


def test_key_value_storage(filename):
    dict_to_test = {"name": "kek", "power": 9001}
    fill_the_file(dict_to_test, filename)
    storage = KeyValueStorage(filename)
    for key in dict_to_test:
        assert storage[key] == dict_to_test[key]


def test_key_value_storage_numb_in_key_raises_error(filename):
    dict_to_test = {9001: 9001}
    fill_the_file(dict_to_test, filename)
    with pytest.raises(ValueError, match="Key is digit"):
        KeyValueStorage(filename)


def test_key_value_storage_build_in_attributes_take_precedence(filename):
    dict_to_test = {"copy": "it is not copy!"}
    fill_the_file(dict_to_test, filename)
    storage = KeyValueStorage(filename)
    assert storage["copy"] == "it is not copy!"
    assert storage.copy != storage["copy"]
