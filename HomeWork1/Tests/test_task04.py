from HomeWork1.Tasks.task04 import check_sum_of_four


def test_check_sum_of_four():

    input_1 = [-20, -30]
    input_2 = [20, 30]
    input_3 = [-100, -200]
    input_4 = [100, 200]

    assert check_sum_of_four(input_1, input_2, input_3, input_4) == 4


def test_check_sum_of_four_2():

    input_1 = [20, 30]
    input_2 = [20, 30]
    input_3 = [100, 200]
    input_4 = [100, 200]

    assert check_sum_of_four(input_1, input_2, input_3, input_4) == 0
