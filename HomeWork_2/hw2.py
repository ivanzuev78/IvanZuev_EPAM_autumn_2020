"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:

    counter = Counter()

    # major_elem = None
    minor_elem = None

    for elem in inp:
        counter[elem] += 1

    major_elem = counter.most_common(1)[0][0]
    minor_elem = counter.most_common()[-1][0]

    # for elem in counter:
    #     if major_elem is None:
    #         major_elem = elem
    #         minor_elem = elem
    #     elif counter[elem] > counter[major_elem]:
    #         major_elem = elem
    #     elif counter[elem] < counter[minor_elem]:
    #         minor_elem = elem

    return major_elem, minor_elem


def test_major_and_minor_elem_1():

    input_1 = [2, 2, 1, 1, 1, 2, 2]

    assert major_and_minor_elem(input_1) == (2, 1)


def test_major_and_minor_elem_2():

    input_2 = [3, 2, 3]

    assert major_and_minor_elem(input_2) == (3, 2)
