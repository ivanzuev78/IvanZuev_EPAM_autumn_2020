import pytest

from HomeWork_7.hw1 import find_occurrences


@pytest.mark.parametrize("elem_to_search", ("str", 42, True, (12, 13)))
def test_find_occurrences_hashable_element(elem_to_search):
    tree = {
        "elem_in_tree": elem_to_search,
        "elem_in_list": [elem_to_search, "bad_elem"],
        "elem_in_dict": {1: elem_to_search, 2: "bad_elem"},
        "elem_in_set": {elem_to_search, "bad_elem"},
        "elem_in_tuple": (elem_to_search, "bad_elem"),
    }

    assert find_occurrences(tree, elem_to_search) == 5


@pytest.mark.parametrize("elem_to_search", ({1, "elem"}, {1: 2, 2: True}))
def test_find_occurrences_unhashable_element(elem_to_search):

    tree = {
        "elem_in_tree": elem_to_search,
        "elem_in_list": [elem_to_search, "bad_elem"],
        "elem_in_dict": {1: elem_to_search, 2: "bad_elem"},
        "elem_in_tuple": (elem_to_search, "bad_elem"),
    }

    assert find_occurrences(tree, elem_to_search) == 4


def test_find_occurrences_element_in_key():

    tree = {
        "elem": "elem",
        "elem_in_dict": {"elem": "elem", 2: "bad_elem"},
    }

    assert find_occurrences(tree, "elem") == 2
