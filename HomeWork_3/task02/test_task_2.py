import time

from HomeWork_3.task02.task02 import slow_calculate, fast_calculate


def test_calculate_equal_result():

    sum_slow = 0
    for i in range(3):
        sum_slow += slow_calculate(i)

    sum_fast = fast_calculate([i for i in range(3)])

    assert sum_slow == sum_fast
