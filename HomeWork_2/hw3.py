"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import unittest
from typing import List, Any, Tuple


def combinations(*args: List[Any]) -> List[List]:

    list_to_return = []

    for i in args[0]:
        if len(args) == 1:
            list_to_return.append([i])

        else:
            for end_of_array in combinations(*args[1:]):
                list_to_return.append([i] + end_of_array)

    return list_to_return
