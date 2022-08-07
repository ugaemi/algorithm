"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""
import unittest
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])


class Test(unittest.TestCase):
    def test_sortedSquares(self):
        solution = Solution()
        self.assertEqual(solution.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(solution.sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


if __name__ == "__main__":
    unittest.main()
