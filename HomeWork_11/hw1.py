class SimplifiedEnum(type):
    """
    Vasya implemented nonoptimal Enum classes.
    Remove duplications in variables declarations using metaclasses.

    from enum import Enum


    class ColorsEnum(Enum):
        RED = "RED"
        BLUE = "BLUE"
        ORANGE = "ORANGE"
        BLACK = "BLACK"


    class SizesEnum(Enum):
        XL = "XL"
        L = "L"
        M = "M"
        S = "S"
        XS = "XS"


    Should become:

    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")


    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")


    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
    """

    def __getattr__(cls, item):
        if f"_{cls.__name__}__keys" in cls.__dict__:
            if item in cls.__dict__[f"_{cls.__name__}__keys"]:
                return str(item)

    def __iter__(cls):
        if f"_{cls.__name__}__keys" in cls.__dict__:
            return (item for item in cls.__dict__[f"_{cls.__name__}__keys"])
        return ()

    def __len__(cls):
        if f"_{cls.__name__}__keys" in cls.__dict__:
            return len(cls.__dict__[f"_{cls.__name__}__keys"])
        return 0
