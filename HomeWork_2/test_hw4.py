import time
from typing import List

from HomeWork_2.hw4 import cache


def func(a, b, *args, **kwargs):
    c, d = 1, 1
    for _ in args:
        c += 1
    for _ in kwargs:
        d += 1

    return (a ** b) ** 2 * c * d


def double(nums: List[int]) -> List[int]:
    return [x * 2 for x in nums]


def test_cache_example():

    cache_func = cache(func)

    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2


def test_cache_kwargs():

    cache_func = cache(func)

    some_args = 100, 200

    val_1 = cache_func(*some_args, s=90)
    val_2 = cache_func(*some_args, s=90)

    assert val_1 is val_2


def test_double_cache():

    cached_double = cache(double)

    some_args = [100, 200, 100, 200]

    val_1 = cached_double(some_args)
    val_2 = cached_double(some_args)

    assert val_1 is val_2
