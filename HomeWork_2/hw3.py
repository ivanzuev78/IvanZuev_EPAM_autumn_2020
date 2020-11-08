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
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:

    list_to_return = []

    if len(args) == 1:
        for i in args[0]:
            list_to_return.append([i])

    else:
        for i in args[0]:
            for tail in combinations(*args[1:]):
                list_to_return.append([i] + tail)

    return list_to_return
