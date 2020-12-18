from HomeWork_7.hw2 import backspace_compare


def test_backspace_compare_equal_strings():
    assert backspace_compare("ab#c", "ad#c")


def test_backspace_compare_not_equal_strings():
    assert not backspace_compare("ab#c", "ad#d")


def test_backspace_compare_backspacing_an_empty_text():
    assert backspace_compare("a###c", "ad####c")
