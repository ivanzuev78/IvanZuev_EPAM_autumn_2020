import time

from HomeWork_3.task01.task01 import cache


@cache(times=2)
def func(a, b):

    return (a ** b) ** 2


def test_cache():

    some_args = 100000, 200000

    time_1 = time.time()
    func(*some_args)
    time_2 = time.time()
    func(*some_args)
    time_3 = time.time()
    func(*some_args)
    time_4 = time.time()
    func(*some_args)
    time_5 = time.time()

    assert time_2 - time_1 > 0
    assert time_3 - time_2 == 0
    assert time_4 - time_3 == 0
    assert time_5 - time_4 > 0
