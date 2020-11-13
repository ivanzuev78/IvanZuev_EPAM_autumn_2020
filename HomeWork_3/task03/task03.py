# I decided to write a code that generates data filtering object from a list of keyword parameters:
from typing import Callable, List, Hashable, Optional, Any, Iterable


class Filter:
    """
    Helper filter class. Accepts single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions: Callable):
        self.functions = functions

    def apply(self, data: Iterable[Any]) -> Iterable[Any]:
        return [item for item in data if all(func(item) for func in self.functions)]


# example of usage:
# positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords: Any) -> Filter:
    """
    Generate filter object for specified keywords
    """

    def keyword_filter_func(keyword_to_check: Hashable):
        def wrapper(input_dict: dict) -> bool:
            return (
                keywords[keyword_to_check] == input_dict[keyword_to_check]
                if keyword_to_check in input_dict
                else False
            )

        return wrapper

    filter_funcs = [keyword_filter_func(keyword) for keyword in keywords]

    return Filter(*filter_funcs)


# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
