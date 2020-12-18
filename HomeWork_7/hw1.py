"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Union


def find_occurrences(tree: dict, element: Any) -> int:
    def look_into_collection(collection_to_check: Union[list, tuple, dict, set]) -> int:
        counter = 0
        if isinstance(collection_to_check, dict):
            collection_to_check = collection_to_check.values()

        for item in collection_to_check:
            if item == element:
                counter += 1
            elif isinstance(item, (list, tuple, set, dict)):
                counter += look_into_collection(item)
        return counter

    return look_into_collection(list(tree.values()))
