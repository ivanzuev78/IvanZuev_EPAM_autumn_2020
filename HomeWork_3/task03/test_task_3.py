import pytest

from HomeWork_3.task03.task03 import make_filter, Filter


def test_filter():

    assert Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    ).apply([-4, -3, 0, 1, 2, 3, 4]) == [2, 4]


def test_specified_filter_example():

    input_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    assert make_filter(name="polly", type="bird").apply(input_data) == [input_data[1]]


def test_specified_filter_no_one_in_input_are_good():
    input_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "name": "Bill",
            "last_name": "Paper",
        },
        {"name": "Bill", "last_name": "Wodoomagic", "type": "person"},
    ]

    assert make_filter(name="Bill", type="bird").apply(input_data) == []


def test_specified_filter_all_in_input_are_good():

    input_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "name": "Bill",
            "last_name": "Paper",
        },
        {"name": "Bill", "last_name": "Wodoomagic", "type": "person"},
    ]

    assert make_filter(name="Bill").apply(input_data) == input_data


def test_specified_filter_empty_input():

    assert make_filter(filter_param="Sorry, but it is empty...").apply([]) == []


def test_specified_filter_returns_part_of_the_input():

    input_data = [
        {
            "name": "Frodo Baggins",
            "race": "hobbit",
        },
        {
            "name": "Bilbo Baggins",
            "race": "hobbit",
        },
        {
            "name": "Aragorn",
            "race": "man",
        },
        {
            "name": "Legolas",
            "race": "elf",
        },
        {
            "name": "Gimli",
            "race": "Dwarf",
        },
    ]

    assert make_filter(race="hobbit").apply(input_data) == input_data[:2]
