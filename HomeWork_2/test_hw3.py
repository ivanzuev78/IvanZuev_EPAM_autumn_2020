from HomeWork_2.hw3 import combinations


def test_combinations_example():

    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]


def test_combinations_len():

    assert len(combinations([1, 2], [3, 4], [5, 6])) == 8
    assert len(combinations([1, 2, 3], [3, 4], [5, 6])) == 12


def test_combinations_input_3arrays():

    assert combinations([1, 2], [3, 4], [5]) == [
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 5],
        [2, 4, 5],
    ]


def test_combinations_empty_input():

    assert combinations([]) == []


def test_combinations_str():

    assert combinations("12", "34") == [["1", "3"], ["1", "4"], ["2", "3"], ["2", "4"]]


def test_combinations_different_types():

    assert combinations([1, "s"], "wo") == [[1, "w"], [1, "o"], ["s", "w"], ["s", "o"]]
