from HomeWork_6.counter import instances_counter


def test_instances_counter_get_created_instances():
    class User:
        __counter = 6
        pass

    decorated_class = instances_counter(User)
    assert decorated_class.get_created_instances() == 0
    decorated_class(), decorated_class(), decorated_class()
    assert decorated_class.get_created_instances() == 3
    assert decorated_class._User__counter == 6


def test_instances_counter_reset_instances_counter():
    class User:
        pass

    decorated_class = instances_counter(User)
    decorated_class(), decorated_class(), decorated_class()
    assert decorated_class.reset_instances_counter() == 3
    assert decorated_class.get_created_instances() == 0
