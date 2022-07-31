"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


class Test(unittest.TestCase):
    def test_search(self):
        solution = Solution()
        self.assertEqual(solution.search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(solution.search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()
