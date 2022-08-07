"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
import unittest
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == "__main__":
    unittest.main()
