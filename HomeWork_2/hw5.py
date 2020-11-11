"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import List, Sequence, Any


def custom_range(sequence: Sequence, *args) -> List[Any]:

    step = 1
    first_elem = 0

    if len(args) == 0:
        return [i for i in sequence]

    if len(args) == 1:
        last_elem = sequence.index(args[0])
    elif len(args) == 2:
        last_elem = sequence.index(args[1])
        first_elem = sequence.index(args[0])
    elif len(args) == 3:
        if not isinstance(args[2], int):
            raise TypeError("Step must be integer!")
        last_elem = sequence.index(args[1])
        first_elem = sequence.index(args[0])
        step = args[2]
    elif len(args) > 3:
        raise IndexError("Too many arguments")

    return [i for i in sequence[first_elem:last_elem:step]]
