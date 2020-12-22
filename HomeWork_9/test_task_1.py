import os

from HomeWork_9.hw1 import merge_sorted_files

import pytest


@pytest.fixture()
def list_of_files():
    files = ["test1.txt", "test2.txt"]
    with open("test1.txt", "w") as f:
        f.write("1\n3\n5\n")
    with open("test2.txt", "w") as f:
        f.write("2\n4\n6\n")

    yield files
    for file in files:
        os.remove(file)


def test_merge_sorted_files_works(list_of_files):
    assert list(merge_sorted_files(list_of_files)) == list(range(1, 7))


def test_merge_sorted_files_is_iterator(list_of_files):
    iter_merge_sorted_files = merge_sorted_files(list_of_files)
    for i in range(1, 7):
        assert next(iter_merge_sorted_files) == i
    with pytest.raises(StopIteration):
        next(iter_merge_sorted_files)
