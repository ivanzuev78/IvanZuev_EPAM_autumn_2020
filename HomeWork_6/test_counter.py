import pytest

from HomeWork_6.counter import instances_counter


@pytest.fixture
def decorated_class():
    @instances_counter
    class User:
        pass

    return User


def test_instances_counter_get_created_instances(decorated_class):
    assert decorated_class.get_created_instances() == 0
    user, _, _ = decorated_class(), decorated_class(), decorated_class()
    assert user.get_created_instances() == 3


def test_instances_counter_reset_instances_counter(decorated_class):
    user, _, _ = decorated_class(), decorated_class(), decorated_class()
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0
