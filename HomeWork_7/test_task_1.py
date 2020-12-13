from HomeWork_7.hw1 import find_occurrences

import pytest


@pytest.mark.parametrize("elem_to_search", ["str", 42, True, (12, 13)])
def test_find_occurrences_hashable_element(elem_to_search):
    tree = {
        "elem_in_tree": elem_to_search,
        "elem_in_list": [elem_to_search, "bad_elem"],
        "elem_in_dict": {1: elem_to_search, 2: "bad_elem"},
        "elem_in_set": {elem_to_search, "bad_elem"},
        "elem_in_tuple": (elem_to_search, "bad_elem"),
    }

    assert find_occurrences(tree, elem_to_search) == 5


@pytest.mark.parametrize("elem_to_search", [{1, "elem"}, {1: 2, 2: True}])
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
        "elem": "first key",
        "elem_in_dict": {"elem": "second key", 2: "bad_elem"},
    }

    assert find_occurrences(tree, "elem") == 0


def test_find_occurrences_deep_nested_dict_and_lists():
    tree = {
        "dict_with_nested_4_elems": {
            "dict_2": {"dict_3": {"dict_4": {1: "elem"}, 1: "elem"}, 1: "elem"},
            1: "elem",
        },
        "list_with_nested_4_elems": [[[["not elem", "elem"], "elem"], "elem"], "elem"],
    }

    assert find_occurrences(tree, "elem") == 8
