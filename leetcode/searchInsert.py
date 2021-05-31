import unittest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                if nums[mid] == target and nums[mid-1] != target:
                    return mid
                else:
                    end = mid - 1
        return start


class Test(unittest.TestCase):
    def test_searchInsert(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 0), 0)
        self.assertEqual(solution.searchInsert([1], 0), 0)


if __name__ == '__main__':
    unittest.main()
