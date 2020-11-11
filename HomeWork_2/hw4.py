"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable, Any


def object_is_cacheable(arg):

    try:
        hash(arg)
        return True
    except:
        return False


def hashable(users_input):
    try:
        hash(users_input)
        return True
    except:
        return False


def make_it_hashable(*args: Any, **kwargs: Any):
    hashable_output = []
    if all(map(hashable, args)):
        hashable_output.append(tuple(i for i in args))
    else:
        for arg in args:
            hashable_output.append(make_it_hashable(*arg))
    if all(map(hashable, kwargs.values())):
        hashable_output.append(tuple(tuple([i, kwargs[i]]) for i in kwargs))
    else:
        for value in kwargs.values():
            hashable_output.append(tuple(make_it_hashable(*value)) for i in kwargs)

    return tuple(hashable_output)


def cache(func: Callable) -> Callable:

    results = {}

    def wrapper(*args, **kwargs):
        if not hashable((*args, *kwargs)):
            hash_ = make_it_hashable(*args, **kwargs)

        else:
            hash_ = (*args, *kwargs)
        if hash_ in results:
            return results[hash_]

        else:
            result = func(*args, **kwargs)
            results[hash_] = result
            return result

    return wrapper
