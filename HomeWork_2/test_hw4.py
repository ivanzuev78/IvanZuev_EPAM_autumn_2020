import time
from HomeWork_2.hw4 import cache


def func(a, b, *args, **kwargs):
    c, d = 1, 1
    for _ in args:
        c += 1
    for _ in kwargs:
        d += 1

    return (a ** b) ** 2 * c * d


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


def test_cache_check_time():

    cache_func = cache(func)

    some_args = 100000, 200000

    time_start = time.time()
    cache_func(*some_args)
    time_mid = time.time()
    cache_func(*some_args)
    time_end = time.time()

    assert time_mid - time_start > time_end - time_mid
