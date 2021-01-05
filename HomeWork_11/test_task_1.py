from collections.abc import Iterable

from HomeWork_11.hw1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


def test_simplified_enum():
    assert ColorsEnum.RED == "RED"


def test_simplified_enum_len():
    assert len(ColorsEnum) == 4


def test_simplified_enum_is_iterable():
    assert isinstance(ColorsEnum, Iterable)
