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
import unittest
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:

    counter = {}

    major_elem = None
    minor_elem = None

    for elem in inp:
        if elem not in counter:
            counter[elem] = 0
        counter[elem] += 1

    for elem in counter:
        if major_elem is None:
            major_elem = elem
            minor_elem = elem
        elif counter[elem] > counter[major_elem]:
            major_elem = elem
        elif counter[elem] < counter[minor_elem]:
            minor_elem = elem

    return major_elem, minor_elem


class MyTestCase(unittest.TestCase):
    def test_major_and_minor_elem(self):

        input_1 = [2, 2, 1, 1, 1, 2, 2]
        input_2 = [3, 2, 3]
        input_3 = [i for i in range(20)] + [i for i in range(19)] + [10]

        self.assertEqual(major_and_minor_elem(input_1), (2, 1))
        self.assertEqual(major_and_minor_elem(input_2), (3, 2))
        self.assertEqual(major_and_minor_elem(input_3), (10, 19))


if __name__ == "__main__":
    unittest.main()
