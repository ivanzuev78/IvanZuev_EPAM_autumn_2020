import pytest

from HomeWork_3.task04.task04 import is_armstrong


@pytest.mark.parametrize("number", [2, 7, 153, 371])
def test_is_armstrong_true(number):
    assert is_armstrong(number) is True


@pytest.mark.parametrize("number", [10, 66, 999])
def test_is_armstrong_false(number):
    assert is_armstrong(number) is False
