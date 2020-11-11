import pytest

from HomeWork_3.task03.task03 import make_filter, Filter


def test_filter():

    assert Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    ).apply([-4, -3, 0, 1, 2, 3, 4]) == [2, 4]


@pytest.fixture
def sample_data():
    input = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    yield input


def test_specified_filter_example(sample_data):

    assert make_filter(name="polly", type="bird").apply(sample_data) == [sample_data[1]]


@pytest.fixture
def specified_filter_input():
    input = [
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
    yield input


def test_specified_filter__no_one_in_input_are_good(specified_filter_input):

    assert make_filter(name="Bill", type="bird").apply(specified_filter_input) == []


def test_specified_filter_all_in_input_are_good(specified_filter_input):

    assert (
        make_filter(name="Bill").apply(specified_filter_input) == specified_filter_input
    )
