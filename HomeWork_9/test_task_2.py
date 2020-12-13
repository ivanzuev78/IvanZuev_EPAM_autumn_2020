from HomeWork_9.hw2 import SuppressorClass, suppressor_function

import pytest


def test_suppressor_class_catch_error():
    with SuppressorClass(IndexError):
        raise IndexError("Raise IndexError from SuppressorClass")
    assert True


def test_suppressor_class_doesnt_catch_other_error():
    with pytest.raises(AttributeError):
        with SuppressorClass(IndexError):
            raise AttributeError("Raise AttributeError from SuppressorClass")


def test_suppressor_function_catch_error():
    with suppressor_function(IndexError):
        raise IndexError("Raise IndexError from suppressor_function")
    assert True


def test_suppressor_function_doesnt_catch_other_error():
    with pytest.raises(AttributeError):
        with suppressor_function(IndexError):
            raise AttributeError("Raise AttributeError from SuppressorClass")
