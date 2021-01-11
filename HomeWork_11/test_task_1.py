from HomeWork_11.hw1 import SimplifiedEnum

import pytest


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


def test_simplified_enum():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.ORANGE == "ORANGE"
    assert ColorsEnum.BLACK == "BLACK"


def test_simplified_enum_doesnt_have_other_atrs():
    with pytest.raises(AttributeError):
        ColorsEnum.YELLOW
