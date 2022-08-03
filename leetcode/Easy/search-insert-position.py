"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
import unittest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return right + 1


class Test(unittest.TestCase):
    def test_searchInsert(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 7), 4)


if __name__ == "__main__":
    unittest.main()
