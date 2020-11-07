from HomeWork_2.hw3 import combinations


def test_combinations_example():

    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]


def test_combinations_len():

    assert len(combinations([1, 2], [3, 4], [5, 6])) == 8
    assert len(combinations([1, 2, 3], [3, 4], [5, 6])) == 12


def test_combinations_3():

    assert combinations([1, 2], [3, 4], [5]) == [
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 5],
        [2, 4, 5],
    ]
