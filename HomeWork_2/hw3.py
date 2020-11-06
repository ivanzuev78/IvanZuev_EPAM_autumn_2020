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
from typing import List, Any, Tuple


def combinations(*args: List[Any]) -> List[List]:

    list_to_return = []

    if not isinstance(args[0], (list, Tuple)):
        for i in args:
            list_to_return.append([i])
        print(list_to_return)
        return list_to_return
    new_args = list(args).pop(-1)
    # print(args)
    print('new_args', new_args)
    for i in args[0]:
        print(i)
        for end_of_array in combinations(k for k in args[1:]):
            list_to_return.append([i] + end_of_array)

    return list_to_return


if __name__ == '__main__':
    print(combinations([1, 2], [3, 4]))