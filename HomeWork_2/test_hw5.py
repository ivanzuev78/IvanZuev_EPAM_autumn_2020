import string

from HomeWork_2.hw5 import custom_range


def test_custom_range_example_1():

    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_custom_range_example_2():

    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_custom_range_example_3():

    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_custom_range_numbs():

    assert custom_range(range(10), 1, 3, 1) == [1, 2]
