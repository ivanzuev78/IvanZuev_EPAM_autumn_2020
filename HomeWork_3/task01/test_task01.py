import time

from HomeWork_3.task01.task01 import cache


@cache(times=2)
def func(a, b):

    return (a ** b) ** 2


def test_cache_val1_is_val_2():
    some_args = 100, 200

    first_result = func(*some_args)
    cached_result = func(*some_args)
    last_result_from_cache = func(*some_args)
    non_cached_result = func(*some_args)

    assert first_result is cached_result
    assert cached_result is last_result_from_cache
    assert last_result_from_cache is not non_cached_result
