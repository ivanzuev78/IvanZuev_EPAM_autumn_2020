"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Union

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0

    def look_into_collection(collection_to_discover: Union[list, tuple, dict, set]):
        nonlocal counter
        if isinstance(collection_to_discover, dict):
            collection_to_discover = collection_to_discover.values()

        for item in collection_to_discover:
            if item == element:
                counter += 1
            elif isinstance(item, (list, tuple, set, dict)):
                look_into_collection(item)

    look_into_collection(list(tree.values()))

    return counter


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
