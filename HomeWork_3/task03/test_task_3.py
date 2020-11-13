import pytest

from HomeWork_3.task03.task03 import make_filter, Filter


def test_filter():

    assert Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    ).apply([-4, -3, 0, 1, 2, 3, 4]) == [2, 4]


@pytest.fixture
def data_from_example_of_the_task():
    input_ = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    return input_


def test_specified_filter_example(data_from_example_of_the_task):

    assert make_filter(name="polly", type="bird").apply(
        data_from_example_of_the_task
    ) == [data_from_example_of_the_task[1]]


@pytest.fixture
def some_data_to_test_filter():
    input_ = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "name": "Bill",
            "last_name": "Paper",
        },
        {"name": "Bill", "last_name": "Wodoomagic", "type": "person"},
    ]
    return input_


def test_specified_filter_no_one_in_input_are_good(some_data_to_test_filter):

    assert make_filter(name="Bill", type="bird").apply(some_data_to_test_filter) == []


def test_specified_filter_all_in_input_are_good(some_data_to_test_filter):

    assert (
        make_filter(name="Bill").apply(some_data_to_test_filter)
        == some_data_to_test_filter
    )
