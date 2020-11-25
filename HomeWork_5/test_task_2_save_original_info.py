import functools
import pytest

from HomeWork_5.save_original_info import print_result


@pytest.fixture
def decorated_func():
    @print_result
    def original_func(*args):
        """This function can sum any objects which have __add___"""
        return functools.reduce(lambda x, y: x + y, args)

    yield original_func


def test_print_result_result_is_printed(decorated_func, capsys):
    decorated_func(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert captured.out == "10\n"


def test_print_result_original_doc_saved(decorated_func):
    assert (
        decorated_func.__doc__
        == "This function can sum any objects which have __add___"
    )


def test_print_result_original_name_saved(decorated_func):
    assert decorated_func.__name__ == "original_func"


@pytest.fixture
def decorated_and_origin_funcs():
    def original_func(*args):
        """This function can sum any objects which have __add___"""
        return functools.reduce(lambda x, y: x + y, args)

    decorated_func = print_result(original_func)
    yield decorated_func, original_func


def test_print_result_original_func_saved(decorated_and_origin_funcs, capsys):
    decorated_func, original_func = decorated_and_origin_funcs
    assert decorated_func.__original_func is original_func
