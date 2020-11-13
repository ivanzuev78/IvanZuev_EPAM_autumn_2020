import pytest


def test_stderr():
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
