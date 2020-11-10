import time

from HomeWork_3.task01.task01 import cache


@cache(times=2)
def func(a, b):

    return (a ** b) ** 2


def test_cache_val1_is_val_2():
    some_args = 100, 200

    val_1 = func(*some_args)
    val_2 = func(*some_args)
    val_3 = func(*some_args)
    val_4 = func(*some_args)

    assert val_1 is val_2 is val_3 is not val_4
