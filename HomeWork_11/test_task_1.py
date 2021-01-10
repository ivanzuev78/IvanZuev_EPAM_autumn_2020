from HomeWork_11.hw1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


def test_simplified_enum():
    assert ColorsEnum.RED == "RED"
