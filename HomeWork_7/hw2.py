def backspace_compare(first: str, second: str) -> bool:
    """
    Given two strings. Return if they are equal when both are typed into
    empty text editors. # means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.

    Examples:
        Input: s = "ab#c", t = "ad#c"
        Output: True
        # Both s and t become "ac".

        Input: s = "a##c", t = "#a#c"
        Output: True
        Explanation: Both s and t become "c".

        Input: a = "a#c", t = "b"
        Output: False
        Explanation: s becomes "c" while t becomes "b".

    """

    def type_this_string(string_to_type):
        real_typed_string = ""
        for char in string_to_type:
            if char == "#":
                real_typed_string = real_typed_string[:-1]
            else:
                real_typed_string += char
            print(real_typed_string)
        return real_typed_string

    return type_this_string(first) == type_this_string(second)
