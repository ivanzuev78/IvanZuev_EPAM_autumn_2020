"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string

a b c d e f g h i j k l m n o p q r s t u v w x y z

assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import List


def custom_range(*args) -> List[str]:

    sequence, *params = args
    step = 1
    first_elem = 0
    if isinstance(args[-1], int):
        *params, step = params

    if len(params) == 1:
        last_elem = sequence.index(params[0])
    elif len(params) == 2:
        last_elem = sequence.index(params[1])
        first_elem = sequence.index(params[0])
    elif len(params) == 0:
        raise TypeError(
            f"custom_range() needs at least 1 argument, that contains in the sequence"
        )

    else:
        raise TypeError(
            f"custom_range() takes 2 to 4 arguments but {len(args)} were given"
        )

    return [i for i in sequence[first_elem:last_elem:step]]
