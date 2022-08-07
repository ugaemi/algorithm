"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
import unittest
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1


if __name__ == "__main__":
    unittest.main()
