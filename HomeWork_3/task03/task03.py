# I decided to write a code that generates data filtering object from a list of keyword parameters:
from typing import Callable, List


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions: Callable):
        self.functions = functions

    def apply(self, data: List[dict]) -> List[dict]:
        return [item for item in data if all(func(item) for func in self.functions)]


# example of usage:
# positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords: dict) -> Filter:
    """
    Generate filter object for specified keywords
    """

    def keyword_filter_func(key_to_check):
        def wrapper(input_dict: dict) -> bool:

            if (
                key_to_check in input_dict
                and keywords[key_to_check] == input_dict[key_to_check]
            ):
                return True
            else:
                return False

        return wrapper

    filter_funcs = []

    for key in keywords:
        filter_funcs.append(keyword_filter_func(key))

    return Filter(*filter_funcs)


# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
