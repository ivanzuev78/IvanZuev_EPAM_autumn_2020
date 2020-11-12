from HomeWork_3.task02.task02 import slow_calculate, fast_calculate


def test_calculate_equal_result():

    sum_slow = 0
    for i in range(3):
        sum_slow += slow_calculate(i)

    sum_fast = fast_calculate([i for i in range(3)])

    assert sum_slow == sum_fast


def test_calculate_numb_of_threds_less_than_numb_of_values():

    sum_slow = 0
    for i in range(13):
        sum_slow += slow_calculate(i)

    sum_fast = fast_calculate([i for i in range(13)], numb_of_threads=7)

    assert sum_slow == sum_fast


def test_calculate_lots_of_threads():

    sum_fast = fast_calculate([i for i in range(10**4)], numb_of_threads=10**4)

    assert True