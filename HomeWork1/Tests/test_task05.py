from HomeWork1.Tasks.task05 import find_maximal_subarray_sum


def test_example():

    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_find_maximal_subarray_sum():

    assert find_maximal_subarray_sum([1, 2, 3, 4], 1) == 4
    assert find_maximal_subarray_sum([1, 2, 3, 4], 10) == 10
