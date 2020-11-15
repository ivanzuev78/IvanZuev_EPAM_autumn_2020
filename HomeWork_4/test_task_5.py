from HomeWork_4.task_5_optional import fizzbuzz


def test_fizzbuzz_up_to_first_fizzbuzz():
    assert list(fizzbuzz(15)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
    ]


def test_fizzbuzz_negative_int_input():
    assert list(fizzbuzz(-15)) == []


def test_fizzbuzz_is_a_generator():
    fizzbuzz_generator = fizzbuzz(3)
    assert next(fizzbuzz_generator) == "1"
    assert next(fizzbuzz_generator) == "2"
    assert next(fizzbuzz_generator) == "fizz"
