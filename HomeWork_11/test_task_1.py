from HomeWork_11.hw1 import SimplifiedEnum


def test_simplified_enum_colors():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")
    assert ColorsEnum.RED == "RED"


def test_simplified_enum_sizes():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")
    assert SizesEnum.XL == "XL"
