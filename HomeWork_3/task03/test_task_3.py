from HomeWork_3.task03.task03 import make_filter, Filter


def test_Filter():

    assert Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    ).apply(range(-10, 10)) == [2, 4, 6, 8]


def test_specified_filter_example():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert (
        make_filter(name="polly", type="bird", last_name="Gilbert").apply(sample_data)
        == []
    )
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]


def test_specified_filter__no_one_in_input_are_good():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
        },
        {"kind": "parrot", "type": "bird"},
    ]
    assert make_filter(name="Ivan", type="man").apply(sample_data) == []
    assert make_filter(name="Bill", type="bird").apply(sample_data) == []


def test_specified_filter_all_in_input_are_good():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
        },
        {
            "name": "Bill",
            "last_name": "Paper",
        },
        {
            "name": "Bill",
            "last_name": "Wodoomagic",
        },
    ]
    assert make_filter(name="Bill").apply(sample_data) == sample_data
