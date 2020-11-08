import time

from HomeWork_3.task02.task02 import slow_calculate, fast_calculate


def test_calculate_time():

    time_slow_start = time.time()
    for i in range(5):
        slow_calculate(i)
    time_slow_end = time.time()
    time_slow_total = time_slow_end - time_slow_start

    time_fast_start = time.time()
    fast_calculate([i for i in range(5)])
    time_fast_end = time.time()
    time_fast_total = time_fast_end - time_fast_start

    assert time_fast_total < time_slow_total


def test_calculate_equal_result():

    sum_slow = 0
    for i in range(3):
        sum_slow += slow_calculate(i)

    sum_fast = fast_calculate([i for i in range(3)])

    assert sum_slow == sum_fast


def test_fast_calculate_is_less_than_a_minute():

    time_fast_start = time.time()
    fast_calculate([i for i in range(501)])
    time_fast_end = time.time()

    time_fast_total = time_fast_end - time_fast_start

    assert time_fast_total < 60
