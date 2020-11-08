"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:

    if len(nums) == 0:
        raise TypeError("Sequence can't be empty.")

    max_result = nums[0]
    for sub_array_len in range(1, k + 1):
        for index_of_nums in range(len(nums) - sub_array_len + 1):
            sub_sum = sum(nums[index_of_nums : index_of_nums + sub_array_len])
            if sub_sum > max_result:
                max_result = sub_sum

    return max_result
