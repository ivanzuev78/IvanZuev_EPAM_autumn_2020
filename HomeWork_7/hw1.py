"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Union


def find_occurrences(tree: dict, element: Any) -> int:
    def look_into_collection(collection_to_discover: Union[list, tuple, dict, set]):
        counter = 0
        if isinstance(collection_to_discover, dict):
            collection_to_discover = collection_to_discover.values()

        for item in collection_to_discover:
            if item == element:
                counter += 1
            elif isinstance(item, (list, tuple, set, dict)):
                counter += look_into_collection(item)
        return counter

    return look_into_collection(list(tree.values()))
